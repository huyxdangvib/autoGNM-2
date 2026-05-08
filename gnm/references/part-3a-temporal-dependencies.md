---
part: 3a
name: "Temporal Comparison & Dependencies"
parent: gnm-instruction.md
---

## Situational Decoding Pattern (Special Use Case)

A distinct GNM pattern for classifying/assessing business situations using deep hierarchical classification trees. Applies to ANY Z-level classification/assessment GNM — not limited to SDC-specific sheets. Not a standard CREATE/REVIEW GNM — it is a diagnostic/assessment tool.

**Cascade structure:**
```
SDC(A) → BSD(Z) + RSD(Z)
```
- **SDC (A-level):** Single-Feature "Development". Zone 3 = Engines pointing to Z-level assessment sheets. Each Engine = one assessment type.
- **BSD v2 (Z-level) — Binary Situational Decoding:** 2×2×2 classification (8 archetypes). Zone 1 = Axis 1 (Risk/Return) × Axis 2 (Normative). Zone 2 = Axis 3 (Scale: High/Low). Zone 3 = Values placing business lines in archetypes using v2 descriptive codes (e.g., TRS-L, VIP-D, SME, DPT). See `part-6-vib-patterns-cascade.md` for full 8-archetype table + [INC] overlay + drift detection.
- **RSD (Z-level) — Rich Situational Decoding:** Deep hierarchical classification tree. Zone 1 may have >3 levels (up to 5) when the classification tree requires single-view assessment — see Zone 1 Depth Exception note above and Rule #13 exception in PART 7.

**Example RSD Zone 1 hierarchy (5 levels):**
```
L0: RSD
L1: Performance | Action
L2: Finance | Governance | Business
L3: Organization | Product | Customer | Channel
L4: TOI | Expense | Provision | Acct&Deposit | Lending | Card | Wealth | Digital | Physical
```

**Key rules for classification/assessment GNMs:**
- Zone 1 Binary Decoding = valid for ANY Z-level classification/assessment GNM (see Zone 1 Decoding note above)
- Deep Zone 1 hierarchy (up to 5 levels hard cap) = valid for ANY Z-level classification/assessment GNM
- These exceptions do NOT apply to standard A/B/C level GNMs (see A-level organizational exception below)
- **Depth limits:** Standard GNMs MUST max 3 levels. Classification GNMs MAY use up to 5 levels (hard cap).
- **A-level organizational exception:** A-level GNMs with nested organizational scope (e.g., ONW(A): RB → NPL&WOR → WOR → Secured/Unsecured) MAY use up to 4 levels when the hierarchy reflects genuine organizational nesting. This SHOULD trigger evaluation of splitting into sub-GNMs. Verified in: VBM Excel, ONW(A) sheet.
- Verified in: VIB Situational Decoding workbook (SDC, sheets SDC(A), BSD(Z), RSD(Z), Mar 2026)

---

## Temporal Comparison Pattern (As-Is / To-Be)

> **Purpose:** Enable GNMs to capture temporal state transitions, similar to TOGAF's baseline/target architecture concept. This allows strategic planning that explicitly compares current state with desired future state.

**When to use:** When a GNM needs to show transformation — e.g., organizational restructuring, strategy evolution, capability maturity progression, or any scenario where "where we are" vs "where we want to be" must be clearly distinguished.

### Approach: Paired Sheets

Create paired GNM sheets with identical Zone 1 Items and Zone 2 Features, but different Zone 3 Values/Engines reflecting current vs target state.

**Sheet naming convention:**
```
MãGNM (Level) — standard sheet (default = current/combined view)
MãGNM (Level) [AS-IS] — current state snapshot
MãGNM (Level) [TO-BE] — target state
MãGNM (Level) [DELTA] — gap analysis (optional, Z-level only)
```

| Sheet Type | Zone 3 Content | Use Case |
|-----------|---------------|----------|
| **[AS-IS]** | Current Values, existing Engines | Document current state |
| **[TO-BE]** | Target Values, planned Engines | Define desired future state |
| **[DELTA]** | Gap indicators: `[GAP]`, `[OK]`, `[NEW]`, `[RETIRE]` | Highlight differences between AS-IS and TO-BE |

