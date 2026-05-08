---
part: 3a
name: "Scoring Methodology"
parent: gnm-instruction.md
---

## Zone 3 Scoring Methodology (Z-Level)

> **Purpose:** Provide a standardized scoring protocol for Z-level GNMs that contain quantitative Values. This enables consistent measurement, comparison, and prioritization across Items and Features. Inspired by AHP (Analytic Hierarchy Process) but simplified for GNM's matrix format.

**When to apply:** Only for **Level Z GNMs** where Zone 3 cells contain quantitative or assessment data (KPIs, maturity scores, priority ratings, risk levels).

### Scoring Scales

Choose ONE scale per GNM (all Zone 3 cells in the same GNM use the same scale):

| Scale | Values | Best For | Example |
|-------|--------|----------|---------|
| **RAG** | `[R]` Red, `[A]` Amber, `[G]` Green | Status tracking, compliance | `[G] On track` |
| **1-5 Rating** | 1=Very Low, 2=Low, 3=Medium, 4=High, 5=Very High | Maturity assessment, capability scoring | `4 - High maturity` |
| **Percentage** | 0%-100% | Completion tracking, target achievement | `78% [^3]` |
| **Weighted Score** | Score × Weight = Weighted | Priority ranking, resource allocation | `4 × 0.3 = 1.2` |

### Optional Feature Weighting

When Features (Zone 2) have different importance levels, assign weights in a dedicated weight row:

```
Row 7 (Features):     Product    | Customer   | Channel    | Conso.
Row 7b (Weights):     0.35       | 0.40       | 0.25       | 1.00
```

**Weight rules:**
1. **Weights sum to 1.00** across all Features (excluding Conso.)
2. **Weight row = Row 7b** — inserted between Zone 2 headers (Row 7) and Zone 3 content (Row 8). This shifts all Dynamic Row Formula calculations by +1 — apply as: `n_effective = n`, but content starts at Row 9 instead of Row 8
3. **Conso. column calculates weighted sum:** For each Item, Conso. = Σ(Feature_score × Feature_weight)
4. **Weight row is optional** — if not present, all Features have equal weight (1/f each)
5. **Weight row styling:** Background #DDEBF7 (same as sub-header), italic text
6. **Only for Z-level GNMs** — A/B/C levels use Engines in Zone 3, not scores

### Weighted Conso. Formula

When Feature Weighting is used, the Conso. column for each Item row calculates:

```
Conso. cell = (Feature1_score × w1) + (Feature2_score × w2) + ... + (FeatureN_score × wN)
```

**Example (3 Features, Product w=0.35, Customer w=0.40, Channel w=0.25):**
```
Item: Digital Banking
├── Product score: 4
├── Customer score: 5
├── Channel score: 3
└── Conso. = (4×0.35) + (5×0.40) + (3×0.25) = 1.4 + 2.0 + 0.75 = 4.15
```

**Excel formula pattern:**
```
=G8*G$7b + H8*H$7b + I8*I$7b
```
Where Row 7b contains weights and Row 8+ contains scores.

### Scoring V-gate Extension

When scoring methodology is used, V-gate adds these checks:
- **Scale consistency** — all Zone 3 scored cells use the same scale
- **Weight sum** — if weight row present, weights sum to 1.00 (±0.01 tolerance)
- **Conso. accuracy** — weighted Conso. values match manual calculation

V-gate output addition: `Score[scale:RAG|1-5|%|weighted, wt_sum:1.00]`

> **Relationship to AHP:** Full AHP requires pairwise comparison matrices between criteria — this is too complex for inline GNM. The GNM scoring methodology uses **direct weight assignment** (a simplified AHP approach). For full AHP analysis, create a dedicated Z1-level sub-GNM with pairwise comparison as Zone 3 content.

---

> **End of Core Zones (1-3).** For Zones 4-9 (Horizontal Consolidation, Vertical Consolidation, Common Matters, Internal & External Referral) → see **PART 3b**.

</zone_definitions>

> **📌 Retrieval Signpost:** For styling details (colors, borders, widths) → see PART 4. For formulas & write order → see PART 5. For Zones 4-9 (engine zones) → see PART 3b. For validation checklists → see PART 7. For examples → see PART 7b (core) / PART 7c (extended). For temporal comparison → see Temporal Comparison Pattern (this file). For dependency notation → see Zone 3 Causal Dependency Notation (this file). For scoring methodology → see Zone 3 Scoring Methodology (this file).

---

