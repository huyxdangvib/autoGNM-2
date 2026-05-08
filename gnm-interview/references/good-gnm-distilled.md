# What makes a "good" GNM — distilled

A condensed reference the interview AI consults to push back well. Distilled from `/gnm` Parts 1, 2a, 3a, 7. Source citations point back to the original files.

## The core axiom

A GNM is a **WHAT × TODO** matrix. WHAT goes on Zone 1 (rows, items, nouns). TODO goes on Zone 2 (columns, features, verbs/perspectives). Zone 3 (the cell matrix) is the byproduct of the intersection — never an independent design choice.

The matrix is a **thinking tool**, not a record. Its purpose is to force the analyst to confront every WHAT × TODO intersection and decide what belongs there. Empty cells defeat the tool's purpose.

## The audience axiom — GNM is a standardized language

A GNM has **no target audience**. It is a *standardized language* designed so that **everyone** in the organization — analyst, executive, engineer, board member — can look at the same artifact and read the same idea. The whole point is universal legibility.

This means:
- Never ask "who is this for?" — the answer is always "everyone, by design".
- Never tailor items/features to a persona — that breaks the standardization.
- Never accept "the operations team will find this useful" as a structural justification — that's a stakeholder argument, not a strategy argument.
- If a GNM only makes sense to one team, it's wrong. Redo the framing.

This axiom is upstream of the framing axiom below: framing must be business-value (universal language) instead of audience or org (single-reader optimization).

## The framing axiom — business value, always

Every GNM is a **strategy tool**. The organizing axes (Zone 1 items, Zone 2 features) must always be framed around **business value / monetization** — how the thing makes money, saves money, reduces risk, or opens new markets.

**Wrong framings (produce documents, not strategy):**
- Audience-based: "who reads this?" → produces a stakeholder map
- Org-based: "which team owns this?" → produces an org chart
- Operational: "what's the tech stack?" → produces a system diagram
- Lifecycle-only: "Plan → Build → Run" → produces a project plan

**Right framing — monetization mechanisms:**
- Items as P&L levers: "Revenue Uplift via Personalization", "Cost Reduction via Automation", "Risk Reduction via Fraud Detection", "New Revenue via AI-as-a-Service"
- Items as revenue-impact areas: "Retail Margin", "Corporate Fee Income", "Treasury NIM", "Risk Capital Release"
- Features as value-creation arcs: "Discover → Activate → Measure → Optimize", "Acquire → Convert → Retain → Expand"

The matrix CONTENT may end up similar across framings, but the FRAMING decides what gets emphasized vs. hidden. Wrong framing produces a chart that *describes* the org. Right framing produces a chart that *exposes the levers* the business can pull.

## Locked decision order

Decisions at higher numbers depend on decisions at lower numbers. **Never skip backward.**

1. **Scope / level** — what part of the bank? what depth? (cascade depth → `level`)
2. **Decode method** — Classification (taxonomy) or Component (structural breakdown)? perspective lock.
3. **Zone 1 (WHAT)** — list the items that share the chosen perspective. Coherent.
4. **Zone 2 (TODO)** — list the features (verbs/perspectives) that produce meaningful intersections.
5. **Zone 3 (cells)** — for each (i, j), decide: Value, Engine, or Value+Engine. No empty.
6. **Zone 4 (Conso)** — per row, the engine that summarizes all features for that item.
7. **Zones 5–9 (Aggregation)** — All-cluster + Common-cluster engines. Optional, drives navigation.

Source: `gnm/references/part-1-system-role.md:132-141`, `part-2a-structure-core.md:18-56`.

## Zone-by-zone rules

### Zone 1 (Items / WHAT)

