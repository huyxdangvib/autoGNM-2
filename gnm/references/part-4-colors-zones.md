---
part: 4
name: "Colors & Zone Positioning"
parent: gnm-instruction.md
---


<part4_styling>

# PART 4: STYLING & LAYOUT REFERENCE

> **TL;DR:** PART 4 là bảng tra cứu styling — chỉ tham chiếu khi cần áp dụng màu sắc, border, vị trí ô, column widths, hoặc row heights. Không chứa logic nghiệp vụ — logic nằm ở PART 2a/2b (Structure) và PART 3a/3b (Zones).


## Master Color Reference Table

Bảng màu thống nhất cho toàn bộ GNM:

| Component | Background | Text Color | Font Style | Border | Wrap |
|-----------|------------|------------|------------|--------|------|
| **Header (Row 4)** | #0070C0 | #FFFFFF | Normal | Medium top | **No** |
| **Sub-header B5:B7** | #FFFFFF | #000000 | Normal | - | **No** |
| **Sub-header C5:C7** | #DDEBF7 | #000000 | Normal | - | **No** |
| **Sub-header E5** | #DDEBF7 | #000000 | Normal | - | **No** |
| **Sub-header Conso.** | #DDEBF7 | #000000 | Normal | - | **No** |
| **Zone Headers (Rows 6-7)** | #DDEBF7 | #000000 | Normal | - | **Yes** |
| **Content - Values (Zone 3)** | #FFFFFF | #000000 | Normal | - | **Yes** |
| **Content - Engines (Zone 3)** | #FFFFFF | #0563C1 | Normal (link) | - | **Yes** |
| **Content - Zone 1 (Items)** | #FFFFFF | #000000 | Normal | - | **Yes** |
| **Content - Zone 4 (Conso.)** | #FFFFFF | #0563C1 | Normal (link) | - | **Yes** |
| **Content - Zone 8,9 (Referral)** | #FFFFFF | #0563C1 | Normal (link) | - | **Yes** |
| **All Cluster (Zone 5,6,7)** | #FFFFFF | #0563C1 | Normal (link) | Thin top | **Yes** |
| **Common Cluster (Zone 8,9)** | #FFFFFF | #0563C1 | Normal (link) | Thin top | **Yes** |
| **Tên GNM (B2)** | #FFFFFF | #000000 | Bold, 14pt | - | **No** |
| **Back-link (A1)** | #FFFFFF | #0563C1 | Normal (link) | - | **No** |

---

## Master Reference Table: Zone + Cluster Positioning

### Tên GNM trong Excel Default Template:
- **Tên Sheet:** `Mã GNM (Level)` - VD: `GEL (B)`, `MTZ (Z)`, `PRD (A)`
- **Vị trí Tên GNM:** Ô B2
- **Giá trị B2:** `EXAMPLE LIBRARY (B)`
- **Định dạng:** Font Myriad Pro, 14pt, in đậm (Bold), nền #FFFFFF, chữ #000000, không indent, no wrap text

### Bảng Định vị 9 Zones

> **[!] Lưu ý về Row Numbers:** Các row numbers trong bảng dưới đây là cho **default template với 3 items** (rows 8-10). Actual row positions sẽ thay đổi động tùy theo số items trong Zone 1. Ví dụ: nếu có 5 items (rows 8-12), thì All cluster sẽ bắt đầu từ row 13, Common từ row 15.

