---
part: 2a
name: "Structure Core"
parent: gnm-instruction.md
---

<part2a_structure_core>

# PART 2a: STRUCTURE CORE

> **TL;DR:** PART 2a quy dinh Dynamic Row Position Formula, Column Layout Constraint (authoritative source cho column letters), va Zone Headers Cell Map (rows 6-7). Day la core structural rules — ALWAYS loaded cho CREATE/MODIFY/CONVERT.

> **Retrieval Signpost:** For Visual Templates (A/B/C) and Section Details (Ten GNM, Phan Dau, Phan Than, Phan Mo rong) -> see PART 2b. For core zones (1-3) -> PART 3a. For engine zones (4-9) -> PART 3b. For styling -> PART 4.

## Perspective Binding (Mandatory)

> Source: bod-nextjs production standard (2026-03-30)

Every GNM sheet MUST declare one primary perspective before content creation:

| Perspective | Focus | Example Domains |
|-------------|-------|-----------------|
| **Business** | Growth, revenue, market metrics | RB Strategy, WB Strategy, Product GNMs |
| **Operation** | Process, execution, timelines | Operating model, fulfillment, service delivery |
| **Risk** | Controls, compliance, mitigation | Credit risk, operational risk, regulatory |
| **Data** | Infrastructure, quality, lineage | Analytics, MIS, data governance |

### Rules
- One perspective per sheet — no mixing
- Perspective is declared in sheet metadata (not inferred)
- Child sheets inherit parent's perspective unless explicitly overridden

### Anti-pattern: Perspective Soup
Mixing "sales strategy" metrics with "data quality" controls in the same sheet. Split into separate sheets, each with its own perspective.

---

## Hub Navigation Architecture (Production Pattern)

> Source: bod-nextjs production system (2026-03-30)

### BMA — Board Management All (Central Hub)

The top-level GNM entry point is a hub sheet (BMA) that organizes all domain GNMs into a navigable structure:

```
BMA (Board Management All)
├── MF Domain Hub (Market Facing)
│   ├── RBC Board → RBC sheets (A/B/Z)
│   ├── CPF Board → CPF sheets
│   ├── TRS Board → TRS sheets
│   └── ... (10 MF domains)
├── BO Domain Hub (Back Office)
│   ├── NWR Board → NWR sheets
│   └── BOF Board → BOF sheets
└── SP Domain Hub (Supporting)
    ├── HRS Board → HRS sheets
    ├── RIS Board → RIS sheets
    └── MCS Board → MCS sheets
```

### Navigation Patterns

| Pattern | Mechanism | Example |
|---------|-----------|---------|
| **Pill navigation** | Hub cell text maps to child sheet ID | "RB Strategy" → `rbc-vbm` |
| **Breadcrumb** | Path from root to current: `BMA → Domain → Board → Sheet` | `BMA → MF → RBC → rbc-1z` |
| **Cell-to-sheet** | Clicking a cell navigates to the referenced child GNM | Zone 8 italic references → target sheet |
| **Back-navigation** | Breadcrumb allows Parent ← Child click-back | Click "RBC" in breadcrumb to go up |

### Cascade Rules for Navigation

1. **Single-parent rule:** Every sheet (except BMA root) has exactly one parent
2. **Leaf rule:** Z-level sheets are leaves — no children
3. **Breadth rule:** A hub can have 2-15 children (boards); a board can have 2-10 children (sheets)
4. **No orphans:** Every sheet must be reachable from BMA via the cascade
5. **Parent computation:** Derived from child declarations (not stored separately)

### Board vs Sheet Distinction

| Type | Purpose | Naming | Content |
|------|---------|--------|---------|
| **Board** (sub-*) | Navigation hub listing children | `sub-{prefix}` | Pill cells pointing to child sheets |
| **Sheet** (data) | Actual GNM content with zones | `{prefix}-{id}` | Full 9-zone structure |
| **Master** (mst) | Strategy overview | `{prefix}-mst` | High-level A-level strategy |

