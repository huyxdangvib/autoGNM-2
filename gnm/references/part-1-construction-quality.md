---
part: 1
name: "Construction Quality & Frameworks"
parent: gnm-instruction.md
---

> **Scope:** These Q1-Q8 checks ensure **construction quality** (is the logic and thinking sound?). For **structural integrity** rules (what makes a valid GNM format), see `part-1-rules-priority.md` § Critical Rules (1-11). Different scope — Q-check numbers do not correspond to Critical Rule numbers.

## GNM Construction Quality Layer

> **Purpose:** Ensures GNM output follows the proper construction pipeline and produces conceptually sound matrices — beyond structural validity. Replaces rigid WHAT-TODO purity enforcement with Decoding-led quality checks that match how GNMs are actually built.
>
> **Key insight:** Zone 1 is **mostly WHAT** but **sometimes TODO**. Zone 2 is **mostly TODO** but **sometimes WHAT**. The axes are flexible — what matters is that the Decoding is correct and the axes are coherent within their chosen perspective. Not everything is WHAT-TODO; the real discipline is _Decode → Structure → Matrix → Content_.

### GNM Construction Pipeline

```
Stage 1: DECODE     → Identify topic, choose decoding method(s), lock perspective
Stage 2: STRUCTURE  → Build Zone 1 axis + Zone 2 axis (sequential, like CPU)
Stage 3: MATRIX     → Fill Zone 3 intersections (parallel, like GPU — all cells at once)
Stage 4: CONTENT    → Engines, Values, Process details, Templates
```

> **CPU/GPU metaphor:** Stages 1-2 are sequential thinking (CPU) — you must decode and structure before you can fill. Stage 3 is parallel thinking (GPU) — the matrix reveals all relationships simultaneously. Stage 4 is output quality.

### Pre-V-gate Quality Checks (run before V-gate Step 4.5)

| # | Check | Pipeline Stage | How to Validate | Severity |
|---|-------|---------------|-----------------|----------|
| Q1 | **Decoding method** | DECODE | Did the builder use the right decoding method for the topic type? Classification for taxonomy, Component for structure (PCSS/BSC), Binary for decisions, Flow for processes. Single vs Dual decoding appropriate? | HIGH |
| Q2 | **Perspective lock** | DECODE | Is there one consistent perspective (phối cảnh) across Zone 1 items? Whether Zone 1 holds WHAT or TODO, all items at the same level must share the same viewing angle (đồng dạng phối cảnh). | HIGH |
| Q3 | **Axis coherence** | STRUCTURE | Are Zone 1 items coherent as a group? Are Zone 2 features coherent as a group? Each axis should be internally logical — MECE for classification, sequential for flow, complete for components. Zone 1 CAN be TODO and Zone 2 CAN be WHAT when the decoding requires it. | HIGH |
| Q4 | **Structure quality** | STRUCTURE | If axis is sequential (flow) → output→input chain intact? If axis is categorical (list) → MECE taxonomy? If axis is components → all parts sum to whole? Match validation method to the decoding method used. | MED |
| Q5 | **Matrix density** | MATRIX | Are Zone 3 intersections meaningful? Each cell should answer "what happens when [Zone 1 item] meets [Zone 2 feature]?" Empty or filler cells = broken matrix. | MED |
| Q6 | **Coverage (10-7-5-(-3))** | MATRIX | Is the topic fully covered? Compare stated intent vs actual GNM content. A GNM that captures 5/10 has already lost 50%. The GNM should be the "10". | LOW |
| Q7 | **Nomenclature** | CONTENT | Names: rõ ràng (clear), cụ thể (specific), nhất quán (consistent), không trùng lặp (non-duplicated). No generic names ("Khác", "Other", "TBD", "Misc"). | MED |
| Q8 | **Content quality** | CONTENT | Zone 3 cells describe full scope of the intersection, not just keywords. Engines are self-explanatory (`[Full Name] CODE(Level)`). Values have measurable scope. Single keywords = information loss. | MED |
| Q9 | **Resolution Test** | STRUCTURE | Before opening a new cascade level, does the additional level pass the Resolution Test? Actionability + Ambiguity + Value-Add must justify the depth. See Q9 detail below. | MED |
| Q10 | **Zone weight gradient** | STRUCTURE | Does the zone content match the declared level? Level A should have heavier Z8-9 (context/relationships) than Z1-7 (core items). Level Z should have dense Z1-7 Values and minimal Z8-9. If a declared A-level has dense Z1-7 but empty Z8-9 → suspect it's actually B or C. If a declared Z-level has heavy Z8-9 → suspect it's actually A or B. Diagnostic: compare Z1-7 vs Z8-9 cell density ratio. | MED |

### Quality Check Output

Append after V-gate line:
```
Quality: Decode[ok|mismatch] Perspective[ok|mixed] Axes[ok|incoherent] Structure[ok|broken] Density[ok|sparse] Coverage[ok|gap] Names[ok|warn] Content[ok|vague]
```

