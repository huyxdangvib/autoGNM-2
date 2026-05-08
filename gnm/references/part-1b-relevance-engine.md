---
part: 1b
name: "Strategy Framework Relevance Engine"
parent: gnm-instruction.md
---

<part1b_relevance_engine>

# PART 1b: STRATEGY FRAMEWORK RELEVANCE ENGINE

> **TL;DR:** PART 1b contains the full Strategy Framework Relevance Engine — scoring matrices, level modifiers, zone mapping guide, and worked example. Load for CREATE tasks only. At Step 2.3, silently score 12 framework categories using GNM Type x Level multipliers, surface top 3-5 as recommended frameworks for Zone 1/2/3 content.

> **Purpose:** When building a GNM, automatically determine which strategy frameworks are most relevant to inform Zone 1/2/3 content decisions. This adapts the "Run-All, Curate by Signal" protocol (originated in CIS Innovation Strategy workflow) for GNM zone content selection. GNM's implementation is self-contained — no CIS files are loaded at runtime. The shared intellectual heritage ensures framework scoring consistency when CIS outputs feed into GNM construction.

## Framework Sources

The Relevance Engine draws from 4 framework databases (124 items total: 51 strategy + 35 innovation + 27 value perspectives + 11 business case phases). The GNM Type → Framework Category Relevance Matrix below handles relevance scoring. For the full catalog of individual frameworks per category, see **Part 1c** (`references/part-1c-framework-catalog.md`).

**Framework databases:**
- Strategy Frameworks (51) — strategic_analysis, value_management, governance, operational_excellence, customer_management, capability_building
- Innovation Frameworks (35) — disruption, business_model, market_analysis, strategic, value_chain, technology, execution
- Value Perspectives (27) — Deloitte Value Map + BSC perspectives
- Business Case Phases (11) — BC (Business Case), PC (Product Concept), PS (Product Specification), CR (Credit & Risk Policy), PP (Pricing & Profitability), OP (Operations & Process), IT (IT & Systems), LC (Legal/Compliance/Documentation), PU (Pilot & UAT), LS (Launch Strategy), PM (Monitoring & Variant Readiness)

## GNM Type -> Framework Category Relevance Matrix

At Step 2 (Extract parameters), after identifying the GNM Type and Level, silently evaluate framework relevance using this matrix. Score each category 0.0-1.5 as a relevance multiplier:

| GNM Type | strategic_analysis | value_management | governance | operational_excellence | customer_management | capability_building | disruption | business_model | market_analysis | value_chain | technology | execution |
|----------|-------------------|-----------------|------------|----------------------|-------------------|-------------------|-----------|---------------|----------------|------------|-----------|----------|
| **Business/Product** | 1.3 | 1.0 | 0.5 | 0.7 | 1.5 | 0.8 | 0.7 | 1.2 | 1.3 | 1.0 | 0.8 | 0.5 |
| **Org Responsibility** | 0.7 | 1.2 | 1.5 | 1.0 | 0.5 | 1.3 | 0.3 | 0.5 | 0.3 | 0.7 | 0.5 | 1.2 |
| **Strategy Catalog** | 1.5 | 1.3 | 1.0 | 0.5 | 0.8 | 1.0 | 1.0 | 1.0 | 1.0 | 0.8 | 0.7 | 0.7 |
| **Schedule/Assignment** | 0.3 | 0.5 | 0.7 | 1.5 | 0.3 | 0.8 | 0.0 | 0.0 | 0.0 | 0.5 | 0.3 | 1.5 |
| **Classification/Assessment** | 1.0 | 0.8 | 0.7 | 0.5 | 1.0 | 0.5 | 1.0 | 0.8 | 1.2 | 0.7 | 0.5 | 0.3 |
| **Org Structure** | 0.5 | 0.7 | 1.5 | 0.8 | 0.3 | 1.3 | 0.3 | 0.3 | 0.3 | 0.5 | 0.5 | 0.8 |

## GNM Level -> Framework Depth Modifier

Apply a second multiplier based on GNM Level — higher levels need strategic frameworks, lower levels need execution frameworks:

| Level | strategic x | operational x | execution x | Rationale |
|-------|-----------|--------------|------------|-----------|
| **A** | 1.5 | 0.5 | 0.3 | Level A = navigation, needs strategic framing |
| **B** | 1.0 | 1.0 | 0.7 | Level B = working matrix, balanced |
| **C** | 0.7 | 1.2 | 1.0 | Level C = detailed, needs operational depth |
| **Z** | 0.3 | 1.3 | 1.5 | Level Z = execution, needs KPIs/metrics/targets |
| **Z1** | 0.0 | 1.0 | 1.5 | Level Z1 = data-only, needs execution templates |

