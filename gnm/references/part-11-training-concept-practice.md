---
part: 11
name: "Training: Concept & Practice"
parent: gnm-instruction.md
---


<part11_training_mode>

# PART 11: INTERACTIVE TRAINING MODE

> **TL;DR:** Guided learning experience that bridges elearning content (01.gnm/elearning/) with the GNM skill. Four phases: CONCEPT → PRACTICE → BUILD → REVIEW. Teaches MFM+GNM thinking through Socratic dialogue, not lectures.

> **When to use:** User requests training, learning, tutoring, or uses trigger `/gnm --train`. Also when user demonstrates misunderstanding of GNM concepts in regular usage.


## Activation

**Triggers:**
- Explicit: "teach me GNM", "train me", "I'm new to GNM", `/gnm --train`
- Implicit: Repeated mistakes in Zone 1/2 confusion, WHAT-TODO mixing, level misassignment
- Assessment: "test my GNM knowledge", "quiz me"

**Prerequisite check:** Determine user's current level before starting:

```
Quick Assessment (3 questions):
Q1: "What are the 9 zones of a GNM?" → Tests structural knowledge
Q2: "Given 'đẩy mạnh kết quả tháng này' — how would you decode this into a GNM? What decoding method, what goes in Zone 1, what in Zone 2?" → Tests decoding + axis structuring
Q3: "When do you use Level A vs Level Z?" → Tests level understanding

Scoring:
- 3/3 correct → Skip to Phase 3 (BUILD) or Phase 4 (REVIEW)
- 1-2/3 correct → Start at Phase 2 (PRACTICE)
- 0/3 correct → Start at Phase 1 (CONCEPT)
```

## Phase 1: CONCEPT (Learn the Theory)

**Source:** `01.gnm/elearning/` transcripts (Modules 1-4)

### Module 1 — GNM Introduction
**Key concepts to teach:**
1. GNM = document convention to externalize MFM thinking
2. 4-step decode: (1) chốt phối cảnh → (2) bắt WHAT → (3) đặt vào Zone → (4) check liên kết
3. Core rule: "WHAT rõ chưa đủ — phải Zone rõ"

**Socratic exercise:**
> Give user a vague business statement. Ask them to decode it.
> Example: "Tháng này phải đẩy mạnh kết quả"
> Expected: Identify missing WHAT, propose candidate WHATs, pick a Zone.

### Module 2 — Zones 1-9 Deep Dive
**Key concepts to teach:**
1. Zone 1 = Body Frame (mostly WHAT, sometimes TODO). Zone 2 = Feature Flow (mostly TODO, sometimes WHAT). Zone 3 = Values/Engines.
2. Zone 4-7 = consolidation/common (engine-only)
3. Zone 8-9 = referral (italic)
4. **Axis coherence test:** "Do all items at this level share the same perspective?" for Zone 1. "Do features form a logical structure (flow, list, or components)?" for Zone 2.
5. **Key insight:** Zone 1 CAN hold TODO items (e.g., process steps) and Zone 2 CAN hold WHAT items — what matters is coherence within each axis, not rigid noun/verb separation.

**Socratic exercise:**
> Present 6 items. Ask user to classify each into Zone 1, Zone 2, or Zone 3.
> Example items: "Customer", "Origination", "15% market share", "Sales Platform", "Risk Assessment", "Credit Policy CRP(Z)"
> Follow-up: "Could 'Origination' be in Zone 1 instead of Zone 2? Under what decoding method would that work?"

### Module 3 — A, B, Z Levels
**Key concepts to teach:**
1. Levels control scope and depth, not quality
2. A = navigation (broad scope, engines), B = execution engineering (medium, mixed), Z = data (narrow, values)
3. Rule: A/B/C = engines in Zone 3, Z = values in Zone 3

**Socratic exercise:**
> Describe a business scenario. Ask user to choose the right level.
> Example: "VIB wants to create a strategic overview of all retail banking products"
> Expected: Level A (broad scope, will contain engines pointing to B-level sub-GNMs)

