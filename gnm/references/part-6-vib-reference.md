---
part: 6
name: "VIB Business Reference"
parent: gnm-instruction.md
---

# PART 6: VIB BUSINESS REFERENCE

> **TL;DR:** PART 6 contains VIB domain context — Business Basic Units, S7 mapping, 10-Phase framework, GNM Type Patterns, 9 Strategic Directions, Flywheel models, Support Function patterns, and Credit Risk patterns. Rules are in PART 1; zone specs in PART 2a/2b/3a.

**This is an index file.** Content is split across 5 sub-files. Load all `part-6-*.md` for full Part 6.

| Sub-file | Content |
|----------|---------|
| `part-6-vib-domain-units.md` | Domain Detection, VBM Glossary, Business Basic Units, Zone 1 Mapping |
| `part-6-vib-strategy-flywheel.md` | S7 Model, 9 Strategic Directions, Flywheel Models, 10-Phase Framework |
| `part-6-vib-patterns-cascade.md` | GNM Type Patterns, VBM Cascade, BFS Methodology, BSD Archetypes, Situation Decoding |
| `part-6-vib-support-functions.md` | Service/Control/Revenue Enabler taxonomy, HR/Risk/MarCom patterns, Naming conventions |
| `part-6-vib-credit-risk.md` | CRAS roll-ups, Customer x Collateral matrix, Approval unbundling, Diagonal sparsity |

> **Retrieval signpost:** Core zones (1-3) → PART 3a. Engine zones (4-9) → PART 3b. Validation → PART 7. Examples → PART 7b/7c.

---

## Level-Based Audience Layer (Sheet Metadata)

> Source: VBS GNM Navigator workflow + BFS methodology (2026-03-30)

Each GNM sheet serves a primary organizational audience. This should be declared as metadata:

| Level | Org Role | Scope | Sheet Characteristics |
|-------|----------|-------|---------------------|
| **A** | Division Head / Executive | Strategic selection & framing | A-level GNMs, broad scope, engines only in Zone 3 |
| **B** | Regional Head / Department Lead | Strategy development & resource allocation | B-level GNMs, tactical depth, per-level separate engines |
| **C** | Program Owner / Solution Manager | Solution-category selection | C-level GNMs, catalog/taxonomy view, sparse matrix OK |
| **D** | Execution Lead / Delivery Owner | Framework-driven execution decomposition | D-level GNMs, navigation hub, 90-100% engines (mostly hyperlinks to Z children) |
| **Z** | Branch Manager / Team Lead | Implementation & execution | Z-level GNMs, concrete values, action-oriented |

### Mapping to ABC Levels

| ABC Level | Primary Audience Level | Secondary |
|-----------|---------------------|-----------|
| A | Level A (executives) | Level B (for context) |
| B | Level B (regional/dept heads) | Level A (oversight), Level Z (direction) |
| C | Level B-Z (tactical managers) | — |
| D | Level Z (execution leads) | Level B (escalation context) |
| Z | Level Z (branch/team leads) | Level B (monitoring) |

### D-Level: Decomposition Hub (codified 2026-04-17)

D sits between C and Z. A D-level sheet takes **one cell** from its C-parent
and decomposes it through a named framework (PCSS-MR, 4P, 7S, Ansoff, etc.),
then navigates to multiple Z-level children via hyperlink engines.

| Axis | D-level spec |
|------|--------------|
| Z1 (Items) | Nouns — typically the framework's component list (e.g. 4 PCSS-MR components). MUST be populated; degenerate/empty Z1 is a VIOLATION (see Part 1 critical rules). |
| Z2 (Features) | Verbs — typically a lifecycle (Design → Deploy → Run → Measure) or the decision cycle (Diagnose → Recommend → Track). |
| Z3 (Matrix) | 90-100% engines (target ~95%). Mix of `engine_text` (sub-process labels) + `engine_hyperlink` (cascade to Z children). **Draft-state exception:** a D-level sheet with 0% formal HYPERLINK engines but populated with embedded `Value (CODE)` bridge-pattern cells (see Part 3a § Draft-State Bridge Pattern) is AMBER, not RED — flag as pre-HYPERLINK draft with producer-owed hyperlink layer. `[exploratory-basis: 3-workbook]` |
| Z4-7 | MAY hold hyperlink engines for inline cascade navigation. |
| Z8-9 | Usually empty when cascade is inlined in Z3-Z7. Do NOT penalize Z8-9 emptiness for D-level sheets. |
| Cascade role | C → D (single cell) → multiple Z children. Never skip levels. Parallel E-siblings under one D-parent are permitted (see "E/F/G: Intermediate Cascade Levels" § Parallel E-siblings). |
| Naming | B2 MUST end with `(D)`. B5 code is the canonical sheet identifier; tab name MAY differ but should be the business label. |

