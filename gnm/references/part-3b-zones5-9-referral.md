---
part: 3b
name: "Zones 5-9 Consolidation & Referral"
parent: gnm-instruction.md
---

## Zones 5-9: Consolidation & Referral (Engine-Only Zones)

> **Đặc điểm chung cho Zone 5-9:** CHỈ chứa Engines (xem **Engine** trong Terminology). Format: `[Tên đầy đủ] MãGNM (Level)`, max 50 ký tự. Tên Engine tự mang nghĩa — không cần Value bổ sung.

### Inline Cascade vs Z8/Z9 Referral (codified 2026-04-17, per Critical Rule #12)

There are TWO valid patterns for expressing parent-child cascade between GNM sheets:

| Pattern | How cascade is expressed | When to use | Z8/Z9 behavior |
|---------|-------------------------|-------------|----------------|
| **Inline Cascade** | HYPERLINK engines embedded inside Z3 cells (engine names like `"Lead allocation (2A)"` with formula `=HYPERLINK("#'2A'!A1", "Lead allocation (2A)")`) or Z4-7 engines | Tight parent→child cascades where the reference is the engine's primary semantic role | Z8/Z9 MAY be empty — do NOT treat as a violation |
| **Z8/Z9 Referral** | Separate named engines in the Common cluster rows (Z8=Internal via Conso. col, Z9=External via Mở rộng cols) | Loose cross-domain references (e.g. HR sheet referring to RB sheet without hierarchical relationship) | Z8/Z9 MUST contain referral engines |

**Rule of thumb:**
- If the engine's name IS a reference to another sheet ("Lead allocation (2A)") → inline cascade. Z8/Z9 MAY be empty.
- If the reference is contextual/supportive (framework, regulator, sibling function) → use Z8/Z9.
- A single workbook SHOULD commit to one primary pattern and apply it consistently across all sheets.

**Production evidence (BNW workbook, 2026-04-16):** All 15 sheets use inline cascade (HYPERLINK engines in Z3-Z7). Z8/Z9 are empty throughout. The cascade BNW(A) → SPS(B) → BSS(C) → NLL(D) → {1B, 2A, 5, 6, 7}(Z) is expressed entirely via inline HYPERLINK engines. Historical examples (VBM workbook) use Z8 for enterprise-wide referrals like `Enterprise strategies VES(Z)`. Both are valid.

**Validator behavior:**
- Do NOT flag "empty Z8/Z9" as a violation unless the sheet has no inline HYPERLINK cascade either (then: orphan warning).
- DO flag "mixed cascade patterns in same workbook" as a consistency warning.
- DO verify every inline HYPERLINK engine resolves to a real sheet (see Part 9 — dangling hyperlink validation).

### Engine-as-Root Model (MAY)

An Engine is not just a label with a HYPERLINK — it MAY be the **root node of a reusable analysis model**. When a GNM cascade uses the Engine-as-Root pattern, each engine-rooted sub-sheet declares its own analytical grammar:

| Layer | Meaning | GNM Mapping |
|-------|---------|-------------|
| **Root** | Engine name | B2 title of sub-GNM sheet |
| **Rows** | Primary object set | Zone 1 Items |
| **Columns** | Interacting object set | Zone 2 Features |
| **Depth / Filters** | Segment, geography, time, BU | Level 2 column or cascade to Z-level |
| **Cell Payload** | Values per intersection | Zone 3 content (simple or structured — see Part 3a) |
| **Measures** | KPIs, cost, risk, compliance | Zone 3 Values at Z-level |

**When to use:** Complex analytical domains where each engine represents a distinct analysis model with its own row/column semantics. The parent GNM (Level A) acts as a Scope Map — its Zone 3 engines point to child sheets that each define their own matrix grammar.

**When NOT to use:** Simple cascades where all sheets share the same row/column structure. Default GNM behavior (engine = label + HYPERLINK) remains the norm.

**Build Spec declaration (optional):** When using Engine-as-Root, the Build Spec MAY include a `matrix_grammar` field per engine to document the analytical model. This lives in the Build Spec only — not rendered in Excel.

```yaml
# Build Spec example — Engine-as-Root declaration
engines:
  - code: PAE
    level: B
    matrix_grammar:
      rows: "Job Family"
      columns: "Career Level"
      payload: "grade code + band code"
      measures: "compa-ratio, market position"
```

