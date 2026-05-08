---
part: 13
name: "GNM Excel Generation — Complete Reference"
parent: gnm-instruction.md
version: "5.3.2"
---

# PART 13: GNM EXCEL GENERATION — COMPLETE REFERENCE

> **When to use:** When generating `.xlsx` files via openpyxl. This is the SINGLE SOURCE OF TRUTH for Excel generation code. Load this file alongside the `xlsx` skill.

> **Token budget:** ~3,000 tokens. Contains complete code template — no need to load Part 4 or Part 2b when generating Excel.

## Quick Reference

| Parameter | Formula | Example (f=1,L2=0,n=5,a=2,c=2) |
|-----------|---------|-------------------------------|
| Phần Thân total cols | f + L2 + 3 | 1+0+3 = 4 (cols E-H) |
| Zone 2 first col | Col(G + L2) | G |
| Conso. col | Col(G + L2 + f) | H |
| Separator col | Col(G + L2 + f + 1) | I |
| Mở rộng cols | Col(G+L2+f+2), Col(G+L2+f+3) | J, K |
| B2 merge end | Conso. col | B2:H2 |
| Last item row | 7 + n | 12 |
| All start row | 8 + n | 13 |
| Common start row | 8 + n + a | 15 |
| End row | 7 + n + a + c | 16 |

## Canonical Styles

```python
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# === FILLS (only 3 colors) ===
HDR_FILL = PatternFill('solid', fgColor='0070C0')   # Header row 4
SUB_FILL = PatternFill('solid', fgColor='DDEBF7')   # Sub-header, zone headers
WHT_FILL = PatternFill('solid', fgColor='FFFFFF')    # Content, everything else

# === FONTS ===
TITLE_FONT = Font(name='Myriad Pro', bold=True, color='000000', size=14)   # B2 only
HDR_FONT   = Font(name='Myriad Pro', bold=True, color='FFFFFF', size=11)   # Row 4
SUB_FONT   = Font(name='Myriad Pro', bold=True, color='000000', size=11)   # Row 5
NORM_FONT  = Font(name='Myriad Pro', color='000000', size=11)              # Values, labels
ENG_FONT   = Font(name='Myriad Pro', color='0563C1', size=11)              # Engine/link text
BACK_FONT  = Font(name='Myriad Pro', color='0563C1', size=11)              # A1 back-link

# === ALIGNMENT ===
WRAP    = Alignment(horizontal='left', vertical='top', wrap_text=True, indent=1)
NO_WRAP = Alignment(horizontal='left', vertical='top', wrap_text=False, indent=1)
NO_WRAP_NO_INDENT = Alignment(horizontal='left', vertical='top', wrap_text=False, indent=0)  # B2, A1

# === BORDERS ===
THIN   = Side(style='thin')
MEDIUM = Side(style='medium')
NO_SIDE = Side(style=None)

# === COLUMN WIDTHS ===
COL_WIDTHS = {
    'separator': 3,        # A, D, post-Conso separator
    'phan_dau': 14,        # B, C
    'zone1': 14,           # E, F, (G if L2=1)
    'zone2_3': 28,         # Feature cols, Conso.
    'mo_rong': 14,         # Extension cols
}

# === ROW HEIGHTS ===
ROW_HEIGHTS = {
    'title': 30,     # Row 2 (B2 title)
    'header': 24,    # Row 4
    'sub_header': 24, # Row 5
    'zone_header': 24, # Rows 6-7 (min, auto-grow with wrap)
    'content': 24,   # Rows 8+ (min, auto-grow with wrap)
}
```

## Complete GNM Builder Class

