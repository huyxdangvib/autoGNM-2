# Push-back Triggers — the 8 rules

A "trigger" is a structural error the AI must call out before accepting the user's answer. Each trigger has a deterministic detection check (mechanical) or a soft AI judgement (fuzzy). All triggers route through `pushback-protocol.md`'s 2-step re-confirmation flow when fired.

## Trigger detection types

| Type | Meaning |
|---|---|
| **mechanical** | Regex / range / count check. Always fires when condition is met. Reliable. |
| **fuzzy** | AI judgement against semantics. May miss cases or false-positive. Document this so users don't expect deterministic behavior. |

---

## #1 — Empty Zone 3 cell

- **Type:** mechanical
- **Source:** `gnm/references/part-1-rules-priority.md:13` (Critical Rule #1)
- **Condition:** user leaves a Z3 cell blank when prompted
- **First push-back:** "Every WHAT × TODO intersection must have content — that's GNM Critical Rule #1. What value or engine belongs at *{item}* × *{feature}*?"
- **Counter-questions:**
  1. "If this combination genuinely doesn't apply, type `skip` and I'll record `—`."
  2. "If it applies but you don't know yet, type `…` and we'll come back to it."
- **Override accept:** explicit `skip` records `—` (this is not an override, it's a documented absence).

---

## #2 — Items are verbs, not nouns

- **Type:** mechanical (heuristic)
- **Source:** `gnm/references/part-3a-zone1-body-frame.md:125-138`
- **Condition:** any Zone 1 item starts with a common verb (`Manage|Process|Handle|Run|Execute|Create|Build|Operate|Monitor|Track|...`) or is gerund-form (`-ing`)
- **First push-back:** "*{item}* reads like an action ('Manage X', '...ing'). Zone 1 items are nouns — the WHAT. If you're describing a process, that probably belongs in Zone 2 (TODO)."
- **Counter-questions:**
  1. "What noun does this action act upon? Use that as the item."
  2. "Should we flip the axes — make Zone 1 the noun-objects and Zone 2 the action you're trying to capture?"

---

## #3 — Zone 1 ≡ Zone 2 taxonomy

- **Type:** fuzzy
- **Source:** `gnm/references/part-3a-zone3-value-matrix.md:137-196` (Identity Matrix Pattern)
- **Condition:** items and features draw from the same taxonomy (e.g. both PCSSMR, both lifecycle phases, both BSC perspectives) — AI judges semantic overlap
- **First push-back:** "Your items and features look like the same taxonomy applied twice. That's the Identity Matrix Pattern — valid only when you explicitly want a diagonal-handoff or self-completeness scan."
- **Counter-questions:**
  1. "Is this a deliberate Identity Matrix? If yes, confirm and I'll log it."
  2. "If not, differentiate one axis — keep the WHAT noun-list, pick a new TODO verb-set."

---

## #4 — Single feature at non-trivial level

- **Type:** mechanical
- **Source:** `gnm/references/part-3a-zone2-feature-flow.md:52-73` (CHANGELOG v5.6.0: multi-feature default)
- **Condition:** `f == 1` — single feature is now legacy per v5.6.0
- **First push-back:** "Multi-feature (2–5) is the default. A single feature collapses the TODO axis into one dimension and loses the matrix structure. Why only one?"
- **Counter-questions:**
  1. "What's the natural decomposition? (Lifecycle: Originate → Operate → Monitor; Pillars: Strategy / Execution / Control; BSC; …)"
  2. "If you genuinely want f=1 (deliberate simplification), type `override: f=1` and I'll log it."

---

## #5 — Zone 2 entry is WHAT, not TODO

- **Type:** mechanical (heuristic) + fuzzy
- **Source:** `gnm/references/part-3a-zone2-feature-flow.md:44-48`
- **Condition:** a feature is a noun-product/segment/channel rather than a verb/perspective (e.g. `"Cards"`, `"SME"`, `"Region"`)
- **First push-back:** "*{feature}* is a WHAT noun, not a TODO. Features must be actions or perspectives the matrix rows are *acted upon by*."
- **Counter-questions:**
  1. "What action are you doing to *{feature}*? Use that verb as the feature (e.g. 'Cards' → 'Issuance' or 'Settlement')."
  2. "Or move *{feature}* to Zone 1 and pick a new TODO verb."

---

## #6 — Engine name vague or > 50 chars

- **Type:** mechanical
- **Source:** `gnm/references/part-1-rules-priority.md:18` (Critical Rule #5)
- **Condition:** engine name is in vague-blacklist (`System|Tool|Process|Platform|Framework` standalone) OR length > 50 chars
- **First push-back (vague):** "*{name}* is too generic — engine names must be self-descriptive. What does this engine actually do? (Format: `[Full Name] CODE`, max 50 chars.)"
- **First push-back (too long):** "*{name}* is {N} chars; max is 50. Trim or use a 3-letter code."
- **Counter-questions:**
  1. "Try a noun-phrase: 'Lead Capture Workflow LCW', 'Fraud Detection Engine FDE'."
  2. "If '*{name}*' is the canonical bank-internal label, type `override` and I'll record it."

---

## #7 — Items lack coherent perspective

- **Type:** fuzzy
- **Source:** `gnm/references/part-1-construction-quality.md:30-56` (Q2/Q3 — perspective lock)
- **Condition:** items mix viewpoints (some by-product, some by-customer, some by-phase) — AI judges
- **First push-back:** "Your items mix perspectives — *{item_a}* is a product, *{item_b}* looks like a customer segment, *{item_c}* a phase. Pick one lens for the whole list."
- **Counter-questions:**
  1. "What perspective ties these together? (product / segment / channel / phase / region)"
  2. "Do you want to keep one and split the others into separate sheets?"
- **Note:** This trigger relies on AI judgement and may miss subtle cases. Document this in user-facing copy.

---

## #8 — Item shape obviously degenerate

- **Type:** mechanical
- **Source:** `gnm/references/part-1-construction-quality.md:66-90` (Q9 — Resolution Test)
- **Condition:** `n == 1` (single item — that's a list, not a matrix), or items are all identical strings (parser will catch)
- **First push-back (n=1):** "GNM needs at least 2 items — otherwise it's a list, not a matrix. What other items belong on this axis?"
- **Counter-questions:**
  1. "What would a sibling item look like? (e.g. if 'Inbound' is your only one, 'Outbound' or 'IVR' likely belong here too)"
  2. "If you genuinely have one item, drop a level — describe it inside Zone 2 features instead."

---

## Trigger summary table

| # | Trigger | Type | When |
|---|---|---|---|
| 1 | Empty Z3 cell | mechanical | per-cell during Z3 |
| 2 | Items are verbs | heuristic | Z1.2 |
| 3 | Z1 ≡ Z2 taxonomy | fuzzy | after Z2.2 |
| 4 | Single feature | mechanical | Z2.1 |
| 5 | Z2 entry is WHAT | heuristic+fuzzy | Z2.2 |
| 6 | Vague / long engine | mechanical | per-cell during Z3, Z4, Z5–9 |
| 7 | Mixed perspective | fuzzy | Z1.2 (after listing) |
| 8 | n=1 degenerate | mechanical | Z1.1 |

Triggers 1, 4, 6, 8 are deterministic — fire reliably. Triggers 2, 3, 5, 7 depend on AI judgement against the user's content; calibrate user expectations accordingly in `pushback-protocol.md`.