| Zone | Section/Phần | Vị trí trong Excel | Mục đích | Loại dữ liệu | Màu nền | Màu chữ | Border |
|------|--------------|-------------------|----------|--------------|---------|---------|--------|
| **Zone 1** | **Phần Thân** | Cột E-F (mặc định) hoặc E-G (khi cần Level 2) | WHAT - Level 0 (Mã GNM) + Level 1 (Item) + Level 2 (nếu cần) | Tên, mã, định danh | Row 6-7: #DDEBF7<br>Row 8+: #FFFFFF | #000000 | - |
| **Zone 2** | **Phần Thân** | 1-5 cột sau Zone 1: Col(G+L2) đến Col(G+L2+f-1) | TODO - Features/Actions | Tính năng, hành động | #DDEBF7 | #000000 | - |
| **Zone 3** | **Phần Thân** | Cùng cột Zone 2, Dòng 8+ | Giá trị/Engines (Item x Feature) | Values, Engines | #FFFFFF | Values: #000000, Engines: #0563C1 (Link) | - |
| **Zone 4** | **Phần Thân** | Cột Conso. = Col(G+L2+f), Dòng 8+ | Horizontal Consolidation of Zone 3 (Engine only) | Engines only | #FFFFFF | #0563C1 (Link) | - |
| **Zone 5** | **Phần Thân** | Cùng cột Zone 2-3, khu vực All | Vertical Consolidation of Zone 3 (Engine only, Feature-level consolidation or Decoding) | Engines only | #FFFFFF | #0563C1 (Link) | - |
| **Zone 6** | **Phần Thân** | Cột Conso., khu vực All | Common matters of Zone 3, 4, 5 (Engine only) | Engines only | #FFFFFF | #0563C1 (Link) | - |
| **Zone 7** | **Phần Mở rộng** | 2 cột Phần Mở rộng, khu vực All | Common matters of Zone 3, 4, 5, 6 (Engine only) | Engines only | #FFFFFF | #0563C1 (Link) | - |
| **Zone 8** | **Phần Thân** | Cột Conso., khu vực Common | Internal functions interaction - Referral to others' GNM | Engines (referral) | #FFFFFF | #0563C1 (Link) | - |
| **Zone 9** | **Phần Mở rộng** | 2 cột Phần Mở rộng, khu vực Common | Extended functions interaction - Referral to others' GNM | Engines (referral) | #FFFFFF | #0563C1 (Link) | - |

**Phân bổ Zones theo Section:**
- **Phần Đầu (B-C):** Không có zone riêng, là bảng định vị chung, columns width 100px cho từng cột (B,C)
- **Phần Thân (E đến Conso.):** Zones 1, 2, 3, 4, 5, 6, 8 — số cột = f+L2+3 (xem PART 2a Scaling Formula)
- **Phần Mở rộng (sau cột separator):** Zones 7, 9 - luôn 2 cột

---

### Zone Header Details (bổ sung cho Bảng Định vị)

> Authoritative Cell Map for rows 6-7 is in **PART 2a → Zone Headers Cell Map**. Below is a summary.
> Chỉ Zone 1, 2, 4 có Header riêng. Zone 3, 5-9 không có header riêng — content bắt đầu trực tiếp.

| Zone | Header Position | Header Content |
|------|-----------------|----------------|
| **Zone 1** | E6:F7 (mặc định) hoặc E6:G7 (có Level 2) | E6=Object, E7=Item (nhãn cố định); F6=(rỗng), F7="-" |
| **Zone 2** | 1-5 cột sau Zone 1, rows 6-7 | Row 6=Feature Group title (chỉ col 1, còn lại rỗng); Row 7=Feature labels ("-" nếu Single-Feature) |
| **Zone 4** | Cột Conso. (H, I, hoặc J), rows 5-7 | Row 5=Conso. (nhãn cố định); Rows 6-7="-" |

**Vị trí động theo số Features và Level 2:**
- Vị trí cột Zone 2 và Conso.: xem Bảng tra cứu nhanh tại PART 2a Column Layout Constraint. Zone 4 headers (rows 6-7) luôn = "-"
- **Phân biệt:** Sub-header (row 5) = Mã GNM + Conso. label. Zone Headers (rows 6-7) = Object/Item + Feature labels.

---

### Bảng Cụm (Clusters), Cột Ngăn Cách và Styling

> **[!] Lưu ý về Row Positions:** Các row positions trong bảng dưới đây là cho **default template với 3 items**. Actual positions sẽ thay đổi động:
> - **Cụm Content:** Rows 8 đến 8+(n-1) với n = số items
> - **Cụm All:** Bắt đầu từ row 8+n
> - **Cụm Common:** Bắt đầu từ row 8+n+số_dòng_All

