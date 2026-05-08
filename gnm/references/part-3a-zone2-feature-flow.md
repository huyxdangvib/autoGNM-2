---
part: 3a
name: "Zone 2 Feature Flow"
parent: gnm-instruction.md
---

## Zone 2: Feature Flow (Actions/Perspectives)

**Mục đích:** Feature flow - luồng các tính năng/hành động áp dụng lên Zone 1. Thể hiện chiều TODO của tư duy MFM - "LÀM GÌ" với mỗi Item ở Zone 1.

**Đặc điểm Zone 2:**
- **Mostly TODO & Sub-TODO:** Thường thể hiện chiều TODO (Làm gì với Item)
- **Sometimes WHAT & Sub-WHAT:** Đôi khi Zone 2 cũng có thể là chiều WHAT (khi Topic cần decoding theo hướng khác)
- **2 levels only:** CHỈ có 2 cấp độ (Feature Group và Features)
- **1 Feature Group per GNM Level:** Mỗi GNM level (A, B, C...Z) chỉ có 1 Feature Group (xem giải thích bên dưới). **Exception:** Z-level execution GNMs (BAP, RSS, RST) may have multiple Feature Groups — see Part 6 VIB Type Patterns.
- **1-5 Features per Group:** Có thể có 1 Feature (Single-Feature Pattern) hoặc nhiều Features (Multi-Feature)
- **Multiple Sub-features per Feature:** Mỗi Feature có thể có nhiều Sub-features (xem giải thích bên dưới)

**Tại sao cần Zone 2:** Zone 2 định nghĩa các hành động, tính năng, hoặc góc nhìn áp dụng lên WHAT. Đây là chiều ngang của ma trận, tạo ra mối quan hệ với Zone 1.

**Decoding áp dụng tại Zone 2 (xác định Features):**

Tương tự Zone 1, Classification và Component-Based Decoding áp dụng tại Zone 2 để xác định Features. VD: Classification → "Management" decode thành Planning, Execution, Monitoring. Component (BSC) → Financial, Customer, Process, Learning & Growth. Flow/Binary Decoding không phù hợp tại Zone 2 — dùng Zone 5 cho Flow, Zone 4/5 cho Binary.

> **Lưu ý:** Kết quả Decoding tạo ra danh sách Features trực tiếp trong Zone 2. Nếu cần decode sâu hơn cho từng Feature, sử dụng Zone 5 (Engines link đến sub-GNM Decoding riêng).

**Cấu trúc Zone 2 (2 levels only, vị trí cột động):**
- Zone 2 nằm ở **1-5 cột ngay sau Zone 1** (tuỳ số Features f=1..5)
- Vị trí cột đầu tiên Zone 2 = Col(G + L2) (L2=0 nếu không có Level 2, L2=1 nếu có)
- **Single-Feature (f=1, không L2):** Zone 2 ở cột G — 1 cột duy nhất
- **Multi-Feature (f=2, không L2):** Zone 2 ở cột G-H — 2 cột
- **Multi-Feature (f=2, có L2):** Zone 2 ở cột H-I — 2 cột (G bị chiếm bởi Level 2)
- **General formula:** Zone 2 chiếm cột Col(G+L2) đến Col(G+L2+f-1), mỗi cột width 200px. Xem Scaling Formula tại PART 2a Column Layout Constraint.

**Layout Zone 2 (2 levels only):**

| Level | Row | Nội dung | Mô tả |
|-------|-----|----------|-------|
| **Feature Group** | Row 6 | Title chung cho nhóm Features | VD: "Development", "Management", "Strategy Development". **Mỗi GNM level chỉ có 1 Feature Group** |
| **Features** | Row 7 | Các Feature cụ thể | **1 hoặc nhiều Features.** Single-Feature: G7="-". Multi-Feature: Feature1, Feature2... |

> **Lưu ý:** Mỗi Feature có thể có nhiều Sub-features (thể hiện trong Zone 3 hoặc GNM con)

**Cách chọn Features (TODO):**
- Features phải là HÀNH ĐỘNG hoặc GÓC NHÌN, không phải WHAT bổ sung
- ✅ Development, Management, Risk Control  -  đây là TODO
- ❌ Product Type, Region  -  đây là WHAT thêm, nên thuộc Zone 1
- Số Features thường **1-5**; nếu cần nhiều hơn, cân nhắc tách thành GNM con