**Examples in production (BNW Development & Delivery workbook):**
- `NLL(D)` — NTB Lending Lead Mgt (child of BSS(C), decomposes via PCSS-MR framework)
- `WLD(D)` — WHCM Lending S&P Delivery (child of WSD(C), decomposes by campaign scope)

**Anti-pattern:** Degenerate Z1 (F='-', empty items) with framework nouns in Z2. This inverts the WHAT-TODO axiom and is a VIOLATION regardless of how common it appears in early-stage drafts.

### E/F/G: Intermediate Cascade Levels (codified 2026-04-20)

For **meta-cognitive cascades** (thinking-engine, taxonomy-engineering, classification-heavy
domains), three intermediate levels MAY sit between D and Z. These are rare but legitimate.

| Level | Role | Z1 (Items) | Z2 (Features) | Z3 Composition | Example (Thinking Processing Unit) |
|-------|------|-----------|---------------|----------------|-----|
| **E** | Lifecycle × Product matrix | Lifecycle phases (Acquisition/Usage/Retention/Upgrade) | Product variants | ≈70-80% Values (rating tiers, priorities) | `ECC(E)` — ETB Individual × Credit Card |
| **F** | Strategy-Flow hub | Customer/segment IDs (MUST populate; degenerate F is a VIOLATION) | Lifecycle verbs (Classify/Select/Design&Run) | 50-70% Engines — hyperlinks to G-level children | `CUS(F)` — Credit Card Usage Strategy |
| **G** | Classification / Selection catalog | Category base-rows (L2 encouraged for hierarchical taxonomies) | Classification facets (demographic/behavioral/financial/...) | 30-50% Values, up to 60% dash `-` acceptable (sparse MECE taxonomies) | `CCC(G)`, `CPC(G)`, `CPS(G)` |

**Cascade role:** E is an operational bridge from D to F. F fans out to multiple G children.
G children are terminal classification catalogs — their cascade-out goes to Z (execution).
G sheets with no direct action/value content are compliant: the action layer is the Z child
(this reconciles MG audit G1/G2 — G is not the terminal; Z is).

**Parallel E-siblings (codified 2026-04-21, v5.12.0):** One D-parent MAY fan out to ≥2
E-children, each occupying a distinct Zone 2 feature column of the D-sheet. The E-children
differ by Z2 feature-axis role (e.g. Classification-E vs Development-E), not by Z1 items.
Legitimate when the D-parent's Z2 decomposition itself is multi-faceted (e.g. MyVIB MPD(D)
decomposes into Function-Classification (AFC-E) AND Function-Development (AFD-E)). Each
sibling MUST have a distinct B5 code and distinct B2 label — silent B2 duplication across
siblings is an AMBER finding (see Part 7 checklist). `[exploratory-basis: 3-workbook]`

**Evidence:** MyVIB workbook MPD(D) → {AFC(E), AFD(E)} (2 siblings via H/I feature cols);
Org-chart workbook FSH(D) → {BNC(E), BNL(E)} (2 siblings via embedded-engine refs).
Producer intent confirmed by distinct Z2 axes (Opening/Management/Termination vs
BRD/UIUX/Tech/Testing/Golive on AFC/AFD respectively).

**Composite-facet features (observed at G-level):** A G-level Z2 feature axis MAY mix
single-view facets (Demographic, Behavioral, Financial) with combinatorial facets
(Double = two-way cross, Triple = three-way cross) in the SAME axis. When used, combinatorial
columns SHOULD reference which single-view columns they combine (comment or header note).

