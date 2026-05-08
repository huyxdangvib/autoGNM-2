---
part: 14
name: "Excel Generation Playbook"
parent: gnm-instruction.md
version: "5.4.0"
purpose: "Consolidated reference for GENERATE task — translates Build Spec into .xlsx via openpyxl"
token_budget: "~3,000 tokens (replaces loading Parts 2a+2b+4+5+13 = ~19K)"
---

# PART 14: EXCEL GENERATION PLAYBOOK

> **When to use:** GENERATE task type — takes a Build Spec (from CREATE Phase 1) and produces `.xlsx`.
> **Replaces loading:** Parts 2a, 2b, 4, 5 (write order), 13 during Excel generation.
> **Requires:** Python + openpyxl.

## Script-Based Generation (Preferred)

The generic script `scripts/generate-gnm.py` reads a Build Spec JSON and produces a fully-formatted GNM Excel workbook deterministically — no LLM needed for rendering.

```bash
python3 .claude/skills/gnm/scripts/generate-gnm.py <build-spec.json> [output.xlsx]
```

The script implements the complete 5-phase write order, validates the spec, computes layout automatically, and applies all canonical styles. Sections below document the spec format and rules the script follows, which also serve as reference for manual/LLM-based generation.

---

## 1. Build Spec → Excel Pipeline

```
Build Spec YAML/MD  →  Compute Layout  →  5-Phase Write  →  .xlsx
(from CREATE)          (this playbook)     (this playbook)
```

**Input:** A Build Spec containing: GNM name, code, level, f, L2, items[], features[], zone3[][], zone4-9 engines.
**Output:** `.xlsx` file with correct 9-zone structure, styling, formulas, borders.

---

## 2. Layout Computation (from Build Spec parameters)

### Column Position Formula

Given `f` = number of features, `L2` = 1 if Level 2 exists, 0 if not:

```
Zone 1 L0:        col E (always)
Zone 1 L1:        col F (always)
Zone 1 L2:        col G (only if L2=1)
Zone 2 Feature k: col chr(ord('G') + L2 + k - 1)   for k=1..f
Conso (Zone 4):   col chr(ord('G') + L2 + f)
Separator:        col chr(ord('G') + L2 + f + 1)
Mở rộng col 1:    col chr(ord('G') + L2 + f + 2)
Mở rộng col 2:    col chr(ord('G') + L2 + f + 3)
```

### Quick Lookup Table

| f | L2 | Zone2 cols | Conso | Sep | Mở rộng | B2 Merge |
|---|-----|-----------|-------|-----|---------|----------|
| 1 | 0 | G | H | I | J-K | B2:H2 |
| 2 | 0 | G-H | I | J | K-L | B2:I2 |
| 2 | 1 | H-I | J | K | L-M | B2:J2 |
| 3 | 0 | G-I | J | K | L-M | B2:J2 |
| 3 | 1 | H-J | K | L | M-N | B2:K2 |
| 4 | 0 | G-J | K | L | M-N | B2:K2 |
| 4 | 1 | H-K | L | M | N-O | B2:L2 |
| 5 | 0 | G-K | L | M | N-O | B2:L2 |
| 5 | 1 | H-L | M | N | O-P | B2:M2 |

### Row Position Formula

Given `n` = number of items, `a` = All rows, `c` = Common rows:

```
First item row:     8
Last item row:      7 + n
All cluster start:  8 + n
All cluster end:    7 + n + a
Common start:       8 + n + a
Common end:         7 + n + a + c    (= END_ROW)
```

Minimum: a ≥ 2, c ≥ 2. Increase when more engines in Zone 5-7 (All) or Zone 8-9 (Common).

---

## 3. Canonical Styles

```python
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

# Fills
HDR_FILL = PatternFill('solid', fgColor='0070C0')   # Header row 4
SUB_FILL = PatternFill('solid', fgColor='DDEBF7')   # Sub-headers, zone headers
WHT_FILL = PatternFill('solid', fgColor='FFFFFF')   # B2, B5
CONTENT_FILL = PatternFill(patternType='gray0625', fgColor='F2F2F2', bgColor='FFFFFF')

# Fonts
TITLE_FONT = Font(name='Myriad Pro', bold=True, color='000000', size=14)  # B2
HDR_FONT   = Font(name='Myriad Pro', bold=True, color='FFFFFF', size=11)  # Row 4
SUB_FONT   = Font(name='Myriad Pro', bold=True, color='000000', size=11)  # Rows 5-7
VAL_FONT   = Font(name='Myriad Pro', color='000000', size=11)             # Values
ENG_FONT   = Font(name='Myriad Pro', color='0563C1', size=11)             # Engines

# Alignment
WRAP    = Alignment(wrap_text=True, vertical='top', horizontal='left', indent=1)
NO_WRAP = Alignment(wrap_text=False, vertical='top', horizontal='left', indent=1)
NO_WRAP_NI = Alignment(wrap_text=False, vertical='top', horizontal='left')  # B2, A1

# Borders
THIN   = Side(style='thin')
MEDIUM = Side(style='medium')

# Number format for (1), (2), (3)
NEG_FMT = '0;(0);0'
```

