---
part: 7
name: "Mistakes & Sync Validation"
parent: gnm-instruction.md
---


<part7_validation>

# PART 7: REFERENCE & VALIDATION

> **TL;DR:** PART 7 là quality assurance — Mistakes & Anti-patterns (18 lỗi xếp theo severity), All/Common Sync Validation (5-step checklist), Pre-Submission Checklist (4 nhóm check), Guardrails (19-point self-check), và **Few-Shot Examples (5 core in Part 7b, 8 extended in Part 7c)**. **⚠️ BẮT BUỘC tham chiếu PART này trước khi finalize output.**

> **📌 Retrieval Signpost:** For critical rules → see PART 1. For structure core (Column Layout, Dynamic Rows) → see PART 2a. For templates & section details → see PART 2b. For core zones (1-3) → see PART 3a. For engine zones (4-9) → see PART 3b.


## ⛔ Mistakes & Anti-patterns (Unified Reference)

> **Cách đọc:** Hợp nhất Mistakes & Anti-patterns theo severity giảm dần. Mistakes #1-7 map to 7 of the 11 Critical Rules (PART 1). Mistake #→Rule #: 1→1, 2→2, 3→4, 4→3, 5→5, 6→11, 7→9. Bổ sung "tại sao sai" và "cách sửa".

| # | Rule | Severity | Lỗi / Anti-pattern | Tại sao sai | Sửa / Thay thế |
|---|------|----------|---------------------|-------------|-----------------|
| 1 | Rule 1 | **HIGH** | Zone 3 có ô trống / Tạo GNM không có Zone 3 | Zone 3 = trái tim GNM, mỗi giao điểm Item×Feature phải có ý nghĩa | Điền Value/Engine hoặc "-". Luôn xác định Zone 3 trước |
| 2 | Rule 2 | **HIGH** | Mã GNM không khớp (B5≠E5≠E8) | Mã GNM là định danh duy nhất, mất đồng bộ → formula lỗi | `E5=B5`, `E8=B5` (formula, không static) |
| 3 | Rule 4 | **HIGH** | Values trong Zone 4-9 thay vì Engines | Zone 4-9 CHỈ chứa Engines (đã là Value — tên mang nghĩa) | Engine format: `[Tên đầy đủ] MãGNM (Level)` |
| 4 | Rule 3 | **HIGH** | Conso. không ở cột cuối Phần Thân | Conso. tổng hợp TẤT CẢ Features → phải là cột cuối | Shift Conso. sang cuối khi thêm Features |
| 5 | Rule 5 | **HIGH** | Engine chỉ có mã, không có tên (`PSC (B)`) | Người đọc không hiểu ô nói về gì | `Production & Supply Chain PSC (B)` |
| 6 | Rule 11 | **HIGH** | Thin border ghi trước Medium / E5-E8 data ghi đè formula | Write Order vi phạm → border mất, formula mất | **5-Phase Write Order**: Data→Formulas→Medium→Thin→Formatting |
| 7 | Rule 9 | **HIGH** | All/Common rows không đồng bộ giữa 3 phần | Phần Đầu 2 dòng, Phần Thân 3 dòng → lệch cấu trúc | Đếm: Phần Đầu = Phần Thân = Phần Mở rộng |
| 8 | - | **MED** | Zone 5 ở cột Conso. / Zone 8 ở cột Feature | Zone 5 = Vertical (cùng cột Zone 2-3); Zone 8 = Referral (cột Conso.) | Zone 5→cột Feature. Zone 6/8→cột Conso. Zone 9→Phần Mở rộng |
| 9 | - | **MED** | Engine ở Zone 1 cols khu vực All | Zone 1 cols trong All rows phải trống | Zone 5 chỉ ở cột Feature, Zone 6 ở cột Conso. |
| 10 | - | **MED** | Level 1-2 taxonomy không đồng chất | L1="Corporate Bond" (Issuer) + L2="Short-term" (Tenor) = 2 chiều khác nhau | L1-L2 phải cha-con cùng chiều. VD: Corporate→Large Cap |
| 11 | - | **MED** | Trộn WHAT và TODO | Zone 1=WHAT, Zone 2=TODO — trộn mất ý nghĩa matrix | Phân tách rõ ràng trước khi bắt đầu |
| 12 | - | **MED** | Item count Phần Đầu ≠ Zone 1 | Index phải phản ánh chính xác structure Body | Cập nhật đồng thời; All/Common shift khi thêm items |
| 13 | - | **MED** | Tạo >3 levels trong Zone 1 | GNM chỉ support L0, L1, L2 — quá sâu = khó đọc | Tách thành sub-GNM. **Exceptions:** (1) Z-level classification GNMs: up to 5 levels (see PART 3a Situational Decoding). (2) A-level organizational GNMs: up to 4 levels for nested scope (see PART 3a). |
| 14 | - | **LOW** | Bỏ qua back-link `<<` ở A1 / dùng hyperlink objects | Lost in navigation; objects dễ hỏng khi copy/rename | Luôn dùng HYPERLINK formula: `=HYPERLINK("#'Parent'!A1","<<")` |
| 15 | - | **LOW** | Quên cột ngăn cách (separator) | Mất visual separation → GNM rối | 3 separators: Cột A, D, and [position per PART 2a Scaling Formula] (width 20px) |
| 16 | - | **LOW** | Sử dụng sai màu nền | Màu có ý nghĩa cố định — #0070C0 (Header), #DDEBF7 (Sub-header), #FFFFFF (Content) | Chỉ dùng 3 màu theo quy định |
| 17 | - | **MED** | Không bật wrap text cho content areas | Nội dung dài bị cắt hoặc tràn sang ô kế bên → mất thông tin, GNM khó đọc | wrap_text=True cho Zone Headers (rows 6-7) và mọi content (rows 8+). wrap_text=False CHỈ cho rows 4-5, B2, A1 |
| 18 | - | **MED** | Không autofit row height sau khi wrap text | Rows giữ chiều cao cố định → nội dung bị ẩn dù đã wrap | Sau Phase 5 (Formatting), gọi autofit row height cho tất cả rows động (6+) |

