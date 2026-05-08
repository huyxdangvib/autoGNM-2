---
part: 10b
name: "Cascade Interactive Navigation Protocol"
parent: gnm-instruction.md
---

<part10b_cascade_interactive_navigation>

# PART 10b: CASCADE INTERACTIVE NAVIGATION PROTOCOL

> **TL;DR:** Extends Part 10 (Cascade DAG Engine) with interactive navigation capabilities. The DAG engine BUILDS cascades; this protocol NAVIGATES them. Users explore cascade levels through a 6-phase cycle (DIMENSION + 5 per-axis phases) with multi-cascade parallel exploration and AI guidance, retaining full strategic control at every decision gate.

> **When to use:** Any session where the user is exploring, reviewing, or traversing an existing cascade — not building one. Entry points include GNM Navigator [GN], Strategy Review [SR], Strategy→GNM Mapper [GM], or direct user request to "explore" or "navigate" a cascade.

---

## Purpose

Enable users to explore GNM cascades interactively through a repeating 5-phase cycle:

```
LANDSCAPE → PANORAMA → RECOMMEND → CHOOSE → DECODE → (repeat at new level)
```

This protocol treats cascade navigation as a **strategic decision process**, not mechanical traversal. Each level is a decision gate where the user chooses direction, informed by AI but not controlled by it.

**Core principle:** The cascade represents strategic choices that are dynamic based on perspective. Sometimes you need to enumerate everything at high level before committing to a path. Sometimes you need to manually scan the taxonomy to decide which items merit deep-diving. The AI provides recommendations based on context — but the human decides the path.

---

## Phase 0: DIMENSION — Multi-Cascade Axis Selection

**Goal:** Before entering the 5-phase cycle, select WHICH cascade dimensions to explore in parallel. A single strategic question can be examined through multiple lenses simultaneously.

**Input:** User's strategic intent or question
**Output:** Selected cascade dimensions (axes) for parallel exploration

**Why This Phase Exists:** Strategic questions are inherently multi-dimensional. "How do we grow RB lending profitability?" involves Product (what you sell), Segment (who you serve), Risk (what protects margin), Channel (how you distribute), and Funding (what it costs). Exploring only one dimension misses cross-dimensional insights.

### Dimension Identification

AI maps user intent to available cascade dimensions:

```
Your intent: "Grow RB lending profitability"

Available exploration dimensions:
| #  | Dimension   | Cascade Root | Why Relevant              | Relevance |
|----|-------------|--------------|---------------------------|-----------|
| 1  | Product     | RBL-mst      | Direct: lending products  | ⭐⭐⭐     |
| 2  | Segment     | RPB/BBK      | WHO you're lending to     | ⭐⭐⭐     |
| 3  | Risk        | RIS          | NPL impacts profitability | ⭐⭐⭐     |
| 4  | Channel     | MVB/BNW      | HOW you distribute        | ⭐⭐       |
| 5  | Funding     | RBD/TRS      | COF drives NIM            | ⭐⭐       |
| 6  | People      | HRS          | Salesforce capability     | ⭐         |
| 7  | Marketing   | MCS          | Acquisition cost          | ⭐         |

AI suggests: Start with Product + Segment + Risk (top 3).
User: "Yes, and add Channel too."
→ 4 dimensions selected for parallel exploration.
```

### VIB Dimension Mapping

VIB's 9 Directions map directly to cascade dimensions:

| Direction | Dimension | Cascade Root(s) |
|-----------|-----------|-----------------|
| D1 Lending & Deposit Growth | Product + Funding | RBL, RBD, TRS |
| D2 Banca & Credit Card | Product | CPF, RBB |
| D3 Transactional Banking | Product + Channel | MVB |
| D4 Customer Services | Segment + Operations | RPB, BBK, BOF |
| D5 Outstanding Channels | Channel | MVB, BNW |
| D6 Branding | Marketing | MCS |
| D7 IT System & People | People + Technology | HRS |
| D8 People Care | People | HRS |
| D9 Risk & Compliance | Risk | RIS |

### Cognitive Load Limits