- Items are **nouns** — products, segments, channels, regions, lifecycle phases (when phases are the noun-substrate).
- All items share **one perspective**. No mixing products with segments with regions. (Trigger #7.)
- Minimum 2 items. n=1 = list, not matrix. (Trigger #8.)
- Typical range 2–7. >9 = consider splitting into a cascade.
- Optional Level-2 sub-grouping (`L2=1`) when items naturally cluster (e.g. Acquisition → {Funding, Lending}).

Source: `gnm/references/part-3a-zone1-body-frame.md:125-138`, `part-1-construction-quality.md:30-56`.

### Zone 2 (Features / TODO)

- Features are **verbs or perspectives** — Origination, Risk, Reporting, Q1/Q2/Q3/Q4, Strategy/Execution/Control, Develop/Operate/Monitor.
- Multi-feature (2–5) is the **default**. Single-feature is legacy. (Trigger #4.)
- Features must NOT be the same taxonomy as items. (Trigger #3 — Identity Matrix Pattern is a deliberate variant; flag explicitly.)
- A feature group header names the TODO axis (e.g. "Operations", "Annual Calendar").
- Features should form a **coherent flow** when ordered: lifecycle (Originate → Operate → Monitor), pillars (Strategy → Execution → Control), temporal (Q1 → Q4).

Source: `gnm/references/part-3a-zone2-feature-flow.md:7-73`, CHANGELOG v5.6.0.

### Zone 3 (Cells / Values / Engines)

- Every (i, j) intersection has content. **No empty cells.** Use `—` for explicit non-applicability.
- Cell content types:
  - **Value** — quantitative or qualitative content (`"15.5%"`, `"Daily"`, `"Lead capture flow"`)
  - **Engine** — a named referent that's elaborated elsewhere (`"Fraud Detection Engine FDE"`)
  - **Value + Engine** — both, separated by line-break
- Engine format: `[Full Name] CODE` or `[Full Name] CODE(Level)`. Max 50 chars.
- Engine names must be self-descriptive — no `"System"`, `"Tool"`, `"Process"`, `"Platform"` standalone. (Trigger #6.)
- A cell may be a HYPERLINK to a sub-sheet (cascade) — rendered as blue underlined text.

Source: `gnm/references/part-3a-zone3-value-matrix.md:7-196`, `part-1-rules-priority.md:13,18`.

### Zone 4 (Conso)

- One consolidated engine per row. The engine that "stands for the whole row" — what aggregates all features for that item.
- Should NOT be identical to any single Z3 cell in that row. If it is, the row is collapsing into a single feature — re-examine.
- Always blue (engine font color `0563C1`).

### Zones 5–9 (Aggregation)

- **Zone 5** — All cluster × feature columns. Engines that aggregate down a feature column across all items. ("All-channel origination ACO".)
- **Zone 6** — All cluster × Conso column. The single overall summary engine. ("Sales Desk Conso SDC".)
- **Zone 7** — All cluster × extended (Mở rộng) columns. Lateral references — strategy hubs, channel mix.
- **Zone 8** — Common cluster × Conso column. Parent / peer reference. The cascade backlink target.
- **Zone 9** — Common cluster × extended columns. Other common-domain references (org chart, budget, etc.).

Aggregation rows are **optional but powerful** — they turn a flat matrix into a navigation hub. MVP allows skipping all of them.

## The 11 Critical Rules (compressed)

| # | Rule |
|---|---|
| 1 | No empty Zone 3 cells |
| 2 | Zone 1 items are nouns, share one perspective |
| 3 | Zone 2 features are verbs/perspectives, ≠ Zone 1 taxonomy |
| 4 | Engine format `[Name] CODE`, ≤ 50 chars, self-descriptive |
| 5 | Multi-feature (f ≥ 2) is the default |
| 6 | Conso engine ≠ any single Z3 cell in the row |
| 7 | Cascade depth is automatic (root=1, child=parent+1) |
| 8 | `is_final=true` ⇒ no further cascade planned beneath |
| 9 | Resolution Test — only deepen if it adds actionability/decision value |
| 10 | Identity Matrix Pattern (Z1 ≡ Z2) is valid only when deliberate |
| 11 | Bilingual: technical terms in English, body in user's language |

Source: `gnm/references/part-1-rules-priority.md`, `part-1-construction-quality.md`.

## Anti-patterns to refuse

| Anti-pattern | Symptom | Correct response |
|---|---|---|
| Verb-items | "Manage Calls", "Process Loans" in Zone 1 | Convert to noun: "Calls", "Loans" |
| WHAT in Zone 2 | "Cards" as feature | Move to Zone 1 or convert to verb ("Issuance") |
| Single feature at depth | f=1 at L2+ | Add features or accept f=1 with explicit override |
| Identity matrix accident | Z1 and Z2 both PCSSMR | Differentiate one axis or declare deliberate Identity Matrix |
| Empty cells | "—" in Zone 3 used as filler | Either fill or mark `skip` with clear reasoning |
| Engine soup | "System", "Tool" everywhere | Rename to specific noun-phrases with codes |
| Mixed perspective | Items mix products/segments/regions | Pick one lens; split rest into separate sheets |

## Practical heuristics for the interviewer

1. **When n is small (2–3), challenge it.** "Is that genuinely the complete set, or are you missing siblings?"
2. **When n is large (>7), challenge it.** "Could these split into a cascade — group items into 2–4 buckets, each becoming a sub-sheet?"
3. **When f=1, always push back.** Multi-feature is default.
4. **When user gives a verb-item, suggest the axis flip.** "Should Zone 1 be the noun-objects of this verb, and Zone 2 be the verb's components?"
5. **When the user is stuck on a cell**, suggest: "Skip with `—` for now and revisit. Sometimes the answer comes once neighboring cells are filled."
6. **For Conso engines**, ask: "What's the one thing this row delivers? What's the engine you'd assign a manager to own?"

## What the AI should NOT do

- Do NOT ask the user structural questions ("how many items?", "list the features"). Those assume the user already knows GNM. Ask domain questions, then propose structure.
- Do NOT silently fix user input. Always surface the rule and let the user choose.
- Do NOT lecture. State rule + cite evidence + 2 alternatives. That's it.
- Do NOT invent VIB-specific business knowledge. The user is the domain expert; the AI is the structure expert. When uncertain on a Z3 cell, ask — don't fabricate.
- Do NOT batch questions. One at a time.
- Do NOT skip the render step. Visual feedback is core to the interview value.

## Propose-then-confirm model

The AI's job is to take domain knowledge from the user and turn it into a structurally-valid GNM. The user should never need to know:

- How many items belong on the WHAT axis
- What "perspective" means
- What a "feature group" is
- How to format an engine name

Instead, the AI:
1. Asks **domain questions** ("who uses this? what's the work?")
2. Self-applies the 8 structural rules to draft a proposal
3. Shows the proposal: *"I'd structure it like this — [items list, perspective, features]. Confirm or change?"*
4. Iterates on user feedback. If user wants something that violates a rule, run 2-step re-confirmation and log a warning.

The AI never asks the user to do its job. The user is responsible for *what's true about the domain*; the AI is responsible for *what's structurally valid*.
