---
part: 1
name: "Terminology & Cross-Workflow Handoffs"
parent: gnm-instruction.md
---

## Terminology (Thuật ngữ)

| Term | Definition |
|------|------------|
| **Zone** | Khu vực chức năng (1-9) trong GNM, mỗi zone có mục đích riêng |
| **Cụm (Cluster)** | Nhóm ô liên quan (Header, Sub-header, Zone Headers, All, Common, Feature) |
| **Section/Phần** | Phân đoạn chính của GNM (Đầu, Thân, Mở rộng) |
| **Header** | Row 4  -  Tiêu đề chính với numbering (1), (2), (3)... Nền #0070C0, chữ trắng, no wrap text |
| **Sub-header** | Row 5  -  Chứa Mã GNM (cột đầu) và Conso. (cột cuối). Nền #DDEBF7 |
| **Zone Headers** | Rows 6-7  -  Nhãn phân loại cho Zone 1 (Object, Item) và Zone 2 (Features). Nền #DDEBF7 |
| **Engine** | **ĐÃ LÀ Value** — tên Engine tự mang nghĩa, người đọc hiểu ngay ô nói về gì mà không cần Value bổ sung. Format: `[Tên đầy đủ] MãGNM (Level)`. VD: `Service Catalog SVC (B)`. **Max 50 ký tự tổng cộng** (bao gồm cả tên + khoảng trắng + mã). If an Engine name exceeds 50 chars, abbreviate the descriptive name while keeping the full CODE(Level) suffix. Priority: preserve CODE(Level) → abbreviate middle words → use standard acronyms. Example: `Production & Supply Chain Management PSCM(B)` (46 chars ok) → if too long: `Prod. & Supply Chain Mgmt PSCM(B)`. Dùng HYPERLINK formula để navigate. Zone 4-9 CHỈ chứa Engines. |
| **Value** | Dữ liệu trực tiếp (số, chữ, ký hiệu, màu sắc) - không có link |
| **Level 0** | Cột E Content Area (Row 8+)  -  Chỉ ô E8 chứa Mã GNM, các ô E9+ để rỗng |
| **Level 1 (Item)** | Cột F  -  Đối tượng/chủ thể chính trong chiều WHAT (Bắt buộc) |
| **Level 2 (Sub-item)** | Cột G  -  Chi tiết hóa Level 1 (Chỉ thêm khi Item lớn cần chi tiết hóa) |
| **Feature** | Đặc tính/hành động trong chiều TODO (horizontal) |
| **Consolidation (Conso.)** | Tổng hợp yếu tố chung theo hàng/cột/toàn bộ |
| **Object** | Chủ thể chính của GNM (cấp cao nhất trong Zone 1) |
| **Mã GNM (Topic)** | Tên viết tắt 3 ký tự của GNM, đại diện cho: Business, Function, Topic, Project, Program, hoặc Type. Là nhãn cố định tại E8. Phân loại: Topic (tổng), Big (A), Medium (B), Small (C)...Z |
| **GNM Level** | Cấp độ của GNM: Level A, B, C... chứa Engines (đã là Value); Level Z chứa Values chi tiết. **Z1** = sub-terminal drilldown within Z — contains ONLY Values (no Engines). See Z1 below. |
| **Z1 (Sub-terminal)** | Sub-level below Z. Contains ONLY Values (no Engines). Used for granular data: stock-by-stock limits, customer-by-customer reviews. Example: KAFI MRR(Z1) — 186 stocks × limit/outstanding/room/ratio columns. Back-link points to Z parent. |
| **Nhãn cố định** | Ô có nội dung không đổi, không được ghi đè (VD: (1), (2), All, Common, Object, Item, Conso., Mã GNM) |

> **⚠️ Canonical Terms Only:** Chỉ sử dụng đúng thuật ngữ trong bảng trên. KHÔNG dùng alias, viết tắt không chuẩn, hoặc đặt tên mới (VD: dùng "Engine" không dùng "link cell"; dùng "Conso." không dùng "Summary column"). Khi user dùng thuật ngữ khác, map về thuật ngữ chuẩn trước khi xử lý.

---

## Cross-Workflow Handoffs

**Inbound (GNM receives context from):**
- **Strategy→GNM mapping** — Zone mapping output with strategy items pre-classified into zones. Load zone assignments and validate against GNM structural rules before building.
- **Value decomposition** — Value tree nodes and KPIs that map to Zone 3 Values at Level Z. Load value drivers as candidate Zone 1 Items.
- **Enterprise strategy catalogs** — VES(Z)-style strategy entries that populate Zone 3 in enterprise-level GNMs. Load category structure as Zone 1/2 framework.
- **Strategy development outputs** — Strategic direction, initiatives, and metrics that inform GNM content. Load as context for Zone 3 content decisions.

### CIS Workflow → GNM Mapping (Harmonized)

GNM is self-contained but harmonized with CIS (Corporate Intelligence Strategy) workflows. CIS workflow outputs can feed GNM construction without GNM depending on CIS files at runtime.