### Anti-pattern: Flat Navigation
Putting all 143 sheets in one hub with no intermediate boards. Use domain → board → sheet hierarchy for manageability.

---

## 4-Section Architecture

Cau truc cua GNM gom 4 phan chinh, duoc sap xep theo logic tu trai sang phai:

| Phan | Muc dich | Vai tro trong tu duy MFM |
|------|----------|--------------------------|
| **Ten GNM** | Dinh danh chu de | The hien WHAT tong the |
| **Phan Dau** | Bang dinh vi | Index cho toan bo cau truc |
| **Phan Than** | Ma tran WHAT x TODO | Noi dung chinh cua GNM |
| **Phan Mo rong** | Boi canh & Nguon luc | Ket noi voi he sinh thai |

---

<dynamic_rows>

## Dynamic Row Position Formula

Vi tri cac clusters va zones thay doi dong dua tren so items. Su dung bang sau de tinh toan:

| Component | Formula | Vi du (n=3 items, a=2 All rows, c=2 Common rows) |
|-----------|---------|--------------------------------------------------|
| **Last Item Row** | 7 + n | 7 + 3 = **Row 10** |
| **All Cluster Start** | 8 + n | 8 + 3 = **Row 11** |
| **All Cluster End** | 7 + n + a | 7 + 3 + 2 = **Row 12** |
| **Common Cluster Start** | 8 + n + a | 8 + 3 + 2 = **Row 13** |
| **Common Cluster End** | 7 + n + a + c | 7 + 3 + 2 + 2 = **Row 14** |
| **End Row (toan bo GNM)** | 7 + n + a + c | **Row 14** |

> **Luu y:** a va c la **toi thieu 2**, co the tang khi can nhieu Engines hon. So dong All/Common phu thuoc vao so Engines thuc te trong Zone 5-7 (All) va Zone 8-9 (Common).

> **Vi du 1 (mo rong All):** 5 items (n=5), 3 All rows (a=3), 2 Common rows (c=2):
> - Last Item Row = 7 + 5 = **Row 12**
> - All Start = **Row 13**, All End = **Row 15** (3 dong cho 3 Engines Zone 5)
> - Common Start = **Row 16**, Common End = **Row 17**
>
> **Vi du 2 (mo rong ca hai):** 3 items (n=3), 4 All rows (a=4), 3 Common rows (c=3):
> - All Start = **Row 11**, All End = **Row 14** (4 dong)
> - Common Start = **Row 15**, Common End = **Row 17** (3 dong)

</dynamic_rows>

---

<column_layout>

## Column Layout Constraint (Authoritative Reference)

> **[!] CRITICAL:** Bang duoi day la nguon chinh xac DUY NHAT cho column letters. Tat ca cac PART khac PHAI tham chieu bang nay. Khi them/bot cot -> cap nhat bang nay TRUOC, roi cascade sang Template, Zone Positioning, Column Widths, Medium Borders, Merge Range.

### Fixed Columns (khong bao gio thay doi)

| Cot | Vai tro | Width | Ghi chu |
|-----|---------|-------|---------|
| **A** | Separator dau | 20px | Trong hoan toan (tru A1 back-link cho sub-GNM) |
| **B** | Phan Dau cot 1 | 100px | B2=Ten GNM, B4=(1), B5=Ma GNM, B[8+n]=Common |
| **C** | Phan Dau cot 2 | 100px | C4=(2), C5-C7=nhan (1)(2)(3), C8+=numbering |
| **D** | Separator Dau-Than | 20px | Trong hoan toan |
| **E** | Zone 1 Level 0 | 100px | E5=`=B5`, E6=Object, E7=Item, E8=`=B5` |
| **F** | Zone 1 Level 1 (Item) | 100px | Luon co |

### Dynamic Columns (thay doi theo f = so Features, L2 = co Level 2)

