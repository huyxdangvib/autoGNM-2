---
part: 6
name: "VIB GNM Patterns & Cascade"
parent: gnm-instruction.md
---

## VIB GNM Type Patterns

Ngoài GNM nội dung chuẩn, VIB Business Model sử dụng các loại GNM đặc biệt tại Z-level:

| Type | Zone 1 | Zone 2 | Zone 3 | Example |
|------|--------|--------|--------|---------|
| **Organizational Responsibility Matrix** | BSC perspectives or work items | Org units (Product, Risk, Legal, Tech) with Action+Dev sub-cols | Specific actions per unit | BAP(Z) |
| **Schedule GNM** | Time periods (weeks, months) | Business domains | Date/time values | RSS(Z) |
| **Team Assignment GNM** | Numbered team slots | Organizational domains | Person names | BAT(Z), RST(Z) |
| **Enterprise Strategy Catalog** | Strategy categories | Domain implementations | Strategy names | VES(Z) |
| **Org Structure Reference** | Numbered org groups | Functional types (Market Facing, Supporting, Governance) | Unit codes/engines | VOS(A) |

> **Note:** These patterns all follow the 9-zone architecture. The key variation is in WHAT (Zone 1) and TODO (Zone 2) interpretation — Zone 1 is not always products/customers; it can be time, org slots, or strategy categories. Zone 2 is not always actions; it can be organizational units or domains.

## GNM Typological Patterns (Production-Derived)

> Source: bod-nextjs production analysis (143 sheets, 2026-03-30)

GNM sheets fall into three types based on **decoding depth** — how many levels have flow/decomposition:

| Type | Decoding at Level 1 | Decoding at Level 2 | Example | When to Use |
|------|--------------------|--------------------|---------|-------------|
| **Listing** | No | No | VBM (board-level navigation, no flows) | Hub/navigation sheets that organize children without adding flow logic |
| **Single Decode** | Yes | No | RBC (strategy at A, then zooms directly to Z) | Domains where one level of flow decomposition is sufficient |
| **Dual Decode** | Yes | Yes | TRS (flow at B, then products at C/Z) | Complex domains needing flow at two organizational levels |

### Type Selection Guide
- **Start with Listing** when the sheet's purpose is purely organizational (hub, board, index)
- **Use Single Decode** when the domain is straightforward: one set of flows drives outcomes directly
- **Use Dual Decode** when different organizational levels need their own flow logic (e.g., division strategy vs product execution)

### Anti-pattern: Type Mismatch
- ❌ Adding Zone 2 flows to a Listing sheet (turns hub into hybrid)
- ❌ Forcing Dual Decode on a simple domain (over-engineering)
- ❌ Using Listing for a sheet that needs Zone 2 flow logic (under-specification)

---

## Cascade Depth Patterns (7 Types)

> Source: VBS Strategy→GNM Mapper workflow (2026-03-30)

GNM cascades follow one of seven depth patterns. Apply the Resolution Test (Q9) at each level gate.

| Pattern | Structure | Frequency (Production) | When to Use |
|---------|-----------|----------------------|-------------|
| **Multi-A Direct** | A→A→Z | **29.5%** (dominant) | Large org narrows scope through multiple A-levels to direct values. Default for VIB. |
| **Multi-A Standard** | A→A→B→Z | **13.6%** | Scope narrowing + execution engineering before measurement |
| **Multi-A Deep** | A→A→B→C→Z | **8.0%** | Complex domains: scope + engineering + tactical before measurement |
| **Z-Cascading** | ...→Z→Z | **28%** (overlay) | Z cascades to sub-Z for deeper measurement. Applies on top of other patterns. |
| **Simple Standard** | A→B→Z | **6.8%** | Single-scope domains with one B-level engineering layer |
| **Direct** | A→Z | **6.8%** | Simple domains, A maps directly to values (e.g., MVB goals) |
| **Operational** | A→A→B→C→D | **1.1%** | Deep operational detail (frontier — NWR domain) |
| **Asymmetric** | Mixed per branch | Common (property) | Different engines resolve at different depths. This is normal — it's a property of any pattern, not a separate pattern. |

