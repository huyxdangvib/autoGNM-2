---
part: 8
name: "Quality Scorecard"
parent: gnm-instruction.md
---


<part8_quality_scorecard>

# PART 8: GNM QUALITY SCORECARD

> **TL;DR:** Transforms V-gate from binary pass/fail into a 10-dimension gradient scorecard (1-10 each, weighted total). Produces a measurable quality rating for every GNM output. Enables improvement tracking across sessions.

> **When to use:** After V-gate passes (all 10 checks OK), run the Quality Scorecard to produce a gradient rating. If V-gate fails, fix first — scorecard applies to structurally valid GNMs only.


## Scoring Dimensions

| # | Dimension | Weight | What It Measures | Scoring Criteria |
|---|-----------|--------|------------------|------------------|
| 1 | **Structural Integrity** | 0.15 | V-gate 10 checks, row sync, column layout | 10=all pass, -1 per warning, -3 per fail |
| 2 | **Taxonomy Quality** | 0.15 | MECE items, perspective consistency, decoding method | 10=MECE+consistent, 7=mostly MECE, 4=mixed perspectives, 1=chaotic |
| 3 | **Feature Flow** | 0.10 | Features form logical flow, output→input chain | 10=clear flow, 7=partial flow, 4=unrelated list, 1=WHAT in TODO |
| 4 | **Zone 3 Density** | 0.10 | % cells with meaningful content (not just "-") | 10=90%+, 8=70-89%, 6=50-69%, 4=30-49%, 2=<30% |
| 5 | **Engine Naming** | 0.10 | Self-explanatory names, ≤50 chars, full format | 10=all clear, -1 per vague name, -2 per missing format |
| 6 | **Cascade Coherence** | 0.10 | Parent↔Child alignment, no orphans, back-links | 10=all linked, 7=minor gaps, 4=orphan sheets, 1=broken cascade |
| 7 | **Decoding Quality** | 0.10 | Correct decoding method, axis coherence, perspective lock | 10=method+perspective+axes all correct, 7=1 axis weak, 4=wrong method, 1=no decoding logic |
| 8 | **Domain Accuracy** | 0.05 | VIB terms correct, business context appropriate | 10=domain expert, 7=mostly correct, 4=generic, 1=wrong domain |
| 9 | **Scope Appropriateness** | 0.10 | Level matches scope, not too deep/shallow | 10=perfect fit, 7=slightly off, 4=wrong level, 1=scope mismatch |
| 10 | **Actionability** | 0.05 | Can a team USE this GNM to make decisions and execute? | 10=immediately actionable, 7=needs minor clarification, 4=conceptual only |

## Calculation

```
Total Score = Σ (dimension_score × weight)
```

All weights sum to 1.00. Total score range: 1.0 - 10.0.

## Rating Bands

| Score | Rating | Symbol | Meaning |
|-------|--------|--------|---------|
| 9.0 - 10.0 | **Excellent** | ⭐⭐⭐ | Production-ready, world-class |
| 7.0 - 8.9 | **Good** | ⭐⭐ | Solid, minor improvements possible |
| 5.0 - 6.9 | **Adequate** | ⭐ | Functional but notable gaps |
| 3.0 - 4.9 | **Needs Work** | ⚠️ | Significant issues, requires revision |
| 1.0 - 2.9 | **Critical** | ❌ | Fundamental problems, rebuild recommended |

## Output Format

Append after V-gate line:

```
Quality: 8.2/10 ⭐⭐ [Struct:9 Tax:7 Flow:8 Z3:9 Eng:8 Casc:10 Dec:7 Dom:9 Scope:8 Act:8]
```

**Expanded format** (when user requests detail or score < 7.0):

```
## GNM Quality Scorecard

| Dimension | Score | Notes |
|-----------|-------|-------|
| Structural Integrity | 9/10 | All V-gate checks pass |
| Taxonomy Quality | 7/10 | L1 items mix product + function perspective |
| Feature Flow | 8/10 | Clear origination→management flow |
| Zone 3 Density | 9/10 | 17/18 cells filled meaningfully |
| Engine Naming | 8/10 | 1 engine name at 48 chars (borderline) |
| Cascade Coherence | 10/10 | All parent↔child links verified |
| Decoding Quality | 7/10 | Zone 2 "Resources" lacks process framing |
| Domain Accuracy | 9/10 | VIB banking terms correct |
| Scope Appropriateness | 8/10 | Level B appropriate for division scope |
| Actionability | 8/10 | Teams can execute with minor clarification |
| **Total** | **8.2/10 ⭐⭐** | Good — address taxonomy mixing and decoding quality |

**Top improvements:** (1) Separate product and function items into distinct GNMs. (2) Reframe "Resources" feature with clearer process scope (e.g., "Resource Allocation").
```

## Dimension Scoring Rules

### 1. Structural Integrity
- Start at 10
- V-gate warning (non-blocking): -1 each
- V-gate fail (fixed before output): -2 each
- Missing separator column: -1
- Wrong merge range: -2

### 2. Taxonomy Quality
- 10: All items MECE, single perspective, correct decoding method used
- 8-9: MECE with 1 arguable overlap
- 6-7: Mixed perspectives but logically grouped
- 4-5: Multiple perspective violations
- 1-3: Items are random list, no taxonomy logic

### 3. Feature Flow
- 10: Clear sequential flow, each feature output feeds next
- 8-9: Mostly sequential with 1 parallel branch
- 6-7: Logical grouping but no clear flow direction
- 4-5: Unrelated features listed without connection
- 1-3: Features contain WHAT items or are duplicative

