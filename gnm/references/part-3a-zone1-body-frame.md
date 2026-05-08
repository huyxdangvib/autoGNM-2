---
part: 3a
name: "Zone 1 Body Frame"
parent: gnm-instruction.md
---


<part3a_core_zones>

# PART 3a: CORE ZONES (1-3)

> **TL;DR:** PART 3a là canonical reference cho 3 Core Zones — Zone 1 (WHAT Items), Zone 2 (TODO Features, 1-5 cột, hỗ trợ Single-Feature Pattern), Zone 3 (Value Matrix = trái tim GNM). Zone 3 KHÔNG để ô trống. For Zones 4-9 (Consolidation & Referral Engines) → see PART 3b.

> **Quy tắc:** Mỗi Zone được định nghĩa MỘT LẦN dưới đây. Tất cả các section khác tham chiếu về đây.

> **📌 Retrieval Signpost:** For structure core (Column Layout, Dynamic Rows) → see PART 2a. For templates & section details → see PART 2b. For styling/colors → see PART 4. For formulas/write order → see PART 5. For Zones 4-9 (engine zones, consolidation & referral) → see PART 3b. For examples → see PART 7b (core) / PART 7c (extended).

<zone_definitions>


## Zone 1: Body Frame (Primary Elements)

**Mục đích:** Body frame - chứa Items & Sub-items, là khung chính của GNM. Thể hiện chiều WHAT của tư duy MFM - "CÁI GÌ" cần được phân tích, quản lý hoặc phát triển.

**Đặc điểm Zone 1:**
- **Mostly WHAT & Sub-WHAT:** Thường thể hiện chiều WHAT (Cái gì cần phân tích)
- **Sometimes TODO & Sub-TODO:** Đôi khi Zone 1 cũng có thể là chiều TODO (khi Topic cần decoding theo hướng khác)
- **Recommended 1-3 levels:** Khuyến nghị sử dụng 1-3 cấp độ phân cấp

**Topic Decoding:**
- **Single decoding:** Topic Decoding tại Zone 1 HOẶC Zone 2
- **Dual decoding:** Topic Decoding tại Zone 1 VÀ Zone 2

**Decoding áp dụng tại Zone 1 (xác định Items):**

Classification Decoding và Component-Based Decoding có thể được sử dụng **ngay tại Zone 1** để xác định cách tổ chức Items:

| Phương pháp | Cách áp dụng tại Zone 1 | Ví dụ |
|-------------|------------------------|-------|
| **Classification Decoding** | Phân loại WHAT theo phả hệ → Items = các lớp phân loại | Topic "Customer" → Items: Corporate, SME, FI (phân loại theo segment) |
| **Component-Based Decoding** | Tách WHAT theo cấu phần (PCSS, BSC...) → Items = các component. **PCSS có thể mở rộng** thêm thành phần nếu ngữ cảnh yêu cầu | Topic "Commercial Banking" → Items: Product, Customer, Salesforce, Sales Platform, Marketing, Risk (**PCSS MR**) |

> **Tại sao chỉ Classification và Component?** Binary Decoding và Flow Decoding tạo cấu trúc ở mức sâu hơn (ra quyết định, chuỗi quy trình), không phù hợp để xác định danh sách Items cấp cao. Nếu cần Binary/Flow, sử dụng chúng tại Zone 4 (Engines link đến sub-GNM).

> **Binary Decoding at Zone 1 (Z-level exception):** For Z-level classification/assessment GNMs, Binary Decoding CAN be applied at Zone 1 to create 2×2 matrices. Full specification → see **Situational Decoding Pattern** section (PART 3a).

> **Flow Decoding at Zone 1 (Z-P exception, codified 2026-04-17):** For **Z-P (Process) sub-type** sheets — RACI matrices, implementation plans, workflow templates — Flow Decoding (PDCA / Plan-Do-Check-Act, SMART, lifecycle stages) MAY be applied at Zone 1 as Items. The sheet's primary purpose is to document a process methodology, so the flow phases ARE the Items. Z-M (Measurement) and Z-T (Template) sub-types MUST still use Classification or Component-Based decoding at Zone 1. Example: `BLC(Z)` uses PDCA (Plan / Do / Check / Act) as Zone 1 Items — valid as a Z-P process template. See Critical Rule #13 (Part 1) for Z-level sub-type taxonomy.

