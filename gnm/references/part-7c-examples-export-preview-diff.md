---
part: 7c
name: "Examples: EXPORT, PREVIEW, DIFF, GENERATE from Build Spec"
parent: gnm-instruction.md
version: "5.5.0"
---

<examples>

<example n="14" task="EXPORT" tags="json,version-control">

### Example 14: EXPORT — JSON Export

**User Input:**
> "Export RBL(B) GNM to JSON format for version control"

**Expected Response:**
```
<thinking>
Step 1: Request Type = EXPORT (Excel/spec → structured JSON)
Step 2: Source = RBL(B), Retail Banking Lending, Level B
Step 2.5: Quote rules:
- PART 5, Export Schema: "$schema: gnm-v1 required"
- PART 5, Schema Rules: "metadata.code must match B5"
- PART 5, Format E: "Source → validation → JSON → render options"
Step 3: Extract 9 zones from RBL(B) structure (3 items, 2 features)
Step 4: Output Format E
</thinking>

<answer>
## EXPORT: RBL(B) → JSON

### Source Identification
| Field | Value |
|-------|-------|
| GNM name | RETAIL BANKING LENDING (B) |
| Code | RBL |
| Level | B |
| Layout | n=3, f=2, L2=0 |

### JSON Output
```json
{
  "$schema": "gnm-v1",
  "metadata": {
    "code": "RBL", "level": "B", "name": "Retail Banking Lending",
    "version": "2026-Q1", "created": "2026-03-16",
    "temporal_state": null, "author": "Retail Strategy Office"
  },
  "zone1": {
    "object": "Lending Product", "item": "Product Line",
    "items": [
      { "id": 1, "level1": "Mortgage", "level2": null },
      { "id": 2, "level1": "Auto Loan", "level2": null },
      { "id": 3, "level1": "Personal Loan", "level2": null }
    ]
  },
  "zone2": { "feature_group": "Lending Management",
    "features": [{ "name": "Origination" }, { "name": "Servicing" }] },
  "zone3": { "matrix": [
    { "item_id": 1, "feature": "Origination", "type": "engine",
      "engine": { "name": "Mortgage Origination Engine", "code": "MOE", "level": "Z" } },
    { "item_id": 1, "feature": "Servicing", "type": "engine",
      "engine": { "name": "Mortgage Servicing Model", "code": "MSM", "level": "Z" } },
    { "item_id": 2, "feature": "Origination", "type": "engine",
      "engine": { "name": "Auto Loan Origination", "code": "ALO", "level": "Z" } },
    { "item_id": 2, "feature": "Servicing", "type": "engine",
      "engine": { "name": "Auto Servicing Framework", "code": "ASF", "level": "Z" } },
    { "item_id": 3, "feature": "Origination", "type": "engine",
      "engine": { "name": "Personal Loan Origination", "code": "PLO", "level": "Z" } },
    { "item_id": 3, "feature": "Servicing", "type": "engine",
      "engine": { "name": "Personal Loan Servicing", "code": "PLS", "level": "Z" } }
  ]},
  "zone4": { "engines": [
    { "item_id": 1, "name": "Mortgage Conso", "code": "MCC", "level": "Z" },
    { "item_id": 2, "name": "Auto Conso", "code": "ACC", "level": "Z" },
    { "item_id": 3, "name": "Personal Conso", "code": "PCC", "level": "Z" }
  ]},
  "zone5": { "engines": [] }, "zone6": { "engines": [] },
  "zone7": { "engines": [] }, "zone8": { "engines": [] }, "zone9": { "engines": [] },
  "cascade": { "parent": "RBL (A)", "children": [] }
}
```

**Render options:** `EXPORT` for git diff | `GENERATE` to rebuild Excel | `DIFF` to compare versions
</answer>
```

</example>

---

<example n="15" task="PREVIEW" tags="ascii,pre-excel,validation">

### Example 15: PREVIEW — ASCII Preview

**User Input:**
> "Preview GNM structure for Corporate Banking Services (B) before generating Excel"

**Expected Response:**
```
<thinking>
Step 1: Request Type = PREVIEW (Format F — ASCII before Excel generation)
Step 2: Topic = Corporate Banking Services, Level B
- Items (n=3): Cash Management, Trade Finance, Treasury
- Features (f=2): Client Coverage, Product Delivery
- L2=0, Template A layout
Step 2.5: Quote rules:
- PART 5, Format F: "Template f=2, L2=0: Zone2=G-H, Conso=I, Sep=J, Ext=K-L"
- PART 7, V-gate: "10 checks required on every output"
- PART 8, Quality: "Score before generating Excel"
Step 4: Build ASCII grid, compute V-gate, score
</thinking>

<answer>
## PREVIEW: CORPORATE BANKING SERVICES (B)

```
     | A  | B      | C   | D  | E      | F                  | G               | H                | I               | J  | K               | L               |
