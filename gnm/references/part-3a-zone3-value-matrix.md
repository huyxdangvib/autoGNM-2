---
part: 3a
name: "Zone 3 Value Matrix"
parent: gnm-instruction.md
---

## Zone 3: Value Matrix (Ma trận Giá trị) - KHU VỰC QUAN TRỌNG NHẤT

**Mục đích:** Thể hiện mối quan hệ giữa mỗi Item (WHAT) và mỗi Feature (TODO).

**Tại sao cần Zone 3:** Zone 3 là **TRÁI TIM** của GNM - nơi giao cắt giữa WHAT x TODO tạo ra giá trị thực sự. Mỗi ô trả lời câu hỏi: "Với Item này, Feature này có giá trị/hành động gì?"

**Vị trí cột Zone 3:** Zone 3 luôn chiếm **CÙNG CỘT với Zone 2** nhưng tại rows 8+ (Content rows). Zone 2 nằm ở rows 6-7 (headers), Zone 3 nằm ở rows 8 trở đi. Cả hai dùng chung f cột (f=1..5) bắt đầu từ Col(G+L2). Xem Scaling Formula tại PART 2a.

**⚠ NGUYÊN TẮC QUAN TRỌNG:**
- **Values/Engines được mô tả thông qua Keywords (recommended max 50 characters)**
- **Engine bản thân ĐÃ LÀ Value** — tên Engine mang nghĩa, giúp người đọc hiểu "ô này nói về gì"
- **Không cần Value bổ sung nếu Engine name đủ rõ** — VD: `Production & Supply Chain PSC(B)` đã đủ nghĩa
- **Value = thông tin trực tiếp, dừng tại đây. Engine = nội dung phức tạp, có sub-GNM riêng**
- Một ô Zone 3 có thể chứa: **Value** hoặc **Value + Engine** hoặc **Engine** (khi Engine đã đủ nghĩa)

**Decision Tree: Khi nào dùng Value vs Value+Engine vs Engine trong Zone 3:**

```
Câu hỏi 1: Nội dung ô này có cần sub-GNM để giải thích chi tiết không?
│
├── KHÔNG cần sub-GNM:
│   └── → Dùng **Value** (thông tin trực tiếp, dừng tại đây)
│       VD: "45%", "High", "[green] On track", "Q1 2026"
│
└── CÓ cần sub-GNM:
    │
    ├── Câu hỏi 2: Tên Engine đã đủ nghĩa cho người đọc hiểu ô nói về gì chưa?
    │   │
    │   ├── ĐỦ NGHĨA (Engine name tự giải thích):
    │   │   └── → Dùng **Engine** (chỉ Engine, không cần Value bổ sung)
    │   │       → Tạo HYPERLINK formula: `=HYPERLINK("#'Sheet'!B2", "EngineName MãGNM (Level)")`
    │   │       → Text color: #0563C1 (link blue)
    │   │       VD: "Production & Supply Chain PSC(B)" — tên đã rõ
    │   │
    │   └── CHƯA ĐỦ NGHĨA (cần context bổ sung):
    │       └── → Dùng **Value + Engine** (Value mô tả + Engine drill-down)
    │           → Engine phần: tạo HYPERLINK formula, text #0563C1
    │           → Value phần: text #000000 (plain text, không link)
    │           VD: "Digital-led, selective ATL" + Engine "Marketing Strategy MKS(Z)"
```

**Tóm tắt:**

| Tiêu chí | Dùng Value | Dùng Engine | Dùng Value + Engine |
|----------|-----------|-------------|--------------------|
| Cần sub-GNM? | Không | Có | Có |
| Engine name đủ nghĩa? | N/A | Có | Không |
| Level phổ biến | Z | A, B, C | B, C |
| Ví dụ | `45%`, `High` | `Service Catalog SVC (B)` | `Digital-led MKS(Z)` |

**Nội dung Zone 3 theo GNM Level:**