| Level | Max Dimensions | What User Sees Per Dimension | Rationale |
|-------|---------------|------------------------------|-----------|
| **DIMENSION phase** (headlines) | **7** | 1-line summary per axis | Miller's Law: 7±2 chunks |
| **PANORAMA** (cross-cascade table) | **5** | 5-6 row comparison per column | Table readability threshold |
| **DECODE** (parallel deep-dive) | **2** | Full zone content per sheet | Deep content requires focus |
| **Recommended sweet spot** | **3** | Balanced depth × breadth | Most questions have 3 primary axes |

### Dimension Tiering

When more than 5 dimensions seem relevant:
1. **Primary** (user-selected, max 3-4): Full PANORAMA + DECODE available
2. **Secondary** (AI-suggested backup, 1-2): PANORAMA visible, DECODE on request
3. **Available** (remainder): Listed in DIMENSION table, explorable if user swaps

### Overflow Protocol
- **>7 relevant dimensions:** Group into meta-categories (e.g., "Revenue dimensions" = Product + Segment + Channel)
- **User selects >5 for PANORAMA:** Warn: "I recommend focusing on 3-4. I'll keep the others available if you want to swap in later."
- **User requests >2 parallel DECODEs:** Sequential: "Let's finish this deep-dive first, then explore the next."

### Dimension Merging

When two dimensions are tightly coupled (their engines overlap), merge them into a single combined dimension:
- **Product × Risk** — pricing must reflect segment risk; explore jointly
- **Channel × Technology** — digital channel IS the technology; merge for efficiency
- **Segment × Marketing** — acquisition strategy is segment-specific; merge when analyzing acquisition

Merged dimensions count as 1 toward cognitive limits.

### Cross-Cascade Synthesis

After parallel LANDSCAPE→PANORAMA cycles, present a unified **Cross-Cascade PANORAMA**:

```
CROSS-CASCADE PANORAMA — "Grow RB Lending Profitability"

              | Product (RBL)     | Segment (RPB/BBK) | Risk (RIS)        | Channel (MVB/BNW)
──────────────|───────────────────|───────────────────|───────────────────|──────────────────
Top Engines   | Net Growth,       | Prime penetration, | NPL prevention,  | Digital adoption,
              | Pricing lever     | Cross-sell ratio   | Early warning    | Branch productivity
──────────────|───────────────────|───────────────────|───────────────────|──────────────────
Key Gap       | Auto loan margin  | MSME under-served  | Business loan NPL| MyVIB lending UX
              | compression       |                    | rising           | incomplete
──────────────|───────────────────|───────────────────|───────────────────|──────────────────
Quick Win     | Reprice personal  | RPB cross-sell     | Tighten BL       | Digital pre-approval
              | loans             | campaign           | scoring model    | flow
──────────────|───────────────────|───────────────────|───────────────────|──────────────────
Direction     | D1 (Lending)      | D4 (Customer)      | D9 (Risk)        | D5 (Channels)
──────────────|───────────────────|───────────────────|───────────────────|──────────────────
Pillar        | Growth            | Productivity       | Risk             | Productivity

💡 CROSS-DIMENSIONAL INSIGHT:
Product gap (auto margin) + Risk gap (BL NPL) share a root cause:
pricing doesn't adequately reflect segment risk. Consider JOINT
exploration of RBL × RIS at B-level.
```

The **INSIGHT** row is where AI adds unique value — identifying patterns that only emerge when viewing multiple dimensions simultaneously. These cross-dimensional connections are hard for humans to spot without side-by-side comparison.

### Post-Synthesis User Options
- "Explore [dimension] deeper" → enter 5-phase cycle for that dimension
- "Merge [X] + [Y] into a combined deep-dive" → fused DECODE
- "Swap in [secondary dimension]" → replace a primary with a secondary
- "Show me more about the insight" → AI elaborates on cross-dimensional connection
- "Add a new dimension" → expand the analysis (within cognitive limits)

### Anti-patterns
- **Forcing all dimensions to same depth** — some dimensions need DECODE, others only need PANORAMA
- **Parallel DECODE of 3+ dimensions** — exceeds cognitive load; sequential is better
- **Skipping DIMENSION phase** — jumping straight to single-cascade exploration misses cross-dimensional insights
- **AI choosing dimensions without showing alternatives** — user must see all available axes

---

