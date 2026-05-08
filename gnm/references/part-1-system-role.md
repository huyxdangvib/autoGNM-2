---
part: 1
name: "System Role & Core Concepts"
parent: gnm-instruction.md
---

<part1_system_role>

# PART 1: SYSTEM ROLE & CORE CONCEPTS

> **TL;DR:** PART 1 defines persona (GNM Builder Expert), 7-step thinking process, 11 Critical Rules, Terminology, Quick Reference Card, harmonized protocols (CIS-compatible, self-contained), Cross-Workflow Handoffs, and Strategy Framework Relevance Engine (summary — full spec in Part 1b, catalog in Part 1c). Communication style & boundaries → see instruction file.

> **Sub-files:** Identity & Thinking (`part-1-identity-thinking.md`), Critical Rules & Priority (`part-1-rules-priority.md`), Terminology & Handoffs (`part-1-terminology-handoffs.md`), Construction Quality (`part-1-construction-quality.md`). This file contains content NOT covered by those sub-files.

---

<data-integrity-protocol note="Optional enrichment: if _hagt/shared/data-integrity-protocol.md is available, load for full protocol. Otherwise, use the GNM addendum below as standalone.">
  <gnm-addendum>
    GNM-specific application: When Zone 3 Values contain quantitative data (KPIs, targets, percentages, financial figures), tag each with [^n] (verified from data file) or [EST] (estimated/benchmark). Engine cells do not need data tags — they are structural references, not data claims. Source Registry is optional for GNMs that contain only Engines (Level A/B) but mandatory for data-heavy GNMs (Level Z/Z1).
  </gnm-addendum>
  <fallback>If the base Data Integrity Protocol file is not in context, apply the GNM addendum rules above as standalone guidelines.</fallback>
</data-integrity-protocol>
<checkpoint-protocol note="Optional enrichment: if _hagt/shared/workflow-checkpoint-protocol.md is available, load for full protocol. Otherwise, use the GNM addendum below as standalone.">
  <gnm-addendum>
    GNM checkpoint gates: Checkpoint after completing each major section output — (1) after Phần Đầu (Index), (2) after Phần Thân Zone 1-3 content, (3) after Phần Thân Zone 4-6 (All cluster), (4) after Phần Mở rộng Zone 7-9 (Common cluster). At each gate, present: [c] Continue to next section / [r] Revise current section / [b] Bookmark and pause. For multi-sheet cascades, also checkpoint after completing each sheet before starting the next.
  </gnm-addendum>
  <fallback>If the base Checkpoint Protocol file is not in context, apply the GNM checkpoint gates above as standalone guidelines.</fallback>
</checkpoint-protocol>
<challenge-signal-protocol note="Optional enrichment: if _hagt/shared/challenge-signal-protocol.md is available, load for full protocol. Otherwise, use the GNM addendum below as standalone.">
  <gnm-addendum>
    GNM cross-workflow signals:
    - **GNM←[GM]**: If Strategy→GNM Mapper output places items in zones that conflict with GNM structural rules (e.g., Values in Engine-only zones), flag: "Zone placement from [GM] conflicts with GNM Rule [N]"
    - **GNM←[VD]**: If Value Decomposition output maps to Zone 3 but items don't match Zone 1 taxonomy, flag: "VD value drivers don't align with GNM Zone 1 Items"
    - **GNM←[ES]**: If Enterprise Strategy Catalog entries don't fit Zone 2 Feature structure, flag: "VES entries exceed Zone 2 capacity (max 5 Features)"
    - **GNM→[VS/SD/IS]**: If building a GNM reveals the upstream strategy has structural gaps (missing Items for key business units, empty Zone 3 cells that should have content), signal back: "GNM construction reveals strategy gap: [specific gap]"
  </gnm-addendum>
  <fallback>If the base Challenge Signal Protocol file is not in context, apply the GNM cross-workflow signals above as standalone guidelines.</fallback>
</challenge-signal-protocol>

---

## Quick Reference Card

> **TL;DR:** GNM = 9-Zone Excel framework visualizing WHAT (vertical) x TODO (horizontal) thinking.

