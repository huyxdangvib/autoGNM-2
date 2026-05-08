---
part: 3b
name: "Zone 4 Horizontal Consolidation"
parent: gnm-instruction.md
---


<part3b_engine_zones>

# PART 3b: ENGINE & REFERRAL ZONES (4-9)

> **TL;DR:** PART 3b là canonical reference cho 6 Engine Zones — Zone 4 (Horizontal Conso.), Zone 5-6 (Vertical & Common Conso.), Zone 7 (Common 3-6), Zone 8-9 (Internal & External Referral). Zone 4-9 CHỈ chứa Engines. For Zones 1-3 (core matrix, always needed) → see PART 3a.

> **Quy tắc:** Mỗi Zone được định nghĩa MỘT LẦN dưới đây. Tất cả các section khác tham chiếu về đây.

> **📌 Retrieval Signpost:** For structure core (Column Layout, Dynamic Rows) → see PART 2a. For templates & section details → see PART 2b. For styling/colors → see PART 4. For formulas/write order → see PART 5. For Zones 1-3 (core zones, Value Matrix) → see PART 3a. For examples → see PART 7b (core) / PART 7c (extended).

<zone_definitions>


## Zone 4: Horizontal Consolidation (Hợp nhất Ngang của Zone 3)

> **TL;DR:** Zone 4 = cột Conso. chứa Engines cho Item-level consolidation hoặc Decoding drill-down. Zone 1/2 decode ở **mức cấu trúc** (tạo Items/Features). Zone 4/5 decode ở **mức chi tiết** (đào sâu từng Item/Feature). Xem bảng tổng quan bên dưới.

**Mục đích:** Horizontal consolidation of Zone 3 — CHỈ chứa Engines (xem **Engine** trong Terminology).

**Tại sao cần Zone 4:** Zone 4 là điểm hợp nhất theo chiều ngang (horizontal) của Zone 3, dùng để liên kết đến các GNM con tổng hợp toàn bộ Features cho từng Item. Zone 4 phục vụ 2 mục đích chính:
1. **Item-level consolidation:** Tổng hợp playbook, guide, hoặc tài liệu tổng quan cho từng Item (VD: `Working Capital Playbook WCP(Z)`)
2. **Decoding topics:** Liên kết đến tài liệu giải mã chi tiết cho từng Item (VD: `Corp Bond Classification CBC(Z)`)

**Đặc điểm quan trọng:**
- **Engine only:** Zone 4 CHỈ chứa Engines (xem **Engine** trong Terminology)
- **Horizontal consolidation:** Tổng hợp theo chiều ngang của Zone 3 (cùng hàng với Items)
- **Dual purpose:** Có thể chứa Item-level consolidation engines HOẶC Decoding topic engines (xem bên dưới)

**Giải thích "Decoding topics" (áp dụng cho Zone 4 và Zone 5):**

"Decoding topics" là các chủ đề cần được **giải mã (decode)** sâu hơn bằng 1 trong 4 phương pháp Decoding của MFM:

| Phương pháp Decoding | Decode gì | Khi nào Zone 4/5 dùng | Ví dụ Engine trong Zone 4/5 |
|---------------------|-----------|----------------------|----------------------------|
| **Classification Decoding** | WHAT theo phả hệ phân loại | Item cần phân loại chi tiết hơn | `Corp Bond Classification CBC(Z)` |
| **Component Based Decoding** | WHAT hoặc TODO theo cấu phần (PCSS, BSC...). PCSS có thể mở rộng (VD: PCSS MR cho commercial bank) | Item/Feature cần phân tích cấu phần | `PCSS MR Breakdown PMR(Z)` |
| **Binary Decoding** | WHAT hoặc TODO theo nhị phân | Cần ra quyết định nhanh giữa các lựa chọn | `Customer Segmentation CSG(Z)` |
| **Flow Decoding** | TODO theo chuỗi công việc | Feature cần diễn giải quy trình chi tiết | `Origination Process Flow OPF(Z)` |

> **Zone 4** (horizontal) thường decode theo chiều **WHAT** → Classification hoặc Component Decoding cho từng Item.
> **Zone 5** (vertical) thường decode theo chiều **TODO** → Flow hoặc Component Decoding cho từng Feature.

**Tổng quan Decoding across Zones (Zone 1 → 5):**