| Thành phần | Section/Phần | Vị trí Excel (Default Template) | Vai trò | Màu nền | Màu chữ | Border | Ghi chú |
|------------|--------------|----------------------------------|---------|---------|---------|--------|---------|
| **Cụm Header (Đầu)** | Phần Đầu | **B4:C4** | Tiêu đề (1), (2) cho index | #0070C0 | #FFFFFF | Medium top border (mỗi ô) | Fixed, không di chuyển |
| **Cụm Header (Thân)** | Phần Thân | **E4 trở đi** | Tiêu đề (1), (2)... cho các Zones | #0070C0 | #FFFFFF | Medium top border | Số cột = f+L2+3 (xem PART 2a Scaling Formula) |
| **Cụm Header (Mở rộng)** | Phần Mở rộng | **2 cột sau separator** | Tiêu đề (1), (2) cho Zones 7,9 | #0070C0 | #FFFFFF | Medium top border | Vị trí thay đổi theo Zone 1 |
| **Cụm Sub-header Phần 1 (Đầu)** | Phần Đầu | **B5:B7** | Mã GNM (B5), B6-B7 rỗng | #FFFFFF | #000000 | - | nền #FFFFFF, chữ #000000 |
| **Cụm Sub-header Phần 2 (Đầu)** | Phần Đầu | **C5:C7** | Nhãn cố định: C5=(1), C6=(2), C7=(3) | #DDEBF7 | #000000 | - | nền #DDEBF7, chữ #000000 |
| **Cụm Sub-header (Thân)** | Phần Thân | **E5 - cột cuối** (row 5) | Mã GNM và Conso. | #DDEBF7 | #000000 | - | **E5** = Mã GNM; **Cột cuối** = Conso. Vị trí thay đổi theo số cột Zone 1 |
| **Cụm Zone Headers (Thân)** | Phần Thân | **E6 - cột cuối** (rows 6-7) | Zone 1 + Zone 2 + Conso. headers | #DDEBF7 | #000000 | - | Zone 1 headers (2-3 cột), Zone 2 headers (1-2 cột), Zone 4 header (1 cột) |
| **Cụm Sub-header (Mở rộng)** | Phần Mở rộng | **2 cột sau separator, rows 5-7** | Common | #DDEBF7 | #000000 | - | Cột 1 = Common label, cột 2 = rỗng/"-" |
| **Cụm Conso.** | Phần Thân | **Cột cuối Phần Thân** | Labels cho Zone 4 | #DDEBF7 | #000000 | - | Row 5: Conso. (nhãn cố định), Rows 6-7: "-" (nhãn cố định). Vị trí: H (Single-Feature), I (không L2), hoặc J (có L2) |
| **Cụm All (Đầu)** | Phần Đầu | **C[8+n]:C[7+n+a]** | Index số cho tất cả Zone 5-7 | #FFFFFF | #000000 | Top: Thin (**CHỈ ô C**, ô B **KHÔNG** có top border) | **C[8+n]**="All" (nhãn cố định); các rows sau = rỗng; ⚠️ Border asymmetry: B không có top border để tách biệt visual giữa Content và All trong Phần Đầu |
| **Cụm All (Thân) - Rỗng** | Phần Thân | Zone 1 columns, khu vực All | Cụm rỗng | #FFFFFF | - | Top: Thin | = số dòng Phần Đầu All |
| **Cụm All (Thân) - Zone 5** | Phần Thân | Zone 2-3 columns, khu vực All | Vertical consolidation of Zone 3 - Engine only (consolidation or Decoding) | #FFFFFF | #0563C1 (link) | Top: Thin | Tương ứng với Zone 2, Zone 3 |
| **Cụm All (Thân) - Zone 6** | Phần Thân | Cột Conso., khu vực All | Common matters of Zone 3, 4, 5 - Engine only | #FFFFFF | #0563C1 (link) | Top: Thin | Tương ứng với cột Conso. |
| **Cụm Common (Đầu)** | Phần Đầu | **B[8+n+a]:C[7+n+a+c]** | Cụm rỗng | #FFFFFF | #000000 | Top: Thin (toàn bộ row, **kể cả B**) | **B[8+n+a]**=Common ở điểm bắt đầu; **C[8+n+a]**="-"; còn lại rỗng; Đồng bộ với Zone 8-9 |
| **Cụm Common (Thân) - Rỗng** | Phần Thân | Zone 1-3 columns, khu vực Common | Cụm rỗng | #FFFFFF | - | Top: Thin | = số dòng Phần Đầu Common |
| **Cụm Common (Thân) - Zone 8** | Phần Thân | Cột Conso., khu vực Common | Internal functions interaction - Referral to others' GNM | #FFFFFF | #0563C1 (link) | Top: Thin | Tương ứng với cột Conso. |
| **Cụm Common (Mở rộng) - Zone 9** | Phần Mở rộng | 2 cột Phần Mở rộng, khu vực Common | Extended functions interaction - Referral to others' GNM | #FFFFFF | #0563C1 (link) | Top: Thin | = số dòng Phần Đầu Common |
| **Cột A (Ngăn cách)** | - | **A** (toàn cột) | Separator Đầu | - | - | - | Width: 20px, để trống |
| **Cột D (Ngăn cách)** | - | **D** (toàn cột) | Separator Đầu-Thân | - | - | - | Width: 20px, để trống |
| **Cột Separator Thân-Mở rộng** | - | **Sau Conso.** (toàn cột) | Separator Thân-Mở rộng | - | - | - | Width: 20px, vị trí thay đổi theo Phần Thân |