```python
"""
GNM Excel Builder — Complete implementation following 5-phase write order.
Usage:
    builder = GNMBuilder()
    builder.add_sheet(config_dict)  # for each sheet
    builder.build('output.xlsx')
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter, column_index_from_string
from copy import copy


class GNMBuilder:
    """Builds GNM Excel workbooks following the 5-phase write order protocol.

    5-Phase Write Order (STRICT — applied across ALL sheets per phase):
      Phase 1: DATA        — cell values, labels, engine text
      Phase 2: FORMULAS    — =B5, =HYPERLINK, number references
      Phase 3: MEDIUM      — section outline borders (Phần Đầu, Thân, Mở rộng)
      Phase 4: THIN        — cluster separator borders (All/Common top lines)
      Phase 5: FORMATTING  — fills, fonts, alignment, widths, heights
    """

    # ── FILLS (only 3 colors) ──
    HDR_FILL = PatternFill('solid', fgColor='0070C0')
    SUB_FILL = PatternFill('solid', fgColor='DDEBF7')
    WHT_FILL = PatternFill('solid', fgColor='FFFFFF')

    # ── FONTS ──
    TITLE_FONT = Font(name='Myriad Pro', bold=True, color='000000', size=14)
    HDR_FONT   = Font(name='Myriad Pro', bold=True, color='FFFFFF', size=11)
    SUB_FONT   = Font(name='Myriad Pro', bold=True, color='000000', size=11)
    NORM_FONT  = Font(name='Myriad Pro', color='000000', size=11)
    ENG_FONT   = Font(name='Myriad Pro', color='0563C1', size=11)
    BACK_FONT  = Font(name='Myriad Pro', color='0563C1', size=11)

    # ── ALIGNMENT ──
    WRAP       = Alignment(horizontal='left', vertical='top', wrap_text=True, indent=1)
    NO_WRAP    = Alignment(horizontal='left', vertical='top', wrap_text=False, indent=1)
    NO_WRAP_NI = Alignment(horizontal='left', vertical='top', wrap_text=False, indent=0)

    # ── BORDER SIDES ──
    THIN   = Side(style='thin')
    MEDIUM = Side(style='medium')

    def __init__(self):
        self.wb = Workbook()
        self.wb.remove(self.wb.active)  # remove default sheet
        self.sheets_config = []

    # ──────────────────────────────────────────────
    # PUBLIC API
    # ──────────────────────────────────────────────

    def add_sheet(self, config):
        """Register a sheet configuration.

        config = {
            'sheet_name': str,       # Excel tab name, e.g. 'RCP (A)'
            'gnm_title': str,        # B2 content, e.g. 'RETAIL CHANNEL PARTNERSHIP (A)'
            'gnm_code': str,         # B5 content, 3-letter code e.g. 'RCP'
            'is_root': bool,         # True = no A1 back-link
            'parent_sheet': str|None,# Tab name for back-link, e.g. 'VBM (A)'
            'f': int,                # Number of features (1-5)
            'L2': int,               # 1 if Level 2 column exists, else 0
            'feature_group': str,    # R6 Zone 2 header text
            'features': [str],       # Feature names for R7 ('-' if single)
            'items': [               # Zone 1 item rows
                {'level1': str, 'level2': str|None},
            ],
            'zone3': [               # Zone 3 values/engines per item row
                # Each element is a list of f entries (one per feature col)
                [{'text': str, 'is_engine': bool, 'link_sheet': str|None}],
            ],
            'zone4': [               # Conso. column per item row
                {'text': str, 'is_engine': bool, 'link_sheet': str|None},
            ],
            'all_engines': {         # All cluster engines
                'zone5': [[str]],    # per All row → list of f engine strings
                'zone6': [str],      # per All row → Conso. engine string
                'zone7': [[str,str]],# per All row → [mr1, mr2] strings
            },
            'common_engines': {      # Common cluster engines
                'zone8': [str],      # per Common row → Conso. engine string
                'zone9': [[str,str]],# per Common row → [mr1, mr2] strings
            },
        }
        """
        self.sheets_config.append(config)

    def build(self, output_path):
        """Execute 5-phase build across ALL sheets, then save."""
        # Create all worksheet objects first
        sheets = []
        for cfg in self.sheets_config:
            ws = self.wb.create_sheet(title=cfg['sheet_name'])
            ws.sheet_view.showGridLines = False
            sheets.append((ws, cfg))

        # PHASE 1: DATA — all sheets
        for ws, cfg in sheets:
            self._phase1_data(ws, cfg)

        # PHASE 2: FORMULAS — all sheets
        for ws, cfg in sheets:
            self._phase2_formulas(ws, cfg)

        # PHASE 3: MEDIUM BORDERS — all sheets
        for ws, cfg in sheets:
            self._phase3_medium_borders(ws, cfg)

        # PHASE 4: THIN BORDERS — all sheets
        for ws, cfg in sheets:
            self._phase4_thin_borders(ws, cfg)

        # PHASE 5: FORMATTING — all sheets
        for ws, cfg in sheets:
            self._phase5_formatting(ws, cfg)

        self.wb.save(output_path)
        print(f"Saved: {output_path}")

    # ──────────────────────────────────────────────
    # LAYOUT CALCULATOR
    # ──────────────────────────────────────────────

    def _get_layout(self, cfg):
        """Calculate all column/row positions from f, L2, and data lengths."""
        f, L2 = cfg['f'], cfg['L2']
        # Column positions (1-indexed). G=7.
        z2_start = 7 + L2              # First Zone 2 feature col
        z2_end   = z2_start + f - 1    # Last Zone 2 feature col
        conso    = z2_end + 1          # Consolidation col
        sep2     = conso + 1           # Separator after Conso
        mr1      = sep2 + 1            # Mở rộng col 1
        mr2      = mr1 + 1             # Mở rộng col 2

        n = len(cfg['items'])
        a = max(len(cfg.get('all_engines', {}).get('zone6', [])), 2)
        c = max(len(cfg.get('common_engines', {}).get('zone8', [])), 2)

        return {
            'f': f, 'L2': L2, 'n': n, 'a': a, 'c': c,
            'z2_start': z2_start, 'z2_end': z2_end,
            'conso': conso, 'sep2': sep2, 'mr1': mr1, 'mr2': mr2,
            'last_item_row': 7 + n,
            'all_start':     8 + n,
            'all_end':       7 + n + a,
            'common_start':  8 + n + a,
            'common_end':    7 + n + a + c,
            'end_row':       7 + n + a + c,
            'phan_than_start_col': 5,   # E=5
            'phan_than_end_col':   conso,
        }

    # ──────────────────────────────────────────────
    # PHASE 1: DATA
    # ──────────────────────────────────────────────

    def _phase1_data(self, ws, cfg):
        """Write all static cell values, labels, and engine text."""
        lay = self._get_layout(cfg)

        # ── Tên GNM (B2) ──
        ws.cell(row=2, column=2, value=cfg['gnm_title'])
        ws.merge_cells(
            start_row=2, start_column=2,
            end_row=2, end_column=lay['conso']
        )

        # ── PHẦN ĐẦU (cols B-C) ──
        # Header row 4
        ws.cell(row=4, column=2, value='(1)')
        ws.cell(row=4, column=3, value='(2)')

        # Sub-header rows 5-7
        ws.cell(row=5, column=2, value=cfg['gnm_code'])  # B5 = GNM code
        ws.cell(row=5, column=3, value=-1)                # C5 → displays as (1)
        ws.cell(row=6, column=3, value=-2)                # C6 → displays as (2)
        ws.cell(row=7, column=3, value=-3)                # C7 → displays as (3)
        # B6, B7 intentionally empty

        # Content numbering (C8 .. C[7+n])
        for i in range(lay['n']):
            ws.cell(row=8 + i, column=3, value=i + 1)

        # All cluster — Phần Đầu
        ws.cell(row=lay['all_start'], column=3, value='All')
        # B column empty in All rows

        # Common cluster — Phần Đầu
        ws.cell(row=lay['common_start'], column=2, value='Common')
        ws.cell(row=lay['common_start'], column=3, value='-')

        # ── PHẦN THÂN Header (Row 4) ──
        for i, col in enumerate(range(5, lay['conso'] + 1)):
            ws.cell(row=4, column=col, value=f'({i + 1})')

        # ── PHẦN THÂN Sub-header (Row 5) ──
        # E5 = formula (Phase 2)
        ws.cell(row=5, column=lay['conso'], value='Conso.')

        # ── Zone Headers (Rows 6-7) ──
        ws.cell(row=6, column=5, value='Object')      # E6
        ws.cell(row=7, column=5, value='Item')         # E7
        ws.cell(row=7, column=6, value='-')            # F7

        if lay['L2']:
            ws.cell(row=7, column=7, value='-')        # G7 when L2=1

        # Zone 2 headers
        ws.cell(row=6, column=lay['z2_start'], value=cfg['feature_group'])
        for fi, feat in enumerate(cfg['features']):
            ws.cell(row=7, column=lay['z2_start'] + fi, value=feat)

        # Conso. headers R6, R7
        ws.cell(row=6, column=lay['conso'], value='-')
        ws.cell(row=7, column=lay['conso'], value='-')

        # ── Zone 1 Content (Items) ──
        for i, item in enumerate(cfg['items']):
            row = 8 + i
            # E8 = formula (Phase 2); E9+ empty
            # F = Level 1
            ws.cell(row=row, column=6, value=item['level1'])
            # G = Level 2 (only when L2=1)
            if lay['L2']:
                ws.cell(row=row, column=7, value=item.get('level2') or '-')

        # ── Zone 3 Content (feature cols) ──
        for i, row_data in enumerate(cfg.get('zone3', [])):
            row = 8 + i
            for fi, cell_data in enumerate(row_data):
                col = lay['z2_start'] + fi
                if isinstance(cell_data, dict):
                    if cell_data.get('is_engine') and cell_data.get('link_sheet'):
                        pass  # HYPERLINK written in Phase 2
                    else:
                        ws.cell(row=row, column=col, value=cell_data.get('text', ''))
                else:
                    ws.cell(row=row, column=col, value=str(cell_data))

        # ── Zone 4 Content (Conso. col) ──
        for i, cell_data in enumerate(cfg.get('zone4', [])):
            row = 8 + i
            if isinstance(cell_data, dict):
                if cell_data.get('is_engine') and cell_data.get('link_sheet'):
                    pass  # HYPERLINK in Phase 2
                else:
                    ws.cell(row=row, column=lay['conso'],
                            value=cell_data.get('text', ''))

        # ── All cluster engines (Zones 5, 6, 7) ──
        all_eng = cfg.get('all_engines', {})
        for ai in range(lay['a']):
            arow = lay['all_start'] + ai
            # Zone 5 — feature cols
            z5 = all_eng.get('zone5', [])
            if ai < len(z5):
                items = z5[ai] if isinstance(z5[ai], list) else [z5[ai]]
                for fi, eng in enumerate(items):
                    if eng:
                        ws.cell(row=arow, column=lay['z2_start'] + fi, value=eng)
            # Zone 6 — conso col
            z6 = all_eng.get('zone6', [])
            if ai < len(z6) and z6[ai]:
                ws.cell(row=arow, column=lay['conso'], value=z6[ai])
            # Zone 7 — mở rộng cols
            z7 = all_eng.get('zone7', [])
            if ai < len(z7):
                mr = z7[ai] if isinstance(z7[ai], list) else [z7[ai], '']
                if len(mr) > 0 and mr[0]:
                    ws.cell(row=arow, column=lay['mr1'], value=mr[0])
                if len(mr) > 1 and mr[1]:
                    ws.cell(row=arow, column=lay['mr2'], value=mr[1])

        # ── Common cluster engines (Zones 8, 9) ──
        com_eng = cfg.get('common_engines', {})
        for ci in range(lay['c']):
            crow = lay['common_start'] + ci
            # Zone 8 — conso col
            z8 = com_eng.get('zone8', [])
            if ci < len(z8) and z8[ci]:
                ws.cell(row=crow, column=lay['conso'], value=z8[ci])
            # Zone 9 — mở rộng cols
            z9 = com_eng.get('zone9', [])
            if ci < len(z9):
                mr = z9[ci] if isinstance(z9[ci], list) else [z9[ci], '']
                if len(mr) > 0 and mr[0]:
                    ws.cell(row=crow, column=lay['mr1'], value=mr[0])
                if len(mr) > 1 and mr[1]:
                    ws.cell(row=crow, column=lay['mr2'], value=mr[1])

        # ── PHẦN MỞ RỘNG Headers ──
        ws.cell(row=4, column=lay['mr1'], value='(1)')
        ws.cell(row=4, column=lay['mr2'], value='(2)')
        ws.cell(row=5, column=lay['mr1'], value='Common')
        ws.cell(row=6, column=lay['mr1'], value='-')
        ws.cell(row=6, column=lay['mr2'], value='-')
        ws.cell(row=7, column=lay['mr1'], value='-')
        ws.cell(row=7, column=lay['mr2'], value='-')

    # ──────────────────────────────────────────────
    # PHASE 2: FORMULAS
    # ──────────────────────────────────────────────

    def _phase2_formulas(self, ws, cfg):
        """Write all formulas AFTER data is in place."""
        lay = self._get_layout(cfg)

        # E5 = =B5 (mirrors GNM code)
        ws.cell(row=5, column=5).value = '=B5'
        # E8 = =B5 (mirrors GNM code as Object anchor)
        ws.cell(row=8, column=5).value = '=B5'

        # Back-link at A1 (non-root sheets only)
        if not cfg.get('is_root', True) and cfg.get('parent_sheet'):
            parent = cfg['parent_sheet']
            ws.cell(row=1, column=1).value = (
                f'=HYPERLINK("#\'{parent}\'!A1", "<<")'
            )

        # Zone 3 HYPERLINK formulas
        for i, row_data in enumerate(cfg.get('zone3', [])):
            row = 8 + i
            for fi, cell_data in enumerate(row_data):
                col = lay['z2_start'] + fi
                if (isinstance(cell_data, dict)
                        and cell_data.get('is_engine')
                        and cell_data.get('link_sheet')):
                    sheet = cell_data['link_sheet']
                    text  = cell_data['text']
                    ws.cell(row=row, column=col).value = (
                        f'=HYPERLINK("#\'{sheet}\'!B2", "{text}")'
                    )

        # Zone 4 HYPERLINK formulas
        for i, cell_data in enumerate(cfg.get('zone4', [])):
            row = 8 + i
            if (isinstance(cell_data, dict)
                    and cell_data.get('is_engine')
                    and cell_data.get('link_sheet')):
                sheet = cell_data['link_sheet']
                text  = cell_data['text']
                ws.cell(row=row, column=lay['conso']).value = (
                    f'=HYPERLINK("#\'{sheet}\'!B2", "{text}")'
                )

    # ──────────────────────────────────────────────
    # PHASE 3: MEDIUM BORDERS
    # ──────────────────────────────────────────────

    def _phase3_medium_borders(self, ws, cfg):
        """Apply medium border outlines around each major section."""
        lay = self._get_layout(cfg)
        end = lay['end_row']

        def outline(min_row, max_row, min_col, max_col):
            for row in range(min_row, max_row + 1):
                for col in range(min_col, max_col + 1):
                    cell = ws.cell(row=row, column=col)
                    eb = cell.border  # existing border
                    cell.border = Border(
                        left   = self.MEDIUM if col == min_col else eb.left,
                        right  = self.MEDIUM if col == max_col else eb.right,
                        top    = self.MEDIUM if row == min_row else eb.top,
                        bottom = self.MEDIUM if row == max_row else eb.bottom,
                    )

        # Phần Đầu outline: B4:C[end]
        outline(4, end, 2, 3)
        # Phần Thân outline: E4:[conso][end]
        outline(4, end, 5, lay['conso'])
        # Phần Mở rộng outline: [mr1]4:[mr2][end]
        outline(4, end, lay['mr1'], lay['mr2'])

    # ──────────────────────────────────────────────
    # PHASE 4: THIN BORDERS (overlay)
    # ──────────────────────────────────────────────

    def _phase4_thin_borders(self, ws, cfg):
        """Apply thin top borders for All/Common cluster separation.

        CRITICAL ASYMMETRY RULE:
        - All cluster:    thin top on C only (NOT B)
        - Common cluster: thin top on BOTH B and C
        """
        lay = self._get_layout(cfg)

        def add_thin_top(row, col):
            cell = ws.cell(row=row, column=col)
            eb = cell.border
            cell.border = Border(
                top=self.THIN,
                left=eb.left, right=eb.right, bottom=eb.bottom,
            )

        # ── All cluster top border ──
        all_row = lay['all_start']
        # Phần Đầu: C only (NOT B) — asymmetry rule
        add_thin_top(all_row, 3)
        # Phần Thân: all cols E through conso
        for col in range(5, lay['conso'] + 1):
            add_thin_top(all_row, col)
        # Phần Mở rộng: mr1, mr2
        for col in [lay['mr1'], lay['mr2']]:
            add_thin_top(all_row, col)

        # ── Common cluster top border ──
        com_row = lay['common_start']
        # Phần Đầu: BOTH B and C
        for col in [2, 3]:
            add_thin_top(com_row, col)
        # Phần Thân: all cols E through conso
        for col in range(5, lay['conso'] + 1):
            add_thin_top(com_row, col)
        # Phần Mở rộng: mr1, mr2
        for col in [lay['mr1'], lay['mr2']]:
            add_thin_top(com_row, col)

    # ──────────────────────────────────────────────
    # PHASE 5: FORMATTING
    # ──────────────────────────────────────────────

    def _phase5_formatting(self, ws, cfg):
        """Apply fills, fonts, alignment, wrap text, column widths, row heights."""
        lay = self._get_layout(cfg)

        # ── Column widths ──
        ws.column_dimensions['A'].width = 3                                    # separator
        ws.column_dimensions['B'].width = 14                                   # Phần Đầu
        ws.column_dimensions['C'].width = 14                                   # Phần Đầu
        ws.column_dimensions['D'].width = 3                                    # separator
        ws.column_dimensions['E'].width = 14                                   # Zone 1
        ws.column_dimensions['F'].width = 14                                   # Zone 1
        if lay['L2']:
            ws.column_dimensions['G'].width = 14                               # Zone 1 L2
        for col in range(lay['z2_start'], lay['z2_end'] + 1):
            ws.column_dimensions[get_column_letter(col)].width = 28            # Zone 2-3
        ws.column_dimensions[get_column_letter(lay['conso'])].width = 28       # Conso.
        ws.column_dimensions[get_column_letter(lay['sep2'])].width = 3         # separator
        ws.column_dimensions[get_column_letter(lay['mr1'])].width = 14         # Mở rộng
        ws.column_dimensions[get_column_letter(lay['mr2'])].width = 14         # Mở rộng

        # ── Row heights ──
        ws.row_dimensions[2].height = 30   # title row
        ws.row_dimensions[4].height = 24   # header row
        ws.row_dimensions[5].height = 24   # sub-header row

        # ── B2 title ──
        b2 = ws.cell(row=2, column=2)
        b2.font = self.TITLE_FONT
        b2.fill = self.WHT_FILL
        b2.alignment = self.NO_WRAP_NI

        # ── A1 back-link ──
        if not cfg.get('is_root', True):
            a1 = ws.cell(row=1, column=1)
            a1.font = self.BACK_FONT
            a1.alignment = self.NO_WRAP_NI

        # ── Row 4: Header styling (HDR_FILL + HDR_FONT) ──
        for col in [2, 3]:                                   # Phần Đầu
            c = ws.cell(row=4, column=col)
            c.font = self.HDR_FONT; c.fill = self.HDR_FILL; c.alignment = self.NO_WRAP
        for col in range(5, lay['conso'] + 1):               # Phần Thân
            c = ws.cell(row=4, column=col)
            c.font = self.HDR_FONT; c.fill = self.HDR_FILL; c.alignment = self.NO_WRAP
        for col in [lay['mr1'], lay['mr2']]:                  # Phần Mở rộng
            c = ws.cell(row=4, column=col)
            c.font = self.HDR_FONT; c.fill = self.HDR_FILL; c.alignment = self.NO_WRAP

        # ── Row 5: Sub-header styling ──
        # B5: white bg, bold
        ws.cell(row=5, column=2).font = self.SUB_FONT
        ws.cell(row=5, column=2).fill = self.WHT_FILL
        ws.cell(row=5, column=2).alignment = self.NO_WRAP
        # C5-C7: DDEBF7 bg, number format 0;(0) so negative shows as (n)
        for r in [5, 6, 7]:
            c = ws.cell(row=r, column=3)
            c.fill = self.SUB_FILL
            c.alignment = self.NO_WRAP
            c.number_format = '0;(0)'
        # B6, B7: white bg
        for r in [6, 7]:
            ws.cell(row=r, column=2).fill = self.WHT_FILL

        # E5 through Conso R5: DDEBF7, bold
        for col in range(5, lay['conso'] + 1):
            c = ws.cell(row=5, column=col)
            c.fill = self.SUB_FILL; c.font = self.SUB_FONT; c.alignment = self.NO_WRAP
        # Mở rộng R5
        c = ws.cell(row=5, column=lay['mr1'])
        c.fill = self.SUB_FILL; c.font = self.SUB_FONT; c.alignment = self.NO_WRAP
        ws.cell(row=5, column=lay['mr2']).fill = self.SUB_FILL

        # ── Rows 6-7: Zone headers (DDEBF7, wrap text) ──
        for r in [6, 7]:
            for col in range(5, lay['conso'] + 1):
                c = ws.cell(row=r, column=col)
                c.fill = self.SUB_FILL; c.font = self.NORM_FONT; c.alignment = self.WRAP
            for col in [lay['mr1'], lay['mr2']]:
                c = ws.cell(row=r, column=col)
                c.fill = self.SUB_FILL; c.font = self.NORM_FONT; c.alignment = self.WRAP

        # ── Content rows (8 to end_row) ──
        for row in range(8, lay['end_row'] + 1):
            # Phần Đầu (B-C)
            for col in [2, 3]:
                c = ws.cell(row=row, column=col)
                c.fill = self.WHT_FILL; c.font = self.NORM_FONT
                c.alignment = self.NO_WRAP

            # Zone 1 cols (E, F, and G if L2)
            for col in range(5, 7 + lay['L2']):
                c = ws.cell(row=row, column=col)
                c.fill = self.WHT_FILL; c.font = self.NORM_FONT
                c.alignment = self.WRAP

            # Zone 2-3 + Conso cols
            for col in range(lay['z2_start'], lay['conso'] + 1):
                c = ws.cell(row=row, column=col)
                c.fill = self.WHT_FILL; c.alignment = self.WRAP
                # Engine text = blue (contains HYPERLINK or engine name pattern)
                val = str(c.value or '')
                if '=HYPERLINK' in val or (
                    '(' in val and ')' in val and len(val) > 5
                ):
                    c.font = self.ENG_FONT
                else:
                    c.font = self.NORM_FONT

            # Mở rộng cols
            for col in [lay['mr1'], lay['mr2']]:
                c = ws.cell(row=row, column=col)
                c.fill = self.WHT_FILL; c.alignment = self.WRAP
                val = str(c.value or '')
                if '(' in val and ')' in val and len(val) > 5:
                    c.font = self.ENG_FONT
                else:
                    c.font = self.NORM_FONT
```