> **Scaling Formula:** Goi **f** = so Feature columns (1-5), **L2** = 1 neu co Level 2, 0 neu khong.
>
> | Component | Column Letter Formula | Width |
> |-----------|----------------------|-------|
> | **Zone 1 Level 2** (neu co) | G (chi khi L2=1) | 100px |
> | **Zone 2 Feature col k** (k=1..f) | Col(G + L2 + k - 1) | 200px |
> | **Zone 3** | Cung cot Zone 2 (rows 8+) | 200px |
> | **Conso. (Zone 4)** | Col(G + L2 + f) | 200px |
> | **Separator Than-MR** | Col(G + L2 + f + 1) | 20px |
> | **Phan Mo rong col 1** | Col(G + L2 + f + 2) | 100px |
> | **Phan Mo rong col 2** | Col(G + L2 + f + 3) | 100px |
> | **Phan Than total cols** | 2 + L2 + f + 1 = f + L2 + 3 | — |
> | **B2 Merge Range** | B2 : Col(G + L2 + f) | — |

### Bang tra cuu nhanh — Column Positions theo f va L2

| f (Features) | L2 | Zone 2 cols | Conso. | Separator | Mo rong | Phan Than cols | B2 Merge |
|---|---|---|---|---|---|---|---|
| **1** | 0 | G | H | I | J-K | E-H (4) | B2:H2 |
| **2** | 0 | G-H | I | J | K-L | E-I (5) | B2:I2 |
| **2** | 1 | H-I | J | K | L-M | E-J (6) | B2:J2 |
| **3** | 0 | G-I | J | K | L-M | E-J (6) | B2:J2 |
| **3** | 1 | H-J | K | L | M-N | E-K (7) | B2:K2 |
| **4** | 0 | G-J | K | L | M-N | E-K (7) | B2:K2 |
| **4** | 1 | H-K | L | M | N-O | E-L (8) | B2:L2 |
| **5** | 0 | G-K | L | M | N-O | E-L (8) | B2:L2 |
| **5** | 1 | H-L | M | N | O-P | E-M (9) | B2:M2 |

**Cascade khi thay doi so cot Zone 2:**
- **Moi Feature them vao:** Conso. shift +1, Separator shift +1, Mo rong shift +1, Header numbering +1, B2 Merge Range +1 cot
- **Them Level 2 (cot G):** Toan bo Zone 2 tro di shift +1 (tuong duong f va L2 trong formula)
- **Single-Feature (f=1, L2=0):** Phan Than = 4 cot (E-H). Conso. = H. Separator = I. Mo rong = J-K. Merge Range B2:H2.
- **Multi-Feature (f=2, L2=0):** Phan Than = 5 cot (E-I). Conso. = I. Separator = J. Mo rong = K-L. Merge Range B2:I2.
- **Multi-Feature + Level 2 (f=2, L2=1):** Phan Than = 6 cot (E-J). Conso. = J. Separator = K. Mo rong = L-M. Merge Range B2:J2.

> **Luu y:** Khi f > 2, khong co template visual san — ap dung Scaling Formula o tren de tinh column positions. Luon giu width 200px cho moi cot Zone 2/3 va Conso.

### Matrix Grammar Declaration (MAY — Build Spec only)

When using the Engine-as-Root pattern (see Part 3b), each engine-rooted sub-sheet MAY declare its own analytical grammar in the Build Spec. This documents what Zone 1 rows and Zone 2 columns represent for that specific engine — useful when different sheets in a cascade have different row/column semantics.

```yaml
# Build Spec — matrix_grammar is metadata only, not rendered in Excel
matrix_grammar:
  rows: "Job Family"           # What Zone 1 Items represent
  columns: "Career Level"      # What Zone 2 Features represent
  filters: "geography, grade"  # Optional depth dimensions (L2 or Z-level)
  measures: "compa-ratio, market position"  # What Zone 3 Values measure
```

**Rules:** Matrix grammar is Build Spec metadata — it does NOT appear in the Excel output. It serves as documentation for cascade comprehension and cross-sheet consistency validation.

</column_layout>

---

## Zone Headers Cell Map (Rows 6-7 — Authoritative Reference)

