---
part: 5
name: "Excel Technical Specifications"
parent: gnm-instruction.md
---

## Excel Technical Specifications

### 1. Số trong ngoặc đơn (Header Row 4)
Number Format: nhập `-1`, `-2`, `-3`... -> hiển thị `(1)`, `(2)`, `(3)`...

| Setting | Value |
|---------|-------|
| **Decimal places** | 0 |
| **Negative numbers** | (1234) |
| **Sample** | `(1)` |

### 2. Sử dụng công thức tự động
- **Đếm dòng:** `=ROW()-ROW($C$7)` trong C8, C9, C10... để tự động tạo số 1, 2, 3...
- **Liên kết Mã GNM:** `=B5` trong ô E5 để đồng bộ mã GNM giữa Phần Đầu và Phần Thân
- **Header numbering:** `(1)`, `(2)`, `(3)` trong các ô C5, C6, C7 cho index structure
- **All indexing:** `=C11` để tự động đánh số trong cụm All nếu cần
- **Tránh circular reference:** Kiểm tra không có công thức tự tham chiếu

### 3. Áp dụng họa tiết chấm (Dotted Pattern)
Zone 3 và các content areas (dòng 8 trở đi) cần có nền chấm nhẹ để phân biệt với header:
1. Chọn vùng content areas: Phần Đầu (B8 trở xuống), Phần Thân (E8 trở xuống), Phần Mở rộng (rows 8 trở xuống)
2. Mở Format Cells -> Fill tab
3. Chọn Pattern Style: "Gray 6.25%" hoặc dotted pattern
4. Pattern Color: Xám nhạt (#F2F2F2)
5. Background: Trắng (#FFFFFF)
6. Lưu ý: Chỉ áp dụng cho content, không áp dụng cho headers (#DDEBF7)

### 4. Format Engine references
- **Format chuẩn: `[Tên đầy đủ] MãGNM (Level)`**
- Ví dụ đúng: `Production & Supply Chain PSC (B)`, `Risk Management Framework RMF (A)`
- Ví dụ sai: `PRD B`, `MTG-Z`, `CBB#Z1`, hoặc chỉ có `PSC (B)` không có tên
- **Engine name phải đủ nghĩa** — người đọc hiểu ngay ô nói về gì
- **50-char overflow:** If Engine name exceeds 50 chars, abbreviate the descriptive name — preserve CODE(Level) suffix first, then abbreviate middle words, then use standard acronyms. VD: `Prod. & Supply Chain Mgmt PSCM(B)`

### 5. Quản lý mở rộng zones
- **Zone 5, 6, 7:** Số dòng Cụm All phải ≥ số Engines nhiều nhất trong Zone 5/6/7. Khi thêm Engine, thêm dòng All ở cả Phần Đầu, Phần Thân và Phần Mở rộng
- **Zone 8, 9:** Số dòng Cụm Common phải ≥ số Engines nhiều nhất trong Zone 8/9. Khi thêm Engine, thêm dòng Common ở cả 3 phần
- Luôn giữ đồng bộ giữa Phần Đầu (index) và các Zone tương ứng trong Phần Thân/Mở rộng
- Khi mở rộng, đảm bảo cập nhật cả styling và borders tương ứng

### 6. Tạo GNM con (Sub-GNM)
Khi cần tạo GNM chi tiết từ các Engines:
1. **Xác định phạm vi:** Từ Engine trong GNM chính, xác định nội dung cần mở rộng
2. **Tạo sheet mới:** Tên sheet = `MãGNM (Level)`  -  VD: `PRD (B)`, `MTG (Z)`
3. **Áp dụng template:** Sử dụng cùng cấu trúc 9-zone cho GNM con
4. **Tạo Engine link từ Parent (HYPERLINK formula):**
   - Trong Parent GNM, tại Zone 3/4/5/6, nhập formula:
   - `=HYPERLINK("#'PRD (B)'!B2", "Production & Supply Chain PRD(B)")`
   - Engine name đã mang nghĩa, không cần Value bổ sung
   - **⚠️ KHÔNG dùng Insert → Hyperlink** — chỉ dùng formula
5. **Tạo back-link ở A1 (BẮT BUỘC - HYPERLINK formula):**
   - Ô A1 của Sub-GNM chứa ký hiệu `<<`
   - **Formula (BẮT BUỘC):** `=HYPERLINK("#'PRD (A)'!A1", "<<")`
   - **⚠️ KHÔNG dùng Insert → Hyperlink** — chỉ dùng formula
   - Mục đích: Cho phép user navigate ngược về GNM cha nhanh chóng
6. **Liên kết ngược:** GNM con's Zone 7 engines MAY include a reference to the parent GNM's scope context (e.g., parent's strategy framework as a Zone 7 engine). This is a cross-cutting context link, different from the A1 `<<` back-link
7. **Đồng bộ styling:** Giữ nguyên color scheme và formatting standards
8. **Khi nào tạo sub-GNM:** Khi Zone 3 cell cần >3 dòng chi tiết, hoặc khi 1 Engine cần giải thích >5 items

**Tóm tắt HYPERLINK formulas cần thiết:**
| Vị trí | Trong Sheet | Formula |
|--------|-------------|---------|
| Engine link | Parent GNM (Zone 3/4/5/6) | `=HYPERLINK("#'Sub-GNM'!B2", "MãGNM (Level)")` |
| Back-link | Sub-GNM (A1) | `=HYPERLINK("#'Parent'!A1", "<<")` |

### 7. DELETE/ARCHIVE Operations (Cascade Integrity)

When removing an Engine or sheet from a GNM workbook:

**Pre-deletion checklist:**
1. **Identify dependents:** Search all sheets for HYPERLINK formulas pointing to the target sheet
2. **Classify impact:**
   - **Leaf deletion** (no sheets link TO the target) → safe to delete
   - **Referenced deletion** (other sheets link to target) → requires cascade update

**Cascade update protocol:**
| Step | Action | Example |
|------|--------|---------|
| 1 | Replace Engine cell with Value or "-" in parent sheet | `=HYPERLINK("#'MTG(B)'!B2", "Mortgage MTG(B)")` → `Mortgage (archived)` |
| 2 | Remove HYPERLINK formula, set text color from #0563C1 to #000000 | Engine becomes plain text |
| 3 | Update Phần Đầu numbering if items removed | Renumber C8+ sequential |
| 4 | Re-run All/Common sync validation (PART 7) | Row counts may change |
| 5 | Delete or hide the target sheet | Right-click → Delete/Hide |

**Archive vs Delete:**
- **Archive (SHOULD):** Hide the sheet (right-click → Hide) rather than deleting. Preserves data for audit trail. Back-link at A1 still works if unhidden later.
- **Delete (MAY):** Permanently remove the sheet. All HYPERLINK references become `#REF!`. Only use when the content is obsolete and unneeded.

**Zone impact rules:**
- Deleting a Zone 3 Engine → replace with "-" or a Value summary (Zone 3 cannot be empty)
- Deleting a Zone 4-9 Engine → replace with "-" (Engine-only zones allow "-" as placeholder)
- Deleting an entire Item (Zone 1 row) → remove row from ALL 3 sections (Phần Đầu, Thân, Mở rộng), update Dynamic Row Formula, re-run sync validation

> **Write Order applies:** After cascade updates, re-run Phase 2 (formulas) → Phase 3 (medium borders) → Phase 4 (thin borders) → Phase 5 (formatting) on affected sheets.

---