| Zone | Vai trò Decoding | Mục đích | Phương pháp phổ biến |
|------|-----------------|----------|---------------------|
| **Zone 1** | **Tạo cấu trúc WHAT** | Decode Topic → danh sách Items | Classification, Component (PCSS / PCSS MR) |
| **Zone 2** | **Tạo cấu trúc TODO** | Decode Topic → danh sách Features | Classification, Component (BSC, PDCA) |
| **Zone 3** | **Phản ánh kết quả giao cắt** | WHAT x TODO → Values/Engines tại mỗi ô | Kết quả tự nhiên từ Decoding Zone 1 + Zone 2 |
| **Zone 4** | **Đào sâu theo chiều WHAT** | Mỗi Item → Engine link đến sub-GNM decode riêng | Classification, Component cho từng Item |
| **Zone 5** | **Đào sâu theo chiều TODO** | Mỗi Feature → Engine link đến sub-GNM decode riêng | Flow, Component cho từng Feature |

> **Nguyên tắc phân biệt:** Zone 1/2 = Decoding ở **mức cấu trúc** (xác định WHAT/TODO). Zone 4/5 = Decoding ở **mức chi tiết** (đào sâu từng Item/Feature đã xác định).

**Cách thể hiện:**
- Nằm ở cột **Conso.** (consolidation), cùng hàng với các Items
- CHỈ chứa Engines liên kết đến GNM con hoặc tài liệu Decoding
- **Engine name phải đủ nghĩa** — người đọc hiểu ngay ô nói về gì

**Format nội dung Zone 4:**
- **`[Tên đầy đủ] MãGNM (Level)`** — Tên đầy đủ + Mã viết tắt
- Tên mang nghĩa, không cần Value bổ sung
- Recommended max 50 characters tổng cộng

**Ví dụ nội dung Zone 4:**

*Item-level consolidation (playbooks, guides):*
| Engine (Tên đầy đủ + Mã) | Nghĩa |
|------------------------------|-------|
| `Working Capital Playbook WCP(Z)` | Tổng hợp toàn bộ hành động cho Working Capital |
| `Production & Supply Chain PSC(B)` | Người đọc hiểu: sản xuất và chuỗi cung ứng |

*Decoding topics (phân loại, phân tích cấu phần):*
| Engine (Tên đầy đủ + Mã) | Nghĩa |
|------------------------------|-------|
| `Corp Bond Classification CBC(Z)` | Decoding phân loại trái phiếu doanh nghiệp |
| `Business Capability Map BCM(B)` | Người đọc hiểu: bản đồ năng lực kinh doanh |

**Bằng chứng VBM Excel — Zone 4 thực tế:**

| Sheet | Zone 4 (Conso. column) | Ghi chú |
|-------|------------------------|---------|
| VBM(A) | Conso. column present with drill-down engines | Root GNM, 6 items × 2 features |
| RBB(A) | Conso. present | Business domains GNM |
| ONW(A) | Conso. present | OVD/NPL/WOR GNM |
| APT(A) | Conso. present | Lending apartment strategy |
| All 12 sheets | Conso. = last column of Phần Thân | Rule 3 PASS across all sheets |

> **Note:** Zone 4 engines in VBM follow informal naming (e.g., `RB (RBB)` instead of `Retail Banking RBB (A)`) — confirmed GAP-3 in VBM review. Standard format `[Full Name] CODE (Level)` is the spec.

---

## Production Usage Patterns (bod-nextjs)

> Source: 143 production GNM sheets analysis (2026-03-30)

### When Zones 4-7 Are Actually Used

In production, Zones 4-7 are populated primarily in **complex, multi-concern domains**:

| Domain | Zone 4-5 Usage | Zone 6-7 Usage | Why |
|--------|---------------|----------------|-----|
| **RIS (Risk)** | Risk categories × business units | Cross-cutting compliance rules | Multiple risk types share common controls |
| **CPF (Card & UPL)** | Product features × segments | Shared acquisition/servicing rules | Card products have high cross-concern overlap |
| **TRS (Treasury)** | Instrument types × markets | ALM rules, regulatory constraints | Treasury instruments share liquidity/capital rules |

### When Zones 4-7 Are Skipped

Most domains (lending, funding, HR, marcom) leave Zones 4-7 empty. This is **normal, not a defect.**

**Decision criteria — use Zones 4-7 when:**
- A cross-topic engine appears in 3+ different Zone 3 items → consolidate in Zone 4/5
- A rule applies to ALL items regardless of Zone 1 category → place in Zone 6/7
- Zone 7 strategic anchors (9 Directions, 3 Key Pillars) → almost always populated

**Skip Zones 4-7 when:**
- Domain is straightforward (one product line, one segment)
- Zone 3 engines are unique per item (no cross-cutting patterns)
- Sheet is Z-level (values don't consolidate the same way as engines)

---