-----+----+--------+-----+----+--------+--------------------+-----------------+------------------+-----------------+----+-----------------+-----------------+
 R2  |    | CORPORATE BANKING SERVICES (B) [B2:I2 merged]                                         |    |                 |                 |
 R3  |    |        |     |    |        |                    |                 |                  |                 |    |                 |                 |
-----+----+--------+-----+----+--------+--------------------+-----------------+------------------+-----------------+----+-----------------+-----------------+
 R4  |    | (1)    | (2) |    | (1)    | (2)                | (3)             | (4)              | (5)             |    | (1)             | (2)             |
 R5  |    | CBS    | (1) |    | =B5    |                    |                 |                  | Conso.          |    | Common          |                 |
 R6  |    |        | (2) |    | Corp   |                    | CBS Mgmt        |                  | -               |    | -               |                 |
 R7  |    |        | (3) |    | Service| -                  | Client Coverage | Product Delivery | -               |    | -               | -               |
-----+----+--------+-----+----+--------+--------------------+-----------------+------------------+-----------------+----+-----------------+-----------------+
 R8  |    |        | 1   |    | =B5    | Cash Management    | CM Coverage     | CM Delivery      | CM Conso CMC(Z) |    |                 |                 |
 R9  |    |        | 2   |    |        | Trade Finance      | TF Coverage     | TF Delivery      | TF Conso TFC(Z) |    |                 |                 |
 R10 |    |        | 3   |    |        | Treasury           | Trs Coverage    | Trs Delivery     | Trs Conso TRC(Z)|    |                 |                 |
-----+----+--------+-----+----+--------+--------------------+-----------------+------------------+-----------------+----+-----------------+-----------------+
 R11 |    |        | All |    |        |                    | CBS All Cov Z5  | CBS All Del Z5   | CBS All Conso Z6|    | CBS All Ext Z7  |                 |
 R12 |    |        |     |    |        |                    |                 |                  |                 |    |                 |                 |
-----+----+--------+-----+----+--------+--------------------+-----------------+------------------+-----------------+----+-----------------+-----------------+
 R13 |    | Common | -   |    |        |                    |                 |                  | CBS Cmn Z8      |    | CBS Cmn Ext Z9  |                 |
 R14 |    |        |     |    |        |                    |                 |                  |                 |    |                 |                 |
-----+----+--------+-----+----+--------+--------------------+-----------------+------------------+-----------------+----+-----------------+-----------------+
     | Sep|  Phan Dau    | Sep|               Phan Than (Zones 1-6, 8)                          | Sep|  Phan Mo rong  |
```

Zone Map: Z1=E-F | Z2=G-H(R6-7) | Z3=G-H(R8+) | Z4=I(R8+) | Z5=G-H(All) | Z6=I(All) | Z7=K-L(All) | Z8=I(Com) | Z9=K-L(Com)
V-gate: Z3[6/6] Sync[a=2,c=2] E5E8[=B5] Layout[9col,B2:I2] ZoneBound[ok] Cite[n/a] TermCheck[ok] DEP[n/a] Score[n/a] Temporal[n/a]
Quality: 8.1/10 Good [Structure:9 Content:8 Naming:8 Completeness:7]

Structure looks correct? [y] Generate Excel / [n] Adjust
</answer>
```

</example>

---

<example n="16" task="DIFF" tags="compare,versioning,vietnamese">

### Example 16: DIFF — Compare Two Versions

**User Input:**
> "So sanh GNM WBL(B) phien ban thang 1 va thang 3"

