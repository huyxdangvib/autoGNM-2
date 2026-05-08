---
part: 7c
name: "Examples: Multi-Sheet DELETE CASCADE"
parent: gnm-instruction.md
---

### Example 13: Multi-Sheet DELETE CASCADE (A->B->Z)

**User Input:**
> "Xoa RBL(B) khoi RBB(A). RBL co 2 sub-GNM: MO(Z) va ALS(Z). Team Lending da duoc merge vao Card team. Archive tat ca."

**Expected Response:**

<thinking>
**Step 1 — Identify task:** DELETE cascade — removing RBL(B) from parent RBB(A), plus 2 child sheets MO(Z) and ALS(Z).

**Step 2 — Extract parameters:**
- Parent: RBB(A) — Retail Banking Business overview
- Target: RBL(B) — Retail Banking Lending (Engine in RBB(A) Zone 3)
- Children: MO(Z) — Mortgage Origination, ALS(Z) — Auto Lending Strategy
- Cascade depth: 3 levels (A -> B -> Z x2)
- Reason: Lending team merged into Card team
- Action: ARCHIVE all 3 sheets

**Step 2.5 — Rule quoting:**
- PART 1, Critical Rule #1: "Zone 3 khong bao gio de o trong" -> after removing RBL(B) engine from RBB(A), cell must have replacement or "-"
- PART 1, Critical Rule #2: "Ma GNM dong bo: E5 = B5 = E8" -> archived sheets keep formulas intact
- PART 1, Critical Rule #8: "Sub-GNM phai co back-link o A1" -> archived sheets update back-link note
- PART 1, Critical Rule #9: "All/Common phai dong bo rows" -> if RBL(B) was referenced in Zone 5/6/7/8 of RBB(A), removing it changes engine count
- PART 5, Write Order: "Phase 2 formulas -> Phase 3 borders" -> cascade updates follow write order

**Step 3 — Pre-deletion checklist (Part 5 §7):**

| Check | RBB(A) | RBL(B) | MO(Z) | ALS(Z) |
|-------|--------|--------|-------|--------|
| Cells referencing target | Zone 3 col G, row for "Lending" | -- | A1 back-link to RBL(B) | A1 back-link to RBL(B) |
| Other GNMs referencing | None | RBB(A) Zone 3 | RBL(B) Zone 3 | RBL(B) Zone 3 |
| Replacement strategy | Redirect to RBC(B) Card team | Archive | Archive | Archive |
| Archive decision | N/A (stays active) | `_archived_RBL` | `_archived_MO` | `_archived_ALS` |

**Step 4 — Execute cascade (bottom-up):**

**Phase A: Archive children first (MO(Z), ALS(Z))**
- MO(Z): Rename sheet to `_archived_MO`
  - B2 append: "[ARCHIVED 2026-03-15 — parent RBL merged into RBC]"
  - A1 back-link: keep pointing to `_archived_RBL` (will exist after Phase B)
- ALS(Z): Rename sheet to `_archived_ALS`
  - B2 append: "[ARCHIVED 2026-03-15 — parent RBL merged into RBC]"
  - A1 back-link: keep pointing to `_archived_RBL`

**Phase B: Archive RBL(B)**
- Rename sheet to `_archived_RBL`
- B2 append: "[ARCHIVED 2026-03-15 — Lending merged into Card team]"
- Zone 3 engines: MO(Z), ALS(Z) HYPERLINKs now point to `_archived_*` sheets -> update formula targets
- A1 back-link: update to `=HYPERLINK("#'RBB (A)'!A1", "<<")`

**Phase C: Update parent RBB(A)**
- Zone 3: Replace `=HYPERLINK("#'RBL (B)'!B2","Retail Banking Lending RBL(B)")` with `=HYPERLINK("#'RBC (B)'!B2","Retail Banking Card RBC(B)")` (Lending merged into Card)
- Zone 5 All rows: If RBL(B) was referenced as a vertical engine, remove and replace with RBC(B) equivalent
- Zone 8 Common rows: Check if RBL(B) was an internal referral -> remove if so
- Re-validate sync: a_head = a_body = a_ext, c_head = c_body = c_ext

**Write Order for cascade:**
```
# Bottom-up archive, top-down update
sheets_archive = ['MO (Z)', 'ALS (Z)', 'RBL (B)']  # children first
sheets_update = ['RBB (A)']

# Phase 1: Data updates (archive notes, replacement labels)
for s in sheets_archive: add_archive_note(s)
for s in sheets_update: update_zone3_replacement(s)

# Phase 2: Formula updates (HYPERLINKs, back-links)
for s in sheets_archive: update_hyperlinks(s)
for s in sheets_update: update_hyperlinks(s)

# Phase 3-5: Borders + formatting on updated parent only
set_section_medium_border('RBB (A)')
set_cluster_thin_border('RBB (A)')
set_formatting('RBB (A)')
```

**Step 4.5 — V-gate (RBB(A) only — archived sheets frozen):**
V-gate: Z3[5/5] Sync[a=2=2=2,c=2=2=2] E5E8[ok] Layout[4col] ZoneBound[ok] Cite[R1,R2,R8,R9] TermCheck[ok]
</thinking>

**Cascade DELETE complete.** Summary:

| Sheet | Action | New Name | Notes |
|-------|--------|----------|-------|
| MO(Z) | ARCHIVE | `_archived_MO` | Back-link to `_archived_RBL` |
| ALS(Z) | ARCHIVE | `_archived_ALS` | Back-link to `_archived_RBL` |
| RBL(B) | ARCHIVE | `_archived_RBL` | All HYPERLINKs updated to archived children |
| RBB(A) | UPDATE | (unchanged) | Zone 3: RBL(B) engine replaced with RBC(B). Sync re-validated |

> **Key principle:** Archive bottom-up (children -> parent), update top-down (parent zone references). This preserves HYPERLINK chain integrity throughout the cascade.

</example>

</examples>

---

> **End of Part 7c (Extended Examples) v4.11.4** — 8 task-specific examples loaded. For core examples (CREATE, REVIEW, MODIFY, EXPLAIN, AMBIGUOUS) -> PART 7b. For rule clarification, PART 1 is authoritative. For structure specs, PART 2a (core) / PART 2b (templates) is SSOT.