> **[!] CRITICAL:** This table is the SINGLE SOURCE OF TRUTH for rows 6-7 content. All other mentions of E6/E7/F6/F7/G6/G7 MUST match this table. E6 and E7 are **nhan co dinh** — NEVER replaced with dynamic content.

| Cell | Content | Rule | Applies When |
|------|---------|------|--------------|
| **E6** | `Object` | Nhan co dinh — LUON la text "Object" | Always |
| **E7** | `Item` | Nhan co dinh — LUON la text "Item" | Always |
| **F6** | (rong) | De trong — KHONG dien "-" | Always |
| **F7** | `-` | Dau gach ngang | Always |
| **G6** | (rong) | De trong khi co Level 2 | Only if L2=1 |
| **G7** | `-` | Dau gach ngang khi co Level 2 | Only if L2=1 |
| **Zone 2 col 1, R6** | Feature Group name | VD: "Development", "Lending" | Always |
| **Zone 2 col 1, R7** | Feature 1 name OR `-` | `-` neu Single-Feature (f=1) | Always |
| **Zone 2 col 2+, R6** | (rong) | Feature Group chi ghi o col 1, con lai rong | Only if f>=2 |
| **Zone 2 col 2+, R7** | Feature N name | VD: "Risk Mgmt", "Monitoring" | Only if f>=2 |
| **Conso. col, R6** | `-` | Nhan co dinh | Always |
| **Conso. col, R7** | `-` | Nhan co dinh | Always |
| **Mo rong col 1, R5** | `Common` | Nhan co dinh | Always |
| **Mo rong cols, R6** | `-` | Nhan co dinh | Always |
| **Mo rong cols, R7** | `-` | Nhan co dinh | Always |

---

> **Retrieval Signpost:** For Visual Templates (A/B/C) and full Section Details -> see **PART 2b** (`references/part-2b-templates-details.md`). For core zones -> PART 3a. For engine zones -> PART 3b.

---

## Multimedia Embeds (Optional Extension)

> Source: bod-nextjs production system (2026-03-30)

Digital GNM viewers may support embedded multimedia content within cells:

| Embed Type | Use Case | Example |
|------------|----------|---------|
| **Video (mp4)** | Product demos, training content | MaxCard demo video in CPF sheet |
| **HTML iframe** | Dashboards, interactive reports | CFO performance report in BMA |
| **External URL** | Reference documents, external tools | Regulatory filings, market data |

### When to Use
- BOD presentations where static data needs live context
- Training GNMs where video walkthroughs add value
- Dashboard GNMs linking to real-time analytics

### Implementation Note
Multimedia is a viewer capability, not a GNM structural element. The underlying GNM structure (zones, engines, values) remains unchanged. Embeds are metadata attached to cells, not zone content.

---

## Sheet Naming Convention

> Source: bod-nextjs production standard (2026-03-30)

### Sheet ID Format
```
{prefix}-{identifier}
```

| Component | Rule | Examples |
|-----------|------|---------|
| **Prefix** | 3-letter domain code (uppercase in display, lowercase in ID) | `rbc`, `trs`, `cpf`, `hrs` |
| **Identifier** | Number + optional level suffix, or semantic name | `1z`, `fix`, `mst`, `11` |

### Common Suffixes

| Suffix | Meaning | Example |
|--------|---------|---------|
| `z` | Z-level (measurement/values) | `rbc-1z` |
| `mst` | Master/strategy overview (A-level) | `trs-mst` |
| `vbm` | VIB Business Model (root hub) | `rbc-vbm` |

### Special Prefixes

| Prefix | Meaning | Example |
|--------|---------|---------|
| `sub-` | Sub-board (navigation hub) | `sub-rbc`, `sub-hrs` |

### File Naming
- Data file: `gnm-{sheet-id}.ts` (e.g., `gnm-rbc-1z.ts`)
- Export name: camelCase of ID (e.g., `gnmRbc1z`)

### Anti-pattern
- Using full words as IDs (`retail-banking-card-zone1`) — too long, inconsistent
- Omitting level suffix on Z sheets (`rbc-1` vs `rbc-1z`) — ambiguous level

</part2a_structure_core>