> **Note:** Frequencies from production analysis of 143 GNM sheets across 88 cascade paths (01.gnm/gnm-nextjs, Mar 2026). Previous theoretical estimates (~80% Standard) significantly overestimated simple patterns and underestimated Multi-A dominance.

### Depth Selection Decision Tree

```
1. Is this a new or scoped domain?
   ├── New/enterprise scope → Start with Standard (A→B→Z)
   ├── Already scoped by parent → Entry-at-B (B→Z)
   └── Planning only → Dashboard (A only)

2. At each level, apply Resolution Test (Q9):
   ├── Actionability: Can owner act? → Yes: continue
   ├── Ambiguity: Meaningful uncertainty? → Yes: continue
   └── Value-Add: Helps decisions? → Yes: open next level
   If all No → STOP at current depth

3. If enterprise-wide with divisions:
   └── Multi-Navigate (A→A'→B→Z)

4. If standard feels insufficient:
   └── Deep (A→B→C→Z) — but verify C adds real value
```

### Anti-pattern: Uniform Depth
Forcing all engines to the same depth (e.g., everything to A→B→C→Z). Let the Resolution Test determine depth per-engine. Asymmetric depth is the natural outcome of resolution-driven design.

---

## VBM Cascade — Verified Structure

Verified from VIB Business Model Excel workbook (VBM, 25 sheets, Mar 2026):

```
VBM (A) — VIB Business Model GNM (root, 6 items × 2 features)
│
│  Zone 3 col G — Business strategies:
├── RBB (A) — RB Business Selection                    [G8: "RB (RBB)"]
│   └── APT (A) — RB Lending Apartment Strategy        [no cell ref in RBB — implicit cascade]
│       └── BAP (Z) — Basic Apartment Product Dev      [no cell ref in APT — implicit cascade]
├── WB                    (no sub-GNM yet)
├── TRS                   (no sub-GNM yet)
├── ONW (A) — NPL & WOR                               [G11: "NPL & WOR (NWO)"]
│   └── WSS — WOR South                               [J13: "WOR South (WSS)" — no sheet yet]
│
│  Zone 3 col H — Function strategies:
├── HRS (A) — HR Strategy                             [H8: "HR (HRS)"]
│   └── HCB (B) — HR C&B Strategy                     [G10: "C&B (HCB)"]
│       └── BFC (C) — BNW Field Sales C&B              [H8: "RB BNW (BCB)"]
├── VRS (A) — Risk Strategy                            [H9: "Risk (VRS)"]
│   └── CRS (B) — Credit Risk Strategy                 [G8: "Credit risk (CRS)"]
│       └── MCS (C) — Mortgage Credit Risk Strategy    [G8: "Mortgage (MCS)"]
├── BTS                   (placeholder, no sheet yet)
├── MCS (A) — Marcom Strategy                          [H11: "Marcom (MCS)"]
│   ├── SSC (B) — Spring Savings Campaign              [I8: "Spring Savings Campaign (SSC)"]
│   │   └── CDO (Z) — Campaign Dev Overview            [G15: "Campaign dev overview (CDO)"]
│   ├── OMP (C) — OOH Media Planning & Buying          [no formal engine ref — contextual child of MCS(A)]
│   └── MOC (B) — Marcom Org Chart                     [Q30: "Marcom org chart (MOC)"]
├── Finance               (placeholder, no sheet yet)
├── ESD                   (placeholder, no sheet yet)
│
│  All row — Zone 5 (Conso. col I):
├── VMI — Meeting & Interaction                        [I14 — engine only, no sheet]
├── VES (Z) — Enterprise Strategies (10 cat × 9 domains) [I15]
│
│  All row — Zone 7 (extension cols K-L):
├── HAGT (A) — VIB Goal                               [L14: "HAGT (HAGT)"]
│   ├── BHT (Z) — Business HAGT Teams                 [N13: "Biz HAGT teams (BHT)"]
│   └── FHT (Z) — Function HAGT Teams                 [N14: "Func. HAGT teams (FHT)"]
├── GNM (Z) — GNM Examples                            [K15: "GNM (GNM)"]
├── BFS (Z) — B&F Selection Methodology                [L15]
│
│  Common row — Zone 5 (Conso. col I):
├── VOS (A) — Org. Structure                           [I16]
│
│  Common row — Zone 9 (extension cols K-L):
├── External stakeholders                              [K16]
│
│  Standalone sheets (no parent cell ref found):
├── APT (A) — has << backlink, implicit child of RBB
├── BAP (Z) — has << backlink, implicit child of APT (sheet name "1 (Z) (2)")
├── RSS (Z) — RB Strategy Dev Schedule (standalone)
└── RST (Z) — RB Strategy Dev Teams (standalone)
```