---

## 🔄 All & Common Cluster Synchronization Validation

> **[!] CRITICAL:** Trước khi output GNM, BẮT BUỘC thực hiện validation này. Đây là nguồn lỗi phổ biến nhất.

### Step 1: Đếm rows
```
n = số items trong Zone 1 Content
a = số dòng Cụm All (tối thiểu 2, tăng theo số Engines Zone 5/6/7)
c = số dòng Cụm Common (tối thiểu 2, tăng theo số Engines Zone 8/9)
```

### Step 2: Xác nhận vị trí
```
Content rows:  8 → 7+n
All start:     8+n
All end:       7+n+a
Common start:  8+n+a
Common end:    7+n+a+c
```

### Step 3: Kiểm tra đồng bộ All (✅ mỗi check)

| Check | Phần Đầu | Phần Thân | Phần Mở rộng | Pass? |
|-------|----------|-----------|--------------|-------|
| Số dòng All | C: "All" + (a-1) rỗng = **a dòng** | Zone 5 + Zone 6 = **a dòng** | Zone 7 = **a dòng** | ☐ |
| Zone 5 vị trí | — | Cùng cột Zone 2-3, rows All | — | ☐ |
| Zone 6 vị trí | — | Cột Conso., rows All | — | ☐ |
| Zone 7 vị trí | — | — | 2 cột Mở rộng, rows All | ☐ |
| Zone 1 cols = trống | — | Cột E-F(/G) khu vực All = trống | — | ☐ |

### Step 4: Kiểm tra đồng bộ Common (✅ mỗi check)

| Check | Phần Đầu | Phần Thân | Phần Mở rộng | Pass? |
|-------|----------|-----------|--------------|-------|
| Số dòng Common | B: "Common" + (c-1) rỗng; C: "-" + (c-1) rỗng = **c dòng** | Zone 8 = **c dòng** | Zone 9 = **c dòng** | ☐ |
| Zone 8 vị trí | — | Cột Conso., rows Common | — | ☐ |
| Zone 9 vị trí | — | — | 2 cột Mở rộng, rows Common | ☐ |
| Zone 1-3 cols = trống | — | Cột E đến Feature cuối, khu vực Common = trống | — | ☐ |

### Step 5: Kiểm tra Thin Top Border
- [ ] Dòng đầu All **Phần Đầu:** Thin top border ở **ô C** (ô B **KHÔNG** có top border)
- [ ] Dòng đầu All **Phần Thân & Mở rộng:** Thin top border ở **tất cả ô** (toàn bộ row)
- [ ] Dòng đầu Common **tất cả Phần:** Thin top border ở **tất cả ô** (bao gồm cả B trong Phần Đầu)

> **Nếu bất kỳ check nào FAIL → DỪNG LẠI và sửa trước khi output.**

---