**Example:**
```
RBB (A) [AS-IS]
├── Zone 3: Current retail banking structure and engines
├── Values reflect current KPIs, current team sizes, current products

RBB (A) [TO-BE]
├── Zone 3: Planned structure with new engines
├── Values reflect target KPIs, target team sizes, new products

RBB (Z) [DELTA]
├── Zone 3 cells use gap tags:
│   [GAP] Revenue per RM: 2.1B → 3.5B (+67%)
│   [OK] NPS Score: 72 → 75 (on track)
│   [NEW] AI-powered lead scoring (not in AS-IS)
│   [RETIRE] Legacy branch workflow (remove by Q4)
```

**Rules for Temporal Comparison:**
1. **Zone 1 and Zone 2 MUST be identical** between [AS-IS] and [TO-BE] sheets — same Items, same Features, same structure
2. **Only Zone 3 content differs** — Values/Engines change to reflect state
3. **[DELTA] sheet is optional** — only create when gap analysis adds value (typically Z-level)
4. **[DELTA] tags:** `[GAP]` = needs improvement, `[OK]` = on track, `[NEW]` = new in TO-BE, `[RETIRE]` = removed in TO-BE
5. **Navigation:** [AS-IS] and [TO-BE] sheets back-link to the standard (combined) parent sheet, not to each other
6. **Back-link formula from temporal sheet:** `=HYPERLINK("#'MãGNM (Level)'!A1", "<<")`
7. **Parent engine link to temporal pair:** Use suffix in display text — `=HYPERLINK("#'RBB (A) [AS-IS]'!B2", "Retail Banking RBB(A) [AS-IS]")`

**Cascade compatibility:** Temporal sheets can exist at any level (A/B/C/Z). A Level A GNM may have temporal variants, and its sub-GNMs can independently have their own temporal variants.

> **When NOT to use:** If the GNM is purely structural (Level A navigation), temporal comparison adds no value. Use temporal comparison primarily for Level B-Z where Zone 3 contains measurable Values or mutable Engines.

---

## Zone 3 Causal Dependency Notation

> **Purpose:** Enable Zone 3 cells to declare dependencies on other GNM elements, allowing readers to understand cause-effect relationships across the matrix. This addresses the gap where BSC Strategy Maps show causal arrows but standard GNMs do not.

**Notation format:** Append a dependency tag after the Value or Engine text in a Zone 3 cell.

```
[DEP: CODE(L)] — This cell depends on the output/completion of ENGINE CODE at Level L
[DEP: CODE(L).Feature] — Dependency on a specific Feature column of another GNM
[DEP: SELF.ItemN] — Internal dependency on another Item within the same GNM
```

**Examples:**
```
Zone 3 cell (Item=Digital Channel, Feature=Development):
"Mobile App Redesign MAR(Z) [DEP: ITS(B)]"
→ Means: Mobile App Redesign depends on IT Systems ITS(B) being in place

Zone 3 cell (Item=NPS, Feature=Target):
"NPS 80+ [DEP: SELF.Training]"
→ Means: NPS target depends on Training item completion within same GNM

Zone 3 cell (Item=Revenue, Feature=Growth):
"15% YoY [DEP: MKS(Z).Digital, CRM(B)]"
→ Means: Revenue growth depends on Digital marketing strategy AND CRM system
```

**Rules for Dependency Notation:**
1. **Optional** — dependency tags are MAY-level, not required
2. **Max 2 dependencies per cell** — if more, the cell is too complex → consider sub-GNM
3. **Format:** `[DEP: ...]` always at END of cell text, after Value/Engine
4. **50-char limit applies to base content** — dependency tag is excluded from the 50-char count
5. **No circular dependencies** — if A depends on B, B MUST NOT depend on A
6. **Cross-sheet dependencies allowed** — reference any Engine in the workbook
7. **V-gate extension:** When dependency notation is used, V-gate adds check: "DEP[no-circular]"
8. **Visual convention (Excel):** Dependency tag text color = #808080 (gray) to distinguish from primary content

**Decision: When to use dependency notation:**

| Scenario | Use Dependency? | Rationale |
|----------|----------------|-----------|
| Level A — navigation GNM | No | Too high-level for causal detail |
| Level B — working matrix | Selective | Only for critical path dependencies |
| Level Z — execution GNM | Yes, recommended | Execution needs clear sequencing |
| Zone 4-9 — Engine zones | No | Engines are references, not causal nodes |

> **Relationship to Strategy Maps:** Dependency notation captures a subset of BSC Strategy Map causality. For full causal modeling, use a dedicated Strategy Map tool alongside GNM — GNM captures WHAT×TODO, Strategy Map captures WHY→HOW.

---