> **Cell reference audit (Mar 2026):** All parent→child links verified via engine name patterns "(CODE)" in cells. Backlinks use "<<" in A1. No HYPERLINK formulas in this workbook version. OMP is child of SSC (not MCS directly). RBB→APT and APT→BAP are implicit cascade (no cell refs, only << backlinks). WSS referenced in ONW but has no sheet yet.

---

## BFS Methodology — Business & Function Selection

Meta-GNM mapping GNM levels to strategy scope:

| Level | Org Role | GNM Focus | GNM Levels |
|---|---|---|---|
| **A** | Executive / Division Head | Business Selection & Framing — Decoding GNMs | A-level |
| **B** | Middle Mgmt / SME | Strategy Development & Delivery — Strategy GNMs | B-level |
| **Z** | Field Sales / Branch | Business Implementation — Function/Execution GNMs | Z-level |

**Topic Types by role:**

| Type | Zone 1 Decoding | Zone 2 Decoding | When |
|---|---|---|---|
| Listing | None | None | Larger topics, Level A role |
| Single Decoding | One of Z1 or Z2 | — | Mid-level |
| Dual Decoding | Both Z1 and Z2 | — | Detailed analysis |

**A→B→Z Thinking Layers:**

| If org level is... | Apply... | Cascade depth |
|---|---|---|
| Division Head / C-suite | Level A pattern | Single shared cascade A→Z |
| Regional Head / RGM | Level B pattern | Per-level separate engines |
| Branch Manager / Team Lead | Level Z pattern | Multi-chain, deeper decomposition |

- **Level A**: One unified engine chain — e.g., VBM(A)→RBB(A)→RBL(A) is ONE cascade narrowing scope. Strategic coherence over granularity.
- **Level B**: Each level gets own engines — e.g., creates SEPARATE B-level GNMs per product (Mortgage B, Personal Loan B), each with own 10-phase matrix. Regional autonomy within Level A's direction.
- **Level Z**: Deep decomposition — e.g., works at Z-level with specific numbers: TAT=3 days, target=50 loans/month, NPL≤1.5%. Operational granularity for daily execution.

---

## BSD v2 Banking Situation Archetypes

Updated Mar 2026. Extends v1 (6 archetypes) to v2 (8 archetypes + [INC] overlay).

BSD uses a **3-axis classification** to categorize all VIB banking situations:
- **Axis 1:** Risk/Return profile (High risk high return vs Sustainable)
- **Axis 2:** Normative compliance (Chuẩn mực vs Không chuẩn mực)
- **Axis 3:** Scale (High scale vs Low scale)