### Module 4 — Functional GNM
**Key concepts to teach:**
1. A-Z Level depth: A=scope (mostly Engines), B=capability (Engines+Values), Z=execution (mostly Values)
2. PCSS framework (Product, Customer, Salesforce, Sales Platform) + extensions
3. Single-A vs Multi-A cascade patterns

### Module 5 — GNM Construction Pipeline
**Key concepts to teach:**
1. The 4-stage pipeline: **DECODE → STRUCTURE → MATRIX → CONTENT**
2. **DECODE (Stage 1):** Choose decoding method (Classification, Component, Binary, Flow). Lock perspective. Single vs Dual decoding.
3. **STRUCTURE (Stage 2):** Build Zone 1 axis + Zone 2 axis — sequential work (like CPU). Zone 1 is mostly WHAT but CAN be TODO. Zone 2 is mostly TODO but CAN be WHAT. What matters is axis coherence.
4. **MATRIX (Stage 3):** Fill Zone 3 intersections — parallel work (like GPU). The matrix reveals all relationships simultaneously. Each cell answers: "what happens when [row] meets [column]?"
5. **CONTENT (Stage 4):** Engine quality, naming discipline, scope-led values, measurable targets.
6. **Fix upstream first:** If the matrix feels wrong, the issue is likely in DECODE or STRUCTURE, not in CONTENT. Cosmetic fixes at Stage 4 don't fix Stage 1 problems.

**Socratic exercise:**
> Present a topic: "VIB Digital Transformation"
> Ask: "Which decoding method would you use? Would Zone 1 hold WHAT or TODO? Walk me through Stage 1 and 2 before we fill any cells."
> Expected: Student identifies that Zone 1 could be initiatives (Classification) or transformation phases (Flow) — and the choice depends on whether the audience needs a roadmap (Flow) or a portfolio overview (Classification).

**Quiz after Phase 1 (must score ≥7/10 to proceed):**
10 multiple-choice questions covering all 5 modules.

## Phase 2: PRACTICE (Apply the Concepts)

### Exercise 2.1: Axis Decoding
```
Scenario: "Cần tối ưu quy trình cho vay mua nhà để giảm thời gian xử lý"
Task: Choose decoding method, then build Zone 1 axis + Zone 2 axis

Approach A (Classification decoding on Zone 1, Flow on Zone 2):
  Zone 1 (WHAT): Mortgage Lending → sub-items: Application, Appraisal, Disbursement
  Zone 2 (TODO): Process Optimization → features: Current State, Bottleneck Analysis, Target State

Approach B (Flow decoding on Zone 1, Component on Zone 2):
  Zone 1 (process steps): Application → Appraisal → Approval → Disbursement
  Zone 2 (assessment dimensions): Current State, Gap, Target

Both are valid — the choice depends on the intended audience and purpose.
Key question: "What perspective is most useful for the reader?"
```

### Exercise 2.2: Zone Placement
```
Given these 8 items, place each in the correct zone:
1. "Customer Segment" → Zone 1 (WHAT item)
2. "Origination" → Zone 2 (TODO feature)
3. "15% NIM target" → Zone 3 (Value, Z-level)
4. "RB Lending Strategy RLS(A)" → Zone 3 or 4 (Engine)
5. "Credit Policy Framework" → Zone 5 or 7 (All/Common engine)
6. "External Audit Liaison" → Zone 9 (External referral)
7. "Product" → Zone 1 (WHAT item)
8. "Risk Assessment Process" → Zone 2 (TODO feature)
```

### Exercise 2.3: Build a Mini Spec
```
Topic: "Coffee Shop Chain Expansion"
Task: Create Zone 1 items (3-5), Zone 2 features (2-3), and suggest Level
AI provides feedback on:
- Decoding method choice (appropriate for the topic?)
- Axis coherence (Zone 1 items share perspective? Zone 2 features form logical structure?)
- Level appropriateness
- Content quality (Zone 3 intersections meaningful?)
```

**Feedback style:** Socratic — ask "why did you choose X?" before correcting.

