---
part: 5
name: "Format I: Markdown Export (Excel → Markdown)"
parent: gnm-instruction.md
version: "1.0.0"
---

## Format I: MARKDOWN EXPORT (GNM Excel → Markdown)

> **Purpose:** Standardized, machine-parseable markdown representation of GNM Excel workbooks. Enables downstream HTML/web rendering, version control (diffable), LLM context injection, and cross-tool interoperability.
>
> **Trigger:** EXPORT task with `--format md` or `--format markdown`, or when user requests "convert to markdown", "export as markdown", "xuất ra markdown".

---

### Design Principles

1. **One sheet = one `##` section** — each GNM sheet maps to a level-2 heading
2. **Bullet lists for multi-item fields** — Conso and Common items MUST use bullet lists, NEVER comma-separated
3. **Pipe tables for Zone 1-3 data** — standard markdown tables with alignment
4. **Semantic labels** — bold labels (`**Code:**`, `**Conso.:**`) for structured extraction
5. **Separator between sheets** — horizontal rule `---` between each sheet section
6. **Preserves GNM zone structure** — Phần Đầu (index), Phần Thân (zones 1-6, 8), Phần Mở rộng (zones 7, 9) mapped to table columns

---

### File Structure

```markdown
# {WORKBOOK TITLE} ({Level})

> Exported from: `{source_filename.xlsx}` | Date: {YYYY-MM-DD}
> Full GNM 9-zone structure with phân tầng (hierarchical zoning) preserved

**GNM Phân Tầng Legend:**
- **Row -1** = Code row (BM1, RBC, etc.)
- **Row -2 (Object)** = Zone group labels → shown as `[Zone: label → col1, col2, ...]`
- **Row -3 (Item)** = Individual column headers
- **Row All** = Consolidated/Common summary references

---

{Sheet sections...}
```

---

### Sheet Section Template

Each GNM sheet follows this exact structure:

```markdown
## Sheet: {sheet_id} ({sheet_level}) — {GNM_NAME} ({gnm_level})

**Code:** {CODE}
```

Where:
- `{sheet_id}` = Excel tab identifier (BMA, 1, 1.3, 2, 2.1, etc.)
- `{sheet_level}` = Position in cascade hierarchy (A=root workbook, B=main sheets, C=sub-GNMs)
- `{GNM_NAME}` = Full GNM name from cell B2
- `{gnm_level}` = The GNM's own Level designation from B2 (A/B/C/Z/Z1)

> **Note:** `{sheet_level}` and `{gnm_level}` often match but can differ. Example: `Sheet: 1.3 (C) — IMPLEMENTATION PLAN (Z)` — the sheet is at cascade depth C but the GNM itself is Level Z (cross-cutting). `Sheet: 6.1 (C) — HOUSEHOLD AUR STRATEGY (B)` — cascade depth C but GNM is Level B.

**Phân tầng (Object row -2):**
- `[Zone: {zone_group_label} → {col1}, {col2}, ...]`
- `[Zone: {zone_group_label_2} → {col1}, {col2}, ...]`

| # | - | {Feature1} | {Feature2} | ... | Conso. | Common |
|---|---|------------|------------|-----|--------|--------|
| 1 | {Item1} | {Z3 value} | {Z3 value} | ... | {Z4 engine} | {Z7 engine} |
| 2 | {Item2} | {Z3 value} | {Z3 value} | ... | {Z4 engine} | {Z7 engine} |
| ... | ... | ... | ... | ... | ... | ... |
| All | | {Z5 engine} | {Z5 engine} | ... | {Z6 engine} | {Z7 engine} |
| | | | | | {Z8 engine} | {Z9 engine} |

**Conso.:**
- {Item 1} ({reference})
- {Item 2} ({reference})
- {Item 3}