| # | Risk/Return | Normative | Scale | v2 Codes | Likely Business Lines | Posture |
|---|---|---|---|---|---|---|
| 1 | High risk high return | Chuẩn mực | High scale | TRS-L, VIP-L, MTG | TRS (large), VIP (lending), Mortgage | Scale with strong risk controls |
| 2 | High risk high return | Chuẩn mực | Low scale | TRS-S, ONW | TRS (small/niche), ONW/NPL recovery | Selective play — optimize, don't scale |
| 3 | High risk high return | Không chuẩn mực | High scale | SME, UPL | SME, Unsecured Personal Lending | Innovate risk models |
| 4 | High risk high return | Không chuẩn mực | Low scale | BNW, NPL | BNW (legacy), NPL (distressed) | Transform or contain |
| 5 | Sustainable | Chuẩn mực | Low scale | HHL | Household/Retail (mass) | Defend and optimize |
| 6 | Sustainable | Chuẩn mực | High scale | VIP-D, ACD | VIP (deposit/CASA), Account & Deposit | Invest and grow |
| 7 | Sustainable | Không chuẩn mực | High scale | DPT | Digital partnerships, BaaS, embedded finance | Pioneer at scale — compliance moat |
| 8 | Sustainable | Không chuẩn mực | Low scale | SBX | Sandbox ventures, pilot programs | Experimental niche — sandbox and learn |

**v2 Changes from v1:**
- Archetypes #7 (Pioneer at Scale) and #8 (Experimental Niche) fill the previously empty Sustainable × Không chuẩn mực quadrant
- Descriptive codes replace ambiguous single-letter codes (e.g., VIP-L vs VIP-D disambiguates lending vs deposit posture)
- **[INC] Incubation Overlay:** Tags pre-revenue or <12-month ventures with additional governance (kill criteria, quarterly review, BCF regulatory gate). Cannot apply to #1 or #6. Expires at 12 months or revenue breakeven.
- **Drift Detection:** Each archetype has drift indicators. When triggered for 2+ consecutive quarters, flags reclassification review via [SR] → [SiD] pathway.

**Usage:** When analyzing a business line's strategic situation, look up its BSD v2 archetype by v2_code for pre-classified diagnostic input. Use descriptive codes (TRS-L, VIP-D, etc.) not legacy single-letter codes.

---

## Situation Decoding GNM Pattern

| Type | Zone 1 | Zone 2 | Zone 3 | Example |
|------|--------|--------|--------|---------|
| **BSD v2** | Situation IDs | Multi-axis classification (risk/return × normative × scale) | v2 archetype codes + [INC] overlay + drift flags | BSD(Z) |
| **RSD** | Domain items | Time-phased assessment (Before/After with Achievement+Challenge) | Achievement/Challenge values | RSD(Z) |

**BSD v2 Zone 3 content:** Each cell contains: archetype number (1-8), v2_code (e.g., TRS-L), [INC] tag if applicable, last_classified date, and drift_flags if any indicator triggered.

**RSD Time-Phased Assessment:** Zone 2 splits into two periods (e.g., Before Jun.25 / After Jun.25), each with Achievement + Challenge sub-columns → creating a **4-column assessment per item**. 18 items total across Performance (Finance), Action (Governance, Business, Channel, Function) domains. Designed to be filled TWICE: retrospective + forward-looking.

---

## Engine Ordinal Index Convention (VIB Legacy)

Some existing VIB GNMs use ordinal indices `(1)`, `(2)` instead of level codes `(Z)`, `(B)` — e.g., `Basic APT product dev. (1)`. This indicates the engine is item #1, #2 in a list. The formal spec requires level codes. When reviewing existing VIB GNMs, map ordinal indices to their actual level.

## Forward-Reference Engines (Valid Intermediate State)

GNM workbooks are built incrementally. An engine in Zone 3 MAY reference a sub-GNM sheet that does not yet exist. This is called a **forward-reference engine** — the HYPERLINK will point to a sheet not yet created.

**VBM evidence:** VBM(A) references 6+ engines (WB, TRS, HR, Risk, BTS, VMI) whose sheets are not present in the workbook. Only RBB, ONW, AIA, VES, VOS, BFS have corresponding sheets. This is a valid state during incremental workbook development — not a structural error.

**Guidelines:**
- Forward-reference engines SHOULD still follow the full Engine format: `[Full Name] CODE (Level)`
- HYPERLINK formulas for missing sheets will produce `#REF!` — this is expected and acceptable during development
- When the workbook is considered "complete," all engines SHOULD have corresponding sheets

---