### Column Widths

| Column Type | Width | Examples |
|-------------|-------|---------|
| Separator | 3 | A, D, post-Conso separator |
| Phần Đầu | 14 | B, C |
| Zone 1 | 14 | E, F, G (if L2) |
| Zone 2/3 | 28 | Feature columns |
| Conso (Zone 4) | 28 | Conso column |
| Mở rộng | 14 | 2 cols after separator |

### Row Heights
- All rows: 18pt minimum, auto-grow with wrap text

---

## 4. Cell Content Map

### Fixed Cells (every GNM)

| Cell | Content | Font | Fill | Wrap |
|------|---------|------|------|------|
| B2 | `{GNM_NAME}` (merged to Conso col) | TITLE_FONT | WHT | No |
| B4, C4 | -1, -2 (NEG_FMT) | HDR | HDR | No |
| E4+ | -1, -2, -3... (NEG_FMT) | HDR | HDR | No |
| B5 | `{GNM_CODE}` | SUB | WHT | No |
| C5 | -1 (NEG_FMT) | SUB | SUB | No |
| C6 | -2 (NEG_FMT) | SUB | SUB | No |
| C7 | -3 (NEG_FMT) | SUB | SUB | No |
| E5 | `=B5` (formula) | SUB | SUB | No |
| E6 | `Object` | SUB | SUB | Yes |
| E7 | `Item` | SUB | SUB | Yes |
| F6 | (empty) | SUB | SUB | Yes |
| F7 | `-` | SUB | SUB | Yes |
| G7 | `-` (only if L2=1) | SUB | SUB | Yes |
| Conso R5 | `Conso.` | SUB | SUB | No |
| Conso R6-7 | `-` | SUB | SUB | Yes |
| MR col1 R5 | `Common` | SUB | SUB | No |
| MR R6-7 | `-` | SUB | SUB | Yes |

### Dynamic Cells (per Build Spec)

| Area | Rows | Content | Font | Fill |
|------|------|---------|------|------|
| Zone 1 L0 (E8) | 8 only | `=B5` formula | VAL | CONTENT |
| Zone 1 L1 (F) | 8..7+n | Item names (group headers) | VAL | CONTENT |
| Zone 1 L2 (G) | 8..7+n | Sub-item names (if L2=1) | VAL | CONTENT |
| Zone 2 (R6) | 6 | Feature Group name (col 1 only) | SUB | SUB |
| Zone 2 (R7) | 7 | Feature names | SUB | SUB |
| Zone 3 | 8..7+n × feature cols | Values (black) or Engines (blue) | VAL/ENG | CONTENT |
| Zone 4 | 8..7+n × Conso col | Engines (blue) | ENG | CONTENT |
| C8+ | 8..7+n | `=ROW()-ROW($C$7)` formula | VAL | CONTENT |
| C(All start) | 8+n | `All` label | VAL | CONTENT |
| B(Common start) | 8+n+a | `Common` label | VAL | CONTENT |
| C(Common start) | 8+n+a | `-` | VAL | CONTENT |
| Zone 5 | All rows × feature cols | Engines (blue) | ENG | CONTENT |
| Zone 6 | All rows × Conso col | Engines (blue) | ENG | CONTENT |
| Zone 7 | All rows × MR cols | Engines (blue) | ENG | CONTENT |
| Zone 8 | Common rows × Conso col | Engines (blue) | ENG | CONTENT |
| Zone 9 | Common rows × MR cols | Engines (blue) | ENG | CONTENT |

---

## 5. Five-Phase Write Order (MANDATORY)

```
Phase 1: DATA          — All cell values, labels, engines    (all sheets)
Phase 2: FORMULAS      — =B5, =ROW()-ROW($C$7), HYPERLINKs  (all sheets)
Phase 3: MEDIUM BORDER — Section outlines                    (all sheets)
Phase 4: THIN BORDER   — Cluster separators (overlay)        (all sheets)
Phase 5: FORMATTING    — Fills, fonts, alignment, wrap       (all sheets)
```

### Phase 3: Medium Border Outlines

Apply medium border rectangle around each section:
- **Phần Đầu:** B4 : C[END_ROW]
- **Phần Thân:** E4 : {Conso}[END_ROW]
- **Phần Mở rộng:** {MR_col1}4 : {MR_col2}[END_ROW]

