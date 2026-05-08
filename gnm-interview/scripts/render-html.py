#!/usr/bin/env python3
"""GNM HTML Live-Preview Generator (gnm-interview)

Emits a static HTML file mirroring the 9-zone Excel layout produced by
generate-gnm.py. Pairs with `serve.sh` (a wee `python -m http.server`)
so the user watches the GNM take shape in a browser tab while the
interview runs.

Usage:
    python3 render-html.py <build-spec.json> [output.html]

Design notes:
  - Auto-refreshes every 2s via <meta http-equiv="refresh">.
  - Reuses validate_spec + compute_layout from generate-gnm.py to
    guarantee the HTML and .xlsx stay in lockstep on validation.
  - Empty/`…`/`—` cells render as muted gray for visibility of progress.
  - Pure-static output: no JS, no build step, opens directly via file://.
"""

import html as _html
import json
import os
import sys
from datetime import datetime

# Reuse validation + layout from the Excel renderer so the two outputs
# can never drift. The filename has a dash, so importlib.util is cleanest.
import importlib.util
_HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    'gnm_renderer', os.path.join(_HERE, 'generate-gnm.py')
)
_gen = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_gen)


PLACEHOLDER_VALUES = {'', '—', '…', '-', None}


def is_placeholder(v):
    if v is None:
        return True
    if isinstance(v, str) and v.strip() in PLACEHOLDER_VALUES:
        return True
    return False


def cell_text(entry):
    """Plain text for a cell — engine objects render as their `text`."""
    if isinstance(entry, dict):
        return entry.get('text') or entry.get('sheet') or ''
    if entry is None:
        return ''
    return str(entry)


def cell_link(entry):
    """If the cell is a HYPERLINK object, return the target sheet name."""
    if isinstance(entry, dict) and 'sheet' in entry:
        return entry['sheet']
    return None


def td(content, *, cls='', colspan=1, rowspan=1, title=''):
    attrs = []
    if cls:
        attrs.append(f'class="{cls}"')
    if colspan != 1:
        attrs.append(f'colspan="{colspan}"')
    if rowspan != 1:
        attrs.append(f'rowspan="{rowspan}"')
    if title:
        attrs.append(f'title="{_html.escape(title)}"')
    attr_str = (' ' + ' '.join(attrs)) if attrs else ''
    return f'<td{attr_str}>{content}</td>'


def render_engine_cell(entry, *, cls='engine', placeholder_glyph=True):
    text = cell_text(entry)
    link = cell_link(entry)
    if is_placeholder(text):
        glyph = '<span class="muted">…</span>' if placeholder_glyph else ''
        return td(glyph, cls=f'{cls} placeholder')
    safe = _html.escape(text)
    if link:
        return td(
            f'<span class="hyperlink-glyph">↗</span> {safe}',
            cls=f'{cls} hyperlink',
            title=f'→ {link}',
        )
    return td(safe, cls=cls)


def render_value_cell(entry):
    text = cell_text(entry)
    if is_placeholder(text):
        return td('<span class="muted">…</span>', cls='value placeholder')
    return td(_html.escape(text), cls='value')


# =============================================================
# TABLE BUILDER — mirrors the same column layout the Excel uses.
# =============================================================
def build_colgroup(lo):
    """Emit a <colgroup> with explicit widths mirroring the Excel constants
    so the browser can't stretch spacer columns to fill the viewport."""
    # Excel WIDTH_* in ~character units; we use ch directly.
    widths = ['3ch']                    # A — narrow
    widths += ['14ch', '14ch']          # B, C — phan dau
    widths += ['3ch']                   # D — sep
    widths += ['14ch', '14ch']          # E, F
    if lo['L2']:
        widths += ['14ch']              # G
    widths += ['28ch'] * lo['f']        # zone2 cols
    widths += ['28ch']                  # conso
    widths += ['3ch']                   # sep
    widths += ['14ch', '14ch']          # mr1, mr2
    cols = ''.join(f'<col style="width:{w}">' for w in widths)
    return f'<colgroup>{cols}</colgroup>'