### Auto-Fix Guidance

> **Principle:** Every fix traces to a pipeline stage. If the issue is in DECODE, fixing at CONTENT level is cosmetic — you must fix upstream first.

| Check | Issue | Pipeline Root Cause | Fix Protocol | Example |
|-------|-------|-------------------|--------------|---------|
| **Q1** | Wrong decoding method | DECODE: Method doesn't match topic type. Classification produces random list when topic needs Flow. Component produces fragmented parts when topic needs Classification hierarchy. | **Identify topic intent → select method:** (1) "List/group things" → Classification. (2) "Break into parts" → Component (PCSS for business). (3) "Decide between options" → Binary. (4) "Sequential process" → Flow. **Then rebuild** Zone 1/2 axes from scratch using correct method. Single decoding if one axis is fixed; Dual decoding if both need structure. | Topic "Quy trình cho vay" (Lending Process) decoded with Classification → random items. Correct: Flow Decoding → Zone 2 features as process chain [Origination → Underwriting → Approval → Disbursement → Monitoring]. Zone 1 can be products (WHAT applied to this flow). |
| **Q2** | Mixed perspective | DECODE: Perspective not locked before Zone 1 was built. Items from different viewing angles mixed at the same level — violates đồng dạng phối cảnh. | **Step 1:** Identify what perspective each item belongs to (Product? Customer? Function? Salesforce?). **Step 2:** Count items per perspective — find the dominant one. **Step 3:** Reclassify outliers: (a) promote to separate GNM if they represent a different scope, or (b) demote to L2 if they are details within a valid L1. | L1=[Home Loan, Auto Loan, RM Team, Customer Segment] → Products (2) + Salesforce (1) + Customer (1). Dominant=Product. Fix: keep Home Loan, Auto Loan; move RM Team to Salesforce GNM; move Customer Segment to Customer GNM. |
| **Q3** | Incoherent axis | STRUCTURE: Zone 1 or Zone 2 items don't form a logical group. This happens when items are added ad-hoc without consistent decoding, or when WHAT and TODO leak across axes incorrectly. | **For Zone 1:** verify all items answer the same question ("what are we managing?" or "what process steps?"). **For Zone 2:** verify all features answer the same question ("what actions?" or "what dimensions?"). If an item doesn't belong, it's either in the wrong zone or the wrong GNM. Remember: Zone 1 CAN hold TODO items and Zone 2 CAN hold WHAT items — coherence matters more than noun/verb. | Zone 1 has [Products, Origination, Customer] — mixes nouns (Products, Customer) with a process (Origination). The decoding was inconsistent. Fix: decide axis type. If Zone 1 = products → move Origination to Zone 2. If Zone 1 = process steps → move Products/Customer to a different GNM or to Zone 2. |
| **Q4** | Broken structure | STRUCTURE: The internal logic of an axis is wrong. Flow axis has no sequence. Classification axis is not MECE. Component axis doesn't sum to the whole. | **Match fix to decoding method:** (1) Flow → reorder by output→input chain; add linking steps for gaps. (2) Classification → check MECE: are items mutually exclusive? collectively exhaustive? (3) Component → do all parts sum to the whole? Missing parts = incomplete. (4) Binary → are branches truly binary? No overlapping options? | Zone 2 features [Approval, Origination, Monitoring] using Flow Decoding → broken sequence. Fix: trace the flow — Origination produces application → Approval evaluates → Monitoring tracks. Correct order: [Origination → Approval → Monitoring]. |
| **Q5** | Sparse matrix | MATRIX: Too many Zone 3 cells are empty, "-", or filler. The matrix isn't producing meaningful intersections — indicating either Zone 1/2 axes are misaligned, or content hasn't been developed. | **Diagnose root cause:** If many cells are genuinely N/A → the axes are misaligned (fix at STRUCTURE stage). If cells should have content but don't → fill with appropriate level content: Engines for A/B levels, Values for Z level. Every cell should answer: "what happens when [row] meets [column]?" | 6/10 Zone 3 cells are "-" → likely Zone 1 items don't all relate to Zone 2 features. Either the perspective is mixed (fix Q2) or the features are too specific. Consider broader features or splitting the GNM. |
| **Q6** | Coverage gap | MATRIX: Topic not fully represented. The GNM captures only part of the intended scope — producing a 5/10 or 7/10 picture instead of the full 10. | **Cross-check against domain knowledge:** (1) For VIB business topics → use PCSS framework: is P represented? C? S? S? (2) For VIB functions → use Part 6 reference. (3) For general topics → list all major aspects of the topic and verify each appears. The test: can someone read this GNM alone and understand the complete topic? | RB Lending GNM has [Home Loan, Auto Loan, Consumer Loan]. Cross-check PCSS: P=3 products (but missing Credit Card, Overdraft). No Customer, Salesforce, or Platform dimension. Coverage ≈ 5/10 for a full RB Lending scope. |
| **Q7** | Bad naming | CONTENT: Nomenclature violations — generic names, vague labels, duplicates, inconsistent patterns. Names that don't communicate clearly force the reader to guess — defeating GNM's purpose. | **Apply 4 naming rules in order:** (1) Rõ ràng — what IS this? Name by nature. (2) Cụ thể — narrow from general to specific. (3) Nhất quán — match sibling naming pattern. (4) Không trùng lặp — no two items mean the same thing. | "Khác" among [Home Loan, Auto Loan, Khác] → (1) It's unsecured personal lending. (2) "Consumer Loan". (3) Pattern "[Type] Loan" → "Consumer Loan". (4) No duplicate. ✅ |
| **Q8** | Vague content | CONTENT: Zone 3 cells use single keywords instead of meaningful scope descriptions. This is information loss — readers get 5/10 instead of 10/10 from each cell. | **Expand using intersection test:** read Zone 1 item + Zone 2 feature → Zone 3 should answer "what is the scope/outcome when [feature] is applied to [item]?" (1) A/B level → Engine reference with full self-explanatory name. (2) Z level → measurable targets, KPIs, or detailed descriptions. Single keywords fail the test. | Item="Home Loan" × Feature="Origination" → Z3="Phát triển" (vague, 2/10). Fix Z-level: "Tăng trưởng 15% hồ sơ qua Digital, target 500/tháng". Fix B-level: "Home Loan Origination HLO(Z)". |
| **Q9** | Unnecessary cascade depth | STRUCTURE: A new level was opened (B from A, C from B, or Z from C) without passing the Resolution Test — the level adds no actionability, resolves no ambiguity, and provides no decision value. | **Apply Resolution Test before opening any new level.** Ask 3 questions: (1) Actionability — can the owner at this level act on the content? (2) Ambiguity — is there meaningful uncertainty the deeper level would resolve? (3) Value-Add — would the additional level help real decisions? All 3 = No → STOP. Any 1 = Yes → consider. All 3 = Yes → open. Asymmetric depth is normal — different engines may resolve at different levels. | Engine X has A→B→C→Z opened "because we have data" but C-level audience can't act on Z values, Z values aren't debated, and no decision depends on Z. → Remove Z. Keep A→B→C. Anti-pattern: Auto-Z — opening Z for every item because metrics exist. |