## Usage Example

```python
builder = GNMBuilder()

# ── Sheet 1: Template C (f=1, L2=0) — Single Feature ──
builder.add_sheet({
    'sheet_name': 'RCP (A)',
    'gnm_title': 'RETAIL CHANNEL PARTNERSHIP (A)',
    'gnm_code': 'RCP',
    'is_root': True,
    'parent_sheet': None,
    'f': 1, 'L2': 0,
    'feature_group': 'Channel Partnership Strategy',
    'features': ['-'],
    'items': [
        {'level1': 'Embedded Finance'},
        {'level1': 'Banca & Protection'},
        {'level1': 'Platform & API'},
        {'level1': 'Agent & Franchise'},
        {'level1': 'Co-Brand Alliance'},
    ],
    'zone3': [
        [{'text': 'Embedded Finance Strategy EMF (B)',
          'is_engine': True, 'link_sheet': 'EMF (B)'}],
        [{'text': 'Banca Partnership Strategy BCP (B)',
          'is_engine': True, 'link_sheet': 'BCP (B)'}],
        [{'text': 'Platform API Strategy PLT (B)',
          'is_engine': True, 'link_sheet': 'PLT (B)'}],
        [{'text': 'Agent Franchise Model AFM (B)',
          'is_engine': True, 'link_sheet': 'AFM (B)'}],
        [{'text': 'Co-Brand Alliance Strategy CBA (B)',
          'is_engine': True, 'link_sheet': 'CBA (B)'}],
    ],
    'zone4': [
        {'text': 'Embedded Finance Playbook EMF (B)',
         'is_engine': True, 'link_sheet': 'EMF (B)'},
        {'text': 'Banca Playbook BCP (B)',
         'is_engine': True, 'link_sheet': 'BCP (B)'},
        {'text': 'Platform Playbook PLT (B)',
         'is_engine': True, 'link_sheet': 'PLT (B)'},
        {'text': 'Agent Playbook AFM (B)',
         'is_engine': True, 'link_sheet': 'AFM (B)'},
        {'text': 'CoBrand Playbook CBA (B)',
         'is_engine': True, 'link_sheet': 'CBA (B)'},
    ],
    'all_engines': {
        'zone5': [[], []],
        'zone6': [
            'Partnership Operating Model POM (B)',
            'Channel Economics CEC (B)',
        ],
        'zone7': [['', ''], ['', '']],
    },
    'common_engines': {
        'zone8': ['', ''],
        'zone9': [
            ['RB Distribution BNW (A)', ''],
            ['Digital Platform DIG (A)', ''],
        ],
    },
})

# ── Sheet 2: Template A (f=2, L2=0) — Two Features ──
builder.add_sheet({
    'sheet_name': 'MCM (A)',
    'gnm_title': 'MARKETING COMMUNICATIONS (A)',
    'gnm_code': 'MCM',
    'is_root': False,
    'parent_sheet': 'VBM (A)',
    'f': 2, 'L2': 0,
    'feature_group': 'Marketing Capability',
    'features': ['Brand Strategy', 'Digital Marketing'],
    'items': [
        {'level1': 'Content Marketing'},
        {'level1': 'Performance Marketing'},
        {'level1': 'Brand Management'},
    ],
    'zone3': [
        [
            {'text': 'Content Strategy CNT (B)',
             'is_engine': True, 'link_sheet': 'CNT (B)'},
            {'text': 'Digital Content DCN (B)',
             'is_engine': True, 'link_sheet': 'DCN (B)'},
        ],
        [
            {'text': 'Perf Marketing PMK (B)',
             'is_engine': True, 'link_sheet': 'PMK (B)'},
            {'text': 'Digital Ads DAD (B)',
             'is_engine': True, 'link_sheet': 'DAD (B)'},
        ],
        [
            {'text': 'Brand Framework BFW (B)',
             'is_engine': True, 'link_sheet': 'BFW (B)'},
            {'text': 'Digital Brand DBR (B)',
             'is_engine': True, 'link_sheet': 'DBR (B)'},
        ],
    ],
    'zone4': [
        {'text': 'Content Playbook CNT (B)',
         'is_engine': True, 'link_sheet': 'CNT (B)'},
        {'text': 'Performance Playbook PMK (B)',
         'is_engine': True, 'link_sheet': 'PMK (B)'},
        {'text': 'Brand Playbook BFW (B)',
         'is_engine': True, 'link_sheet': 'BFW (B)'},
    ],
    'all_engines': {
        'zone5': [['Omni-Channel OCH (B)', ''], ['MarTech Stack MTS (B)', '']],
        'zone6': ['Marketing Ops MOP (B)', 'Analytics Platform ANP (B)'],
        'zone7': [['', ''], ['', '']],
    },
    'common_engines': {
        'zone8': ['', ''],
        'zone9': [['Data Platform DPL (A)', ''], ['CRM System CRM (A)', '']],
    },
})

# ── Sheet 3: Template B (f=2, L2=1) — Two Features + Level 2 ──
builder.add_sheet({
    'sheet_name': 'PRD (B)',
    'gnm_title': 'PRODUCTION & SUPPLY CHAIN (B)',
    'gnm_code': 'PRD',
    'is_root': False,
    'parent_sheet': 'MCM (A)',
    'f': 2, 'L2': 1,
    'feature_group': 'Production Capability',
    'features': ['Manufacturing', 'Logistics'],
    'items': [
        {'level1': 'Assembly Line', 'level2': 'Auto Assembly'},
        {'level1': 'Assembly Line', 'level2': 'Manual Assembly'},
        {'level1': 'Quality Control', 'level2': None},
        {'level1': 'Packaging', 'level2': 'Standard Pack'},
    ],
    'zone3': [
        [
            {'text': 'Auto Assembly AAM (C)',
             'is_engine': True, 'link_sheet': 'AAM (C)'},
            {'text': 'Auto Logistics ALG (C)',
             'is_engine': True, 'link_sheet': 'ALG (C)'},
        ],
        [
            {'text': 'Manual Process MNP (C)',
             'is_engine': True, 'link_sheet': 'MNP (C)'},
            {'text': 'Manual Ship MSH (C)',
             'is_engine': True, 'link_sheet': 'MSH (C)'},
        ],
        [
            {'text': 'QC Framework QCF (C)',
             'is_engine': True, 'link_sheet': 'QCF (C)'},
            {'text': 'QC Logistics QCL (C)',
             'is_engine': True, 'link_sheet': 'QCL (C)'},
        ],
        [
            {'text': 'Pack Standard PST (C)',
             'is_engine': True, 'link_sheet': 'PST (C)'},
            {'text': 'Pack Ship PSH (C)',
             'is_engine': True, 'link_sheet': 'PSH (C)'},
        ],
    ],
    'zone4': [
        {'text': 'Auto Playbook AAM (C)',
         'is_engine': True, 'link_sheet': 'AAM (C)'},
        {'text': 'Manual Playbook MNP (C)',
         'is_engine': True, 'link_sheet': 'MNP (C)'},
        {'text': 'QC Playbook QCF (C)',
         'is_engine': True, 'link_sheet': 'QCF (C)'},
        {'text': 'Pack Playbook PST (C)',
         'is_engine': True, 'link_sheet': 'PST (C)'},
    ],
    'all_engines': {
        'zone5': [['Lean Ops LOP (C)', ''], ['Supply Chain SCM (C)', '']],
        'zone6': ['Production Ops POP (C)', 'Warehouse WHS (C)'],
        'zone7': [['', ''], ['', '']],
    },
    'common_engines': {
        'zone8': ['', ''],
        'zone9': [['ERP System ERP (B)', ''], ['IoT Platform IOT (B)', '']],
    },
})

builder.build('/path/to/output.xlsx')
```