> **How to apply:** Final relevance score = (GNM Type multiplier) x (Level modifier for the framework's meta-category). Meta-categories: strategic = strategic_analysis + market_analysis + disruption; operational = operational_excellence + governance + value_chain + customer_management; execution = execution + capability_building + technology.

## Run-All, Curate by Signal (GNM Adaptation)

When executing Step 2 (Extract parameters) for a CREATE task:

1. **Silently scan** ALL framework categories using the relevance matrix above
2. **Score** each category: Type multiplier x Level modifier = final relevance
3. **Surface top 3-5 categories** (score >= 1.0) as "recommended frameworks to consult"
4. **Compress** low-relevance categories (score < 0.5) — do not mention unless user asks
5. **Present** to user: "Based on this GNM's type ({type}) and level ({level}), these frameworks are most relevant for informing content:"
   - For Zone 1 Items: [frameworks that help determine WHAT taxonomy]
   - For Zone 2 Features: [frameworks that help determine TODO dimensions]
   - For Zone 3 Values: [frameworks that help determine content at each intersection]

## Framework -> Zone Mapping Guide

| Framework Category | Zone 1 (WHAT) | Zone 2 (TODO) | Zone 3 (Values) | Zone 4-9 (Engines) |
|-------------------|---------------|---------------|----------------|-------------------|
| **strategic_analysis** | *** Market segments, business units | ** Strategic dimensions | ** Strategic positioning values | *** Sub-GNM for deep analysis |
| **value_management** | ** Value drivers as Items | *** BSC perspectives as Features | *** KPIs, targets, metrics | ** Value tree sub-GNMs |
| **governance** | ** Control domains as Items | *** Governance layers as Features | ** Policies, standards | ** Control framework sub-GNMs |
| **operational_excellence** | *** Processes as Items | *** Process stages as Features | *** SLAs, metrics, status | ** Process sub-GNMs |
| **customer_management** | *** Customer segments as Items | ** Lifecycle stages as Features | *** Segment-specific strategies | ** Segment deep-dive sub-GNMs |
| **capability_building** | ** Capability domains as Items | ** Development dimensions | ** Maturity scores, targets | *** Capability plan sub-GNMs |
| **disruption** | ** Innovation vectors as Items | * Disruption lens | ** Innovation assessment | *** Innovation sub-GNMs |
| **business_model** | *** Business model blocks | ** Revenue/cost dimensions | ** Model parameters | ** BM deep-dive sub-GNMs |
| **market_analysis** | ** Market segments | *** Analysis dimensions | *** Market data, sizing | ** Market sub-GNMs |
| **value_chain** | *** Value chain activities | ** Chain stages as Features | ** Activity assessments | *** Activity sub-GNMs |
| **execution** | ** Initiative portfolio | *** Execution dimensions | *** OKRs, milestones, status | ** Initiative sub-GNMs |

> *** = Primary use (strong fit) | ** = Secondary use (useful) | * = Occasional use (context-dependent)

## Worked Example

**Request:** "Create a Level A GNM for VIB Retail Banking Business strategy"

**Step 2 evaluation:**
- GNM Type: Business/Product -> strategic_analysis=1.3, customer_management=1.5, business_model=1.2
- Level: A -> strategic x 1.5, operational x 0.5, execution x 0.3
- Final scores: strategic_analysis = 1.3 x 1.5 = **1.95**, customer_management = 1.5 x 0.5 = **0.75**, business_model = 1.2 x 1.5 = **1.80**, market_analysis = 1.3 x 1.5 = **1.95**, value_management = 1.0 x 0.5 = **0.50**

**Surface to user:**
"For this Level A Business GNM, the most relevant frameworks are:
- **Zone 1 Items:** Strategic analysis (Five Forces, PESTLE) suggests segmenting by market/competitive position; Customer management suggests segmenting by customer segments (Corporate, SME, FI, Retail)
- **Zone 2 Features:** Business model frameworks suggest Features like Product, Channel, Revenue Model; or PCSS (Product, Customer, Salesforce, Sales Platform)
- **Zone 3 Content:** At Level A, Zone 3 will be predominantly Engines pointing to Level B sub-GNMs per business domain
- **Recommendation:** PCSS-based Zone 1 taxonomy with business domain Features — consistent with VBM(A) pattern"

---

</part1b_relevance_engine>
