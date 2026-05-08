---
part: 6
name: "VIB Credit Risk GNM Patterns"
parent: gnm-instruction.md
---

## Credit Risk GNM Patterns

### Hanging vs Flat Structure

| Structure | When |
|-----------|------|
| **Flat (no L2):** Products in Zone 1, BL in Zone 2 | Products map 1:1 to business lines (diagonal) |
| **Hanging (L2=1):** BL in L1, Products in L2 | Want to show portfolio tree explicitly |

Both valid. Flat is simpler. For VIB: Flat works because every product naturally belongs to one BL.

### CRD(B) Listing Pattern — CRAS Roll-ups

CRD(B) works best as **Listing pattern** — independent engine lists per business line, NOT a cross-product matrix.

```
Zone 2 Features:  RB           WB           TRS          Enterprise
                  --           --           ---          ----------
                  Mortgage     TCG          Bank         IFRS9
                  Auto         Corp Lending SeCo         Concentration
                  BL/SME       WB CRAS      TRS CRAS     Rating Model
                  Personal                               Stress Testing
                  UPL                                    Collections
                  Card                                   Enterprise CRAS
                  RB CRAS
```

**Key insight:** Each column's "All" row = **CRAS (Credit Risk Appetite Statement)** for that business line — the sub-budget allocated from enterprise to each division.

**Why Listing (not cross-product):**
- Products belong to exactly ONE business line → cross-product cells would be empty
- Each column is self-contained portfolio catalog → independent engine lists
- CRAS at column bottom consolidates → natural roll-up to Enterprise CRAS
- Board reads: "RB has 6 product strategies + consolidated appetite. WB has 2. TRS has 2."

### Diagonal Sparsity Is Valid for Strategy GNMs

When Zone 1 items belong to exactly ONE Zone 2 feature:

```
             | RB    | WB    | TRS   |
Mortgage     | ████  |       |       |
Auto         | ████  |       |       |
TCG          |       | ████  |       |
Bank         |       |       | ████  |
```

- **33% density is OK** if the diagonal represents strategic allocation
- Empty cells = structurally impossible combinations, NOT missing data
- This is the CRO's Board conversation: "grow mortgage, control BL, tighten TRS"

### Strategic Diagonal vs Operational Matrix

| | Diagonal (Listing/Catalog) | Dense Matrix (Cross-Product) |
|--|---------------------------|------------------------------|
| **Zone 3** | Each BL has its own product list (independent) | Every item x every feature is meaningful |
| **Density** | ~30-40% filled | 100% filled |
| **Question** | "What products exist in each BL?" | "How does each risk component affect each BL?" |
| **Owner** | Business-facing (Credit Risk Head allocating portfolio) | Capability-facing (CRO building frameworks) |

Choose diagonal/listing for **portfolio allocation**. Choose dense matrix for **capability building**.

---

### Product Overlap Check at Z-Level

Before finalizing Zone 1 product list, verify no two products would produce nearly identical Z-sheets:

| Risk | Example |
|------|---------|
| **Personal vs UPL** | Same scoring model, same collection flow, same approval authority → merge into "Unsecured Consumer" |
| **Card vs UPL** | Same team manages both → consider merging |
| **BL vs WB "Others"** | SME BL overlaps with WB small corporate → define turnover threshold |

**Rule:** Two products deserve separate Z-sheets ONLY if they have different risk profiles, different teams, or different regulatory treatment. Otherwise merge and use sub-sections within one Z-sheet.

---

### "Approval Model" Unbundling — 3 Pieces, 3 Owners

When someone says "put the approval model here," ask: WHICH part?

| Component | Owner | Regulatory | Where in GNM |
|-----------|-------|------------|-------------|
| **Policy** (cutoffs, LTV, DTI) | Credit Risk Head | OCC Credit Risk | Row inside product Z-sheet |
| **Model** (scorecard design, validation) | Model Risk Head | **SR 11-7** | MRA(B) → Credit Scoring Models |
| **Process** (delegation, override, auto-rate) | Credit Ops | Operational Risk | Enterprise column → Approval Governance |

**Rule:** Mixing these violates ownership separation. The credit team USES the model; the model risk team GOVERNS it.

---

### Customer x Collateral = The Real Credit Decision Matrix

When Risk "takes control" at product-specific level (e.g., Mortgage), the deepest decoding is:

```
Zone 1 = Customer Segments         Zone 2 = Collateral Types
-------------------------         -------------------------
Payroll                    x      Apartment | Landed | Land+Build | Commercial RE
Self-Employed              x
HNW / Affluent             x
Viet Kieu                  x
First-Time Buyer           x
```

**Why Customer x Collateral beats all other combinations:**

| Decision Factor | What Drives It | GNM Axis |
|----------------|---------------|----------|
| **PD (Probability of Default)** | Customer income stability, track record | **Zone 1 (rows)** |
| **LGD (Loss Given Default)** | Collateral liquidity, valuation certainty | **Zone 2 (columns)** |
| **Approval decision** | The intersection | **Zone 3 cell** |

Zone 3 = actual approval parameters: LTV, score cutoff, DTI limit, approval authority level. Every cell directly executable by a Credit Officer.

**Product Type** (Home Purchase vs Refinance vs HELOC) becomes a **Common engine** — overlay of additional rules on the Customer x Collateral base matrix.

---

### VIB Product Taxonomy -> GNM Level Mapping (Credit Risk View)

```
Taxonomy Level        GNM Level     Zone Content
--------------        ---------     ------------
Core Product      ->   A-level       Zone 1 Items (portfolio segments)
Product Type      ->   B-level       Zone 1 Items (sub-products)
Product Variant   ->   Z-level       Zone 3 Values (parameter adjustments)
```

Product Variants (Payroll Mortgage, Developer Partnership, Green Home Loan) are commercial modifications — they DON'T change risk structure. They adjust pricing, eligibility, channel. Variants appear as **annotations within Z-level Values**, not separate items.

**Result:** Often need only 2 levels (A+B), not 3 — because B-level Zone 3 IS executable with variant annotations.

---

### B-Level Decoding Decision Tree

```
Is the B-level GNM for an entire Core Product (Mortgage, Auto, Card)?
|
+-- YES, distinct Product Types with different risk profiles?
|   -> Zone 1 = Product Types, Zone 2 = Policy x Monitoring
|      Example: Mortgage -> Home Purchase, Refinance, HELOC, Renovation
|
+-- YES, Risk wants to control the approval decision directly?
|   -> Zone 1 = Customer Segments, Zone 2 = Collateral Types
|      Zone 3 = LTV, DTI, score, authority (the decision matrix)
|      Product Types -> Common engine overlay
|
+-- YES, product is simple (few types, uniform risk)?
    -> Zone 3 Values directly in parent B-cell — no sub-GNM needed
       Example: Credit Card — Rewards/Premium/Secured fit in one B-sheet
```

**Key learning:** The deeper Risk wants to control, the more the GNM shifts from organizational structure (Product x BL) toward decision variables (Customer x Collateral).

---
