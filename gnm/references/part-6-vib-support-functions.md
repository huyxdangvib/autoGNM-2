---
part: 6
name: "VIB Support Function GNM Patterns"
parent: gnm-instruction.md
---

## Support Function GNM Design

> **Core principle:** Don't copy VBM(A) blindly. Each support function must be decoded from first principles — ask "how does the function leader ACTUALLY think?" before choosing a pattern.

### Function Taxonomy — Service vs Control vs Revenue Enabler

| Type | Example | Relationship to BL | Zone 2 Pattern |
|------|---------|---------------------|----------------|
| **Service** (serves BL) | HR | Serves all divisions equally | Business x Function (Listing) |
| **Control** (constrains BL) | Risk | Constrains all divisions independently | Risk Types x Framework (Component) OR Products x BL (Strategy) |
| **Revenue enabler** | MarCom | Drives BL sales pipeline (lopsided) | Acquisition x Engagement (modes) |

**Key distinctions:**
- HR has HRBPs genuinely embedded in business lines (real org units) → mirrors VBM(A)
- Risk officers are extensions of Risk Type COE, not "Risk for Retail" teams → does NOT mirror VBM(A)
- MarCom budget is 80%+ Retail → lopsided business columns, no "TRS Marketing"

### HR Mirrors VBM(A) — CRO Does NOT

- **CHRO ~ mini-CEO for people** — manages all divisions' people needs equally → Business x Function listing works
- **CRO ≠ mini-CEO for risk** — manages risk TYPES, not divisions. Business lines are exposure sources, not customers
- Copying HR's "Business x Function" to Risk misrepresents Risk's independence requirement (OCC 12 CFR 30 App D)

### Two Valid Risk GNMs — Different Owners

| GNM | Owner | Zone 1 | Zone 2 | Purpose |
|-----|-------|--------|--------|---------|
| RSK(A) — Risk Management | CRO | Risk Types | Framework x Oversight | Build the risk management organization |
| CRD(B) — Credit Risk Strategy | CRO/Credit Risk Head | Credit Products | Business Lines (RB, WB, TRS) | Deploy/constrain risk across portfolio |

**BRS(Z) sets targets. RSK(A->B->Z) is the machinery.**

### MarCom — Revenue Enabler Pattern

MarCom is NOT a support function in the traditional sense. Design consequences:
- Business column is lopsided (2 engines: RB Product Marketing + WB Institutional Comms)
- No "TRS Marketing" — interbank relationships are Sales, not MarCom
- B-level for RPM(B) uses **Acquisition x Engagement** as Zone 2 features — the two modes of product marketing
- Each product gets Z-sheets for both lead generation and deepening

MCM(A) uses **Schedule x Strategic Hanging = Hybrid Pattern:**

| Element | Standard Schedule GNM | MCM(A) Hybrid |
|---------|----------------------|---------------|
| Zone 2 | Temporal (Q1-Q4) | Temporal (Q1-Q4) |
| Zone 1 | Flat items | **Hanging** — L1 = strategic modes, L2 = activities |
| Zone 3 | Operational values | Campaign descriptions + KPI targets |

**Parameters:** f=4, L2=1, n=18 → 72-cell matrix serving as both strategy document AND marketing calendar.

**Why hybrid needed:** Pure Schedule loses strategic dimension; pure Strategic loses temporal rhythm. Hybrid gives CMO BOTH "what" (L1 strategic intent) AND "when" (Q1-Q4 columns).

### Symmetric L2 Items Across Strategic Modes

MCM(A) has the SAME 7 activities under BOTH Acquisition AND Engagement & Retention. This is valid because:

| Mode | Mindset | Funding Example |
|------|---------|-----------------|
| **Acquisition** | Hunter — "find new depositors" | Spring Savings Campaign: 8.5% promo, 5K new depositors |
| **Engagement** | Farmer — "deepen existing depositors" | CaSa Activation Sprint: reactivate dormant, 500B balance growth |

**Rule:** Symmetric L2 items across L1 groups are valid when:
1. The content genuinely differs in each group
2. The leader would staff different teams for each
3. Merging them would lose the strategic distinction

### Brand & Awareness — The Non-Product-Linked Leg

MCM(A) has 3 L1 groups but only 2 are product-linked (Acquisition: 7, Engagement: 7). The third:

```
Brand & Awareness (4 items):
  - Performance Branding
  - Intl Standards & Awards
  - Employer Branding
  - Innovation & Digital
```

**Design lesson:** When a strategic mode serves the WHOLE organization rather than product segments, its item count will naturally be smaller. Don't force symmetry.

---

### Decoding Paths for Functions

| Path | Type | Best Level | When |
|------|------|------------|------|
| Employee Lifecycle (Flow) | Flow | B or Z | Inside a specific function (e.g., Talent Acquisition) |
| Capabilities (Component) | Component | A (simple) | Building function from scratch |
| Strategic vs Operational (Classification) | Classification | One-time | CIS Situation Decoding — not a standing GNM |
| Business x Function (Listing) | Listing (Dual) | A | Mature org with HRBP + COE + Shared Services model |
| Risk Types x BL (Component x Strategy) | Component | A->B | Risk function — types at A, BL at B |

Each decoding method finds its right level in the cascade rather than competing at the same level.

---

### VBM <-> Function GNMs Naming Convention

| Position | VBM(A) | HRS(A) | VRS(A) | MCS(A) |
|----------|--------|--------|--------|--------|
| Feature Group | Businesses & Functions strategies (f=2) | Development | Development | (Marcom-specific) |
| Cascade | → HCB(B) → BFC(C) | → HCB(B) → BFC(C) | → CRS(B) → MCS(C) | → SSC(B) → CDO(Z), OMP(C), MOC(B) |
| Z5 Meeting (All) | VMI | — | — | — |
| Z5 Strategies (All) | VES | — | — | — |
| Z7 Goal (All ext) | HAGT(A) → BHT(Z), FHT(Z) | — | — | — |
| Z7 Methodology (All ext) | BFS via GNM(Z) | — | — | — |
| Z9 Org Structure (Common ext) | VOS | — | — | — |
| Z9 External (Common ext) | External stakeholders | — | — | — |

> **Note:** Old naming convention used HRM/RSK. Actual workbook uses HRS/VRS/MCS. MCS code reused at A-level (Marcom) and C-level (Mortgage Credit Risk) — unique per level.

Consistent naming convention across all support functions.

---
