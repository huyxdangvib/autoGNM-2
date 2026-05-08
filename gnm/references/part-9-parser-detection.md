---
part: 9
name: "Parser: Fingerprint & Layout Detection"
parent: gnm-instruction.md
---


<part9_parser>

# PART 9: GNM EXCEL PARSER

> **TL;DR:** Protocol for reading existing .xlsx files and extracting GNM semantic structure (AST). Enables intelligent REVIEW, MODIFY, and DIFF operations by parsing raw Excel into zone-mapped data. Uses openpyxl.

> **When to use:** REVIEW (reads user's Excel), MODIFY (reads then modifies), DIFF (reads two files), EXPORT (reads then converts to JSON).


## GNM Fingerprint Detection

Before parsing, verify the file IS a GNM workbook by checking fingerprint signals:

| Signal | Cell/Pattern | Expected | Confidence |
|--------|-------------|----------|------------|
| **Name cell** | B2 | Non-empty text, MUST end with `(A)`, `(B)`, `(C)`, `(D)`, `(Z)`, `(Z1)`, `(Z2)` | High |
| **Code cell** | B5 | 2-4 uppercase letters | High |
| **Formula E5** | E5 | Formula `=B5` or same value as B5 | High |
| **Header colors** | Row 4 fill | `#0070C0` (blue) | High |
| **Sub-header colors** | Row 5 fill | `#DDEBF7` (light blue) | Medium |
| **3-color palette** | All cells | Only `#0070C0`, `#DDEBF7`, `#FFFFFF` backgrounds | Medium |
| **Object label** | E6 | Text "Object" | High |
| **Item label** | E7 | Text "Item" | High |
| **Separator cols** | A, D | Empty, narrow width (~20px) | Medium |
| **Formula error tokens** | Any cell | No `#REF!`, `#NAME?`, `#NULL!`, `#DIV/0!`, `#VALUE!`, `#N/A`, `#NUM!` | High (negative signal) |

**Level suffix validation:** B2 MUST end with a parenthesized level in
{A, B, C, D, E, F, G, Z, Z1, Z2}. Any other suffix (e.g. `(SDP)`) is a WARN —
report the sheet as `level=UNKNOWN` and flag for producer review.
D-level is the execution-decomposition hub between C and Z (see Part 6).
E/F/G are intermediate rungs between D and Z for meta-cognitive / taxonomy-engineering cascades:
E = lifecycle × product matrix, F = strategy-flow hub, G = classification/selection catalog.
See Part 6 § "E/F/G: Intermediate Cascade Levels" for compliance targets.

**Business-code-as-suffix anti-pattern (codified 2026-04-21, v5.12.0):** When B2 suffix
equals the B5 business code (e.g. B5=`PNS`, B2 ends with `(PNS)`), this is the
**orphan-scaffold anti-pattern** — a template sheet where the level letter was
accidentally overwritten with the business code. Parser emits RED finding:
`"B2 level-suffix = business code (PNS); expected (Z) or another level letter.
Likely orphan-scaffold template. Recommend: fix B2 to end with correct level
letter AND add parent cascade link."` Do NOT emit `level=UNKNOWN` in this case —
infer level from Z3 density / Z1 structure heuristic. Evidence: VEM-family
3-workbook (2026-04-21) — `PNS (Z)` tab with B2=`PRODUCT NORMAL STANDARDIZATION
(PNS)`, zero Z3 content, no inbound cascade — 3/3 workbooks. `[exploratory-basis: 3-workbook]`

**Disambiguation note (`(G)` semantics):** `(G)` ALWAYS denotes Level G when it is the
final parenthesized token in B2 — never a grid/type variant. If a future workbook needs
to declare a grid-variant on a typed level, use a composite suffix `(X-G)` (reserved,
not yet in production). Bare `(G)` = Level G.

**Formula-error scan (codified 2026-04-21, v5.12.0):** During parse, scan every cell's
computed value for Excel error tokens `#REF!`, `#NAME?`, `#NULL!`, `#DIV/0!`, `#VALUE!`,
`#N/A`, `#NUM!`. Any hit emits a RED finding (`formula-error: {token} at {sheet}!{cell}`).
Do NOT abort the parse on first hit — continue and aggregate all error cells into the
review report. Typical cause: formulas copy-pasted from a source workbook whose
cross-workbook references became dangling when the source was deleted or moved.
Evidence: `2(F)` sheet in VEM org-chart — 28 cells in cols X/Y rows 34-47 carry
`=#REF!+#REF!` live errors (2026-04-21). `[exploratory-basis: 3-workbook]`

**Tab-name whitespace check (codified 2026-04-21, v5.12.0):** During Step 1 sheet
enumeration, strip each tab name and compare to the original; if they differ
(leading or trailing whitespace present), emit AMBER finding
(`tab-name-whitespace: '{raw_name}' has leading/trailing whitespace`). Rationale:
HYPERLINK formulas targeting the sheet (`=HYPERLINK("#'{name}'!...")`) break
silently if the formula omits the whitespace. Evidence: `AFD (E) ` tab (trailing
space) in VEM myvib workbook (2026-04-21). `[exploratory-basis: 3-workbook]`

**draft_state flag resolution (codified 2026-04-21, v5.12.0):** During Step 1 sheet
enumeration, parser MUST read the A-level root sheet's Conso cell (I5). If value
`draft_state=true`, subsequent per-cell bridge-pattern AMBER findings (see Part 3a
§ Draft-State Bridge Pattern) aggregate into a single workbook-level AMBER summary
rather than per-cell output. Precedence: dangling-refs, formula errors (#REF! et al.),
orphan-scaffold anti-pattern, and tab-whitespace findings continue to emit at their
original severity regardless of the flag — they are not draft-state symptoms.
`[exploratory-basis: 3-workbook]`

**Confidence thresholds:**
- ≥5 High signals: Confirmed GNM → proceed with full parse
- 3-4 High signals: Likely GNM → parse with warnings
- <3 High signals: Not a GNM → abort and report

## Parse Protocol (7 Steps)

### Step 1: Sheet Enumeration

```python
import openpyxl
wb = openpyxl.load_workbook(filepath, data_only=False)
sheets = []
for name in wb.sheetnames:
    ws = wb[name]
    if ws['B2'].value:  # Non-empty B2 = potential GNM sheet
        sheets.append({
            'name': name,
            'code': ws['B5'].value,
            'level': _extract_level(ws['B2'].value),  # Parse (A)/(B)/(C)/(D)/(Z)/(Z1)/(Z2) from name
            'has_backlink': ws['A1'].value == '<<' or '<<' in str(ws['A1'].value or '')
        })
```

### Step 2: Column Layout Detection

For each sheet, detect the column structure dynamically:

```python
def detect_columns(ws):
    # Find Zone 2 start: first column after F (or G if L2) with content in row 6 or 7
    has_level2 = ws['G7'].value == '-' and ws['G6'].value in (None, '', '-')
    zone2_start = 'H' if has_level2 else 'G'
    
    # Count features: scan row 7 from zone2_start until hitting Conso. marker
    features = []
    col = column_index_from_string(zone2_start)
    while True:
        cell_r5 = ws.cell(row=5, column=col)
        cell_r7 = ws.cell(row=7, column=col)
        if cell_r5.value and 'Conso' in str(cell_r5.value):
            conso_col = col
            break
        if cell_r7.value and cell_r7.value != '-':
            features.append({'col': col, 'name': cell_r7.value})
        elif cell_r7.value == '-' and not features:
            # Single-Feature: feature name is in R6, R7="-"
            features.append({'col': col, 'name': ws.cell(row=6, column=col).value})
        col += 1
        if col > 20:  # Safety limit
            break
    
    return {
        'has_level2': has_level2,
        'zone2_start': zone2_start,
        'features': features,
        'conso_col': conso_col,
        'feature_count': len(features)
    }
```