def build_table(spec, lo):
    """Yield <tr> rows that match the Excel grid 1:1.

    Column layout (1-indexed, mirrors generate-gnm.py):
      A | B | C | D(sep) | E | F | [G if L2] | zone2_cols... | conso | sep | mr1 | mr2
    """
    gnm = spec['gnm']
    lang = spec.get('session', {}).get('lang', 'en')
    z1 = spec['zone1']
    z2 = spec['zone2']
    z3 = spec['zone3']
    z4 = spec['zone4']

    f_cnt = lo['f']
    n = lo['n']
    a = lo['a']
    c = lo['c']
    L2 = lo['L2']

    # Total visible columns: A B C D E F (G?) [zone2 × f] conso sep mr1 mr2
    # We render 1 logical row per Excel row (B2 merge handled in row 2).
    zone1_label_cols = 2 + L2  # E, F, G?

    rows = []

    # ---- Row 1: A1 backlink + B1 warning ----
    parent = spec.get('parent') or {}
    warnings = spec.get('warnings') or []
    a1 = ''
    if parent.get('backlink'):
        a1 = td(f'<a href="#">« {_html.escape(parent.get("sheet", ""))}</a>',
                cls='backlink')
    else:
        a1 = td('', cls='spacer')
    b1 = td('', cls='spacer', colspan=1)
    if warnings:
        plural = 's' if len(warnings) != 1 else ''
        b1 = td(
            f'⚠ {len(warnings)} rule override{plural} logged',
            cls='warning',
            colspan=2 + f_cnt + L2 + 1 + 1 + 2,  # spans the rest of the row visually
        )
    rows.append('<tr>' + a1 + b1 + '</tr>')

    # ---- Row 2: B2 merged title ----
    suffix = _gen.level_suffix(gnm['level'], gnm['is_final'], lang)
    title = _html.escape(f"{gnm['name']} {suffix}")
    title_span = 2 + 2 + L2 + f_cnt + 1  # B..conso (matches b2_merge in Excel)
    rows.append(
        '<tr>'
        + td('', cls='spacer')
        + td(title, cls='title', colspan=title_span)
        + td('', cls='spacer')
        + td('', cls='spacer', colspan=2)
        + '</tr>'
    )

    # ---- Row 3: spacer ----
    total_cols = 1 + 2 + 1 + 2 + L2 + f_cnt + 1 + 1 + 2
    rows.append('<tr><td class="spacer-row" colspan="{}"></td></tr>'.format(total_cols))

    # ---- Row 4: header row (negative numbers, dark blue) ----
    hdr_cells = [td('', cls='spacer')]
    hdr_cells.append(td('-1', cls='hdr'))
    hdr_cells.append(td('-2', cls='hdr'))
    hdr_cells.append(td('', cls='spacer'))
    # phan_than: E, F, [G], zone2..., conso
    phan_than_count = 2 + L2 + f_cnt + 1
    for i in range(phan_than_count):
        hdr_cells.append(td(f'-{i + 1}', cls='hdr'))
    hdr_cells.append(td('', cls='spacer'))
    hdr_cells.append(td('-1', cls='hdr'))
    hdr_cells.append(td('-2', cls='hdr'))
    rows.append('<tr>' + ''.join(hdr_cells) + '</tr>')

    # ---- Row 5: subheaders ----
    sub5 = [
        td('', cls='spacer'),
        td(_html.escape(gnm['code']), cls='sub bold'),
        td('-1', cls='sub'),
        td('', cls='spacer'),
        td(_html.escape(gnm['code']), cls='sub bold'),  # E5 = B5
        td('', cls='sub'),
    ]
    if L2:
        sub5.append(td('', cls='sub'))
    for _ in range(f_cnt):
        sub5.append(td('', cls='sub'))
    sub5.append(td('Conso.', cls='sub bold'))
    sub5.append(td('', cls='spacer'))
    sub5.append(td('Common', cls='sub bold'))
    sub5.append(td('', cls='sub'))
    rows.append('<tr>' + ''.join(sub5) + '</tr>')

    # ---- Row 6: feature_group ----
    sub6 = [
        td('', cls='spacer'),
        td('', cls='sub'),
        td('-2', cls='sub'),
        td('', cls='spacer'),
        td('Object', cls='sub bold'),
        td('', cls='sub'),
    ]
    if L2:
        sub6.append(td('', cls='sub'))
    sub6.append(td(_html.escape(z2.get('feature_group', '')),
                   cls='sub bold', colspan=f_cnt))
    sub6.append(td('-', cls='sub'))
    sub6.append(td('', cls='spacer'))
    sub6.append(td('-', cls='sub'))
    sub6.append(td('', cls='sub'))
    rows.append('<tr>' + ''.join(sub6) + '</tr>')

    # ---- Row 7: features ----
    sub7 = [
        td('', cls='spacer'),
        td('', cls='sub'),
        td('-3', cls='sub'),
        td('', cls='spacer'),
        td('Item', cls='sub bold'),
        td('-', cls='sub'),
    ]
    if L2:
        sub7.append(td('-', cls='sub'))
    if f_cnt == 1:
        sub7.append(td('-', cls='sub'))
    else:
        for feat in z2['features']:
            sub7.append(td(_html.escape(feat), cls='sub bold'))
    sub7.append(td('-', cls='sub'))
    sub7.append(td('', cls='spacer'))
    sub7.append(td('-', cls='sub'))
    sub7.append(td('-', cls='sub'))
    rows.append('<tr>' + ''.join(sub7) + '</tr>')

    # ---- Rows 8..7+n: Zone 1 items + Zone 3 + Zone 4 ----
    for i, item in enumerate(z1['items']):
        cells = [
            td('', cls='spacer'),
            td('', cls='value'),
            td(str(i + 1), cls='value muted'),
            td('', cls='spacer'),
            td('', cls='value'),  # E
            td(_html.escape(item.get('l1') or ''), cls='value bold'),
        ]
        if L2:
            cells.append(td(_html.escape(item.get('l2') or ''), cls='value'))
        for k in range(f_cnt):
            cells.append(render_value_cell(z3[i][k]))
        cells.append(render_engine_cell(z4[i]))
        cells.append(td('', cls='spacer'))
        cells.append(td('', cls='value'))
        cells.append(td('', cls='value'))
        rows.append('<tr>' + ''.join(cells) + '</tr>')

    # ---- All cluster (row all_start..all_end) ----
    z5 = spec.get('zone5', []) or []
    z6 = spec.get('zone6', []) or []
    z7 = spec.get('zone7', []) or []
    for ri in range(a):
        z5_row = z5[ri] if ri < len(z5) else []
        if not isinstance(z5_row, list):
            z5_row = [z5_row]
        z6_val = z6[ri] if ri < len(z6) else ''
        z7_pair = z7[ri] if ri < len(z7) else []
        if not isinstance(z7_pair, list):
            z7_pair = [z7_pair, '']
        z7_pair = (z7_pair + ['', ''])[:2]

        cells = [
            td('', cls='spacer'),
            td('', cls='value'),
            td('All' if ri == 0 else '', cls='value bold'),
            td('', cls='spacer'),
            td('', cls='value'),
            td('', cls='value'),
        ]
        if L2:
            cells.append(td('', cls='value'))
        for k in range(f_cnt):
            v = z5_row[k] if k < len(z5_row) else ''
            cells.append(render_engine_cell(v, cls='engine cluster', placeholder_glyph=False))
        cells.append(render_engine_cell(z6_val, cls='engine cluster', placeholder_glyph=False))
        cells.append(td('', cls='spacer'))
        cells.append(render_engine_cell(z7_pair[0], cls='engine cluster', placeholder_glyph=False))
        cells.append(render_engine_cell(z7_pair[1], cls='engine cluster', placeholder_glyph=False))
        rows.append('<tr>' + ''.join(cells) + '</tr>')

    # ---- Common cluster ----
    z8 = spec.get('zone8', []) or []
    z9 = spec.get('zone9', []) or []
    for ri in range(c):
        z8_val = z8[ri] if ri < len(z8) else ''
        z9_pair = z9[ri] if ri < len(z9) else []
        if not isinstance(z9_pair, list):
            z9_pair = [z9_pair, '']
        z9_pair = (z9_pair + ['', ''])[:2]

        cells = [
            td('', cls='spacer'),
            td('Common' if ri == 0 else '', cls='value bold'),
            td('-' if ri == 0 else '', cls='value muted'),
            td('', cls='spacer'),
            td('', cls='value'),
            td('', cls='value'),
        ]
        if L2:
            cells.append(td('', cls='value'))
        for k in range(f_cnt):
            cells.append(td('', cls='value'))
        cells.append(render_engine_cell(z8_val, cls='engine cluster', placeholder_glyph=False))
        cells.append(td('', cls='spacer'))
        cells.append(render_engine_cell(z9_pair[0], cls='engine cluster', placeholder_glyph=False))
        cells.append(render_engine_cell(z9_pair[1], cls='engine cluster', placeholder_glyph=False))
        rows.append('<tr>' + ''.join(cells) + '</tr>')

    return '\n'.join(rows)