---

## Q9 — Resolution Test (Cascade Depth Gate)

> Source: VBS Strategy→GNM Mapper workflow (2026-03-30)

Before opening a new cascade level (B from A, C from B, Z from C), apply the Resolution Test:

| Question | Yes → | No → |
|----------|-------|------|
| **Actionability:** Can the owner at this level act on the content? | Supports opening new level | Content may be too abstract — stay at current level |
| **Ambiguity:** Is there meaningful uncertainty that a deeper level would resolve? | Supports opening new level | Current level is sufficient |
| **Value-Add:** Would the additional level help real decisions? | Open the new level | Stop — avoid over-decomposition |

### Decision Rule
- **All 3 = No** → STOP. Do not open a new level. Current depth is sufficient.
- **Any 1 = Yes** → Consider opening. Weigh cost of additional level vs. clarity gained.
- **All 3 = Yes** → Open the level. There is clear need for deeper decomposition.

### Common Application
- **A→B gate:** "Does the B-level audience (regional heads) need their own flow logic, or is A-level direction sufficient?"
- **B→Z gate:** "Are values debated? Do multiple people interpret 'improve' differently? If not, skip Z."
- **Asymmetric depth is normal:** Different engines within the same GNM may resolve at different levels. Engine X may need A→B→Z while Engine Y stops at A→B.

### Anti-pattern: Auto-Z
Opening Z-level for every B-level item "because we have data." Z should only open when value ambiguity exists — not because metrics are available.

---

<create-only reason="Relevance Engine only used for CREATE tasks — skip for REVIEW/EXPLAIN/MODIFY/CONVERT">

## Strategy Framework Relevance Engine

> **Full Relevance Engine specification** is in `references/part-1b-relevance-engine.md` (scoring matrices) and `references/part-1c-*.md` (124 framework descriptions). Load both for CREATE tasks only. Below is a summary for quick reference.

**What it does:** At Step 2.3, silently score 12 framework categories using GNM Type x Level multipliers, surface top 3-5 (score >= 1.0) as recommended frameworks for Zone 1/2/3 content decisions.

**When to use:** CREATE tasks only. Skip for REVIEW/EXPLAIN/MODIFY/CONVERT.

**Quick reference:** See Part 1b for the full GNM Type -> Framework Category Relevance Matrix, Level Depth Modifiers, Framework -> Zone Mapping Guide, and Worked Example.

</create-only>

---

