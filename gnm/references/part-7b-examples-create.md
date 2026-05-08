---
part: 7b
name: "Examples: CREATE"
parent: gnm-instruction.md
---


<part7b_examples>

# PART 7b: FEW-SHOT EXAMPLES (CORE)

> **TL;DR:** 5 Core Few-Shot Examples (CREATE, REVIEW, MODIFY, EXPLAIN, AMBIGUOUS). For task-specific examples (TAXONOMY, CONVERT, CASCADE, VGATE_FAILURE, SINGLE_FEATURE, DELETE_ARCHIVE, REVIEW_VIB, DELETE_CASCADE_MULTI) → load Part 7c.

> **Retrieval Signpost:** For validation logic, mistakes, checklists -> PART 7. For critical rules -> PART 1. For structure core (Column Layout, Dynamic Rows) -> PART 2a. For templates & section details -> PART 2b. For core zones (1-3) -> PART 3a. For engine zones (4-9) -> PART 3b.

## Few-Shot Examples

<examples>
<example type="CREATE">


### Example 1: CREATE Request -> Response

**User Input:**
> "Tao GNM cho Wholesale Banking Lending, level B, voi 3 products: Working Capital, Medium-Long Term, LC UPAS. Features la Origination va Risk Management."

**Expected Response:**
```
<thinking>
Step 1: Request Type = CREATE
Step 2: Parameters:
- Topic: Wholesale Banking Lending
- Level: B -> Zone 3 mostly Engines
- WHAT: Working Capital, Medium-Long Term, LC UPAS (3 items, no Level 2)
- TODO: Origination, Risk Management (2 features)

Step 2.5: Quote rules:
- PART 1, Critical Rule #1: "Zone 3 khong bao gio de o trong"
- PART 1, Critical Rule #4: "Zone 4-9 CHI chua Engines"
- PART 2a, Column Layout: Khong Level 2 -> Zone 2 = G-H, Conso. = I
- PART 3a, Zone 3: "Engine ban than DA LA Value" -> Level B = mostly Engines

Step 3: Validate
- 3 items x 2 features = 6 Zone 3 cells
- WHAT vs TODO: Products = WHAT, Origination/Risk = TODO
- All/Common: 2 dong moi cum (default)
- Column layout: E-F (Zone 1), G-H (Zone 2), I (Conso.)

Step 4.5: Self-verify checklist
- Zone 3: all 6 cells filled
- E5=B5, E8=B5 (formula)
- All sync: 2 rows x 3 phan
- Common sync: 2 rows x 3 phan
</thinking>

<answer>
## GNM SPECIFICATION: WHOLESALE BANKING LENDING (B)

### 1. Overview
| Property | Value |
|----------|-------|
| Ten GNM | WHOLESALE BANKING LENDING (B) |
| Ma GNM | WBL |
| WHAT (Zone 1) | Working Capital, Medium-Long Term, LC UPAS |
| TODO (Zone 2) | Origination, Risk Management |
| Co Level 2 | No (3 products dong cap) |

### 2. Zone 1: Items (Cot E-F)

**Zone Headers (Rows 6-7):** E6=Object, E7=Item, F6=(rong), F7="-"

| Level 0 (E) | Level 1 (F) |
|-------------|-------------|
| WBL | Working Capital |
| (rong) | Medium-Long Term |
| (rong) | LC UPAS |

### 3. Zone 2: Features (Cot G-H, Rows 6-7)
| G6 | H6 |
|----|----|
| Lending | (rong) |
| Origination | Risk Mgmt |

### 4. Zone 3: Value Matrix (Rows 8-10, Cot G-H)
**Logic:** Moi giao diem Item x Feature co Engine rieng voi ma duy nhat.

| Item | Origination | Risk Mgmt |
|------|-------------|----------|
| Working Capital | WC Origination Process WCO(Z) | WC Risk Framework WCR(Z) |
| Medium-Long Term | MLT Origination Process MTO(Z) | MLT Risk Framework MTR(Z) |
| LC UPAS | LCUP Origination Process LCO(Z) | Trade Risk Assessment TRA(Z) |

> **Luu y:** Moi Engine co ma rieng (WCO, MTO, LCO, WCR, MTR, TRA) vi moi o link den 1 sub-GNM khac nhau. KHONG dung cung ma cho nhieu o.

### 5. Zone 4: Conso. Column (I8-I10)
| Item | Conso. (Engine) | Loai |
|------|-----------------|------|
| Working Capital | Working Capital Playbook WCP(Z) | Consolidation |
| Medium-Long Term | MLT Product Playbook MLP(Z) | Consolidation |
| LC UPAS | Trade Finance Classification TFC(Z) | Decoding |

> **Dual purpose:** Zone 4 co the chua consolidation engines (Playbook/Guide) HOAC decoding engines (Classification/Component). O day, LC UPAS dung Decoding vi can phan loai chi tiet cac loai hinh Trade Finance.

> **Zone 4 CHI chua Engines, KHONG chua Values.**
> - Sai: `Working Capital | Mang trong yeu, tang truong 20% YoY` (day la Value, khong co link)
> - Dung: `Working Capital | Working Capital Playbook WCP(Z)` (Engine -- ten du nghia + link sub-GNM)

### 6. Zone 5-9: All & Common Clusters

**Cum All (Rows 11-12, 2 dong):**

| Vung | G11 (Feature 1) | H11 (Feature 2) | I11 (Conso.) | K11-L11 (Mo rong) |
|------|-----------------|-----------------|--------------|-------------------|
| **Zone 5** | Lending Origination Standards LOS(Z) | Risk Policy Framework RPF(Z) | -- | -- |
| **Zone 6** | -- | -- | WB Lending Governance WLG(Z) | -- |
| **Zone 7** | -- | -- | -- | Enterprise Lending Policy ELP(A) |

> Zone 5 nam o cot Feature (G-H), Zone 6 o cot Conso. (I), Zone 7 o Phan Mo rong (K-L). Zone 1 cols (E-F) o All rows = trong.

**Cum Common (Rows 13-14, 2 dong):**

| Vung | E-H (Zone 1-3 cols) | I13 (Conso.) | K13-L13 (Mo rong) |
|------|---------------------|--------------|-------------------|
| **Zone 8** | *(trong)* | Credit Administration CRA(B) | -- |
| **Zone 9** | *(trong)* | -- | External Audit Liaison EAL(A) |

> Zone 8 o cot Conso. (I), Zone 9 o Phan Mo rong (K-L). Zone 1-3 cols (E-H) o Common rows = trong.

**Dong bo check:** All = 2 dong (Phan Dau C11:C12 = Phan Than = Phan Mo rong) | Common = 2 dong (Phan Dau B13:C14 = Phan Than = Phan Mo rong)

### 7. Excel Implementation
- Sheet name: `WBL (B)`
- E5 formula: `=B5`
- E8 formula: `=B5`
- Conso. position: Column I
- Separator columns: A (20px), D (20px), J (20px)
- Total columns Phan Than: 5 (E-I)
- B2 merge: B2:I2
- Write Order: Phase 1 Data → Phase 2 Formulas (E5=B5, E8=B5) → Phase 3 Medium borders → Phase 4 Thin borders → Phase 5 Formatting & Wrap Text

### 8. Assumptions to Verify
> ✏️ **Please confirm or adjust these assumptions before Excel generation:**
> 1. **Zone 5-9 engine names** — proposed based on WB Lending domain defaults (Part 3b). Your org may use different names for lending standards, governance, and referrals.
> 2. **Feature Group "Lending"** — inferred as the perspective grouping Origination + Risk Mgmt. Alternative: "Credit Lifecycle", "Lending Value Chain".
> 3. **Zone 4 per-item engines** — each item gets its own consolidation playbook. Alternative: shared single CPA engine across all items.

### Notes
- Level B nen co Engines cho hau het Zone 3 cells
- Neu can chi tiet hon, tao sub-GNM WBL(Z) cho tung product
</answer>
```

</example>

---

<example type="REVIEW">

