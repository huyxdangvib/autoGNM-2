---
part: 7c
name: "Examples: Single-Feature CREATE"
parent: gnm-instruction.md
---

### Example 10: Single-Feature CREATE (f=1, Template C)

**User Input:**
> "Tao GNM cho KAFI Securities Business Strategy, level B, voi Items: Retail Brokerage Business, Fixed Income Trading, Equity & Derivatives, Branch Network, Digital Channel. Feature duy nhat: Strategy Development."

**Expected Response:**
```
<thinking>
Step 1: Request Type = CREATE (Single-Feature Pattern)
Step 2: Parameters:
- Topic: KAFI Securities Business Strategy
- Level: B -> Zone 3 = Engines
- WHAT: 5 items, grouped under L1: Business (3) + Channel (2). L2 = 0 (no sub-items)
- TODO: 1 Feature only -> Single-Feature Pattern (Template C)
- f=1, L2=0 -> 4-col Phan Than (E-H), Conso. at H, B2:H2 merge

Step 2.5: Quote rules:
- PART 3a, Single-Feature Pattern: "Zone 2 chi co 1 cot Feature... Zone 4 (Conso.) dong vai tro nhu chieu TODO thu 2"
- PART 2b, Template C: "Zone 2 chi co 1 cot (G), Zone 3 cung 1 cot (G), Conso. o H"
- PART 2a, Column Layout: f=1, L2=0 -> Phan Than = 4 cot (E-H)
- PART 1, Critical Rule #1: "Zone 3 khong bao gio de o trong"
- PART 1, Critical Rule #3: "Conso. luon la cot cuoi cung" -> H for f=1

Step 3: Validate
- 5 items x 1 feature = 5 Zone 3 cells
- WHAT vs TODO: Business/Channel = WHAT, Strategy Development = TODO
- All/Common: 2 dong moi cum (default)
- Column layout: E-F (Zone 1), G (Zone 2/3), H (Conso.)
- G7 = "-" (single feature, no sub-feature row needed)

Step 4.5: Self-verify
- Zone 3: all 5 cells filled
- E5=B5, E8=B5 (formula)
- All sync: 2 rows x 3 phan
- Common sync: 2 rows x 3 phan
- Layout: 4 cols (E-H), Conso. at H
- B2 merge: B2:H2
</thinking>

V-gate: Z3[5/5] Sync[a=2=2=2,c=2=2=2] E5E8[ok] Layout[4col] ZoneBound[ok] Cite[n/a] TermCheck[ok]

<answer>
## GNM SPECIFICATION: KAFI SECURITIES BUSINESS STRATEGY (B)

### 1. Overview
| Property | Value |
|----------|-------|
| Ten GNM | KAFI SECURITIES BUSINESS STRATEGY (B) |
| Ma GNM | KBS |
| Pattern | **Single-Feature** (Template C, f=1) |
| WHAT (Zone 1) | 5 items: Retail Brokerage Business, Fixed Income Trading, Equity & Derivatives, Branch Network, Digital Channel |
| TODO (Zone 2) | Strategy Development (1 Feature) |
| Level 2 | No |
| Phan Than | 4 cot (E-H), Conso. at H |
| B2 Merge | B2:H2 |

### 2. Zone 1: Items (Cot E-F)

**Zone Headers:** E6=Object, E7=Item, F6=(rong), F7="-"

| Level 0 (E) | Level 1 (F) |
|-------------|-------------|
| KBS | Business |
| (rong) | (rong) |
| (rong) | (rong) |
| (rong) | Channel |
| (rong) | (rong) |

> **Note:** L1 labels "Business" (row 8) and "Channel" (row 11) group items -- see Template C in PART 2b.

### 3. Zone 2: Feature (Cot G, Row 6-7)
| G6 | G7 |
|----|----|
| Strategy Development | **-** |

> **Single-Feature:** G7 = "-" vi chi co 1 feature, khong can sub-feature row.

### 4. Zone 3: Value Matrix (Rows 8-12, Cot G)
| # | Item (F) | Strategy Development (G) |
|---|----------|--------------------------|
| 1 | Retail Brokerage Business | Retail Brokerage Strategy RBS(Z) |
| 2 | Fixed Income Trading | Fixed Income Trading Strategy FIT(Z) |
| 3 | Equity & Derivatives | Equity & Derivatives Strategy EDS(Z) |
| 4 | Branch Network | Branch Network Strategy BNS(Z) |
| 5 | Digital Channel | Digital Channel Strategy DCS(Z) |

### 5. Zone 4: Conso. Column (H) -- "2nd Dimension"
| Item | Conso. (H) | Role |
|------|------------|------|
| Retail Brokerage | - | (no cross-cutting engine needed) |
| Fixed Income Trading | FI Limit Review FLR(Z) | Decoding |
| Equity & Derivatives | - | |
| Branch Network | - | |
| Digital Channel | - | |

> **Zone 4 as "2nd dimension":** In Single-Feature GNMs, Conso. provides space for cross-cutting Engines that don't fit the single TODO perspective. Most cells may be "-".

### 6. Zone 5-9: All & Common Clusters

**Cum All (Rows 13-14, 2 dong):**
| Zone | G (Feature col) | H (Conso.) | J-K (Mo rong) |
|------|----------------|-------------|----------------|
| **Zone 5** | Securities Strategy Standards SSS(Z) | -- | -- |
| **Zone 6** | -- | KBS Governance Framework KGF(Z) | -- |
| **Zone 7** | -- | -- | Enterprise Securities Policy ESP(A) |

**Cum Common (Rows 15-16, 2 dong):**
| Zone | E-G (Zone 1-3 cols) | H (Conso.) | J-K (Mo rong) |
|------|---------------------|-------------|----------------|
| **Zone 8** | *(trong)* | Compliance Administration CPA(B) | -- |
| **Zone 9** | *(trong)* | -- | External Audit Liaison EAL(A) |

### 7. Excel Implementation
- Sheet name: `KBS (B)`
- B2 merge: B2:H2
- E5 = `=B5`, E8 = `=B5`
- Conso. position: Column H (NOT I -- single feature shifts everything left)
- Separator: Col I (between Than and Mo rong)
- Header numbering: (1)-(4) only
</answer>
```

</example>

---

<example type="DELETE_ARCHIVE">