---

### Multi-Feature as Default (2-5 Features — KHUYẾN NGHỊ ở mọi Level)

> **Nguyên tắc MFM (ref: MFM_Thinking_to_AI_Technology, 2026):** MFM là ngôn ngữ tư duy chuẩn hóa — "Do the right thing" (đúng vấn đề) VÀ "Do things right" (chuẩn hóa định dạng). Single-feature collapses TODO axis thành 1 chiều, mất đi khả năng phân tích đa chiều (multi-dimensional matrix). **Multi-feature is the default** — mỗi Item phải được phân tích dưới nhiều góc nhìn TODO để tạo Value Matrix thực sự.

**Tại sao Multi-Feature là default:**
- WHAT × TODO tạo ma trận 2 chiều = trái tim của GNM. f=1 biến ma trận thành danh sách 1 chiều.
- VBM(A) — workbook gốc của VIB — dùng f=2 ("Business strategies" / "Function strategies"), không phải f=1.
- AI Content Factory (MFM vision) cần multi-dimensional context làm Source of Truth. Single-feature Source of Truth → single-dimensional thinking.
- Zone 4 (Conso.) KHÔNG phải là "chiều TODO thứ 2" — nó là consolidation. Dùng Zone 4 thay Feature là workaround, không phải thiết kế đúng.

**Gợi ý Feature decomposition theo Level:**

| Level | Gợi ý Features (f=2-3) | Ví dụ |
|-------|------------------------|-------|
| **A** | VIB 3 Pillars: Growth / Productivity / Risk | SFI(A): 3 domains × 3 pillars = 9 cells |
| **A** | VBM pattern: Business strategies / Function strategies | VBM(A): 6 items × 2 features |
| **B** | Engineering lifecycle: Configure / Operate | TIM(B): 4 items × 2 features |
| **B** | BSC: Financial / Customer / Process / Learning | Strategy GNM: items × 4 perspectives |
| **Z** | Inherit parent Features or use domain-specific | Per-position dashboards: metrics × 3 pillars |

> **Khi nào nên mở rộng sang 2+ Features:** Luôn luôn — trừ khi có lý do rõ ràng để giảm xuống f=1 (xem Single-Feature Legacy section bên dưới). Mỗi Item cần phân tích dưới nhiều góc nhìn TODO đồng thời (VD: "Growth" + "Productivity" + "Risk"), và mỗi Item có giá trị khác nhau cho mỗi góc nhìn.

---

### Single-Feature Pattern (1 Feature — Legacy, dùng có chủ đích)

> **⚠️ THAY ĐỔI từ v5.0:** Single-Feature KHÔNG CÒN là pattern "phổ biến ở Level A/B". Đây là pattern hợp lệ nhưng là deliberate simplification, chỉ dùng khi có lý do cụ thể. Mặc định là Multi-Feature.

**Khi nào f=1 hợp lệ:**
- Hub/Navigation sheets thuần túy (Listing type — không có flow logic)
- GNM tạm thời (draft/prototype) sẽ được nâng cấp sau
- Domain đơn giản thực sự chỉ có 1 góc nhìn TODO (hiếm)

| Đặc điểm | Mô tả |
|-----------|-------|
| **Khi nào dùng** | ⚠️ CHỈ khi domain thực sự có 1 TODO perspective duy nhất, hoặc GNM chỉ là navigation hub |
| **Zone 2 layout** | 1 cột: G6 = Feature Group, G7 = "-" hoặc Feature name |
| **Zone 3 trở thành** | Danh sách Engines 1 chiều (1 Engine per Item) — mất tính matrix |
| **Phần Thân** | Chỉ có 4 cột (E-F-G-H) thay vì 5 cột |
| **Rủi ro** | Collapses thinking to 1 dimension. Zone 4 bị lạm dụng làm "pseudo-Feature". Không tạo được multi-dimensional Source of Truth cho AI processing. |

**Ví dụ: Single-Feature ở Level B (legacy pattern)**
> R6 = Feature Group title ("Strategy Development"). R7 = Feature placeholder ("-" for single-feature). Zone 2 occupies column G only.

