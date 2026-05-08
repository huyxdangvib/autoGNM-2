---
part: 7c
name: "Examples: Delete & Review VIB"
parent: gnm-instruction.md
---

### Example 11: DELETE Engine with Cascade Update

**User:** "Delete the sub-GNM for 'Digital Banking' from VBM(A). The team has been merged into Retail Banking."

<thinking>
**Step 1 — Identify task:** DELETE operation — removing a Zone 3 Engine (sub-GNM reference) and cascading updates.

**Step 2 — Extract parameters:**
- Target: VBM(A) sheet
- Engine to delete: "Digital Banking DB (B)" — a Zone 3 Engine in Body section
- Reason: Team merged into Retail Banking
- Cascade scope: DB(B) sub-GNM sheet + any Zone 5/6/7/8/9 engines referencing DB(B)

**Step 2.5 — Rule quoting:**
- Rule 1: "Zone 3 không có ô trống" → after deletion, cell must contain "-" or replacement value
- Rule 2: "Mã GNM đồng bộ" → if DB(B) sheet deleted, all HYPERLINK references break
- Rule 11: "Write Order" → cascade updates follow Phase 2→3→4→5

**Step 3 — Pre-deletion checklist (Part 5 §7):**
1. ✅ Identify all cells referencing DB(B): VBM(A) Zone 3 cell E10, Zone 5 engine in All row
2. ✅ Check if other GNMs reference DB(B): None found
3. ✅ Determine replacement: Merge content into "Retail Banking RB (B)" or mark "-"
4. ✅ Archive decision: ARCHIVE (rename sheet to `_archived_DB`) — preserves history

**Step 4 — Execute cascade:**

**Sheet: VBM(A)**
- Zone 3 cell E10: Replace `=HYPERLINK("#'DB'!B2","Digital Banking DB (B)")` with `=HYPERLINK("#'RB'!B2","Retail Banking RB (B)")` (merged into existing engine)
- Zone 5 All row: If DB(B) had a vertical engine here, remove and shift remaining engines up; adjust `a` count
- Re-run Sync Validation: a_head = a_body = a_ext? ✅

**Sheet: DB (B)**
- Rename to `_archived_DB` (archive, not delete)
- Update A1 back-link to point to VBM(A)
- Add note in B2: "[ARCHIVED 2026-03-15 — merged into RB(B)]"

**Write Order:** Data updates → Formula updates (E10 HYPERLINK) → Medium borders (unchanged) → Thin borders (recheck All row if shifted) → Formatting

**Step 4.5 — V-gate:**
V-gate: Z3[12/12] Sync[a=2=2=2,c=2=2=2] E5E8[ok] Layout[10col] ZoneBound[ok] Cite[R1,R2,R11] TermCheck[ok]
</thinking>

**Cascade update complete.** Changes applied to VBM(A): Zone 3 engine at E10 redirected from DB(B) to RB(B). DB(B) sheet archived as `_archived_DB`. All/Common sync validated. No other GNMs reference DB(B).

</example>

---

<example type="REVIEW_VIB">

### Example 12: REVIEW + VIB Domain Context

**User Input:**
> "Review GNM RBL(B) cua toi. RBL la Retail Banking Lending, level B, 4 items: Mortgage, Auto, Business Loan, VP. Features: Origination, Servicing. Zone 3 co Engine 'Mortgage Orig MO(Z)' nhung toi khong co Zone 5 engine nao trong All rows."

**Expected Response:**
```
<thinking>
Step 1: Request Type = REVIEW
Step 2: Parameters:
- Topic: RBL (Retail Banking Lending), Level B
- domain_context = "vib" (RBL is VIB Retail Banking Lending per PART 6 VIB Reference)
- Load PART 6 for domain validation
- Items: 4 (Mortgage, Auto, Business Loan, VP)
- Features: 2 (Origination, Servicing)
- L2 = 0
- f=2, L2=0 -> Phan Than = 5 cot (E-I), Conso. at I

Step 2.5: Quote rules:
- PART 6, VIB Business Basic Units: "RBL | RB | Lending | Mortgage / Auto / Business loan / VP" -> Items match VIB domain hierarchy
- PART 1, Critical Rule #9: "Cum All/Common phai dong bo rows -- So dong All trong Phan Dau = Zone 5/6 (Than) = Zone 7 (Mo rong)"
- PART 3b, Zone 5: "Zone 5: Vertical Consolidation -- Cluster: All -- Vi tri cot: Zone 2-3 cols" -> All rows MUST have Zone 5 engines in Feature columns

Step 3: Validate
- Zone 3: 4x2 = 8 cells, user mentions at least 1 engine -> check completeness
- All rows missing Zone 5: CRITICAL violation of Rule #9 and Zone 5 spec
- VIB naming: "Mortgage Orig MO(Z)" -> check format against Rule #5
</thinking>

<answer>
## GNM REVIEW: RBL (B)

### Domain Context
- VIB Retail Banking Lending (PART 6 confirmed: RBL maps to RB > Lending)
- Items match VIB BBU hierarchy: Mortgage, Auto, Business Loan, VP

### Summary
| Metric | Status |
|--------|--------|
| Structure Compliance | Critical |
| Data Integrity | OK |
| VIB Domain Alignment | OK |
| Overall | **NEEDS FIXES** |

### Issues Found
| # | Zone | Issue | Severity | Fix |
|---|------|-------|----------|-----|
| 1 | Zone 5 (All) | All rows co 0 Zone 5 engines -- dong bo bi pha | **HIGH** | Them Zone 5 engines vao Feature cols (G-H) trong All rows |
| 2 | Zone 3 | Engine name "Mortgage Orig MO(Z)" = 22 chars -> OK nhung ten rut gon co the gay nham lan | **LOW** | De nghi doi thanh "Mortgage Origination MO(Z)" (30 chars, ro nghia hon) |

### Detail Fixes

**Issue 1: Zone 5 trong trong All rows (CRITICAL)**
- Rule vi pham: PART 1, Rule #9 "Cum All/Common phai dong bo rows"
- Rule vi pham: PART 3b, Zone 5 "Vertical Consolidation -- Feature cols (All rows)"
- Impact: Mat dong bo giua Phan Dau (a=2), Phan Than (a=0 engines?), va Phan Mo rong (a=?)
- Fix:
  1. Them Zone 5 engines vao All rows, Feature cols (G-H):
     - G row(8+n): `Lending Origination Standards LOS(Z)` (chuan origination chung cho 4 products)
     - H row(8+n): `Lending Servicing Framework LSF(Z)` (chuan servicing chung)
  2. Them Zone 6 engine vao Conso. col (I) All row: `RBL Governance Framework RGF(Z)`
  3. Re-validate: a_head = a_body = a_ext

**Issue 2: Engine name suggestion (LOW)**
- "Mortgage Orig" -> "Mortgage Origination" ro nghia hon, van duoi 50 chars
- Khong bat buoc -- engine name hien tai hop le

### VIB Domain Notes
- RBL(B) nang cap tu: VBM(A) -> RBL(B) cascade (xem PART 6 BBU table)
- VP (Vay phi) la VIB-specific product -- khong co trong generic banking templates
- Goi y: Them forward-reference engine cho VP sub-GNM neu can drill-down: `VP Lending Strategy VPL(Z)`

Ban muon toi tao Zone 5/6 engines cu the hon khong?
</answer>
```

</example>

---

<example type="DELETE_CASCADE_MULTI">