| Zone | Tên | Mục đích | Cluster | Vị trí cột | Scope |
|------|-----|---------|---------|-------------|-------|
| **5** | Vertical Consolidation | Hợp nhất dọc Zone 3 — Feature-level consolidation hoặc Decoding topics | All | Zone 2-3 cols | Tổng hợp tất cả Items cho từng Feature |
| **6** | Common Matters (3,4,5) | Yếu tố nền tảng chung cho Zone 3+4+5 | All | Cột Conso. | Giao điểm All×Conso. |
| **7** | Common Matters (3-6) | Mở rộng Zone 6, kết nối bối cảnh rộng hơn | All | Phần Mở rộng (2 cột) | Giao điểm All×Phần Mở rộng |
| **8** | Internal Referral | Liên kết đến GNM của chức năng nội bộ khác | Common | Cột Conso. | Cùng tổ chức |
| **9** | External Referral | Liên kết đến GNM của đối tác/bên ngoài | Common | Phần Mở rộng (2 cột) | Partners, vendors, regulators |

**Đồng bộ hành/dòng:**
- Zone 5+6+7 → số dòng = Cụm All (Phần Đầu = Phần Thân = Phần Mở rộng)
- Zone 8+9 → số dòng = Cụm Common (Phần Đầu = Phần Thân = Phần Mở rộng)
- Zone 1 cols ở khu vực All = **trống**. Zone 1-3 cols ở khu vực Common = **trống**

**Cross-Cutting / Shared Service Pattern (Zone 8 guidance):**

When a topic spans multiple BUs but is owned by a central function, apply this pattern:
- **Zone 1** = the topic's OWN decomposition (the central function's segments/components)
- **Zone 8** = the BU GNMs this function SERVES (input sources, receiving BUs)

This prevents the shared service from duplicating business units' scope in Zone 1.

| Example | Central Function | Zone 1 (Own decomposition) | Zone 8 (Serves) |
|---------|-----------------|---------------------------|-----------------|
| NPL Business Model | CRO | RB NPL, SME NPL, WB NPL | RBL, WB Credit, Finance |
| BNW Strategy | RB BNW | Geographic segments | RBL, RBD, RBC, RBB, HRP, ITD |

**Ví dụ Engines cho từng Zone (generic):**

| Zone | Engine ví dụ |
|------|-------------|
| 5 | `Control Objective Framework COF(Z)`, `Process Performance Indicator PPI(B)` |
| 6 | `Enterprise Architecture Principle EAP(Z)`, `Information Security Policy ISP(A)` |
| 7 | `Strategic Planning Guideline SPG(A)`, `Business Continuity Plan BCP(Z)` |
| 8 | `Risk Management Framework RMF(A)`, `Internal Audit Charter IAC(B)` |
| 9 | `Third Party Risk Assessment TPR(A)`, `Vendor Due Diligence VDD(B)` |

**Domain-specific Engine Templates (VIB):**

Use these as defaults when creating GNMs for common VIB domains. Adapt names/codes to match actual topic.

| Domain | Z5 (Vertical Conso.) | Z6 (Foundation) | Z7 (Dashboard/Tools) | Z8 (Internal Ref) | Z9 (External Ref) |
|--------|---------------------|-----------------|---------------------|-------------------|-------------------|
| **RB Lending** | Lending Origination Standards LOS(Z) | RB Lending Governance RLG(Z) | RB Lending Dashboard RLD(Z) | Credit Administration CRA(B) | SBV Lending Regulations SLR(A) |
| **RB Deposits** | Deposit Operations Standards DOS(Z) | Deposit Product Governance DPG(Z) | Deposit Performance Dashboard DPD(Z) | Treasury Operations TRO(B) | SBV Deposit Regulations SDR(A) |
| **WB Lending** | WB Credit Policy WCP(Z) | WB Lending Governance WLG(Z) | WB Portfolio Dashboard WPD(Z) | Credit Administration CRA(B) | Basel Compliance BSL(Z) |
| **Cards** | Card Operations Standards COS(Z) | Card Product Governance CPG(Z) | Card Performance Dashboard CPD(Z) | Payment Systems PMS(B) | Visa/MC Network Standards VMS(A) |
| **BNW** | BNW Channel Standards BCS(Z) | BNW Strategy Governance BSG(Z) | BNW Network Dashboard BND(Z) | HR Resource Planning HRP(B) | Market Intelligence MKI(A) |

> **Rule of thumb:** Z5 = operational standards, Z6 = governance/framework, Z7 = dashboards/monitoring tools, Z8 = internal supporting function, Z9 = external regulator/partner. When unsure, label assumptions with ✏️.

**Bằng chứng VBM Excel — Zones 5-9 thực tế:**