| Concept | Key Points |
|---------|------------|
| **Structure** | 4 Sections: Tên GNM → Phần Đầu (Index) → Phần Thân (Matrix) → Phần Mở rộng (Context) (→ PART 2a/2b) |
| **Core Zones** | Zone 1 (WHAT Items) + Zone 2 (TODO Features, 1-5 cột) = Zone 3 (Value Matrix) (→ PART 3a) |
| **Engine Zones** | Zone 4-7: Consolidation & Common Matters (Engine only) (→ PART 3b) |
| **Referral Zones** | Zone 8 (Internal) + Zone 9 (External): Links to others' GNM (→ PART 3b) |
| **GNM Levels** | A/B/C = Engines (đã là Value, tên đủ nghĩa); Z = Detail Values; **Z1** = sub-terminal Values-only drilldown (no Engines) |
| **Feature Pattern** | **Multi-Feature (2-5 cột) là DEFAULT** ở mọi level (ref: MFM AI paper). Phần Thân = f+L2+3 cột (→ PART 2a). Single-Feature (1 cột): legacy pattern, chỉ dùng cho hub/navigation sheets. Phần Thân 4 cột. |
| **Content Format** | Engine: `[Tên đầy đủ] MãGNM (Level)` (max 50 chars). VD: `Service Catalog SVC (B)` (→ PART 5) |
| **Key Colors** | Header=#0070C0, Sub-header=#DDEBF7, Content=#FFFFFF (→ PART 4) |
| **Navigation** | **LUÔN dùng HYPERLINK formulas** (không dùng hyperlink objects). Parent→Sub: `=HYPERLINK("#'PRD (B)'!B2", "Production & Supply Chain PRD (B)")` / Sub→Parent: `=HYPERLINK("#'PRD (A)'!A1", "<<")` at A1 |

**Zone Summary:**
```
Zone 1 (WHAT) + Zone 2 (TODO) -> Zone 3 (Value Matrix)
Zone 3 -> Zone 4 (Horizontal) + Zone 5 (Vertical) -> Zone 6 (Common 3-5)
Zone 6 -> Zone 7 (Common 3-6)
Zone 8 (Internal Referral) + Zone 9 (External Referral)
```

**Bidirectional Navigation (HYPERLINK formulas only):**
```
Parent GNM ──[=HYPERLINK("#'Sub'!B2", "Engine Name MãGNM (Level)")]──→ Sub-GNM
    A1: (empty)                                                        A1: <<
              ←──[=HYPERLINK("#'Parent'!A1", "<<")]────────────────────┘
```
> ⚠️ KHÔNG dùng Insert → Hyperlink. Luôn nhập HYPERLINK formula trực tiếp.

---

## Cascade Patterns

GNM cascades can take two forms depending on organizational scale. Both are valid.

**Multi-A Cascade** — Level A repeats multiple times, progressively narrowing scope before reaching B. Used in large organizations with multiple business layers.

```
VBM(A) → WO Recovery(A) → RB NPL(A) → Workout(B) → KPIs(Z)
```

**Single-A Cascade** — One A-level index links directly to B. Used in focused organizations or single-domain topics.

```
KBS(A) → RBB(B) → Product(Z) → Detail(Z1)
BNW GEO(A) → ACC/PRO/INV/TRF(B) → region(Z)
```

**A→Z Direct (no B-level):**
Some VIB cascades skip B entirely: VBM(A) → AIA(Z), VBM(A) → VES(Z), VBM(A) → BFS(Z). This occurs when the topic doesn't require execution engineering (10-Phase). The A-level scopes the topic, and Z-level provides direct execution values (schedules, team assignments, strategy catalogs). The entire VBM workbook (12 sheets) operates as a pure A+Z executive model with no B-level sheets — B-level is reserved for product/service engineering GNMs (e.g., RBL, RBF) that live in separate workbooks.

**Multi-Dimensional Matrix System (MAY):**
For complex analytical domains with multiple engines, a cascade MAY be organized as a **3-layer matrix system** where each engine is the root of its own analysis model:

```
Layer 1 — Scope Map (Level A)
  Zone 1 = Big Topics (domain areas)
  Zone 3 = Engines pointing to Layer 2 sheets

Layer 2 — Engine Map (Level B)
  Each engine-rooted sheet declares its own Row x Column semantics
  Zone 3 = sub-engines or structured values

Layer 3 — Detail Matrix (Level Z)
  Zone 3 = structured cell payloads (Impact | Owner | KPI | Risk | Initiative)
```

This pattern is useful when: (1) a domain has 5+ distinct engines, (2) each engine has its own analytical dimensions (different row/column meanings), (3) the audience needs both executive overview and operational detail. See Part 3a for structured cell payload grammar and Part 3b for Engine-as-Root model.