### Phase 4: Thin Border Overlays

| Cluster | Phần Đầu | Phần Thân | Phần Mở rộng |
|---------|----------|-----------|--------------|
| **All** (top) | Cell C ONLY (NOT B) | All cols E to Conso | All cols MR1 to MR2 |
| **Common** (top) | Cells B AND C | All cols E to Conso | All cols MR1 to MR2 |

### Phase 5: Formatting Rules

| Area | Wrap | Indent |
|------|------|--------|
| B2 (Title) | No | 0 |
| A1 (Back-link) | No | 0 |
| Row 4 (Header) | No | 1 |
| Row 5 (Sub-header) | No | 1 |
| Rows 6-7 (Zone headers) | Yes | 1 |
| Rows 8+ (all content) | Yes | 1 |

---

## 6. HYPERLINK Patterns

```python
# Parent → Sub-GNM link (in Zone 3/4/5/6 cells)
'=HYPERLINK("#\'PRD (B)\'!B2", "Production & Supply Chain PRD(B)")'

# Sub → Parent back-link (in cell A1)
'=HYPERLINK("#\'VBM (A)\'!A1", "<<")'
```

**Rules:**
- Always use formula `=HYPERLINK(...)`, never Insert → Hyperlink
- Engine name max 50 chars, must be self-descriptive
- Format: `[Full Name] CODE(Level)`

---

## 7. Multi-Sheet Write Order

When generating CASCADE workbooks with multiple sheets:

```python
# ✅ CORRECT: 5 phases sequentially across ALL sheets
for sheet in sheets: write_data(sheet)          # Phase 1
for sheet in sheets: write_formulas(sheet)      # Phase 2
for sheet in sheets: set_medium_border(sheet)   # Phase 3
for sheet in sheets: set_thin_border(sheet)     # Phase 4
for sheet in sheets: set_formatting(sheet)      # Phase 5
```

NEVER process one sheet completely before moving to the next.

---

## 8. Build Spec Format (Input to GENERATE)

The CREATE phase outputs a Build Spec in this format.

**Pre-generation validation (check before writing any cells):**
- `layout.a` ≥ 2 (All cluster minimum 2 rows)
- `layout.c` ≥ 2 (Common cluster minimum 2 rows)
- `layout.f` between 1 and 5 (feature count)
- `layout.n` ≥ 1 (at least 1 item)
- `zone1.items` length == `layout.n`
- `zone3` matrix dimensions == n × f
- `zone4` length == n
- `zone2.features` length == f
- `zone5` row count ≤ `layout.a`
- `zone8`/`zone9` row count ≤ `layout.c`
- If `layout.L2` == 1, every item must have `l2` field
- `gnm.code` is exactly 3 uppercase letters
- `gnm.level` is A, B, C, or Z

If any check fails, STOP and report the error — do not generate a broken workbook.

```yaml
gnm:
  name: "MARKETING & COMMUNICATIONS (A)"
  code: MCM
  level: A
  sheet_name: "MCM (A)"

layout:
  f: 4          # number of features
  L2: 1         # 1=has Level 2, 0=no
  n: 18         # number of items
  a: 2          # All cluster rows
  c: 2          # Common cluster rows

zone2:
  feature_group: "Annual Calendar"
  features: ["Q1 2026", "Q2 2026", "Q3 2026", "Q4 2026"]

zone1:
  items:
    - l1: "Acquisition"
      l2: "Funding"
    - l1: ""              # empty = same L1 group as above
      l2: "Lending"
    # ... remaining items

zone3:
  # matrix[item_index][feature_index] = cell content
  - ["Q1 campaign text", "Q2 text", "Q3 text", "Q4 text"]
  # ... one array per item

zone4:
  # conso engine per item
  - "Funding Acquisition FNA(B)"
  # ... one per item

zone5:  # All cluster, feature cols
  - ["Q1 Review QCR(Z)", "Q2 Review QCR(Z)", "Q3 Review QCR(Z)", "Q4 Review QCR(Z)"]

zone6:  # All cluster, Conso col
  - "Annual MarCom Dashboard AMD(Z)"

zone7:  # All cluster, Mở rộng cols (pairs)
  - ["Channel Mix Strategy CHL(B)", ""]
  - ["Brand Architecture BRA(B)", ""]

zone8:  # Common cluster, Conso col
  - "Enterprise Strategy VES(A)"

zone9:  # Common cluster, Mở rộng cols (pairs)
  - ["Budget & ROI BDG(Z)", ""]
  - ["MarCom Organization MOS(A)", ""]

parent:  # only for sub-GNMs
  sheet: "VBM (A)"
  backlink: true
```

The GENERATE phase reads this spec and produces the Excel file following sections 1-7 above.
