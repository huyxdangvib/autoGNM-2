---
part: 7
name: "Pre-Submission Checklist"
parent: gnm-instruction.md
---

## ✅ Pre-Submission Checklist

Trước khi hoàn thành GNM, kiểm tra các mục sau:

### Structure Check
- [ ] Tên GNM ở B2 với format `TÊN GNM (Level)`
- [ ] **B2 label uniqueness:** B2 label SHOULD be unique across sibling sheets in the workbook — identical B2 on two sheets with different B5 codes = AMBER (copy-paste bleed). Evidence: `AFC (E)` + `AFD (E)` in VEM myvib share B2=`CURRENT ACCOUNT FUNCTION CLASSIFICATION (E)` despite different B5 codes (2026-04-21). `[exploratory-basis: 3-workbook]`
- [ ] **B2 Merge Range** khớp Bảng tra cứu nhanh (PART 2a): B2 : Col(G+L2+f) — **AMBER** (cosmetic): unmerged B2 is a style deviation but does NOT affect zone semantics, cascade resolution, or parser output. Downgrade from Structural RED to Cosmetic AMBER per MTI 2026-04-20 finding (11/11 sheets in `Thinking processing unit - 260418` are unmerged yet functionally valid GNMs).
- [ ] **Column layout** khớp Column Layout Constraint (PART 2a § Column Position Formula): separator đúng vị trí, Conso. ở cột cuối Thân
- [ ] Phần Đầu có đủ: Header (1)(2), Mã GNM, Content numbering, All, Common
- [ ] Phần Thân có đủ: Zone 1-6, 8 với cột Conso. ở cuối
- [ ] Phần Mở rộng có đủ: Zone 7, 9
- [ ] 3 Separators: Cột A, D, and Col(G+L2+f+1) per PART 2a Scaling Formula (width 20px)
- [ ] **Column widths:** 20px (separators), 100px (Phần Đầu, Zone 1, Phần Mở rộng), 200px (Zone 2-3, Conso.)
- [ ] **Cụm All/Common đồng bộ:** Passed All & Common Synchronization Validation (xem section trên)

### Data Integrity Check
- [ ] Zone 3 không có ô trống (tất cả có Value hoặc "-")
- [ ] Zone 3 Engines có HYPERLINK formula đến sub-GNM (`=HYPERLINK("#'Sheet'!B2", "EngineName MãGNM (Level)")`) — text color #0563C1
- [ ] Mã GNM đồng bộ: E5 = B5 = E8 (dùng formula)
- [ ] Item count: Phần Đầu = Zone 1
- [ ] All cluster rows = Zone 5/6/7 rows
- [ ] Common cluster rows = Zone 8/9 rows
- [ ] Zone boundary — every engine/value in correct zone position: Zone 5 in Feature cols (All rows), Zone 6 in Conso. col (All rows), Zone 8 in Conso. col (Common rows), Zone 9 in Extension cols (Common rows). Zone 1 cols empty in All; Zone 1-3 cols empty in Common.

### Format Check
- [ ] Engine format đúng: `[Tên đầy đủ] MãGNM (Level)` (ví dụ: `Production & Supply Chain PSC (B)`)
- [ ] Keywords ≤ 50 ký tự (tên + mã kết hợp)
- [ ] 3 màu nền: #0070C0, #DDEBF7, #FFFFFF
- [ ] Header row 4: Nền xanh #0070C0, chữ trắng
- [ ] Zone 4-9: CHỈ chứa Engines (Engine ĐÃ LÀ Value - cái tên mang nghĩa)
- [ ] Sub-GNM: Ô A1 chứa `<<` với HYPERLINK formula đến parent sheet, không indent, no wrap text
- [ ] **Wrap text:** Content areas (Zone Headers rows 6-7, Zone 1-9 rows 8+) = wrap_text=True; Headers (row 4), Sub-headers (row 5), B2, A1 = wrap_text=False
- [ ] **Row heights:** Rows động (6+) tự động giãn theo nội dung (autofit sau wrap text)

### Taxonomy Check
- [ ] Level 1 và Level 2 cùng chiều phân loại (đồng chất)
- [ ] Zone 2 Features là TODO (hành động), không phải WHAT

### GNM Construction Quality Check (v5.0)
> Cross-ref: Q-codes map to Part 1 → GNM Construction Quality Layer checks Q1-Q8.
> Pipeline: DECODE → STRUCTURE → MATRIX → CONTENT.

**DECODE stage:**
- [ ] **Q1 — Decoding method:** Correct method for topic type (Classification/Component/Binary/Flow). Single vs Dual decoding appropriate.
- [ ] **Q2 — Perspective lock:** All Zone 1 items share single consistent perspective (đồng dạng phối cảnh) — whether axis holds WHAT or TODO.

**STRUCTURE stage:**
- [ ] **Q3 — Axis coherence:** Zone 1 items form a coherent group. Zone 2 features form a coherent group. (Zone 1 CAN hold TODO, Zone 2 CAN hold WHAT — coherence matters, not noun/verb rigidity.)
- [ ] **Q4 — Structure quality:** Flow axis has output→input chain. Classification axis is MECE. Component axis sums to whole.

**MATRIX stage:**
- [ ] **Q5 — Matrix density:** Zone 3 intersections are meaningful — not empty or filler.
- [ ] **Q6 — Coverage (10-7-5-(-3)):** Topic is fully covered — no major business aspects omitted.

**CONTENT stage:**
- [ ] **Q7 — Nomenclature:** No generic names ("Other", "Misc", "TBD"), no duplicated item names.
- [ ] **Q8 — Content quality:** Zone 3 cells describe full scope of intersection, not just keywords.

### Excel Write Order Check (khi tạo file)
- [ ] Phase sequence: Data → Formulas → Medium Borders → Thin Borders → **Formatting & Wrap Text**
- [ ] E5 & E8 = `=B5` formula trên mọi sheet (không bị data ghi đè)
- [ ] Thin top borders (All/Common) vẫn hiển thị sau khi áp medium borders
- [ ] **Wrap text = Yes** cho content areas (Zone Headers rows 6-7, Zone 1-9 content rows 8+, All, Common)
- [ ] **Wrap text = No** cho headers (row 4), sub-headers (row 5), B2 (Tên GNM), A1 (back-link)
- [ ] **Row autofit** được gọi sau khi set wrap text — rows tự động giãn theo nội dung

---

> **Your role as GNM Builder Expert:** The Pre-Submission Checklist above IS your guardrails. Every unchecked item = ❌ that must be fixed before outputting. Catch errors BEFORE the user sees them.

---

## 📚 Few-Shot Examples

> **Few-Shot Examples** are split across sub-files: **5 core examples** in `references/part-7b-*.md` (always-loaded) and **8 extended examples** in `references/part-7c-*.md` (load on demand for specialized task types). Consult Part 7b before ANY output.

---