**Expected Response:**
```
<thinking>
Step 1: Request Type = DIFF (Format G — side-by-side version comparison)
Step 2: GNM_A = WBL(B) Jan, GNM_B = WBL(B) Mar (Wholesale Banking Lending)
Step 2.5: Quote rules:
- PART 5, Format G: "Tags: [NEW]/[RETIRE]/[GAP]/[OK]"
- PART 5, Format G: "Sections: Structural → Zone 1 → Zone 3 → Quality"
Step 3: Infer typical WBL changes Jan→Mar: 1 item added, 1 retired, zone3 updates
Step 4: Output Format G with delta tags
</thinking>

<answer>
## GNM DIFF: WBL(B) Jan vs WBL(B) Mar

### Structural Comparison
| Aspect | WBL Jan | WBL Mar | Delta |
|--------|---------|---------|-------|
| Items | 3 | 3 | unchanged (1 swap) |
| Features | 2 | 2 | unchanged |
| Level | B | B | unchanged |
| Zone 3 density | 5/6 (83%) | 6/6 (100%) | +17% |

### Zone 1 Changes
| Item | WBL Jan | WBL Mar | Change |
|------|---------|---------|--------|
| Working Capital | present | present | [OK] |
| Term Loan | present | present | [OK] |
| LC / UPAS | present | removed | [RETIRE] — absorbed into Trade Finance |
| Trade Finance | absent | added | [NEW] — broader scope |

### Zone 3 Cell Changes
| Item x Feature | WBL Jan | WBL Mar | Tag |
|---------------|---------|---------|-----|
| Trade Fin x Origination | — | TF Origination TFO(Z) | [NEW] |
| Trade Fin x Risk Mgmt | — | TF Risk Framework TRF(Z) | [NEW] |
| LC UPAS x Origination | LC Orig Engine LCO(Z) | — | [RETIRE] |
| LC UPAS x Risk Mgmt | UPAS Risk Model URM(Z) | — | [RETIRE] |
| Working Cap x Risk Mgmt | WC Risk WCR(Z) | WC Risk Management WCR(Z) | [GAP] name update only |

### Quality Comparison
| Dimension | WBL Jan | WBL Mar | Delta |
|-----------|---------|---------|-------|
| Structure | 8.0 | 8.0 | +0.0 |
| Content | 7.5 | 8.5 | +1.0 |
| Completeness | 7.0 | 9.0 | +2.0 |
| Total | 7.5/10 | 8.5/10 | +1.0 |

**Summary:** 1 item retired (LC/UPAS), 1 added (Trade Finance), 2 new Zone 3 engines, Zone 3 density +17%. Quality improved +1.0 driven by completeness.
</answer>
```

</example>

---

<example n="17" task="GENERATE" tags="build-spec,excel,script">

### Example 17: GENERATE — Build Spec to Excel

**User Input:**
> "Generate Excel from this Build Spec JSON: {gnm: 'DPS(B)', layout: {n:3, f:2, L2:0}, zone1: ['Current Account', 'Savings', 'Term Deposit'], zone2: ['Acquisition', 'Retention'], ...}"

**Expected Response:**
```
<thinking>
Step 0: Build Spec detected -> skip Steps 1-3, go directly to GENERATE
Step 2.3: Load PART 14 ONLY (replaces Parts 2a+2b+4+5+13 = ~19K tokens)
- f=2, L2=0 -> Template A, Zone2=G-H, Conso=I, Sep=J, Ext=K-L
- n=3, a=2 (default), c=2 (default)
- Row layout: Header R4-7, Items R8-10, All R11-12, Common R13-14
Step 4: Execute 5-phase write order per PART 14
</thinking>

<answer>
## GENERATE: DPS(B) — Deposit Products

### Build Spec Validated
| Field | Value | Status |
|-------|-------|--------|
| Code | DPS | ok |
| Level | B | ok |
| Layout | n=3, f=2, L2=0 | ok -> Template A |
| Zone2 cols | G (Acquisition), H (Retention) | computed |
| Conso col | I | computed |
| B2 merge | B2:I2 | computed |

### 5-Phase Write Order

```python
sheets = ['DPS (B)']

# Phase 1: Static data (all cells, no formulas)
write_data('DPS (B)')
# R2: "DEPOSIT PRODUCTS (B)" | R4-7: headers
# R8: Current Account | R9: Savings | R10: Term Deposit
# Zone3 G-H R8-10: 6 engine cells
# Zone4 I R8-10: 3 consolidation engines
# All R11-12: Zone5 G-H, Zone6 I, Zone7 K-L
# Common R13-14: Zone8 I, Zone9 K-L

# Phase 2: Formulas
write_formulas('DPS (B)')
# E5=B5, E8=B5, B2:I2 merge

# Phase 3: Section borders (medium)
set_section_medium_border('DPS (B)')

# Phase 4: Cluster borders (thin)
set_cluster_thin_border('DPS (B)')

# Phase 5: Formatting
set_formatting('DPS (B)')  # wrap_text=True, autofit columns
```

### Zone 3 Matrix (6 cells)
| Item | Acquisition (G) | Retention (H) | Conso. (I) |
|------|----------------|---------------|------------|
| Current Account | CA Acquisition CAA(Z) | CA Retention CAR(Z) | CA Conso CAC(Z) |
| Savings | Savings Acquisition SAA(Z) | Savings Retention SAR(Z) | Savings Conso SAC(Z) |
| Term Deposit | TD Acquisition TDA(Z) | TD Retention TDR(Z) | TD Conso TDC(Z) |

**Output:** `_bmad-output/DPS-B.xlsx` | Sheet: `DPS (B)` | E5=`=B5` E8=`=B5` confirmed
V-gate: Z3[6/6] Sync[a=2,c=2] E5E8[=B5] Layout[9col,B2:I2] ZoneBound[ok] Cite[n/a] TermCheck[ok] DEP[n/a] Score[n/a] Temporal[n/a]
</answer>
```

</example>

</examples>
