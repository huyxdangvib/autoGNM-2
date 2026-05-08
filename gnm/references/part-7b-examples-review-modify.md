---
part: 7b
name: "Examples: REVIEW & MODIFY"
parent: gnm-instruction.md
---

### Example 2: REVIEW Request -> Response

**User Input:**
> "Review GNM nay giup toi: Zone 3 co 2 o trong, Ma GNM o E5 la 'PRD' nhung B5 la 'PROD'"

**Expected Response:**
```
<thinking>
Step 1: Request Type = REVIEW
Step 2: Detected issues: (a) 2 empty Zone 3 cells, (b) Ma GNM mismatch E5!=B5
Step 2.5: Quote rules:
- PART 1, Critical Rule #1: "Zone 3 khong bao gio de o trong"
- PART 1, Critical Rule #2: "Ma GNM phai dong bo: E5 = B5 = E8"
Step 3: Both are HIGH severity violations.
</thinking>

<answer>
## GNM REVIEW

### Summary
| Metric | Status |
|--------|--------|
| Structure Compliance | Issues |
| Data Integrity | Critical |
| Format Standards | Issues |
| Overall | **NEEDS FIXES** |

### Issues Found
| # | Zone | Issue | Severity | Fix |
|---|------|-------|----------|-----|
| 1 | Zone 3 | 2 o trong trong Value Matrix | **HIGH** | Dien Values hoac "-" vao tat ca o |
| 2 | Zone 1 | Ma GNM khong dong bo (E5!=B5) | **HIGH** | Sua E5 thanh formula `=B5` |

### Detail Fixes

**Issue 1: Zone 3 o trong**
- Rule vi pham: "Zone 3 KHONG duoc de o trong"
- Impact: Mat moi lien he Item-Feature, nguoi doc khong hieu
- Fix: Xac dinh gia tri hoac dien "-" / "N/A"

**Issue 2: Ma GNM khong dong bo**
- Rule vi pham: "Ma GNM phai dong bo: E5 = B5 = E8"
- Impact: Inconsistency, formulas co the loi
- Fix:
  1. Xac dinh Ma GNM dung: "PRD" hay "PROD"?
  2. Ghi vao B5
  3. E5 dung formula `=B5`
  4. E8 cung dung formula `=B5`
</answer>
```

</example>

---

<example type="MODIFY">

### Example 4: MODIFY Request -> Response

**User Input:**
> "GNM WBL (B) hien co 2 Features: Origination va Risk Mgmt. Toi muon them Feature thu 3 la 'Portfolio Monitoring'."

**Expected Response:**
```
<thinking>
Step 1: Request Type = MODIFY (add Feature to existing GNM)
Step 2: Parameters:
- Target: WBL (B) — Wholesale Banking Lending
- Current: 2 Features (Origination, Risk Mgmt) → 3 Features (+Portfolio Monitoring)
- Impact: New col I in Zone 2-3, shift Conso. I→J, shift Separator & Extension cols
Step 2.5: Quote rules:
- PART 1, Critical Rule #1: "Zone 3 khong bao gio de o trong" → new Feature col must have Values/Engines for all Items
- PART 2a, Column Layout Constraint: Feature count determines column structure → recalculate B2 merge range
- PART 5, Write Order: "Phase 1 Data → Phase 2 Formulas → Phase 3 Medium → Phase 4 Thin → Phase 5 Formatting"
Step 3: Build modification plan — impact all 3 sections (Phan Dau, Than, Mo rong).
</thinking>

<answer>
## GNM MODIFICATION: WBL (B) -- Add Feature "Portfolio Monitoring"

### Impact Analysis
| Component | Before | After | Action |
|-----------|--------|-------|--------|
| Zone 2 (Features) | 2 Features (G-H) | 3 Features (G-I) | Them cot I = "Portfolio Monitoring" |
| Zone 3 (Value Matrix) | 3 Items x 2 Features | 3 Items x 3 Features | Them 3 cells cot I (rows 8-10) |
| Zone 4 (Conso.) | Cot I | **Shift -> Cot J** | Di chuyen toan bo Conso. content |
| Separator Than-Mo rong | Cot J | **Shift -> Cot K** | Cap nhat width 20px |
| Phan Mo rong | Cot K-L | **Shift -> Cot L-M** | Cap nhat vi tri 2 cot |
| Header (Row 4) | (1)-(5) | (1)-(6) | Them (6) tai J4 |
| B2 Merge Range | B2:I2 | **B2:J2** | Mo rong merge |

### Step-by-Step Modifications

**1. Zone 2 Update (Row 6-7):**
| G6 | H6 | I6 |
|----|----|----|
| Lending | (rong) | (rong) |
| Origination | Risk Mgmt | Portfolio Monitoring |

**2. Zone 3 -- New Column I (Rows 8-10):**
| Item | Portfolio Monitoring (I) |
|------|--------------------------|
| Working Capital | WC Portfolio Dashboard WPD(Z) |
| Medium-Long Term | MLT Portfolio Review MPR(Z) |
| LC UPAS | Trade Portfolio Tracker TPT(Z) |

> Zone 3 KHONG duoc de o trong -- moi Item phai co Engine/Value cho Feature moi.

**3. Zone 4 (Conso.) Shift I -> J:**
- Di chuyen toan bo Zone 4 engines sang cot J
- Cap nhat Sub-header: J5 = "Conso."
- Cap nhat Zone Headers: J6 = "-", J7 = "-"

**4. Zone 5 Update (All rows, cung cot Zone 2-3):**
- **Existing engines giu nguyen:** G11 = `Lending Origination Standards LOS(Z)`, H11 = `Risk Policy Framework RPF(Z)` (khong thay doi)
- **Them** cot I trong khu vuc All cho Zone 5
- VD: I11 = `Portfolio Monitoring Standards PMS(Z)`

**5. Header Row 4 Update:**
- Them J4 = (6) cho cot Conso. moi
- Format: nhap `-6`, Number Format (1234)

**6. Formulas to Update:**
- E5 = `=B5` (khong doi)
- E8 = `=B5` (khong doi)
- B2 merge range: B2:J2 (mo rong them 1 cot)

### Checklist After Modification
- [ ] Zone 3 cot moi (I8-I10): Khong co o trong
- [ ] Conso. dung o cot cuoi (J) -- khong con o cot I
- [ ] Zone 5 co Engine o cot I (khu vuc All)
- [ ] All/Common rows van dong bo (khong thay doi so dong)
- [ ] Header numbering lien tuc: (1)-(6)
- [ ] Separator Than-Mo rong shift dung vi tri
- [ ] **B2 Merge Range cap nhat: B2:J2** (mo rong theo so cot moi)
- [ ] **Column widths:** Cot moi I = 200px (Zone 2-3 content)
- [ ] Medium borders cap nhat: Phan Than = E4:J[end]
- [ ] Write Order: Data -> Formulas -> Medium -> Thin
</answer>
```

</example>

---

<example type="AMBIGUOUS">