**Validator behavior:** When sheet has B2 suffix `(E)`, `(F)`, or `(G)`, apply the
composition target in the table above, NOT the D or Z targets. Degenerate Z1 at F-level
(empty Items) remains a VIOLATION (parallel to D-level rule). G-level empty Z3 cells MAY be
left as `-` (unlike A/B where `-` signals incomplete matrix) since sparse classification
is MECE-expected.

**Discovery source:** `Thinking processing unit - 260418` workbook mining (MTI Step 3,
2026-04-20) + `VEM Triple` workbook mining (MTI, 2026-04-21: vem-card-usage-strategy,
vem-myvib, vem-org-chart-function — E-level present in 3/3 workbooks, F-level in 2/3) +
**producer-declared deliberate convention (2026-04-21)**.

**MUST-level specification (promoted 2026-04-21, v5.13.0):** E/F/G composition targets
are enforced as MUST-pass. Violations emit **RED findings** (not AMBER):
- Degenerate Z1 at F-level (empty Items) = RED VIOLATION (parallel to D-level rule)
- E-level ratio deviation >15 percentage points from target = RED
- F-level ratio deviation >15 percentage points from target = RED
- G-level empty Z3 cells as `-` remain compliant (MECE-expected); this is NOT a violation

Evidence threshold crossed: 4+ workbooks (prior TPU + VEM triple) plus explicit producer
intent confirmation. Prior SHOULD-level / AMBER-only posture retired as of v5.13.0.

### Usage Note
bod-nextjs production currently uses ABC/D/Z levels structurally but does not encode level-based audience as explicit metadata. This mapping enables role-based filtering when implemented.

---

## S7 Strategy Model ↔ GNM Level Mapping

VIB's S7 seven-step strategy model maps to GNM levels through the zone weight gradient:

| S7 Steps | Thinking Mode | GNM Level | Zone Weight | Character |
|----------|--------------|-----------|-------------|-----------|
| Steps 1-2 (External + Internal Analysis) | Context scanning | **Level A** | Few Z1-7, **heavy Z8-9** (classical) OR few Z1-7 + empty Z8-9 (inline-cascade per Rule #12) | Relationships, stakeholders, forces |
| Steps 3-5 (Strategic Choice, How to Win) | Engineering | **Level B-C** | Growing Z1-7, moderate Z8-9 | Products, segments, tactics |
| Steps 6-7 (Formulation, Implementation) | Operational | **Level D-E** | Dense Z1-7, minimal Z8-9 | Tasks, assignments, processes |
| Steps 8-9 (Change Enablement, HAGT) | Measurement | **Level Z** | Dense Values Z1-7, no Z8-9 | KPIs, targets, outcomes |

**Practical implication:** When translating VS workflow output to GNM structure via [GM], the S7 step that produced the content determines the GNM level. External analysis (S7 Step 2) maps to A-level Engines. Initiative list (S7 Step 6) maps to B/C-level. KPI targets (S7 Step 6 table) map to Z-level Values.

---

## Strategy Lifecycle Status Tracking

> Source: VBS Enterprise Strategy Catalog workflow (2026-03-30)

Zone 3 strategy entries (particularly in VES and A-level strategy GNMs) should carry lifecycle status:

| Status | Meaning | Visual Indicator |
|--------|---------|-----------------|
| **ACTIVE** | Currently being executed, resources allocated | Green badge |
| **PAUSED** | Temporarily suspended (resource constraint, dependency block) | Yellow badge |
| **COMPLETED** | Delivered, transitioned to BAU operations | Blue/gray badge |
| **FAILED** | Abandoned due to invalidated assumptions or unresolvable blockers | Red badge |
| **DRAFT** | Under development, not yet approved | Outline/dashed badge |

### Governance Rules
- Flag strategies with no status update in 2+ quarters — they may be orphaned
- Strategy Review [SR] workflow should update statuses as part of its Step 1 baseline loading
- VES(Z) catalog uses this as standard metadata for all ~73 strategy entries