| GNM Level | Zone 3 Content | Ví dụ cụ thể |
|-----------|----------------|-------------|
| **Level A, B, C...** | **Engines** (tên đủ nghĩa) hoặc Values + Engines | `Service Catalog SVC (B)`, `Control Framework CTL(B)` |
| **Level Z** | **Values chi tiết** (+ Engines Z1, Z2...) | `45%`, `[x]`, `High`, `[green] On track`, `Q1 2026` |

**Tỷ trọng Value vs Engine thay đổi theo Level:**

| Level | Tỷ trọng | Ý nghĩa | VBM Example |
|-------|----------|----------|-------------|
| **A** | Almost all Engines | Mọi Item×Feature đều cần sub-GNM | VBM(A): RBB, HR, Risk, BTS — all Engines |
| **A** (scope) | Engines + some placeholders | Scope selection with some items TBD | APT(A): "Basic APT (1)", "Product 1 centric dev." |
| **B** | Most Engines | Phần lớn cần drill-down, một số đủ rõ | — (no B-level in VBM; see RBL/RBF examples) |
| **C** | Balanced | Cân bằng giữa Value và Engine | — |
| **Z** | Most Values | Phần lớn là thông tin thực thi cuối cùng | BAP(Z): specific actions per org unit |
| **Z** (pure data) | All Values | Schedules, names, dates, strategy lists | RSS(Z): "9/3: Morning", BAT(Z): person names |

**GNM Composition Pattern by Level:**

Mỗi level có đặc trưng composition khác nhau — từ navigation (A) đến execution (Z):

| Level | Nhiều hơn (More) | Ít hơn (Less) | Tính chất GNM |
|-------|-------------------|---------------|---------------|
| **A** | Cấu hình treo (Engines), Decoding | Matrix planning | **Navigation GNM** — chủ yếu Engines trỏ đến sub-GNMs, decode phân rã scope, tư duy rộng theo S7 Steps 1-3 |
| **B** | Matrix nội dung thực, Zone 2 thiên perspectives/domains | Cấu hình treo | **Working matrix GNM** — scope đã hẹp, Zone 2 features mang tính góc nhìn/lĩnh vực (noun-like TODO: BSC perspectives, 10-Phase domains), nhiều Values hữu ích hơn |
| **Z** | Value framework | Engines | **Execution GNM** — số liệu, ngày, KPI, trạng thái cụ thể |

> **Xu hướng:** A→Z = giảm dần Engines (cấu hình treo), tăng dần Values (nội dung thực thi). A = "nghĩ rộng, trỏ nhiều", Z = "làm cụ thể, ghi chi tiết." C-level nằm giữa B và Z — balanced Engine/Value (xem ABC table ở trên).