## Phần Đầu Content Map (Critical — Most Error-Prone)

This table shows EXACT content for every cell in Phần Đầu (cols B-C):

| Row | Col B | Col C | Notes |
|-----|-------|-------|-------|
| R4 | `(1)` | `(2)` | Header. `#0070C0` bg, white bold text |
| R5 | `{GNM_CODE}` | `-1` (formatted as `(1)`) | Sub-header. B=white bg, C=`#DDEBF7` bg. Number format: `0;(0)` |
| R6 | *(empty)* | `-2` (formatted as `(2)`) | B=white bg, C=`#DDEBF7` bg |
| R7 | *(empty)* | `-3` (formatted as `(3)`) | B=white bg, C=`#DDEBF7` bg |
| R8 | *(empty)* | `1` | Content numbering starts. White bg |
| R9 | *(empty)* | `2` | |
| ... | *(empty)* | `n` | |
| R[8+n] | *(empty)* | `All` | All cluster. **Thin top border on C only, NOT B** |
| R[9+n] | *(empty)* | *(empty)* | |
| R[8+n+a] | `Common` | `-` | Common cluster. **Thin top border on BOTH B and C** |
| R[9+n+a] | *(empty)* | *(empty)* | |

## Border Asymmetry Rule (Critical)

- **All cluster top border:** Thin on C only (not B) — visually separates Content from All in Phần Đầu while keeping B continuous
- **Common cluster top border:** Thin on BOTH B and C — fully separates Common section