> **Note:** AIA tab in VBM Excel is labeled "(A)" but Zone 3 content is predominantly Values → functional level is Z. When tab labels conflict with Zone 3 content, trust the content.

**Z→Z Cascading (28% of production paths):**
Z is NOT always terminal. Z-level sheets can cascade to sub-Z for deeper measurement detail. Patterns: A→B→Z→Z, A→A→Z→Z, A→A→B→Z→Z. This is valid when a measurement domain needs sub-breakdowns (e.g., regional KPIs → branch KPIs → product KPIs).

**Rule:** Multi-A for multi-layer orgs (e.g., Group → Division → BU). Single-A for focused orgs or single BU. Both patterns are equally valid — the cascade depth reflects organizational reality, not GNM quality.

---

## Level-to-Scope Mapping (ABCDEZ)

Maps organizational roles to GNM cascade positions. Full 6-level model with zone weight gradient.

**The Zone Weight Gradient** — the architectural fingerprint of each level:
- Level A: **few** Engines in Z1-7, **heavy** Z8-9 (context-rich, scope-light)
- Levels B→E: Z1-7 grows denser, Z8-9 thins out progressively
- Level Z: **dense** Values in Z1-7, **minimal** Z8-9 (measurement-pure)

| Level | Question | Z1-7 | Z8-9 | Zone 3 | Org Role | Exemplars |
|-------|----------|------|------|--------|----------|-----------|
| **A** | What scope? | Few Engines | **Heavy** | Engines → B | Executive / Division Head | BMA, RBC(MST), HRG, RIS |
| **B** | How to win? | More Engines | Moderate | Engines → C | Strategy / Product Head | WBS-1, PCS(TRS), MOF(HRS) |
| **C** | How specifically? | Dense Engines | Light | Engines → D | Regional / Team Lead | WBS-1a, BBK-1.1, RPB-2.1 |
| **D** | Who/resources? | Dense Engines | Minimal | Engines → E | Manager / Project Lead | NWR-1.2.9 (frontier) |
| **E** | Process detail? | Very Dense | Almost none | Engines → Z | Process Owner | (frontier — emerging) |
| **Z** | Numbers? | Dense **Values** | Minimal | Terminal | Field / Branch Manager | RBC-1z, TRS-FIX, WBS-11 |

**Production evidence (143 sheets):** A=25, B=20, C=7, D=1, E=0, Z=90. Ratio: every A-level scope generates ~3.6 Z-level sheets.

**S7↔Level mapping:**
- S7 Steps 1-2 (External/Internal Analysis) → Level A thinking (context-heavy Z8-9)
- S7 Steps 3-5 (Strategic Choice, How to Win) → Level B-C (engineering, Z1-7 growing)
- S7 Steps 6-7 (Formulation, Implementation) → Level D-E (operational, Z1-7 dense)
- S7 Steps 8-9 (Change, HAGT Harmonization) → Level Z (measurement)

**Examples across industries:**
- Banking: CEO/BMA (A) → Division Heads/MST (A) → Product Strategy (B) → Tactical (C) → Operations (D) → Branch KPIs (Z)
- Securities KAFI: CEO (A) → BU Heads RBB/FIT/E&D (B) → Traders (Z)
- NPL: Division Head CRO (A) → Portfolio Managers (B) → Solution Dev (C) → Case Detail (D) → KPIs (Z)

---

<create-only reason="Relevance Engine only used for CREATE tasks — skip for REVIEW/EXPLAIN/MODIFY/CONVERT">

## Strategy Framework Relevance Engine

> **Full Relevance Engine specification** is in `references/part-1b-relevance-engine.md` (scoring matrices) and `references/part-1c-framework-catalog.md` (124 framework descriptions). Load both for CREATE tasks only. Below is a summary for quick reference.

**What it does:** At Step 2.3, silently score 12 framework categories using GNM Type x Level multipliers, surface top 3-5 (score >= 1.0) as recommended frameworks for Zone 1/2/3 content decisions.

**When to use:** CREATE tasks only. Skip for REVIEW/EXPLAIN/MODIFY/CONVERT.

**Quick reference:** See Part 1b for the full GNM Type -> Framework Category Relevance Matrix, Level Depth Modifiers, Framework -> Zone Mapping Guide, and Worked Example.

</create-only>

---

</part1_system_role>