**Z-Level Sub-Types (codified 2026-04-17, per Critical Rule #13):**

Z-level is NOT monolithic. Three distinct sub-types with different compliance targets:

| Sub-type | Code | Purpose | Z3 Composition | Production Examples | Compliance Target |
|----------|------|---------|----------------|---------------------|-------------------|
| **Z-M** | Measurement | Dashboards, KPIs, goals, numeric reports | Mostly Values (numbers, formulas, text-numerics) | `7(Z) NTB Lending Lead Goal`, `2A(Z) Lead Allocation` (BNW) | ≈90% Values |
| **Z-P** | Process | RACI matrices, implementation plans, workflow templates, PDCA patterns | Mostly Engines (R/A/C/I codes, action names, phase labels) | `5(Z) RACI`, `6(Z) Implementation Plan`, `BLC(Z) Campaign Pattern` (BNW) | ≈80% Engines |
| **Z-T** | Template | Scaffold sheets awaiting data population | Mostly empty (to be filled later) | `2A.1(Z) WHCM Lead Details` (BNW) | ≈80% empty — acceptable as WIP |

**Validator behavior:** Before applying a Z-level ratio check, identify the sub-type from (in priority order):
1. Build Spec `z_subtype` field if declared
2. Zone 1 content — PDCA/SMART/flow phases → Z-P; numeric/KPI items → Z-M; empty-scaffold → Z-T
3. Zone 3 value distribution as fallback
4. Sheet name / B2 label heuristic (RACI/Plan/Workflow → Z-P; Goal/Dashboard → Z-M; blank rows → Z-T)

Apply the correct compliance target. A RACI matrix being 100% engines is NOT a violation — it is an exemplary Z-P.

**Build Spec declaration (optional but recommended):**
```yaml
z_subtype: "Z-M"   # Z-M | Z-P | Z-T
```

**Why sub-typing matters:** The pre-2026-04-17 rule "Z-level ≈90% Values" was a false universal. It flagged legitimate process templates (RACI, Plan, PDCA) as violations. BNW workbook mining proved 4 of 6 Z-level sheets in the BNW cascade are Z-P or Z-T — each compliant under its correct sub-type. Sub-typing restores validation integrity.

**Nguyên tắc viết Value tại Level A, B, C (Scope-Led Principle):**

Zone 3 Values tại Level A-C phải mô tả **đúng scope đầy đủ** của mối quan hệ
Item x Feature, không chỉ highlight một khía cạnh nổi bật. Phân biệt giữa
các Items bằng **trọng tâm** (focus/emphasis), không bằng cách **bỏ bớt scope**.

| Cách viết | Ví dụ | Đánh giá |
|-----------|-------|----------|
| ❌ Chỉ ghi khía cạnh nổi bật | "Digital & influencer mktg" | Gây hiểu lầm chỉ làm digital |
| ✅ Ghi scope + trọng tâm | "Digital-led, selective ATL" | Rõ: digital là focus, ATL vẫn có |

**Format khuyến nghị:** `[Trọng tâm]-led, [bổ sung]` hoặc tương đương —
đảm bảo người đọc hiểu Item có full scope, chỉ khác nhau ở trọng tâm.

**Yêu cầu đồng nhất:** Tất cả Values trong cùng 1 cột Zone 3 phải cùng
góc nhìn và cùng mức độ chi tiết. Không trộn lẫn các chiều phân tích
khác nhau (VD: không trộn kênh vs giai đoạn vs mục tiêu trong cùng 1 cột).

**Decoding tại Zone 3:** Zone 3 values phản ánh kết quả giao cắt của Decoding Zone 1 × Zone 2. Zone 1/2 = Decoding **cấu trúc** (Items/Features). Zone 4/5 = Decoding **chi tiết** (đào sâu). Xem bảng tổng quan tại Zone 4 (PART 3b).

**Quy tắc quan trọng Zone 3:**
- Zone 3 KHÔNG được để ô trống (điền "-" hoặc "N/A" nếu không có giá trị)
- Keywords recommended max 50 characters. Engine format: `[Tên đầy đủ] MãGNM (Level)`
- Chọn Value/Engine/Value+Engine theo Decision Tree ở trên

### Identity Matrix Pattern (codified 2026-04-20, v5.11.0)

When Zone 1 items and Zone 2 features use the **same label set**
(e.g. Z1=[P,C,S₁,S₂,M,R] and Z2=[P,C,S₁,S₂,M,R]), the sheet produces
an identity matrix. **Two distinct variants with different compliance targets.**

**Axis flexibility:** The shared label set may be PCSSMR-6, PCSSMRcoSy-8, Full-11,
or a context-specific 6-subset (e.g. BDR-Development uses {P, C, SF, Channel, System, Collateral}).
Document the chosen set in B2 or Feature Group. See `vib-business-glossary.md` §
Eleven Business Components for canonical sets.

#### Variant A — Diagonal Identity (cascade-handoff)

- **Shape:** Only diagonal cells populated; off-diagonal empty or `-`
- **Job:** Single self-similar handoff from parent to child at top-of-cascade (A/B)
- **Evidence:** `TPU(A)`, `CPT(B)` in Thinking Processing Unit workbook — 1 engine on diagonal, 35/36 empty
- **Verdict:** AMBER — legitimate at A/B as "Listing-type" navigation, but degenerate in information density. Consider flattening to Single-Feature with Conso.
- **Anti-pattern marker:** More than 2 consecutive diagonal-identity sheets in a cascade = over-fragmented; collapse.

#### Variant B — Full Identity (completeness scanner)

- **Shape:** Every cell populated (with Y, H/M/L intensity, or initiative codes)
- **Job:** **Scope completeness audit** — asserts "every component-pair interaction has been considered." Functions as organizational coverage scanner for silo gaps.
- **Evidence:** `BDR × Development` (VIB internal, 6-component × 6-component = 36 cells fully populated with Y)
- **Verdict:**
  - GREEN when cells carry non-uniform payload (H/M/L, initiative codes, or short descriptors)
  - AMBER when uniformly Y (shape without signal — valid scope declaration only)
  - RED when diagonal cells repeat off-diagonal meaning (axis collapse)
- **Required enhancement:** All-Y acceptable as first-pass scope declaration, SHOULD evolve to H/M/L or initiative codes for actionability.

#### Common rules (both variants)

1. **Axis homogeneity disclosure:** When Z1=Z2, B2 or Feature Group **SHOULD** flag this deliberately (e.g. `Z1=Z2=PCSSMR-6` in B2 or Feature Group label). Explicit disclosure is **RECOMMENDED for new sheets**; pre-v5.11.0 sheets are grandfathered as annotation-debt (AMBER finding), not violations. Silent axis-collapse is an AMBER Q3 axis-coherence finding, never RED.
2. **Diagonal is NOT automatically degenerate** at VIB: P×P = portfolio mix, C×C = segment migration, S₂×S₂ = omnichannel, R×R = 3 lines of defense. Document each diagonal cell's meaning in a comment or Zone 6 consolidation.
3. **Complement with differentiated matrix downstream:** Identity-matrix sheets SHOULD be followed by a child where Z2 differentiates from Z1 (verbs, lifecycle, perspectives) — prevents cascade from staying in self-reference mode.

#### Variant C — Scope Completeness Matrix (non-identity, Y-uniform) — codified 2026-04-21, v5.12.0

- **Shape:** Z1 ≠ Z2 (asymmetric axes — e.g. Z1=PCSSMRcoSy-8 components × Z2=BU-5) but Z3 payload is uniform Y-marker throughout.
- **Job:** Scope-completeness scan over a non-square cross-axis — asserts "every component × BU intersection has been considered/owned." Sibling of Variant B (Full Identity) but for asymmetric axes.
- **Evidence:** `BDR(B)` in 2/3 VEM workbooks — 8 PCSSMRcoSy components × 5 BU features, 19/56 cells = Y (34%), rest empty. `MPD(D)` / `FSH(D)` in VEM family — same shape with 2-level Z1 hierarchy.
- **Verdict:**
  - GREEN when cells carry non-uniform payload (H/M/L, initiative codes) — same rule as Variant B
  - AMBER when uniformly Y on a populated diagonal-equivalent — valid first-pass scope declaration; producer owed evolve to H/M/L or initiative codes
  - AMBER when >50% empty (as in the VEM-family BDR) — flag as "scope under-scanned"; NOT RED since the Y-layer can legitimately be populated incrementally
- **Required enhancement:** Same as Variant B — all-Y acceptable as first-pass; evolve to H/M/L or initiative codes.
- `[exploratory-basis: 3-workbook]`

#### When NOT to use any variant

- Scope decomposition needs asymmetric axes AND per-cell descriptive content (use standard matrix, not Scope Completeness)
- Prioritization signal is primary output (use Voting Matrix instead)
- Only 2-3 components matter (use standard decomposition, not 5×8+ completeness scan)

**Legacy compatibility:** Pre-v5.11.0 Z1=Z2 sheets without explicit
axis-homogeneity disclosure (e.g. `TPU(A)`, `CPT(B)`, BDR × Development)
are grandfathered under this codification — named patterns apply
(Variant A or Variant B verdicts) but disclosure is annotation-debt
to resolve at next revision, NOT a structural violation.

**Discovery source:** Thinking Processing Unit 260418 (Variant A, 2 sheets: TPU, CPT) + BDR × Development scan (Variant B, 1 sheet), MTI iteration 2026-04-20.

---

### Voting Matrix (B-Level Prioritization)

> Source: VBS Strategy→GNM Mapper workflow (2026-03-30)

At B-level, Zone 3 cells may contain multi-role prioritization scores using the Voting Matrix format:

#### Format
```
voter1/voter2/.../voterN (total) /rank
```

Where:
- Each voter assigns a priority score (1 = highest priority, N = lowest)
- Voters are typically different organizational roles or stakeholder groups
- `(total)` = sum of all voter scores
- `/rank` = overall priority rank (lower total = higher rank)

#### Example
For a B-level GNM with 3 voting roles (Product, Sales, Risk):

| Engine | Product | Sales | Risk | Total | Rank |
|--------|---------|-------|------|-------|------|
| Digital onboarding | 1 | 2 | 3 | (6) | /1 |
| Branch optimization | 3 | 1 | 2 | (6) | /1 |
| Risk model upgrade | 2 | 3 | 1 | (6) | /1 |
| Marketing automation | 4 | 4 | 4 | (12) | /4 |

Cell value: `1/2/3 (6) /1`

#### When to Use
- B-level Zone 3 cells where multiple roles must agree on priority
- Initiative ranking across PCSSMR components
- Resource allocation decisions with competing stakeholders

#### When NOT to Use
- A-level (too strategic for tactical voting)
- Z-level (values are measured, not voted on)
- Single-owner domains (no multi-role conflict)

---

### Structured Cell Payload (MAY)

For analytical GNMs (especially Z-level), Zone 3 cells MAY use a **multi-field payload** instead of a single value. This is optional — simple values remain the default.

**Payload Grammar (3 tiers, pick one per GNM):**

| Tier | Format | Use when |
|------|--------|----------|
| **Simple** | `H/M/L + Owner + Initiative` | Quick assessment, board overview |
| **Standard** | `Impact \| KPI \| Risk \| Capability \| Initiative` | Working-level analysis |
| **Coded** | `H/M/L / Owner / KPI-code / Risk-code / Initiative-ID` | Data-dense, cross-reference ready |

**Rules:**
- All cells in the same Zone 3 MUST use the same tier (no mixing within one sheet)
- Payload tier is declared in Build Spec — not mixed at runtime
- The `|` delimiter separates fields within one cell (wrap text applies)
- At Level A/B: structured payload is uncommon — Engines dominate Zone 3
- At Level Z: structured payload is most useful — Values carry operational detail

**Example (Z-level, Standard tier):**
```
| Item       | Feature: Risk Assessment         | Feature: Monitoring           |
|------------|----------------------------------|-------------------------------|
| Mortgage   | H | LTV ratio | Credit risk | R3  | M | Delinquency | Market | R7  |
| Auto Loan  | M | DTI ratio | Credit risk | R4  | L | Default rate | Op risk | R2 |
```

**Build Spec declaration:**
```yaml
zone3:
  payload_tier: "standard"  # simple | standard | coded
  fields: ["impact", "kpi", "risk", "capability", "initiative"]
```

**Ví dụ Zone 3 cho GNM Level B:**

**Case 1: Mỗi cell có Engine riêng (khác sheet)**
```
| Item      | Feature 1                         | Feature 2                      |
|-----------|-----------------------------------|--------------------------------|
| Corporate | Corp Service Catalog CSC(Z)       | Corp Control Framework CCF(Z)  |
| SME       | SME Service Offer SSO(Z)          | SME Standard Controls SSC(Z)   |
```
> Mỗi Engine có mã riêng → mỗi ô link đến 1 sub-GNM khác nhau.

**Case 2: Nhiều items cùng link đến 1 sheet (ít phổ biến)**
```
| Item      | Feature 1                         | Feature 2                      |
|-----------|-----------------------------------|--------------------------------|
| Corporate | Service Catalog SVC (B)            | Control Framework CTL(B)       |
| SME       | Service Catalog SVC (B)            | Control Framework CTL(B)       |
```
> Tên + mã giống hệt → cùng link đến 1 sheet. Dùng khi Corporate và SME chia sẻ cùng catalog.

> **Lưu ý:** Engine name đã mang nghĩa (VD: "Service Catalog") + Mã link (VD: "SVC (B)") trong cùng 1 ô. Không cần tách 2 dòng.

**Engine Link Formula (Parent → Sub-GNM):**

Engines trong Zone 3, 4, 5, 6 sử dụng **HYPERLINK formula** để liên kết **từ Parent GNM đến Sub-GNM**:
- **Formula syntax:** `=HYPERLINK("#'SheetName'!B2", "DisplayText")` **OR** `=HYPERLINK("#'SheetName'!A1", "DisplayText")`
- **Target:** `!B2` (canonical — lands on GNM name cell) OR `!A1` (valid alternative — lands on back-link cell, better UX for round-trip navigation). A single workbook SHOULD commit to one target convention per-cascade.
- **DisplayText:** `[Tên đầy đủ] MãGNM (Level)` — Engine bản thân đã là Value, cái tên mang nghĩa
- **Lưu ý:** Dấu `#` ở đầu target là bắt buộc để link nội bộ workbook

| Parent Sheet | Target Sub-GNM | Engine Formula (đặt trong Zone 3/4/5/6) |
|--------------|----------------|----------------------------------------|
| `PRD (A)` | `PRD (B)` | `=HYPERLINK("#'PRD (B)'!B2", "Production & Supply Chain PRD(B)")` |
| `PRD (A)` | `PRD (Z)` | `=HYPERLINK("#'PRD (Z)'!B2", "Quality Assurance PRD(Z)")` |
| `PRD (B)` | `PRD (Z1)` | `=HYPERLINK("#'PRD (Z1)'!B2", "Inventory Control PRD(Z1)")` |
| `CBB (A)` | `CBB (B)` | `=HYPERLINK("#'CBB (B)'!B2", "Core Banking CBB(B)")` |

**Back-Link Formula (Sub-GNM → Parent):**

Mỗi Sub-GNM **BẮT BUỘC** có back-link ở ô A1 để navigate ngược về Parent:
- **Vị trí:** Ô **A1** của Sub-GNM sheet
- **Display:** `<<` (ký hiệu quay lại), **không indent, no wrap text**
- **Formula (BẮT BUỘC dùng formula, không dùng hyperlink object):**
  ```
  =HYPERLINK("#'ParentSheet'!A1", "<<")
  ```
- **Tại sao dùng formula:** Đảm bảo link không bị hỏng khi copy sheet hoặc rename

| Sub-GNM Sheet | Parent Sheet | Back-Link Formula (đặt tại A1) |
|---------------|--------------|-------------------------------|
| `PRD (B)` | `PRD (A)` | `=HYPERLINK("#'PRD (A)'!A1", "<<")` |
| `PRD (Z)` | `PRD (A)` | `=HYPERLINK("#'PRD (A)'!A1", "<<")` |
| `PRD (Z1)` | `PRD (B)` | `=HYPERLINK("#'PRD (B)'!A1", "<<")` |
| `MTG (Z)` | `MTG (B)` | `=HYPERLINK("#'MTG (B)'!A1", "<<")` |

**Bidirectional Navigation:** See Quick Reference Card (PART 1) for ASCII diagram. Summary: Parent→Sub via `=HYPERLINK("#'Sub'!B2", ...)` in Zone 3/4/5/6. Sub→Parent via `=HYPERLINK("#'Parent'!A1", "<<")` at A1.

> **Lưu ý:** Zone 3 engines dùng format `[Tên đầy đủ] MãGNM (Level)` để link đến GNM sheets khác (ví dụ: `Production & Supply Chain PSC (B)`). Zones 4-9 engines cũng theo format tương tự để link đến policies, dashboards, external documents.

#### Compact Engine Format (tight-cascade exception, codified 2026-04-20)

In cascades where parent and child codes form a tight single-letter-swap chain — i.e. the
engine code alone is sufficient for the reader to understand the drill-down target (because
the code itself is semantically meaningful within the cascade context) — engines MAY use the
**compact form `CODE`** instead of the full `[Full Name] CODE (Level)` format.

| Situation | Recommended form | Example |
|-----------|------------------|---------|
| Nav-heavy top-of-cascade (A/B) with diagonal-identity matrices | Compact `CODE` is acceptable | `CPT` (parent TPU(A) → CPT(B)) |
| Mid-cascade intermediate rungs (C/D/E) where the code is a household term for the reader | Compact `CODE` is acceptable | `RCP`, `RIC`, `ECC` |
| Any downstream cascade where reader ambiguity would arise | MUST use full format | `Customer classification (CCC)` at F-level |
| A/B-level forward-reference engines (sheets not yet created) | MUST use full format for self-documentation | — |

**Rule:** A workbook SHOULD commit to one format convention per-cascade-branch. Mixing
compact (at A/B) and full (at F/G) within the same cascade is acceptable and appears in
production (`Thinking processing unit - 260418`: A-D use compact, F+ use full). Parser
validators MUST accept both forms as valid Engine content.

**Evidence:** 5 sheets in `Thinking processing unit - 260418` (CPT/RCP/RIC/ECC/CUS)
consistently use compact codes at B-E levels; CUS(F) switches to full format for
its downstream G-level children. Consistent producer intent, not format drift.

#### Draft-State Bridge Pattern (codified 2026-04-21, v5.12.0)

When a workbook is in "first-version, no hyperlinks yet" state, producers commonly
express cascade semantically via two non-canonical formats that the parser MUST
detect as AMBER draft-state (not RED) findings:

| Pattern | Cell-content shape | Regex | Meaning |
|---------|-------------------|-------|---------|
| **Bare-code string** | `CODE` alone (no parens, no HYPERLINK formula) at an engine position | `^[A-Z]{2,4}$` | Cascade target code; HYPERLINK layer OWED |
| **Embedded Value-Engine** | Tag + paren-code | `^[HMLY+]?\s*\((\w{2,4})\)$` | Single cell doubles as value-marker (H/M/L/Y) + forward-ref code; HYPERLINK layer OWED |

**Verdict:** AMBER — "draft-state cascade: semantic reference present, hyperlink layer owed."
Parser resolves the paren-code / bare-code to the target sheet (if it exists) and reports
(a) which cells are in draft-state bridge form and (b) whether the referenced sheet exists.
Dangling references (paren-code does not resolve to any sheet in workbook) are a separate
AMBER "dangling forward-reference" finding.

**NOT a permanent valid variant.** Per producer declaration (VEM-family intake 2026-04-21),
bridge-pattern cells SHOULD evolve to canonical `=HYPERLINK("#'Sheet'!B2", "[Full Name] CODE (Level)")`
formulas before the workbook is considered published. Parser re-review post-hyperlink-add
converts AMBER bridge findings to GREEN.

**Workbook-level draft_state opt-in:** Producers MAY set `draft_state=true` in the
A-level root sheet's Conso cell (I5) to suppress per-cell AMBER findings during
pre-hyperlink authoring. Parser then emits ONE workbook-level AMBER summarizing
bridge-cell counts (e.g. `"draft_state=true — 47 bridge-pattern cells, 0 HYPERLINK
formulas, hyperlink layer owed"`). Dangling references, #REF! tokens, PNS-style
orphan-scaffold violations, and structural bugs remain reported regardless of the
flag. Remove the flag (or set false) when authoring the hyperlink layer to re-enable
strict per-cell reporting.

**Evidence:** VEM-family 3-workbook mining (2026-04-21): 0 HYPERLINK formulas across 23
sheets, 100% of cascade is expressed via bridge pattern. Examples: `RCP(C) I8 = "H (RIC)"`,
`MPD(D) H8 = "Y (AFC)"`, `FSH(D) J10 = "H(BNC)"`, `CUS(F) G8 = "CSD"` (bare code).
`[exploratory-basis: 3-workbook]`

---