```text
     │ E      │ F        │ G                              │ H (Conso.)              │
─────┼────────┼──────────┼────────────────────────────────┼─────────────────────────┤
 R6  │ Object │          │ Strategy Development           │ -                       │  ← Zone 2 Header: Feature Group
 R7  │ Item   │ -        │ -                              │ -                       │  ← Zone 2 Header: Feature (dash = single)
 R8  │ KBS    │ Business │ Retail Brokerage Business (1)  │                         │
 R9  │        │          │ Fixed Income Trading (2)       │                         │
 R10 │        │          │ Equity & Derivatives (3)       │                         │
 R11 │        │ Channel  │ Branch Network (4)             │                         │
 R12 │        │          │ Digital (5)                    │                         │
─────┼────────┼──────────┼────────────────────────────────┼─────────────────────────┤
 R13 │        │          │                                │ FI Limit Review (2.5)   │ ← Zone 4 as "2nd dimension"
```

**Single-Feature Layout:** f=1, L2=0 → Phần Thân = 4 cột (E-H). Conso. = H. B2 Merge = B2:H2. Header numbering: (1)-(4). Xem Bảng tra cứu nhanh tại PART 2a.

---

**Khi cần nhiều hơn 1 Feature Group:**

Mỗi GNM level chỉ có 1 Feature Group (Row 6). Nếu business context yêu cầu nhiều Feature Groups, áp dụng 1 trong 3 giải pháp:

| Tình huống | Giải pháp | Ví dụ |
|-----------|-----------|-------|
| 2 Feature Groups cùng cấp | **Tách thành 2 GNM** cùng Level, mỗi GNM 1 Feature Group | `Product Development PRD(B)` + `Product Management PRM(B)` |
| 1 Group chính + 1 Group phụ | **Gộp vào 1 Feature Group** dùng tên perspective rộng hơn bao trùm cả hai | Feature Group = "Lifecycle" bao gồm: Design, Build, Operate, Monitor |
| Quá nhiều Features (>5) | **Tách GNM con** theo Feature Group, GNM cha chứa Engine link | GNM cha Level B → GNM con Level C cho từng Feature Group |

> **Nguyên tắc:** Ưu tiên tìm 1 tên perspective chung (VD: "Lifecycle", "Value Chain", "Governance") bao trùm các Features trước khi quyết định tách GNM.

**Cách thể hiện:**
- **Feature Group (Row 6):** Development, Management, Analysis, Control...
- **Features (Row 7):** Các features cụ thể trong group

**Nội dung điển hình (Zone 2 linh hoạt theo GNM Type):**

| GNM Type | Feature Group (R6) | Features (R7) | f | VBM Example |
|----------|-------------------|---------------|---|-------------|
| **Business Selection** | "Businesses & Functions strategies" | Business strategies / Function strategies | 2 | VBM(A): 6 items, f=2 |
| **Business Domains** | "Business domains" | Product/Customer/Channel | 3 | RBB(A) |
| **Org Responsibility** | Per-unit groups | Action + Development sub-cols per unit | 6 | BAP(Z): Product, Risk, Legal, Tech, Other |
| **Schedule** | Per-business domain | Sub-features per domain | 6+ | RSS(Z): Lending, Funding, Card, BNW... |
| **Team Assignment** | Per-team type | Sub-features per team | 4 | BAT(Z): Business, AI, Technology, Leadership |
| **Strategy Catalog** | "Business" + "Functional" | 9 domains: Enterprise, RB, WB, TRS, HR, Risk, Marcom, ESD, Technology | 9 (2 groups) | VES(Z): 10 cat × 9 domains |

> **Scale:** Features typically 1-5, nhưng Z-level execution GNMs (BAP, RSS, RST) có thể có 6+ feature groups với nhiều sub-features per group. Zone 2 R7 sub-features hiển thị trong cùng Feature Group column.

**Ví dụ cấu trúc Zone 2 — Single-Feature (không Level 2 - cột G):**
```
G6: Strategy Development
────────────────────────
G7: -
```

**Ví dụ cấu trúc Zone 2 — Multi-Feature (không Level 2 - cột G-H):**
```
G6: Development    │ H6: (rỗng)
───────────────────┼─────────────
G7: Product Design │ H7: Risk Mgmt
```

**Ví dụ cấu trúc Zone 2 (có Level 2 - cột H-I):**
```
H6: Development    │ I6: (rỗng)
───────────────────┼─────────────
H7: Product Design │ I7: Risk Mgmt
```

---