# =============================================================
# PROGRESS BAR — what fraction of cells are populated
# =============================================================
def progress(spec, lo):
    total = 0
    filled = 0

    # Z1 items.l1
    for item in spec['zone1']['items']:
        total += 1
        if not is_placeholder(item.get('l1')):
            filled += 1

    # Z2 features
    for feat in spec['zone2']['features']:
        total += 1
        if not is_placeholder(feat):
            filled += 1

    # Z3 matrix
    for row in spec['zone3']:
        for cell in row:
            total += 1
            if not is_placeholder(cell_text(cell)):
                filled += 1

    # Z4 conso
    for v in spec['zone4']:
        total += 1
        if not is_placeholder(cell_text(v)):
            filled += 1

    pct = round(100 * filled / total) if total else 0
    return filled, total, pct


CSS = """
:root {
  --hdr: #0070c0;
  --sub: #ddebf7;
  --eng: #0563c1;
  --warn: #c00000;
  --muted: #b5b5b5;
  --border: #4a4a4a;
  --thin-border: #c8c8c8;
  --bg: #fafafa;
  --content: #ffffff;
}
* { box-sizing: border-box; }
body {
  font-family: 'Myriad Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg);
  margin: 0;
  padding: 24px;
  color: #1a1a1a;
}
.shell { max-width: 1600px; margin: 0 auto; }
header {
  display: flex; align-items: center; justify-content: space-between;
  padding-bottom: 12px; border-bottom: 1px solid var(--thin-border);
  margin-bottom: 16px;
}
.brand { font-weight: 700; font-size: 13px; letter-spacing: .04em; color: #555; }
.meta  { font-size: 12px; color: #777; }
.progress { display: flex; align-items: center; gap: 8px; margin: 4px 0 16px; font-size: 12px; color: #555; }
.bar { width: 240px; height: 6px; background: #e6e6e6; border-radius: 3px; overflow: hidden; }
.fill { height: 100%; background: var(--hdr); transition: width .3s ease; }

.grid-wrap { overflow-x: auto; }
table.gnm {
  border-collapse: collapse;
  background: var(--content);
  box-shadow: 0 1px 3px rgba(0,0,0,.06);
  table-layout: fixed;
}
table.gnm td {
  padding: 6px 9px; vertical-align: top;
  font-size: 12px; line-height: 1.35;
  border: 1px solid var(--thin-border);
  word-wrap: break-word; overflow-wrap: break-word;
}
table.gnm td.spacer { background: var(--bg); border: none; padding: 0; }
table.gnm tr td.spacer-row { background: var(--bg); border: none; height: 6px; padding: 0; }

.hdr {
  background: var(--hdr); color: #fff; font-weight: 700;
  text-align: center; font-size: 10px;
  padding: 3px 6px;
  letter-spacing: .02em;
}
.sub  { background: var(--sub); }
.bold { font-weight: 700; }
.value { background: var(--content); }
.engine { background: var(--content); color: var(--eng); font-weight: 600; }
.engine.cluster { color: var(--eng); }
.placeholder, .muted { color: var(--muted); font-style: italic; font-weight: 400; }
.title {
  font-size: 16px; font-weight: 700;
  text-align: left; padding: 10px 12px;
  background: #fff; border: none;
}
.warning { color: var(--warn); font-style: italic; font-size: 11px; border: none; background: transparent; padding: 4px 0; }
.backlink a { color: var(--eng); text-decoration: none; font-weight: 600; }

.hyperlink { color: var(--eng); }
.hyperlink-glyph { font-size: 10px; opacity: .7; }

footer {
  margin-top: 24px; padding-top: 12px;
  border-top: 1px solid var(--thin-border);
  font-size: 11px; color: #888; display: flex; justify-content: space-between;
}
.live-dot {
  display: inline-block; width: 8px; height: 8px; border-radius: 50%;
  background: #2ea043; margin-right: 6px;
  animation: pulse 1.4s ease-in-out infinite;
  vertical-align: middle;
}
@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50%      { opacity: .4; transform: scale(.85); }
}
"""