*Zone 5 (Vertical Consolidation — All row, Feature columns):*
| Sheet | Zone 5 Engines (All row) |
|-------|--------------------------|
| VBM(A) | `Meeting & Interaction VMI(Z)`, `VIB Goal(Z)`, `AI AIA(Z)` |
| APT(A) | `Segment 1 centric dev.`, `Implementation plan`, `Goal & Target`, `External analysis`, `Perf. Dashboard`, `Internal analysis` |

*Zone 6 (Common of 3-5 — All row, Conso. col):*
| Sheet | Zone 6 present? |
|-------|-----------------|
| VBM(A) | Yes |
| APT(A) | Yes |

*Zone 7 (Common of 3-6 — All row, Mở rộng cols):*
| Sheet | Zone 7 Engines |
|-------|----------------|
| VBM(A) | `Org. structure VOS(A)`, `External stakeholders` |

*Zone 8 (Internal Referral — typically Common row, Conso. col):*
| Sheet | Zone 8 Engines | Row Location |
|-------|----------------|--------------|
| VBM(A) | `Enterprise strategies VES(Z)`, `GNM`, `B&F selection methodology BFS(Z)` | All row (merged All/Common) |
| AIA(Z) | `Biz & AI teams BAT(Z)` | Common row |
| APT(A) | `Business strategy team` | Common row |

> **Note:** VBM(A) merges Zone 5-8 into a single All section — Zone 8 function is preserved even though row label is "All." See VBM Practical Note in PART 2b.

*Zone 9 (External Referral — Common row, Mở rộng cols):*
| Sheet | Zone 9 Engines |
|-------|----------------|
| VBM(A) | `External stakeholders` |

**VBM Zone Summary — 12 sheets × populated zones:**

| Sheet | Z4 | Z5 | Z6 | Z7 | Z8 | Z9 |
|-------|----|----|----|----|----|----|
| VBM(A) | Y | Y (3 engines) | Y | Y (2 engines) | Y (3 engines) | Y |
| RBB(A) | Y | min | min | — | — | — |
| ONW(A) | Y | min | min | — | — | — |
| APT(A) | Y | Y (6 engines) | Y | — | Y (1 engine) | — |
| AIA(Z) | Y | min | min | — | Y (1 engine) | — |
| BFS/BAT/RSS/RST/BAP/VES/VOS | Y | min | min | — | — | — |

> **"min"** = All/Common rows present but minimal (label only, no significant engines documented).

---

## Tổng quan Logic 9 Zones

```
┌─────────────────────────────────────────────────────────────────────┐
│                         GNM STRUCTURE                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   PHẦN ĐẦU          │    PHẦN THÂN                      │   PHẦN MỞ RỘNG│
│   (Index)           │    (WHAT x TODO Matrix)           │   (Context)   │
│                     │                                   │               │
│   ┌─────────────┐   │   ┌────────────────────────────┐  │  ┌──────────┐ │
│   │ Mã GNM      │   │   │ Zone 1      │ Zone 2      │  │  │ Common   │ │
│   │ (1)(2)(3)   │   │   │ L0 │ L1    │ TODO        │  │  │          │ │
│   ├─────────────┤   │   │ (L2 nếu cần)│             │  │  │          │ │
│   │ 1, 2, 3...  │   │   ├─────────────┼─────────────┤  │  │          │ │
│   │ (Rows)      │   │   │ Items       │   Zone 3    │Z4│  │ (trống)  │ │
│   ├─────────────┤   │   │             │ Value Matrix│  │  │          │ │
│   │ All         │   │   ├─────────────┼─────────────┤  │  ├──────────┤ │
│   │             │   │   │(rỗng)       │   Zone 5    │Z6│  │  Zone 7  │ │
│   ├─────────────┤   │   │             │ Col Conso.  │  │  │ Context  │ │
│   │ Common      │   │   ├─────────────┼─────────────┤  │  ├──────────┤ │
│   │             │   │   │(rỗng)       │  (rỗng)     │Z8│  │  Zone 9  │ │
│   └─────────────┘   │   │             │             │  │  │ External │ │
│                     │   └─────────────┴─────────────┘  │  └──────────┘ │
│                     │                                   │               │
└─────────────────────────────────────────────────────────────────────┘
```

</zone_definitions>

> **📌 Retrieval Signpost:** For Core Zones 1-3 (Value Matrix, Items, Features) → see PART 3a. For styling details (colors, borders, widths) → see PART 4. For formulas & write order → see PART 5. For validation checklists → see PART 7. For examples → see PART 7b (core) / PART 7c (extended).

---