## The 6-Phase Navigation Cycle (DIMENSION + 5-Phase)

The full protocol is now:

```
DIMENSION → [per selected axis:] LANDSCAPE → PANORAMA → RECOMMEND → CHOOSE → DECODE
    │                                                        │
    │           Cross-Cascade Synthesis after PANORAMA        │
    │                                                        │
    └── Select N cascade axes ←─────── Swap/add dimensions ──┘
```

---

## The 5-Phase Navigation Cycle (Per Dimension)

### Phase 1: LANDSCAPE — Enumerate All Options

**Goal:** Show the user everything that exists at the current cascade level.

**Input:** Current cascade node (e.g., VBM root, or a specific A-level GNM)
**Output:** Complete sibling list with metadata

**Process:**
1. Query the DAG adjacency list (Part 10) for all children of the current node
2. For each child, extract:
   - Sheet code and display name
   - Level (A/B/C/Z)
   - Domain (MF/BO/SP or VIB business domain)
   - Typological pattern (Listing/Single Decode/Dual Decode — from Part 6)
   - Number of descendants (depth indicator)
   - Zone 3 density (populated vs. forward-reference/empty cells)
   - Status (if tracked in session memory: ACTIVE/PAUSED/COMPLETED/FAILED/DRAFT)
3. Present as enumerated table sorted by domain, then by sheet order

**Presentation Format:**
```
Current Position: [breadcrumb path, e.g., VBM → MF]
Children of [current node] — [N] items across [M] domains:

| # | Code | Name | Level | Domain | Type | Depth | Status |
|---|------|------|-------|--------|------|-------|--------|
| 1 | rbc  | RB Customer Strategy | A | MF | Single Decode | 4 sheets | ACTIVE |
| 2 | cpf  | Card & UPL Strategy | A | MF | Dual Decode | 17 sheets | ACTIVE |
| 3 | trs  | Treasury Strategy | A | MF | Dual Decode | 13 sheets | ACTIVE |
| ... | ... | ... | ... | ... | ... | ... | ... |
```

**Taxonomy Scanning Mode:** When the user wants to explore WHAT items exist across a subtree (not just direct children), expand Zone 1 items from all descendant sheets into a flat taxonomy list. Groups results by cascade branch. Enables the "search taxonomy to decide" navigation pattern — AI-assisted manual scanning.

**Anti-pattern:** Showing only 2-3 "relevant" items at this phase. LANDSCAPE must show ALL children. Filtering happens in RECOMMEND, not here.

---

### Phase 2: PANORAMA — Compare at High Level

**Goal:** Enable meaningful comparison between siblings WITHOUT drilling down.

**Input:** LANDSCAPE output (sibling list)
**Output:** Comparison matrix with key differentiators

**Process:**
1. For each sibling, extract high-level summary:
   - Primary Zone 1 items (WHAT — top 3-5 nouns)
   - Primary Zone 2 features (TODO — top 3-5 actions)
   - Zone 3 engine count (how many levers)
   - Key metrics (if Z-level exists: top 3 KPIs)
   - Strategic alignment (which of 9 Directions / 3 Pillars)
   - Cross-references (Zone 8-9 dependencies)
2. Present as comparison matrix — each column scannable in under 10 seconds

**Presentation Format:**
```
PANORAMA — Comparing [N] siblings at [level]:

| Dimension    | rbc          | cpf                | trs             |
|--------------|--------------|--------------------|-----------------|
| Focus (Z1)   | Retail seg., | Cards, UPL,        | FX, bonds, ALM  |
|              | deposits     | activation         |                 |
| Actions (Z2) | Acq→Serve    | Acq→Activate       | Price→Trade     |
|              | →Retain      | →Spend             | →Settle         |
| Engines (#)  | 12           | 17                 | 9               |
| Key KPIs     | CASA ratio,  | Card activation,   | NIM, COF        |
|              | NTB          | ARPU               |                 |
| Direction    | D1, D3, D4   | D2, D3             | D1 (funding)    |
| Pillar       | Growth+Prod. | Growth             | Growth+Risk     |
| Dependencies | CPF (x-sell),| RBC (cust. base)   | RIS (ALM risk)  |
|              | HRS          |                    |                 |
```