**Common:**
- {Item 1} ({reference})
- {Item 2} ({reference})
- {Item 3}
```

---

### Column Mapping Rules

| GNM Zone | Markdown Column | Content |
|----------|----------------|---------|
| Phần Đầu | `#` column | Row number (1, 2, 3... All, Common) |
| Phần Đầu | `-` column | Item code or group label (from Zone 1) |
| Zone 1 (Items) | First content column or `-` | Item names, level 1 |
| Zone 1 L2 | Second `-` column | Sub-items (if Level 2 exists, add a second `-` column) |
| Zone 2 (Features) | Column headers | Feature names from row 7 |
| Zone 3 (Values) | Data cells | Values, Engine references, or `-` |
| Zone 4 (Conso) | `Conso.` column or **Conso.:** section | Consolidation engines |
| Zone 5 (All×Features) | `All` row × Feature columns | All-row engines |
| Zone 6 (All×Conso) | `All` row × Conso column | All×Conso engines |
| Zone 7 (All×Extension) | `Common` column in header, or **Common:** dedicated section | Extension engines |
| Zone 8 (Common×Conso) | Common row × Conso column | Common×Conso engines |
| Zone 9 (Common×Extension) | Common row × Common columns | Common×Extension engines |

---

### Conso & Common Formatting Rules

> **⚠️ CRITICAL:** These rules prevent downstream HTML/web rendering issues where items collapse into single merged cells.

#### Rule 1: Always Use Bullet Lists

```markdown
<!-- ✅ CORRECT — each item on its own bullet -->
**Conso.:**
- Pricing strategy (RPS)
- Implementation plan (RLI)
- Business HAGT team (BHT)

**Common:**
- Goal & Target (RLG)
- Perf. Dashboard (RLP)
- External analysis
- Internal analysis
```

```markdown
<!-- ❌ WRONG — comma-separated on single line -->
**Conso.:** Pricing strategy (RPS), Implementation plan (RLI), Business HAGT team (BHT)
**Common:** Goal & Target (RLG), Perf. Dashboard (RLP), External analysis, Internal analysis
```

#### Rule 2: Reference Codes in Parentheses

When a Conso/Common item has an Engine reference code, append it in parentheses:
- `- Pricing strategy (RPS)` — Engine code RPS
- `- Implementation plan (12)` — Sheet reference 12
- `- External analysis` — No reference (plain text)

#### Rule 3: Separate Conso and Common Sections

Always output Conso and Common as **separate labeled sections** after the data table. Never merge them into a single line or combine with other content. If a GNM has no Conso/Common engines (Zones 4-9 are empty), omit the sections entirely — do not output empty headers.

#### Rule 4: Order Preservation

List items in the same order as they appear in the Excel rows (top-to-bottom for Conso All rows, then Common rows).

---

### Phân Tầng (Object Row) Encoding

Zone group labels from Excel row 6 (Object row) are encoded as inline code blocks:

```markdown
**Phân tầng (Object row -2):**
- `[Zone: {group_label} → {col1}, {col2}, {col3}]`
```

**Rules:**
- One bullet per zone group
- Arrow `→` separates group name from constituent columns
- Commas separate column names within a group
- If a zone group spans a single column, use: `[Zone: {label} → {col}]`
- If zone groups are paired (e.g., Output + Detail), note in parenthetical: `*Each zone has paired columns: Output + Detail (Link)*`

---

### Data Table Formatting

#### Row Types

| Row Type | `#` Column | `-` Column | Data Columns |
|----------|-----------|------------|--------------|
| **Content rows** | `1`, `2`, `3`... | Item code/label | Zone 3 values |
| **All rows** | `All` | (empty) | Zone 5 engines |
| **Common rows** | (empty) | `Common` or (empty) | Zone 8/9 engines |
| **Sub-header rows** | (empty) | **Bold label** | Category label spanning |

#### Level 2 Items (Dual `-` Columns)

When a GNM has L2 sub-items, the table gets two `-` columns: one for the category group and one for the sub-item:

```markdown
| # | - | - | Feature1 | Feature2 | Conso. |
|---|---|---|----------|----------|--------|
| 1 | Category A | Sub-item 1 | value | value | |
| 2 | | Sub-item 2 | value | value | |
| 3 | Category B | Sub-item 3 | value | value | |
```

