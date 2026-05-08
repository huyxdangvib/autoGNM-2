---
part: 6
name: "VIB Strategy Models & Flywheel"
parent: gnm-instruction.md
---

## S7 Strategy Model → GNM Vertical Decoding

Mô hình chiến lược S7 của VIB ánh xạ trực tiếp sang các cấp độ GNM thông qua **vertical decoding** — giải mã dọc. VIB uses the S7 seven-step strategy model. S7 steps decode vertically through GNM levels — each level is a deeper resolution of the level above.

### The Engine↔Value Gradient (Zone 3 Only)

Zone 3 content follows a gradient — NOT a binary switch between Engines and Values:

| GNM Level | Zone 3 Ratio | Character | S7 Steps | BNW Example |
|-----------|-------------|-----------|----------|-------------|
| **A** (navigation matrix) | ~95% Engines | Strategic scope — defines WHAT domains | Steps 1-3 | 4 geographic segments as Zone 1, Engines→B |
| **B** (cross-concern engines) | ~80% Engines / ~20% Values | Execution engineering — HOW to achieve | Steps 4-5 | Initiative features per segment |
| **C/D** (intermediate) | Adjustable mix — more Values the deeper you go | Operational detail | Steps 5-6 | Sub-initiative decomposition |
| **Z** (terminal) | ~90% Values / ~10% Engines | Measurable targets | Steps 6-7 | Specific revenue/customer targets per region |

> **Key principle:** As you decode from A→Z, the Engine→Value ratio shifts. Strategy-heavy levels carry more Engines (navigation pointers). Execution-heavy levels carry more Values (measurable outcomes). The mix is adjustable based on the resolution needed.

> **Scope:** This gradient applies to **Zone 3 only**. Zones 1, 2, and 4-9 follow their own distinct rules at each level.

### Resolution-Driven Depth

**Core Principle:** Decode until the level resolves the problem. That level is Z (terminal). Z is a role, not a fixed level.

**Default: A→B→Z (3-level).** Deviate only when the Resolution Test demands it:
- **Actionability** — Can the owner act with what's in this cell? YES → stop (terminal).
- **Ambiguity** — Is there meaningful ambiguity? YES → decode deeper.
- **Value-Add** — Would another level help decisions? NO → stop.

**Patterns:** Standard (A→B→Z) | Direct (A→Z) | Deep (A→B→C→Z) | Multi-Navigate (A→A'→B→Z) | Entry-at-B (B→Z) | Dashboard (A only) | Asymmetric (mixed per branch).

**Asymmetric depth is normal:** Within one A-level GNM, different Engines can resolve at different depths. Apply the Resolution Test per-Engine, not per-GNM.

> **VIB-specific only.** This mapping applies to VIB's S7 framework. Non-VIB organizations use different strategy models.

### S7 Full Reference

| # | Step | Phase | Content |
|---|---|---|---|
| 1 | External SWOT | Formulation | Market forces, macro-economic forces, key trends, industry forces & competitors, market opportunities & threats |
| 2 | Internal SWOT | Formulation | Business performance, customer perspectives, operations management, customer management, product & innovation, risk & regulatory, organizational capability |
| 3 | Where we want to go | Formulation | Customer segments, products/services, channels, geography |
| 4 | How to get it | Formulation | Customer perspectives, internal perspectives, organizational capability, risk perspectives → Output: Statement of a Strategy |
| 5 | Strategy selection & business case | Formulation | Vision, targets, business model & business case, list of initiatives |
| 6 | Key initiatives prioritization & implementation | Execution | Ranked, resourced, sequenced execution plan |
| 7 | Monitoring, reporting & control | Control | Real-time tracking, structured reporting, 3 lines of defense (1st: Business units, 2nd: Risk/Compliance, 3rd: Internal Audit) |

---

## VIB 9 Strategic Directions

| # | Direction | Domain | Pillar |
|---|---|---|---|
| 1 | Intensive Lending & Deposit Growth | Revenue / Volume | Growth |
| 2 | Leading Banca & #1 Credit Card | Revenue / Product | Growth |
| 3 | Betting On Transactional Banking | Revenue / Platform | Growth |
| 4 | Great Customer Services | Customer Experience | Productivity |
| 5 | Outstanding Channels | Distribution | Productivity |
| 6 | Effective & Massive Branding | Marketing | Growth |
| 7 | Outstanding IT System & People | Capability | Productivity |
| 8 | Taking Good Care of People | Culture / HR | Productivity |
| 9 | Risk Management & Compliance | Risk | Risk |

**3 Key Pillars:** Growth (D1, D2, D3, D6), Productivity (D4, D5, D7, D8), Risk (D9)

---

## VIB Flywheel Models

### Flywheel 1 — Strategic Growth Engine
Self-reinforcing cycle: Regulatory-aligned Strategy → Pushing (active sales) → Pulling (brand/digital attraction) → Card acquisition & activation → Smart spending competencies (data, loyalty) → reinforces Strategy → repeat.

### Flywheel 2 — Operational Excellence Engine
8-component cycle: Product & Service → Customer Experience → Sales Force → Risk → Sales Platform (163 BR, MyVIB, website) → Operating Model Excellence → Optimal LIR/DIR → Prime → reinvests in Products → repeat.

| Dimension | Flywheel 1 | Flywheel 2 |
|---|---|---|
| Focus | Strategic positioning | Operational execution |
| Time horizon | Medium-long term | Short-medium term |
| Primary driver | Card & spending data | Product quality & NIM |
| S7 connection | Steps 3–4 (Where/How) | Steps 5–6 (Formulation/Execution) |

---

## VIB 10-Phase Product Development Framework (Level B)

Applies to VIB retail banking product GNMs at Level B. Zone 2 Feature Group = the phase that the GNM covers, or a lifecycle perspective spanning multiple phases.

**The 10 phases:**
1. Business Need Identification
2. Product Concept & Design
3. Credit / Risk Policy
4. Pricing & Finance
5. Process & Ops Design
6. Tech & System Configuration
7. Legal / Compliance / Documentation
8. Pilot / UAT
9. Launching
10. Monitoring (+ RACI)

**Scope boundary — this framework is NOT universal:**

| Context | B-Level Features | 10-Phase? |
|---------|-----------------|-----------|
| VIB RB Lending (RBL) | 10-phase product dev | YES |
| VIB RB Deposit (RBF) | 10-phase product dev | YES |
| VIB BNW ACC(B) | Segment-specific features (Lending, Deposit, Card, Banca, Ops) | NO — BNW uses BU-specific |
| KAFI Securities RBB(B) | "Strategy Development" single-feature ⚠️ _legacy f=1_ | NO — securities domain, legacy pattern |
| Uniben FMCG | Different feature structure | NO — FMCG domain |

> **Use only when:** Topic is a VIB retail banking product (RBL, RBF, RBC, RBB, UPL). For all other VIB units and non-VIB organizations, derive B-level features from the specific business context.

---