> **💡 PCSS Extensibility:** PCSS (Product, Customer, Salesforce, Sales Platform) là framework cốt lõi 4 thành phần, **không phải khuôn cứng**. Tùy ngữ cảnh kinh doanh có thể mở rộng thêm thành phần bổ sung:
> - **PCSS MR** (+Marketing, +Risk): Mô hình chuẩn cho **Commercial Bank** — Marketing (chiến lược thương hiệu & thu hút khách hàng) và Risk (quản trị rủi ro tín dụng, thị trường, vận hành) là 2 trụ cột không thể thiếu
> - **PCSS + T** (Technology): Khi digital/tech là trụ cột riêng biệt
> - **PCSS + P** (Partnership/Ecosystem): Khi hệ sinh thái đối tác quan trọng
> - **Custom extensions:** Bất kỳ thành phần nào phù hợp với đặc thù ngành/tổ chức
>
> Nguyên tắc: Giữ nguyên 4 core components (P-C-S-S), bổ sung thêm khi có lý do nghiệp vụ rõ ràng. VD: Commercial Bank → PCSS MR (6 thành phần).

> **Lưu ý:** Kết quả Decoding tạo ra danh sách Items trực tiếp trong Zone 1. Nếu cần decode sâu hơn cho từng Item, sử dụng Zone 4 (Engines link đến sub-GNM Decoding riêng).

**Tại sao cần Zone 1:** Zone 1 định nghĩa chủ thể chính mà GNM đang mô tả. Đây là chiều dọc của ma trận, tạo nền tảng cho toàn bộ phân tích.

**Cấu trúc Zone 1 = 2 phần logic:**

| Phần | Rows | Nội dung | Styling |
|------|------|----------|---------|
| **Header Area (Zone Headers)** | Rows 6-7 | E6=Object (nhãn cố định), E7=Item (nhãn cố định), F6=(rỗng), F7="-", G6-G7=see Cell Map PART 2a | Nền #DDEBF7 |
| **Content Area** | Rows 8+ | E8=Mã GNM (nhãn cố định), E9+=rỗng; F=Level 1 Items; G=Level 2 (nếu có) | Nền #FFFFFF |

> **[!] QUAN TRỌNG:** Zone Headers (rows 6-7) KHÁC với Sub-header (row 5). Sub-header chứa Mã GNM và Conso., còn Zone Headers chứa Object/Item labels.

**Hệ thống phân cấp Zone 1 (2-3 cột linh hoạt):**
Zone 1 sử dụng **2 cột mặc định (E-F)**, mở rộng thêm **cột G khi cần chi tiết hóa**:

| Cột | Level | Vai trò | Ví dụ | Khi nào dùng? |
|-----|-------|---------|-------|---------------|
| **E** | **Level 0** | Nhãn cố định (Mã GNM) | "GEX" ở E8, còn lại rỗng | Luôn có |
| **F** | **Level 1 - Item** | Phân loại chính | "Corporate", "SME", "FI" | Luôn có |
| **G** | **Level 2 - Sub-item** | Chi tiết hóa Item | "Large Cap", "Mid-tier" | Chỉ khi Item cần chi tiết hóa |

**Lưu ý về tính đồng chất (Taxonomy) và khi nào thêm Level 2 (cột G):**
- Item có ≥2 sub-categories cần Zone 3 values khác nhau
- Level 1 và Level 2 PHẢI cùng chiều phân loại (cùng taxonomy)
- Ví dụ đúng: Customer Segment -> Sub-segment (Corporate -> Large Cap)
- Ví dụ SAI: Issuer Type -> Tenor (Corporate Bond -> Short-term) - không đồng chất