**Scenario Presentation:** When multiple strategic scenarios exist (e.g., conservative vs. aggressive approach), PANORAMA presents them as alternative views of the same cascade:
- Scenario A: "Focus on growth" — highlight D1/D2/D3 branches
- Scenario B: "Focus on risk" — highlight D9/RIS branches
- Scenario C: "Balanced" — all branches with equal weight

**Anti-pattern:** Raw data dumps. PANORAMA must SYNTHESIZE — each column should be human-scannable in 10 seconds.

---

### Phase 3: RECOMMEND — AI-Guided Prioritization

**Goal:** Highlight the most relevant branches based on current context.

**Input:** PANORAMA matrix + user context (query, role, situation)
**Output:** Ranked recommendation list with reasoning and suggested path

**Context Sources for Recommendation:**
1. **User's stated intent** — "I need to understand lending risk" → prioritize RBL, RIS branches
2. **User's role (A-Z level from Part 6)** — Executive (Level A) → strategic A-level GNMs; Branch Manager (Level Z) → Z-level execution GNMs
3. **Current situation** — If coming from SiD (Situation Decoder), use BSD v2 classification (Part 6) to filter relevant branches
4. **Session history** — What has the user already explored? Deprioritize visited nodes
5. **Strategic priority** — Which 9 Directions / 3 Pillars are currently emphasized?
6. **Cross-references** — If exploring RBC, surface CPF (card cross-sell dependency) as contextually linked

**Relevance Scoring:** Apply Part 1b scoring logic — match user intent keywords against Zone 1/2 content of each sibling. Multiply by role-based level modifier (Level A→A-level weight, Level Z→Z-level weight).

**Recommendation Format:**
```
Based on your context: [1-line summary of intent + role + situation]

HIGH RELEVANCE:
  [1] cpf (Card & UPL) — Directly addresses your card activation concern.
      17 descendant sheets, Dual Decode pattern. Start here.
  [2] rbc (RB Customer) — Foundation context for retail strategy.
      12 descendant sheets, Single Decode. Quick overview first.

MODERATE RELEVANCE:
  [3] trs (Treasury) — Funding cost impacts card economics (COF → card pricing).
      Review if cost optimization is a factor.

LOW RELEVANCE (available):
  [4-N] ... listed for completeness

Suggested path: cpf → rbc → trs (if cost angle matters)
```

**Recommendation Principles:**
- Always show ALL options (LANDSCAPE completeness) — just rank them
- Explain WHY each is ranked (traceability)
- Suggest a navigation PATH (sequence), not just individual items
- Respect that the user may disagree — recommendation is input, not directive
- If context is insufficient to rank meaningfully, ask a clarifying question

**Anti-pattern:** Hiding low-relevance options. The user may know something the AI doesn't. Show everything, rank everything.

---

### Phase 4: CHOOSE — User Decision Gate

**Goal:** Capture the user's explicit choice of which branch to explore.

**Input:** RECOMMEND output
**Output:** Selected branch(es) to proceed with

**Interaction Patterns:**
1. **Single selection:** "Let's look at cpf" → proceed to DECODE for CPF
2. **Multiple selection:** "Show me CPF and RBC side by side" → parallel DECODE for both
3. **Override:** "Actually, I want to look at HRS" → user overrides AI recommendation; acknowledge and proceed
4. **Clarification:** "Tell me more about the difference between CPF and RBB" → loop back to PANORAMA with focused comparison between those two
5. **Defer:** "I'll come back to this" → save current breadcrumb to session memory, return to parent level

**Decision Logging (Part 12 integration):**
Record choice in session memory for feedback loop:
- Which node was chosen
- Why (if user stated)
- Which AI recommendations were accepted vs. rejected
- Whether user overrode the recommendation

**Anti-pattern:** Auto-selecting for the user. Even if AI confidence is high, always wait for explicit choice. The cascade represents the user's strategic decision — the AI advises, the user decides.

---

### Phase 5: DECODE — Deep-Dive Selected Branch

**Goal:** Fully render the chosen branch content, then offer to repeat the cycle at the next level.

**Input:** Selected branch from CHOOSE
**Output:** Full sheet content (all zones) + next-level LANDSCAPE offer