This asymmetry is the single most common Excel generation mistake. The `_phase4_thin_borders` method handles it explicitly.

## Zone Empty Rules (Critical)

| Cluster | Zone 1 cols (E-F/G) | Zone 2-3 cols | Conso. col | Mở rộng cols |
|---------|---------------------|---------------|------------|-------------|
| **Content** (R8+) | Items | Values/Engines | Zone 4 engines | *(empty)* |
| **All** | **EMPTY** | Zone 5 engines | Zone 6 engines | Zone 7 engines |
| **Common** | **EMPTY** | **EMPTY** | Zone 8 engines | Zone 9 engines |

## Template Scaling Summary

| Template | f | L2 | Zone 2 start | Conso. col | Total Phần Thân cols |
|----------|---|-----|-------------|------------|---------------------|
| C | 1 | 0 | G (7) | H (8) | 4 |
| A | 2 | 0 | G (7) | I (9) | 5 |
| B | 2 | 1 | H (8) | J (10) | 6 |
| *(f=3, L2=0)* | 3 | 0 | G (7) | J (10) | 6 |
| *(f=3, L2=1)* | 3 | 1 | H (8) | K (11) | 7 |
| *(f=4, L2=0)* | 4 | 0 | G (7) | K (11) | 7 |
| *(f=5, L2=0)* | 5 | 0 | G (7) | L (12) | 8 |

The `_get_layout()` method handles all scaling automatically. No hardcoded column letters.

## Cell Merge Rules

- **B2 (Tên GNM):** Merge B2 to Conso. column (e.g., B2:H2 for f=1/L2=0; B2:I2 for f=2/L2=0)
- **Zone headers (R6):** Feature Group name in Zone 2 col 1 only; remaining Zone 2 cols R6 are empty (NOT merged)
- **Separator columns (A, D, post-Conso):** No content, no merge — just set width to 3
- **Never merge** Zone 3 value/engine cells, Zone 1 item cells, or All/Common content cells

## Engine HYPERLINK Patterns

```python
# Parent → Sub link (Zone 3/4 engine linking to child sheet)
'=HYPERLINK("#\'PRD (B)\'!B2", "Production & Supply Chain PRD (B)")'

# Sub → Parent back-link (A1 of child sheet)
'=HYPERLINK("#\'VBM (A)\'!A1", "<<")'
```

Both are Excel formulas, not openpyxl Hyperlink objects. Written as string values starting with `=`.