This pattern appears in BOD sheets like LIS (Sheet 4.1), RPB (Sheet 5), EAS (Sheet 5.6), RBB (Sheet 6), HAS (Sheet 6.1).

#### Special Common Labeling

When Common items are tied to a specific column rather than spanning all features, use parenthetical annotation:

```markdown
**Common (C&B column):** JG & SBS Scale ()
```

This indicates the Common engine appears only in the C&B feature column, not across all features.
| Empty cell | (leave blank) |
| Dash/placeholder | `-` |
| Checkmark/flag | `X`, `Y`, or descriptive text |
| Bold sub-category | `**{text}**` |
| Numeric value | Number as-is |

#### Multi-Feature Layout

For GNMs with many features (f > 5), if the table becomes too wide:
- Keep all columns — do NOT split into multiple tables
- Use abbreviated column headers if needed
- Let markdown viewers handle horizontal scrolling

---

### Additional Content

When Zone 3 rows contain extra detail rows beyond the main table (e.g., additional Technology rows 6-8):

```markdown
**Additional ({zone_group} rows {N}-{M}):** {content1}, {content2}, {content3}
```

When a sheet has timeline columns with no data:

```markdown
*Note: {column_name} columns ({col1}, {col2}, {col3}) exist in headers but contain no data yet.*
```

---

### Inline Conso/Common in Table (Alternative Layout)

Some GNMs render Conso and Common directly as table columns (when they have per-row engines):

```markdown
| # | - | Feature1 | Feature2 | Conso. | Common |
|---|---|----------|----------|--------|--------|
| 1 | Item1 | value | value | Engine1 (CODE) | |
| 2 | Item2 | value | value | | |
| All | | Z5 engine | Z5 engine | Z6 engine | Z7 engine |
```

When Conso/Common appear **both** inline (per-row) and as summary sections:
- Inline: Per-row Zone 4 engines in the `Conso.` column within the table
- Section: Zone 5-9 summary engines in the `**Conso.:**` / `**Common:**` bullet sections below the table
- This hybrid layout is common for GNMs with per-item consolidation (e.g., LIS, RPB, EAS, HAS)

**Example (hybrid — from BOD LIS sheet):**
```markdown
| # | - | - | Customer Offering | Product Offering | Salesforce Delivery | Conso. |
|---|---|---|---|----|-----|--------|
| 1 | Non-Lending Customer | PnP | PnP Customer Offering | ILP/ULP | PRM | Customer Implementation Plan (4) |
| 6 | Lending Customer | Lending | New Product Offering | Term Life YRT | BSP/RM | |

**Conso.:**
- Customer Offering (1)
- Product Roadmap (2)
- Salesforce Delivery (3)

**Common:**
- Goals
- Business case
- Perf. Dashboard
- Customer Segmentation
```

---

### Multi-Sheet Workbooks

For workbooks with multiple GNM sheets:

1. **Order sheets by sheet ID** (Sheet 1, 1.1, 1.3, 2, 2.1, 3, 3.1, etc.)
2. **Use `---` separator** between each sheet section
3. **Cross-references** — when a cell contains `(2.1)` or similar sheet reference, preserve the reference as-is
4. **Sub-GNM indicator** — sheets with decimal IDs (e.g., `2.1`, `3.1`) are sub-GNMs of the parent integer sheet
5. **Include all sheets** — do not omit empty or sparse sheets

---

### Validation Checklist

Before finalizing markdown export:

- [ ] Every Conso item is on its own bullet line (not comma-separated)
- [ ] Every Common item is on its own bullet line (not comma-separated)
- [ ] Phân tầng uses `[Zone: ...]` inline code format
- [ ] Table headers match Excel column headers
- [ ] All row and Common row are present (not omitted)
- [ ] Sheet sections are separated by `---`
- [ ] Engine references preserve their codes/levels
- [ ] No empty sheet sections (include even if sparse)
- [ ] File header includes source filename and export date

---

> **📌 Retrieval Signpost:** For Zone definitions → PART 3a/3b. For Column Layout rules → PART 2a. For Engine format → PART 5 Technical Specs §4. For JSON export alternative → PART 5 JSON Export.