def render_html(spec_path, output_path=None, refresh_seconds=2):
    with open(spec_path, 'r', encoding='utf-8') as fh:
        spec = json.load(fh)

    errors = _gen.validate_spec(spec)
    lo = _gen.compute_layout(spec) if not errors else None

    gnm = spec['gnm']
    if not output_path:
        output_path = os.path.join(os.path.dirname(spec_path), 'current.html')

    timestamp = datetime.now().strftime('%H:%M:%S')

    if errors:
        body = (
            '<div class="shell">'
            f'<header><div class="brand">GNM live preview</div>'
            f'<div class="meta">spec invalid · {timestamp}</div></header>'
            '<div style="padding:18px;background:#fff5f5;border:1px solid #ffd0d0;'
            'border-radius:6px;color:#a40000;">'
            '<b>Build Spec validation failed</b><ul>'
            + ''.join(f'<li>{_html.escape(e)}</li>' for e in errors)
            + '</ul></div></div>'
        )
    else:
        filled, total, pct = progress(spec, lo)
        purpose = _html.escape(gnm.get('purpose', ''))
        body = f"""<div class="shell">
<header>
  <div class="brand">GNM · live preview</div>
  <div class="meta"><span class="live-dot"></span>{gnm['code']} · {timestamp} · refresh {refresh_seconds}s</div>
</header>
<div style="font-size:12px;color:#666;margin-bottom:6px;">{purpose}</div>
<div class="progress">
  <span>Cells filled: <b>{filled}/{total}</b> ({pct}%)</span>
  <div class="bar"><div class="fill" style="width:{pct}%"></div></div>
</div>
<div class="grid-wrap"><table class="gnm">{build_colgroup(lo)}{build_table(spec, lo)}</table></div>
<footer>
  <span>{os.path.basename(spec_path)}</span>
  <span>auto-refresh: {refresh_seconds}s · save spec.json to update</span>
</footer>
</div>"""

    page = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="{refresh_seconds}">
<title>GNM · {gnm.get('code', '???')} · live</title>
<style>{CSS}</style>
</head><body>
{body}
</body></html>
"""

    tmp = output_path + '.next'
    with open(tmp, 'w', encoding='utf-8') as fh:
        fh.write(page)
    os.replace(tmp, output_path)
    return output_path


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 render-html.py <build-spec.json> [output.html]')
        sys.exit(1)
    spec_file = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else None
    out = render_html(spec_file, out_file)
    print(f'→ {out}')
