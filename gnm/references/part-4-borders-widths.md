---
part: 4
name: "Borders, Column Widths & Row Heights"
parent: gnm-instruction.md
---

### Cấu hình Toàn bộ Section (Medium Borders)

> **[!] Lưu ý:** End row trong bảng dưới là dynamic. Formula: **End Row = 7 + số_items + số_dòng_All + số_dòng_Common**. Default template: 7 + 3 + 2 + 2 = **14**.

| Section | Vùng Toàn bộ Section | Mục đích | Medium Border | Ghi chú |
|---------|---------------------|----------|---------------|---------|
| **Phần Đầu** | **B4:C[end]** | Bảng định vị index cho toàn bộ GNM | Medium border bao quanh | Bao gồm Header + Sub-header + Content + All + Common |
| **Phần Thân** | **E4:[Conso][end]** | Ma trận WHAT x TODO với Zones 1-6, 8 | Medium border bao quanh | Số cột = f+L2+3 (xem Scaling Formula PART 2a) |
| **Phần Mở rộng** | **2 cột sau separator** | Bối cảnh và nguồn lực bên ngoài | Medium border bao quanh | Luôn 2 cột (Zones 7, 9) |

**Chi tiết áp dụng Medium Border:**
- **Phần Đầu:** Border bao quanh từ Header row 4 đến Common row cuối
- **Phần Thân:** Border bao quanh từ E4 đến cột Conso. và row cuối
- **Phần Mở rộng:** Border bao quanh 2 cột sau separator

> **Ví dụ cụ thể:**
> - Không có Level 2: Phần Thân = E4:I[end], Phần Mở rộng = K4:L[end]
> - Có Level 2: Phần Thân = E4:J[end], Phần Mở rộng = L4:M[end]

**Lưu ý quan trọng:**
- Cột D và Separator Thân-Mở rộng KHÔNG có border, chỉ có width 20px
- Medium border CHỈ áp dụng cho outline của từng section, không áp dụng cho internal borders
- Internal borders (giữa các cụm) vẫn theo quy định riêng của từng Zone/Cluster
- Vị trí Separator thay đổi: J (không Level 2) hoặc K (có Level 2)
- **⚠️ Thứ tự áp dụng border:** Medium section borders (Phase 3) PHẢI được áp dụng TRƯỚC, sau đó Thin cluster borders (Phase 4) overlay lên — xem **Excel Write Order Protocol** (PART 5)
  
### Cấu hình độ rộng cột của toàn bộ GNM

| Thành phần | Không có Level 2 | Có Level 2 | Width |
|------------|------------------|------------|-------|
| Separator đầu | Cột A | Cột A | 20px |
| Phần Đầu | Cột B-C | Cột B-C | 100px/cột |
| Separator Đầu-Thân | Cột D | Cột D | 20px |
| Zone 1 (Level 0) | Cột E | Cột E | 100px |
| Zone 1 (Level 1) | Cột F | Cột F | 100px |
| Zone 1 (Level 2) | - | Cột G | 100px |
| Zone 2-3 content | Cột G-H | Cột H-I | 200px/cột |
| Conso. (Zone 4) | Cột I | Cột J | 200px |
| Separator Thân-Mở rộng | Cột J | Cột K | 20px |
| Phần Mở rộng | Cột K-L | Cột L-M | 100px/cột |

> **Quy tắc shift:** Khi thêm Level 2 (cột G), tất cả cột từ Zone 2 trở đi shift sang phải 1 vị trí.

## Row Height Configuration

| Row Type | Rows | Height (pt) | Height (px) | Loại | Ghi chú |
|----------|------|-------------|-------------|------|---------|
| **Header** | Row 4 | 18pt | 24px | Cố định | Không thay đổi, no wrap text |
| **Sub-header** | Row 5 | 18pt | 24px | Cố định | Không thay đổi, no wrap text |
| **Zone Headers** | Rows 6-7 | 18pt (min) | 24px (min) | Động | Wrap text = Yes → tự động tăng height nếu nội dung dài |
| **Content** | Rows 8+ (items) | 18pt (min) | 24px (min) | Động | Wrap text = Yes → tự động tăng height nếu nội dung dài |
| **All** | Rows sau Content | 18pt (min) | 24px (min) | Động | Wrap text = Yes → tự động tăng height nếu Engine name dài |
| **Common** | Rows sau All | 18pt (min) | 24px (min) | Động | Wrap text = Yes → tự động tăng height nếu Engine name dài |

> **Lưu ý:** 
> - **Rows cố định (Header, Sub-header):** Chiều cao 18pt (24px), không wrap text, không thay đổi
> - **Rows động (Zone Headers, Content, All, Common):** Chiều cao tối thiểu 18pt (24px), **wrap text = Yes**, chiều cao tự động tăng theo nội dung

---

## Wrap Text Rules

> **[!] CRITICAL:** Wrap text là yếu tố quan trọng để GNM hiển thị đúng trong Excel. Khi thiếu wrap text, nội dung dài bị cắt hoặc tràn sang ô kế bên, gây mất thông tin và khó đọc.

| Vùng | Wrap Text | Lý do |
|------|-----------|-------|
| **Header (Row 4)** | **No** | Tiêu đề ngắn ((1), (2)...), không cần xuống dòng |
| **Sub-header (Row 5)** | **No** | Mã GNM và Conso. labels ngắn, không cần wrap |
| **Tên GNM (B2)** | **No** | Tiêu đề chính trên 1 dòng, giữ gọn |
| **Back-link (A1)** | **No** | Chỉ chứa `<<`, không cần wrap |
| **Zone Headers (Rows 6-7)** | **Yes** | Feature labels có thể dài (VD: "Learning & Growth") |
| **Zone 1 Content (Items)** | **Yes** | Tên Item/Sub-item có thể dài (VD: "Corporate Banking") |
| **Zone 2-3 Content (Values/Engines)** | **Yes** | Values và Engine names có thể dài (VD: "Production & Supply Chain PSC(B)") |
| **Zone 4 (Conso.)** | **Yes** | Engine names có thể dài |
| **Zone 5-7 (All)** | **Yes** | Engine names có thể dài |
| **Zone 8-9 (Common)** | **Yes** | Referral Engine names có thể dài |
| **Phần Đầu Content (B-C)** | **No** | Numbering và labels ngắn |
| **Separator columns (A, D, ...)** | **No** | Trống hoàn toàn |

> **Nguyên tắc chung:** No wrap cho các ô cố định/labels ngắn (headers, sub-headers, B2, A1). **Yes wrap cho mọi content area** (Zone 1-9 từ row 6 trở xuống) để đảm bảo nội dung hiển thị đầy đủ, không bị cắt.

**Implementation (openpyxl / ExcelJS):**
```python
# openpyxl example
from openpyxl.styles import Alignment

# Wrap text cho content areas (rows 6+)
wrap_alignment = Alignment(horizontal='left', vertical='top', wrap_text=True, indent=1)
# No wrap cho headers/sub-headers (rows 4-5)
nowrap_alignment = Alignment(horizontal='left', vertical='top', wrap_text=False, indent=1)
# No wrap, no indent cho B2 và A1
nowrap_noindt = Alignment(horizontal='left', vertical='top', wrap_text=False, indent=0)
```

---