**Quy tắc sử dụng Zone 1:**
1. **Mặc định 2 cột (E-F):** Level 0 (Mã GNM nhãn cố định) + Level 1 (Items)
2. **Thêm cột G khi cần:** Chỉ tạo Level 2 khi Item lớn buộc phải chi tiết hóa
3. **Level 0 (Cột E):** Chỉ chứa Mã GNM ở ô E8 (nhãn cố định), các ô E9+ để rỗng
4. **Level 1 (Cột F):** Item chính, khi có nhiều Sub-items thì chỉ ghi ở dòng đầu tiên
5. **Level 2 (Cột G - nếu có):** Chi tiết hóa Item, "-" nếu không có
6. **Đồng bộ với Phần Đầu:** Số dòng content = số items được đánh số trong cụm Content của Phần Đầu

**Ví dụ 1 - Mặc định 2 cột (không cần chi tiết hóa):**
```
Level 0 (E)  │ Level 1 (F)
─────────────┼──────────────
GEX          │ Corporate    ← Row 8: Mã GNM + Item
(rỗng)       │ SME          ← Row 9
(rỗng)       │ FI           ← Row 10
```

**Ví dụ 2 - Mở rộng 3 cột (khi Item cần chi tiết hóa):**
```
Level 0 (E)  │ Level 1 (F)  │ Level 2 (G)
─────────────┼──────────────┼─────────────
GEX          │ Corporate    │ Large Cap    ← Row 8: Corporate cần chi tiết
(rỗng)       │              │ Mid-tier     ← Row 9: thuộc Corporate
(rỗng)       │ SME          │ -            ← Row 10: SME không cần chi tiết
(rỗng)       │ FI           │ Bank         ← Row 11: FI cần chi tiết
(rỗng)       │              │ NBFI         ← Row 12: thuộc FI
```

**Lưu ý quan trọng:**
- Cột E (Level 0): Chỉ ô E8 có giá trị Mã GNM (nhãn cố định), các ô còn lại rỗng
- Cột F (Level 1): Không lặp lại nếu đã ghi ở dòng trên (thể hiện cấu trúc cha-con)
- Cột G (Level 2): CHỈ tạo khi có Item buộc phải chi tiết hóa, các zones khác sẽ shift sang phải

> **Zone 1 Depth:** Standard GNMs: MUST max 3 levels (L0-L2). Z-level classification/assessment GNMs: MAY use up to 5 levels. A-level organizational GNMs: MAY use up to 4 levels for nested scope. See **Situational Decoding Pattern** (PART 3a) and Rule #13 (PART 7).

**Cách thể hiện:**
- **Nhãn "Object":** Định nghĩa loại chủ thể (VD: Product, Customer, Department)
- **Nhãn "Item":** Phân loại các yếu tố con (VD: Product Type, Segment)
- **Danh sách Items:** Các phần tử cụ thể cần phân tích (Level 1 + Level 2 nếu có)

**Nội dung điển hình (Zone 1 linh hoạt theo GNM Type):**

| GNM Type | Zone 1 Items | VBM Example |
|----------|-------------|-------------|
| **Business/Product** | Tên sản phẩm, phân khúc, BU | VBM: 6 items (Biz: RB, WB, TRS, NPL&WOR; Func: HR, Risk, BTS, Marcom, Finance, ESD) |
| **Org Responsibility** | BSC perspectives, work items | BAP: Growth-Productivity + Risk → 29 items |
| **Schedule** | Thời kỳ (tuần, tháng) | RSS: Mar W1, W2, W3, W4 (4 items) |
| **Team Assignment** | Numbered team slots | BAT: 25 numbered rows; RST: 8 rows |
| **Strategy Catalog** | Strategy categories | VES: 10 enterprise strategy categories |
| **Org Structure** | Numbered org groups | VOS: 7 organizational units |
| **Classification/Assessment** | Binary axes or classification tree | BSD: X/Y × Standard/Non-standard |

> **Scale:** Zone 1 ranges from 3 items (focused topics) to 29+ items (detailed execution matrices). Items × Features = total Zone 3 cells. Khi items > 15, cân nhắc tách sub-GNM trừ khi GNM là execution-level (Z) cần single-view.

---

