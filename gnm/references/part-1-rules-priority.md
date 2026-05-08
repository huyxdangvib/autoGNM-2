---
part: 1
name: "Critical Rules & Priority"
parent: gnm-instruction.md
---

> **Scope:** These 11 Critical Rules govern **structural integrity** (what makes a valid GNM). For **construction quality** checks (conceptual soundness: decoding, axis coherence, matrix density), see `part-1-construction-quality.md` § Pre-V-gate Quality Checks (Q1-Q8). Different scope — do not confuse Rule #N with Q-check #N.

## ⚠️ CRITICAL RULES (Non-Negotiable)

| # | Rule | Why Critical |
|---|------|-------------|
| 1 | **Zone 3 không bao giờ để ô trống** | Zone 3 = Value Matrix, mọi giao điểm WHAT x TODO phải có nghĩa |
| 2 | **Mã GNM phải đồng bộ: E5 = B5 = E8** | B5 (Phần Đầu) = source of truth. **E5 (Sub-header row 5) = `=B5`**. **E8 (Level 0 row 8) = `=B5` OR `=E5`** (both chain to B5 — mathematically equivalent; v5.12.0 clarification). Cả 2 phải là FORMULA, không static text. Write Order: Phase 1 skip E5/E8 → Phase 2 ghi formula. Producers MAY use `=E5` at E8 for shorter formula; validators MUST accept both forms. |
| 3 | **Conso. luôn là cột cuối cùng** | Conso. tổng hợp TẤT CẢ Features |
| 4 | **Zone 4-9 CHỈ chứa Engines** | Engines ĐÃ LÀ Value — tên mang nghĩa, không cần Value bổ sung |
| 5 | **Engine format: `[Tên đầy đủ] MãGNM (Level)`** | VD: `Production & Supply Chain PSC (B)` — tên mang nghĩa |
| 6 | **Keywords tối đa 50 ký tự** | Đảm bảo hiển thị gọn trong ô Excel |
| 7 | **Chỉ dùng 3 màu nền** | #0070C0 (Header), #DDEBF7 (Sub-header), #FFFFFF (Content) |
| 8 | **Sub-GNM phải có back-link ở A1** | Ô A1 chứa `<<` với **HYPERLINK formula** `=HYPERLINK("#'Parent'!A1", "<<")` |
| 9 | **Cụm All/Common phải đồng bộ rows** | Số dòng All trong Phần Đầu = Zone 5/6 (Thân) = Zone 7 (Mở rộng). Số dòng Common trong Phần Đầu = Zone 8 (Thân) = Zone 9 (Mở rộng) |
| 10 | **Khu vực trống bắt buộc trong All/Common** | All rows: Zone 1 columns = trống. Common rows: Zone 1 + Zone 2-3 columns = trống. CHỈ Conso. và Mở rộng có Engines |
| 11 | **Excel Write Order: Data → Formulas → Medium → Thin → Formatting** | Phải tuân thủ 5-phase sequence: (1) Data/Labels, (2) Formulas (E5=B5, E8=B5), (3) Section Medium borders, (4) Cluster Thin borders overlay, (5) Formatting & Wrap Text (alignment, wrap_text=True cho content areas, row autofit). Sai thứ tự → border ghi đè, formula bị mất, wrap text bị reset |
| 12 | **Cascade MAY be inlined via HYPERLINK engines in Z3-Z7 — Z8/Z9 are OPTIONAL** | Production (BNW Development & Delivery, 2026-04-16) proves inline cascade is a valid — often preferred — pattern. Empty Z8/Z9 rows do NOT invalidate a GNM when HYPERLINK engines in Z3-Z7 carry the parent-child cascade. Validators MUST NOT penalize empty Z8/Z9 when the workbook uses inline cascade. Choose ONE cascade mechanism per workbook (inline OR Z8/Z9) and apply consistently |
| 13 | **Z-level sheets fall into 3 sub-types: Z-M / Z-P / Z-T — with different compliance targets** | **Z-M (Measurement)** ≈90% Values — KPI/goals/dashboards (e.g. 7(Z) Lead Goal, 2A(Z) Lead Allocation). **Z-P (Process)** ≈80% Engines — RACI/Plan/Workflow (e.g. 5(Z) RACI, 6(Z) Implementation Plan, BLC(Z) Campaign Pattern). **Z-T (Template)** ≈80% empty scaffold awaiting data (e.g. 2A.1(Z) WHCM Lead Details). Validators MUST identify sub-type BEFORE applying ratio checks. A RACI with 100% engines (R/A/C/I codes) is valid Z-P, NOT a violation. Flow Decoding (PDCA/SMART) at Z1 is ALLOWED for Z-P sheets only |

</critical_rules>

---

## Instruction Priority

### MUST (Bắt buộc - Vi phạm = GNM không hợp lệ)
- Zone 3 điền đầy đủ (không ô trống)
- Engine format: `[Tên đầy đủ] MãGNM (Level)` — tên mang nghĩa
- 3 màu nền theo quy định
- Mã GNM đồng bộ: E5 = B5 = E8 (dùng formula `=B5`)
- Conso. ở cột cuối cùng
- Sub-GNM phải có `<<` back-link tại A1 (HYPERLINK formula)
- **Cụm All/Common đồng bộ rows:** Số dòng Phần Đầu = Phần Thân = Phần Mở rộng
- **Khu vực trống bắt buộc:** Zone 1 cols ở All rows = trống; Zone 1-3 cols ở Common rows = trống
- **Keywords ≤ 50 ký tự** (tên + mã cộng lại)
- **Excel Write Order bắt buộc:** Data/Labels → Formulas (E5=B5, E8=B5) → Section Medium Borders → Cluster Thin Borders (overlay) → Formatting & Wrap Text (alignment, wrap, autofit)

### SHOULD (Nên làm - Best practice)
- Sử dụng HYPERLINK formulas (không dùng hyperlink objects)
- Level 1-2 taxonomy đồng chất

### MAY (Có thể - Tùy chọn)
- Dotted pattern cho content areas
- Mở rộng All/Common clusters
- Italic cho Zone 8/9 referral
- Conditional formatting

---

> **Cascade Patterns & Level-to-Scope Mapping:** See `part-1-system-role.md` § Cascade Patterns and § Level-to-Scope Mapping for full definitions (Multi-A, Single-A, A→Z Direct patterns and organizational role mapping).

---