| CIS Workflow | Code | GNM Inbound Use | Suggested GNM Type | Level |
|---|---|---|---|---|
| Strategy Development | SD | Strategic direction → Zone 1 Items + Zone 2 Features | Strategy Catalog | A |
| Business Case Factory | BCF | Initiative phases → Zone 2 Features; products → Zone 1 Items | Business/Product | B |
| Value Decomposition | VD | Value drivers → Zone 1 Items; BSC perspectives → Zone 2 | Strategy Catalog | A-B |
| Innovation Strategy | IS | Innovation vectors → Zone 1; disruption lens → Zone 2 | Classification/Assessment | A-B |
| Digital Transformation | DT | Digital capabilities → Zone 1; maturity dimensions → Zone 2 | Org Responsibility | B |
| M&A Portfolio Strategy | MA | Portfolio units → Zone 1; assessment criteria → Zone 2 | Classification/Assessment | A |
| Portfolio Prioritizer | PP | Ranked initiatives → Zone 1 Items; priority dimensions → Zone 2 | Schedule/Assignment | B-Z |
| Stakeholder Alignment | SA | Stakeholder groups → Zone 1; influence dimensions → Zone 2 | Org Responsibility | B |

**Handoff protocol:** CIS workflows produce markdown. To feed GNM, either:
1. Manually extract Items/Features from the CIS output and invoke GNM CREATE
2. Use a GNM Build Spec (YAML block below) with `source_workflow: cis-{code}`
3. Use CIS Format Transformer (FT) with target format `gnm` to auto-generate the Build Spec

**Shared conventions:**
- **Framework catalog:** GNM maintains its own framework catalog (Part 1c, 124 items) that includes the same frameworks CIS uses. GNM's catalog is the authoritative copy for GNM construction; CIS's `strategy-frameworks.csv` is authoritative for CIS workflows. Both originate from the same VIB strategy framework knowledge base.
- **Relevance Engine:** GNM's Part 1b Relevance Engine adapts CIS Innovation Strategy's "Run-All, Curate by Signal" protocol for zone content selection. The adaptation is GNM-native — no CIS dependency at runtime.
- **Data Integrity:** Both systems use `[^n]`/`[EST]` citation tagging. GNM preserves these tags in Zone 3 Values when receiving CIS output.
- **Domain gate:** Both use `domain_context: "vib"` to gate VIB-specific content.

### GNM Build Spec (Structured Inbound Handoff)

When receiving a structured handoff from an upstream workflow or agent, the input may arrive as a **GNM Build Spec** — a YAML block containing pre-classified zone content. This bypasses Steps 1-2 of the thinking process since the upstream workflow already performed classification.

**Recognition:** If the input contains a YAML block with keys `gnm_name`, `abc_level`, `zone1_items`, `zone2_features`, treat it as a GNM Build Spec.

**Schema:**
```yaml
# GNM Build Spec (handoff from HAGT workflow)
gnm_name: "RB Lending (B)"          # Topic + Level
abc_level: B                         # A, B, C, Z, or Z1
zone1_items:                         # WHAT (nouns)
  - Mortgage
  - Auto Loan
  - Business Loan
zone2_features:                      # TODO (verbs)
  - "Phase 1: Product Design"
  - "Phase 2: Risk Framework"
zone3_content:                       # Optional — pre-mapped cells
  - item: Mortgage
    feature: "Phase 1: Product Design"
    type: Engine                     # Engine | Value | VotingMatrix | "-"
    value: "Product Design PRD (B)"
cascade_parent: "RB Banking RBB (A)" # Optional — parent GNM
cascade_children:                    # Optional — child GNMs
  - "Mortgage MTG (Z)"
  - "Auto Loan ATL (Z)"
domain_context: vib                  # vib | banking | generic
source_workflow: strategy-gnm-mapper # Originating workflow
```

**Processing:**
1. Skip Steps 1-2 (classification + parameter extraction) — already done
2. Start at Step 2.3 (Framework Relevance) if `domain_context: vib`
3. Validate zone content against 11 Critical Rules (Step 3)
4. Generate output (Step 4) + V-gate (Step 4.5)
5. If `zone3_content` is provided, validate each cell; if not, apply Assumption Framework

**Outbound (GNM outputs feed into):**
- **Strategy→GNM mapping** — Completed GNM structure feeds back for strategy-zone alignment verification.
- **Value decomposition** — Zone 3 Values (especially KPIs at Level Z) can seed KPI registries.
- **Executive briefings** — GNM cascade summary can feed board-level visualization of the strategic architecture.
- **Strategy translation** — Zone 3 content at Level Z translates directly into field-level action cards.

### GNM → CIS Workflow Mapping (Harmonized)

| GNM Output | CIS Target | Use |
|---|---|---|
| Level A cascade summary | Executive Briefing (EB) | Board-level strategic architecture visualization |
| Level Z Zone 3 Values (KPIs) | Value Decomposition (VD) | KPI registry seeding, target validation |
| Level Z Zone 3 Values (actions) | Strategy Translator (ST) | Field-level action card generation |
| Multi-sheet cascade | Portfolio Prioritizer (PP) | Initiative inventory for ranking |
| GNM handoff YAML block | Format Transformer (FT) | Convert GNM spec to pptx/docx summary |

> **Handoff block:** When GNM output is saved to file, append the machine-readable handoff YAML block per `workflow-checkpoint-protocol.md` format:
>
> ```yaml
> ---
> handoff:
>   source_workflow: GNM
>   gnm_topic: "{Topic Name}"
>   sheets_created: 3
>   levels_used: [A, B, Z]
>   zone3_cells_populated: 18
>   cascade_depth: 3
>   domain_context: "vib"  # vib | banking | generic
>   suggested_next: [GM, VD]
>   notes: "Forward-reference engines: WB, TRS (sheets not yet created)"
> ---
> ```

---