**Process:**
1. Load the selected sheet's full content (all 9 zones)
2. Display with:
   - **Breadcrumb:** `VBM → MF → CPF → cpf-mst` (navigable — user can jump to any ancestor)
   - **Zone summary:** Key insights from Zone 1 (WHAT), Zone 2 (TODO), Zone 3 (engines/values)
   - **Cross-references:** Zone 8-9 dependencies highlighted (with sibling nodes they link to)
   - **Depth indicator:** "This sheet has [N] children. Explore deeper?"
3. Apply Q9 Resolution Test (Part 1 Q9) to guide depth recommendation:
   - Actionability: Can the user act on this level's content?
   - Ambiguity: Is there meaningful uncertainty that deeper levels would resolve?
   - Value-Add: Would going deeper help the user's stated intent?
4. Based on Resolution Test result:
   - If children exist AND test suggests value in going deeper:
     → "This sheet has [N] children. LANDSCAPE the next level?"
     → Yes: restart cycle at Phase 1 for this node's children
     → No: stay at current level, offer to go back up or explore a sibling
   - If no children, or test says stop:
     → Offer: go to next sibling, go back up one level, or end navigation

**Navigation Aids:**
- **Breadcrumb** with clickable ancestors (jump to any ancestor level)
- **Sibling arrows** for horizontal navigation (prev sibling | next sibling)
- **Depth meter:** "Level 2 of 4 in this branch"
- **Back to recommendations:** "Return to last RECOMMEND view"

**Anti-pattern:** Auto-drilling to the deepest level. Each level must pause for user decision. The user controls navigation speed and depth — not the AI.

---

## Recursive Navigation Flow (Full 6-Phase)

```
┌──────────────────┐
│    DIMENSION      │ ← Select cascade axes (max 7 headlines)
│  (Phase 0)        │   User picks 3-5 for parallel exploration
└────────┬─────────┘
         │
         ├── Axis 1 ──┐
         ├── Axis 2 ──┼── Parallel LANDSCAPE → PANORAMA per axis
         └── Axis 3 ──┘
                  │
         ┌───────▼────────┐
         │ CROSS-CASCADE   │ ← Unified multi-dimension comparison
         │ SYNTHESIS        │   + cross-dimensional insights
         └───────┬────────┘
                 │
         ┌───────▼────────┐
         │   RECOMMEND     │ ← AI ranks dimensions + branches
         └───────┬────────┘
                 │
         ┌───────▼────────┐
         │    CHOOSE       │ ← User picks dimension(s) to DECODE
         └───────┬────────┘
                 │
         ┌───────▼────────┐
         │    DECODE       │ ← Deep-dive (max 2 parallel)
         └───────┬────────┘
                 │
         Has children?
         ├── Yes → LANDSCAPE next level (single-cascade 5-phase)
         ├── No  → Offer: sibling / back up / swap dimension / end
         └── User: "Swap in [secondary]" → return to DIMENSION
```

**Cognitive funnel:** Wide at DIMENSION (7 axes), medium at PANORAMA (5 columns), narrow at DECODE (2 parallel). The protocol self-regulates information density.

**Depth tracking:** The cycle tracks breadcrumb state per dimension. At any phase, the user can say "go back" to re-enter the cycle at the parent level's LANDSCAPE, "start over" to return to root, or "swap dimension" to return to DIMENSION phase with a different axis selection.

---

## Integration Points

| Phase | Uses From Existing Parts | Reference |
|-------|--------------------------|-----------|
| LANDSCAPE | DAG adjacency list, sheet metadata, typological patterns | Part 10, Part 6 |
| PANORAMA | Zone 1/2/3 definitions, domain model, depth patterns | Part 3a, Part 6 |
| RECOMMEND | Relevance scoring (Type × Level multipliers), A-Z level roles, BSD v2 | Part 1b, Part 6 |
| CHOOSE | Session memory for logging choices and overrides | Part 12 |
| DECODE | Zone rendering, Q9 Resolution Test | Part 3a, Part 1 (Q9) |
| All phases | Breadcrumb state via DAG ancestry traversal | Part 10 |
| All phases | VIB domain keywords for context matching | Part 6 |
| All phases | Session history to avoid re-recommending visited nodes | Part 12 |

---

## Entry Points