**Vị trí các mảng không sử dụng (phải để trống):**
- **Phần Mở rộng, rows 8-[end items]:** Tương ứng với Zone 3 rows, để trống
- **Zone 1 columns, khu vực All:** Dưới Zone 1, trái Zone 5, để trống
- **Zone 1-3 columns, khu vực Common:** Dưới Zone 5, trái Zone 8, để trống

---

## Z-Level Traffic-Light Conditional Formatting

> Source: bod-nextjs production standard (2026-03-30)

Z-level value cells MUST use traffic-light background colors to enable visual scanning (especially for BOD presentations):

| Status | Hex Code | Alt Hex | RGB | Usage |
|--------|----------|---------|-----|-------|
| **Green** (on-track) | `#28a745` | `#4caf50` | 40,167,69 | Target met or exceeded |
| **Yellow** (at-risk) | `#ffc107` | `#ffeb3b` | 255,193,7 | Within tolerance but trending negative |
| **Orange** (warning) | `#fd7e14` | `#ff9800` | 253,126,20 | Below target, intervention needed |
| **Red** (off-track) | `#dc3545` | `#f44336` | 220,53,69 | Significantly below target |

### Application Rules
- Apply to Zone 3 value cells at Z-level only (not A/B/C engine cells)
- Use white text (`#fff`) on green, orange, and red backgrounds for contrast
- Yellow background uses default dark text
- Negative values (e.g., `(3,285.0)`) typically get red background
- Percentages above target get green; below get yellow/orange/red based on severity
- Thresholds are domain-specific — define per GNM, not globally

---

**Styling chung cho toàn bộ GNM:**
- **Font:** Myriad Pro 11pt (normal), 14pt (tiêu đề B2)
- **Row Height:** 18pt cho tất cả rows (xem Row Height Configuration)
- **Alignment:** Left, top, increased indent (trừ A1 backlink và B2 Tên GNM: không indent)
- **Wrap Text:** BẮt buộc (xem Wrap Text Rules bên dưới)
- **Gridlines:** Tắt (không hiển thị)
- **Viền ngoài sections:** xem bảng Zone
- **Viền nội bộ:** xem bảng Zone

---