### 4. Zone 3 Density
- Count cells with meaningful content (Engine name, Value, Value+Engine)
- Exclude "-" cells from "meaningful" count
- Formula: `meaningful_cells / total_cells × 10`

### 5. Engine Naming
- Start at 10
- Missing full name (code-only like `PSC(B)`): -3 per engine
- Name > 50 chars: -1 per engine
- Vague/generic name: -2 per engine
- Duplicate codes across sheets: -2 per duplicate

### 6. Cascade Coherence
- 10: Every engine links to existing sheet, all back-links work
- 8-9: Forward references noted (sheets not yet created)
- 6-7: 1-2 orphan engines (link to non-existent sheet)
- 4-5: Cascade structure unclear, missing layers
- 1-3: No cascade logic, disconnected sheets
- N/A: Single-sheet GNM → auto-score 10

### 7. Decoding Quality
- Check decoding method matches topic type (Q1 from Construction Quality Layer)
- Check perspective consistency across Zone 1 items (Q2)
- Check axis coherence: Zone 1 items form a logical group, Zone 2 features form a logical group (Q3)
- Zone 1 CAN hold TODO items, Zone 2 CAN hold WHAT items — coherence matters, not noun/verb rigidity
- 10: Correct decoding method, locked perspective, both axes coherent
- -1 per incoherent axis item, -3 for wrong decoding method

### 8. Domain Accuracy
- VIB domain: check against Part 6 terminology and business units
- Banking domain: check standard banking terms
- Generic: check for internal consistency
- 10: All terms match domain, business context correct
- -1 per incorrect term, -3 per fundamentally wrong domain mapping

### 9. Scope Appropriateness
- Level A: Should cover broad scope (division/enterprise), Zone 3 mostly engines
- Level B: Should cover medium scope (department/product line), mixed engines+values
- Level Z: Should cover narrow scope (specific product/KPI), Zone 3 mostly values
- 10: Level perfectly matches topic breadth and Zone 3 content type
- -2 per mismatch (e.g., Z-level with all engines, A-level with detailed values)

### 10. Actionability
- 10: A team member can read this GNM and know exactly what to do
- 8-9: Clear with minor clarification needed
- 6-7: Provides direction but lacks specificity for execution
- 4-5: Conceptual framework only, needs significant translation
- 1-3: Confusing or contradictory, blocks rather than enables action

## Task Integration

| Task Type | Scorecard Behavior |
|-----------|-------------------|
| **CREATE** | Always produce scorecard after V-gate |
| **REVIEW** | Produce scorecard for the reviewed GNM (input) |
| **MODIFY** | Produce before/after scorecard comparison |
| **EXPLAIN** | Skip scorecard (no GNM output) |
| **CONVERT** | Produce scorecard for converted output |
| **CASCADE** | Produce per-sheet scorecard + aggregate |
| **EXPORT** | Include scorecard in JSON metadata |
| **PREVIEW** | Produce scorecard for preview structure |

---

## TypeScript GnmSheet Quality Extension

> Added: v5.6.1 (Mar 2026). Extends scorecard for TypeScript-serialized GNM codebases.

When scoring TypeScript GnmSheet files (via gnm-miner AUDIT), apply these additional rules:

### Modified Dimension Scoring

| # | Dimension | TypeScript Adaptation |
|---|-----------|---------------------|
| 1 | **Structural Integrity** | Check colgroup for data columns (not all 4px separators). Degenerate sheets auto-score 1. |
| 4 | **Zone 3 Density** | Count `z-l2` cells with non-empty text vs total `z-l2` cells. |
| 5 | **Engine Naming** | Check `dangerousHtml` cross-refs for valid `data-ref`/`data-sheet` targets. |
| 6 | **Cascade Coherence** | Verify `gnmChildSheets` mappings resolve to existing sheet IDs in `gnm-sheet-registry.ts`. Check for orphaned sheets (in registry but not in `gnmSubOrder`). |

### Additional TypeScript-Specific Checks

| Check | Rule | Severity |
|-------|------|----------|
| **Degenerate detection** | All colgroup widths are `4px` → zero data columns | FAIL (score=1) |
| **Duplicate detection** | Two sheets with identical content (diff = only id/export) | WARN (score-=2) |
| **Orphan detection** | Sheet in `gnm-sheet-registry.ts` but not in `gnmSubOrder` | WARN (score-=1) |
| **Forward-ref validation** | Hub cells link to non-existent sub-sheets | INFO (per Part 6, valid during dev) |
| **Domain consistency** | Sheet `domain` matches parent's domain in `gnmSubMeta` | WARN if mismatch |

### Aggregate Scoring for Codebase

When scoring an entire TypeScript GNM codebase (not a single sheet):

```
Codebase Score = (Σ sheet_scores / N) × coverage_multiplier
```

Where:
- `N` = total sheet count (excluding degenerate)
- `coverage_multiplier` = `1.0 - (unlinked_hub_items / total_hub_items) × 0.2`
  - Penalizes up to 20% for unlinked BMA hub items

### Task Integration Extension

| Task Type | Scorecard Behavior |
|-----------|-------------------|
| **MINE** | Produce aggregate codebase scorecard |
| **AUDIT** | Produce per-sheet scorecard + aggregate |
| **GAP** | Produce coverage score only (not per-sheet) |

---

> **📌 Retrieval Signpost:** For V-gate checks → see orchestrator (`gnm-instruction.md`). For validation rules → PART 7. For construction quality checks → PART 1 (GNM Construction Quality Layer). For TypeScript parser → `gnm-miner/references/ts-parser-protocol.md`.