Users can enter the navigation cycle from multiple starting points:

| Entry | Starting Node | First Phase |
|-------|--------------|-------------|
| **Fresh start** | VBM root | LANDSCAPE of all top-level domains |
| **From GNM Navigator [GN]** | Classified topic → nearest cascade node | LANDSCAPE of that node's children |
| **From Strategy→GNM Mapper [GM]** | Newly built cascade root | LANDSCAPE of the built structure |
| **From Strategy Review [SR]** | Existing strategy cascade | LANDSCAPE with change indicators |
| **Direct jump** | User specifies a sheet code (e.g., "open cpf") | DECODE of that sheet + offer to LANDSCAPE siblings |
| **Taxonomy search** | User provides topic keywords | Search across Zone 1/2 items → nearest node → LANDSCAPE |

---

## Taxonomy Search Integration

When users say "find everything related to [topic]" or want to manually scan before committing:

1. Search Zone 1 items across ALL sheets in the cascade for keyword matches
2. Search Zone 2 features for related actions
3. Group results by cascade branch (which A-level ancestor contains the match)
4. Present: "Found [N] related items across [M] branches: [list by branch]"
5. Offer LANDSCAPE of the most relevant branch, or PANORAMA comparison of top branches

This supports the "manual taxonomy scan to decide which items to deep-dive" pattern — the user browses the taxonomy, the AI organizes and surfaces matches.

---

## Scenario-Based Navigation

When multiple strategic scenarios shape which branches matter:

| Scenario Type | PANORAMA Behavior | RECOMMEND Behavior |
|---------------|-------------------|-------------------|
| **Conservative vs. Aggressive** | Show both risk profiles side by side | Weight by stated risk appetite |
| **Growth vs. Productivity vs. Risk** | Filter columns by pillar alignment | Recommend by current strategic priority |
| **Short-term vs. Long-term** | Separate by time horizon markers in Zone 3 | Recommend based on urgency stated in context |
| **A-Z Level Role-based** | Highlight sheets relevant to role's level | Weight A-level for Level A, Z-level for Level Z |

---

## Anti-Patterns Summary

| Anti-Pattern | Phase | Why It's Wrong |
|-------------|-------|----------------|
| Filtering in LANDSCAPE | Phase 1 | Hides options — user cannot see the full picture |
| Raw data in PANORAMA | Phase 2 | Not scannable in 10 seconds; defeats comparison purpose |
| Hiding low-relevance in RECOMMEND | Phase 3 | User may have context the AI lacks |
| Auto-selecting in CHOOSE | Phase 4 | Removes user agency; cascade navigation is strategic |
| Auto-drilling in DECODE | Phase 5 | User controls depth; the AI does not |
| Skipping LANDSCAPE for "obvious" paths | Any | Obvious to AI ≠ obvious to user |
| Jumping straight to RECOMMEND | Any | PANORAMA builds shared understanding first |

---

## Future Extensions (Planned)

| Extension | Description | Priority | Depends On |
|-----------|-------------|----------|------------|
| **Reverse Cascade** | Bottom-up navigation: trace from failing Z-level KPI upstream to root cause strategic decision. DECODE runs backwards (Z→C→B→A). | P1 | DAG ancestry traversal (Part 10) |
| **Auto-Distill to EB** | After navigation session, auto-generate Executive Brief [EB] from the path taken — decisions become narrative backbone. | P1 | Session memory (Part 12), EB workflow |
| **Trigger-Based Alerts** | Automated cascade navigation triggered by KPI threshold breaches from [MD] Monitoring Dashboard. | P2 | MD workflow integration (A14) |
| **Time Dimension** | Historical/future cascade comparison — show how a cascade looked N quarters ago vs now vs projected. | P3 | Historical snapshot infrastructure |
| **Collaborative Sessions** | Multi-user cascade navigation with role-filtered views (Level A sees strategic, Level Z sees execution). | P4 | Multi-session state management |

---

> **Retrieval Signpost:** For building cascades (not navigating) → Part 10. For relevance scoring logic → Part 1b. For Q9 Resolution Test → Part 1. For A-Z level role definitions → Part 6. For session logging of navigation choices → Part 12.

</part10b_cascade_interactive_navigation>
