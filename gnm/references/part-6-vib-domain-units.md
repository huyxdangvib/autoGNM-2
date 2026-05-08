---
part: 6
name: "VIB Domain Detection & Business Units"
parent: gnm-instruction.md
---


<part6_vib_reference>

# PART 6: VIB BUSINESS REFERENCE

> **TL;DR:** PART 6 chứa VIB domain context — Business Basic Units (Retail/Wholesale/Treasury/Corporate), Level 0→3 hierarchy, GNM Naming Convention, S7→GNM mapping, 10-Phase framework, GNM Type Patterns, 9 Strategic Directions, and Flywheel models. KHÔNG chứa rules — rules nằm ở PART 1 (Critical Rules) và PART 2a/2b.

> **📌 Retrieval Signpost:** For core zones (1-3) → see PART 3a. For engine zones (4-9) → see PART 3b. For validation → see PART 7. For examples → see PART 7b/7c.


## Domain Detection

At the start of any GNM construction task, detect the domain context:
- **VIB indicators**: mentions of VIB, retail banking, lending, deposits, CASA, branches, RB, WB, TRS, BNW, Digital Banking → load Part 6 VIB reference fully
- **Banking indicators** (non-VIB): mentions of bank, credit, loans, interest rate, NIM, NPL, CAR, Basel → load banking-relevant examples, skip VIB-specific references
- **Generic context**: no banking indicators → skip Part 6 entirely, use generic GNM examples only
- Store domain: `domain_context: "vib" | "banking" | "generic"` in GNM metadata

> This detection uses the same domain gate pattern as CIS workflows. VIB-specific content (PCSS MR, BNW GEO, VBM workbook) should only appear when domain_context = "vib". When receiving CIS workflow output as inbound context, the `source_workflow: cis-{code}` field in the Build Spec automatically sets domain_context to "vib".

### VBM Sheet Abbreviation Glossary

| Abbreviation | Full Name | Level | Parent | Description |
|---|---|---|---|---|
| **VBM** | VIB Business Model GNM | A | — (root) | Root index of all VIB business & function strategies |
| **RBB** | RB Business Selection | A | VBM | RB domains (5 items × 3 feats: Product centric, Customer centric, Channel) |
| **APT** | RB Lending Apartment Strategy | A | RBB | Apartment lending (3 items × 3 feats: All segments, Segment 1, Segment n) |
| **ONW** | OVD NPL & Workout | A | VBM | NPL strategy (10 items: BNW/Card/NPL&WOR × Development FG) |
| **HRS** | HR Strategy | A | VBM | HR strategies; f=1 Development; 4 items: Organization, Recruitment, C&B(HCB), L&D ⚠️ _Legacy f=1 — recommend multi-feature (e.g., Growth/Productivity/Risk)_ |
| **HCB** | HR C&B Strategy | B | HRS | HR C&B (6 items × 4 feats: MF HO, Field sales, SP HO, Field SP) |
| **BFC** | BNW Field Sales C&B Framework | C | HCB | Field sales C&B (11 items × 6 feats: SBS, CLP, PB, SI, STI, Super Bonus) |
| **VRS** | Risk Strategy | A | VBM | Risk strategies; f=1 Development; 7 items: Credit(CRS), Operational, Market, Liquidity +3 ⚠️ _Legacy f=1 — recommend multi-feature (e.g., Prevention/Detection/Recovery)_ |
| **CRS** | Credit Risk Strategy | B | VRS | Credit risk (6 items × 4 feats: RB, WB, TRS, Enterprise) |
| **MCS** | Mortgage Credit Risk Strategy | C | CRS | Mortgage credit risk (3 items × 5 product feats: Home purchase, Refinance, Home equity, Under construction, Renovation) |
| **MCS** | Marcom Strategy | A | VBM | Marcom strategies (20 items × 8 feats: Name/Target pairs across modes) |
| **SSC** | Spring Savings Campaign | B | MCS(A) | Campaign (7 items × 11 channel feats: KOL, Social ads, PR, OOH, Events +6) |
| **CDO** | Campaign Dev Overview | Z | SSC | Campaign dev (4 items × 7 feats: Brief, Creative, Assets, Media, Launch, Ops, Reporting) |
| **OMP** | OOH Media Planning & Buying | C | MCS(A) | OOH media (27 items × 9 feats: Billboard, Digital OOH, Transit, Street furniture +5) |
| **MOC** | Marcom Org Chart | B | MCS(A) | Marcom org (12 items × 1 feat: Head of Strategic marketing) |
| **HAGT** | HAGT | A | VBM | VIB Goal framework; FG: Basic prompting + Skills + AI agents (3 items) |
| **BHT** | Business HAGT Teams | Z | HAGT | Business HAGT teams (22 items × 5 feats: Business, AI, GNM, Technology, Governance) |
| **FHT** | Function HAGT Teams | Z | HAGT | Function HAGT teams (28 items × 5 feats: Function, AI&tech, GNM, Technology, Governance) |
| **GNM** | GNM Examples | Z | VBM | GNM examples (12 items × 6 feats: Decoding, To do list, Hanging, Matrix, Flow, Process/Value) |
| **VES** | VIB Enterprise Strategy | Z | VBM | Strategy catalog (10 categories × 9 domains; 73 entries) |
| **BFS** | Business & Function Selection Methodology | Z | VBM | BFS method (3 items × 6 feats: Strategic scope, Visual, Output, Organization +2) |
| **VOS** | VIB Organizational Structure | A | VBM | Org structure; FG: Market Facing + Supporting + Governance; 7 items |
| **VMI** | VIB Meeting & Interaction | Z | VBM | Meeting framework — VBM Zone 5 engine only, no dedicated sheet in workbook |
| **RSS** | RB Strategy Development Schedule | Z | VBM | Strategy schedule (4 items × 4 feats: Apartment, Structured Funding, Card usage, Mortgage PNS) |
| **RST** | RB Strategy Development Teams | Z | VBM | Strategy teams (8 items × 11 feats: Funding, Lending, Card&UPL, Payment, Banca +6) |
| **BAP** | Basic Apartment Product Dev | Z | APT | Org responsibility matrix (29 items × 10 feats, BSC perspectives) |
| **BAT** | Business & AI Teams | Z | — | Team assignment — no sheet in current workbook (may be separate file) |
| **BTS** | Business Technology Strategy | — | VBM | Technology function engine (placeholder, no sheet yet) |
| **VEM** | VIB Enterprise Management | A | — (family root) | Universal cascade anchor for the VEM workbook family (Card Usage, MyVIB, Org Chart, HAGT-meeting). Byte-identical across every VEM-rooted workbook (3/3 confirmed 2026-04-21). B2="VIB ENTERPRISE MANAGEMENT (A)", Z1=[Business strategy, Organization & Function], Z2=[Design & Run, Governance]. |
| **PNS** | Post-launch Solution Scaffold | Z (intended) | cascade-terminal | Universal Z-level terminal placeholder used across the VEM workbook family. **Producer-declared "meant to be linked" (2026-04-21); current 3/3 orphan-in-workbook state = VIOLATION, not convention.** See Part 9 parser B2-suffix check and restructure guidance. |

> **Note:** MCS code used at both A-level (Marcom) and C-level (Mortgage Credit Risk) — not a conflict since GNM codes are unique per level. BCB sheet canonical code = BFC (from B5 cell).

---

## VIB Business Basic Units

Bảng dưới đây thể hiện cấu trúc đơn vị kinh doanh cơ bản của một ngân hàng thương mại quy mô trung (Mid-tier Commercial Bank). Đây là ví dụ thực tế để áp dụng vào Zone 1 của GNM.

| Mã GNM (Level 0) | Business Level 1 | Business Level 2 | Business Level 3 |
|------------------|------------------|------------------|------------------|
| **RBL** | RB | Lending | Mortgage |
| **RBL** | RB | Lending | Auto |
| **RBL** | RB | Lending | Business loan |
| **RBL** | RB | Lending | VP |
| **RBF** | RB | Funding | Smart funding |
| **RBF** | RB | Funding | Dynamic funding |
| **RBC** | RB | Card | Credit card |
| **RBC** | RB | Card | Debit card |
| **RBB** | RB | Banca | Life insurance |
| **RBB** | RB | Banca | Credit life insurance |
| **RBP** | RB | Privilege banking | Priority segment |
| **RBP** | RB | Privilege banking | Premier segment |
| **BBK** | RB | Business banking | TBD |
| **UPL** | RB | UPL | TBD |
| **BNW** | RB | BNW | Branch 1-n |
| **DIG** | RB | Digital | MyVIB |
| **DIG** | RB | Digital | Max Digital bank |
| **DIG** | RB | Digital | Max Super Agent app |
| **WBL** | WB | Lending | Working capital |
| **WBL** | WB | Lending | Medium long term |
| **WBL** | WB | LC upas | - |
| **WBF** | WB | Funding | Current account |
| **WBF** | WB | Funding | Term deposit |
| **WBT** | WB | Transaction | LC |
| **WBT** | WB | Transaction | Bank guarantee |
| **TRA** | TRS | Asset | Lending |
| **TRA** | TRS | Asset | Investment |
| **TRA** | TRS | Asset | Interbank |
| **TRA** | TRS | Asset | Cash & Balance at SBV |
| **TRA** | TRS | Asset | Others |
| **TRL** | TRS | Liability | Interbank |
| **TRL** | TRS | Liability | Market 1 funding |
| **TRL** | TRS | Liability | Others |

### Mapping to Zone 1 GNM

This 4-column structure maps directly to Zone 1:

| Zone 1 Column | Mapping | Example |
|---------------|---------|-------|
| **Level 0 (Cột E)** | Mã GNM (cột đầu tiên trong 7.1) | "WBL", "RBL", "TRA" |
| **Level 1 (Cột F)** | Business Level 2 | "Lending", "Funding", "Asset" |
| **Level 2 (Cột G)** | Business Level 3 | "Working capital", "Mortgage", "Interbank" |

> **Lưu ý:** Business Level 1 (RB, WB, TRS) đã implicit trong Mã GNM. VD: **WBL** = **W**holesale **B**anking **L**ending

### Ví dụ GNM cho WB Lending

```
Level 0 (E)  │ Level 1 (F)      │ Level 2 (G)
─────────────┼──────────────────┼─────────────────
WBL          │ Lending          │ Working capital    ← Row 8
(rỗng)       │                  │ Medium long term   ← Row 9
(rỗng)       │ LC upas          │ -                  ← Row 10
(rỗng)       │ Funding          │ Current account    ← Row 11
(rỗng)       │                  │ Term deposit       ← Row 12
(rỗng)       │ Transaction      │ LC                 ← Row 13
(rỗng)       │                  │ Bank guarantee     ← Row 14
```

### Lưu ý về Taxonomy

Khi sử dụng bảng này trong GNM:

1. **Level 1 -> Level 2 phải đồng chất:** 
   - [x] Lending -> Mortgage, Auto (cùng chiều Product Type)
   - [x] Funding -> Smart funding, Dynamic funding (cùng chiều Product Type)
   - [x] Asset -> Lending, Investment, Interbank (cùng chiều Asset Class)

2. **Business Level 1 (RB, WB, TRS) có thể là:**
   - Object trong Zone 1 (nếu GNM tổng thể ngân hàng)
   - Hoặc đã implicit trong Mã GNM (VD: RBL = Retail Banking Lending)

3. **Khi nào cần Level 2:**
   - Chỉ thêm Level 2 (cột G) khi Level 1 cần chi tiết hóa với ≥2 sub-items có Zone 3 values khác nhau
   - VD: "Digital" cần chi tiết thành MyVIB, Max Digital bank, Max Super Agent app

---

## Production BOD Context — bod-nextjs (Q1.2026)

> Source: Comprehensive mining of `02.vib-projects/08.bod2026/bod-nextjs/` (144 sheets, Mar 2026)

The bod-nextjs project is a **quarterly BOD Meeting snapshot** — not the full VBM workbook. It uses a different code system optimized for the meeting presentation context. Understanding the mapping between VBM canonical codes and BOD production codes is essential for MINE, REVIEW, and CONVERT tasks.

### BOD vs VBM Relationship

| Aspect | VBM Master Workbook | BOD Meeting (bod-nextjs) |
|--------|--------------------|-----------------------|
| **Purpose** | Full enterprise strategy model | Quarterly performance review deck |
| **Root** | VBM(A) — 6 items × 2 features | BMA — BOD Meeting matrix (8 rows × 13 cols) |
| **Scope** | All strategy + org + HAGT + methodology | Performance KPIs + strategy updates per domain |
| **Sheets** | ~25 (VBM workbook) | 144 (across 15 Excel workbooks) |
| **Missing from BOD** | VOS, HAGT, VES, BFS, GNM examples, VMI | Expected — these are methodology sheets, not meeting content |
| **Unique to BOD** | — | BMA hub, per-domain workbooks, KPI Z-level data |

### BOD Production Sheet Prefix Catalog

| Prefix | BOD Code | VBM Equivalent | Domain | Sheets | Source Excel |
|--------|----------|---------------|--------|--------|-------------|
| **BMA** | BMA | — (hub) | — | 1 | GNM-HUB.xlsx |
| **RBC** | RBC | RBB (partially) | MF | 6 | MF-RB-RB Strategy.xlsx |
| **TRS** | TRS | TRS | MF | 14 | MF-TRS-Treasury Strategy.xlsx |
| **WBS** | WBS | WB | MF | 11 | MF-WB-WB Strategy.xlsx |
| **RBL** | RBL | RBL | MF | 7 | MF-RB-RB Lending Strategy.xlsx |
| **BBK** | BBK | BBK | MF | 15 | MF-RB-BB Strategy.xlsx |
| **CPF** | CPF | RBC (card subset) | MF | 15 | MF-RB-Card & UPL Strategy.xlsx |
| **RPB** | RPB | RBP | MF | 13 | MF-RB-Privilege Banking.xlsx |
| **RBD** | RBD | RBF | MF | 7 | MF-RB-Funding Strategy.xlsx |
| **RBB** | RBB | RBB (banca subset) | MF | 9 | MF-RB-Wealth Insurance.xlsx |
| **MVB** | MVB/MBG | DIG | MF | 13 | MF-RB-MyVIB Strategy.xlsx |
| **NWR** | NWR | ONW | BO | 8 | BO-NPL-Workout.xlsx |
| **HRS** | HRS | HRS | SP | 9 | Supporting-Enabler-HR.xlsx |
| **MCS** | MCS | MCS(A) | SP | 2 | Supporting-Enabler-Marcom.xlsx |
| **RIS** | RIS | VRS | SP | 13 | Supporting-Control-Risk.xlsx |

### BOD Hub Matrix (BMA) Structure

BMA is organized as a **domain × pillar** grid, not the VBM's business × function split:

```
BMA Columns:  Object | - | RB | WB | TRS | BO Field | BO HO | Enabler | Control | Tech | Conso. | Common
BMA Rows:     1-8 (strategic pillars) + All + Common
```

**BMA → Sub-GNM Navigation** (14 active links + 3 unlinked):

| Row | MF Columns | BO Columns | SP Columns | Tech Column |
|-----|-----------|-----------|-----------|-------------|
| 1 | RB Strategy→rbc-vbm, WB Strategy→wbs-vbm, TRS Strategy→trs-vbm | NPL & WOR→nwr-bof | HR Strategy→sub-hrs | ⚠️ Tech Master (unlinked) |
| 2 | Card & UPL→cpf-mst | | Marcom→sub-mcs, Risk→sub-ris | ⚠️ CRM (unlinked) |
| 3 | RB Funding→rbd-mst | | | ⚠️ Core banking (unlinked) |
| 4 | RB Lending→rbl-mst | | | |
| 5 | RB Wealth & Ins.→rbb-mst | | | |
| 6 | RB Privilege→rpb-mst | | | |
| 7 | RB Business Banking→bbk-mst | | | |
| 8 | MyVIB→sub-mvb | | | |

**Finance** links to iframe (`/vib-cfo-bod-q1-2026-creative.html`) — no GNM sub-sheets.

### Cascade Depth in BOD Production

BOD uses **Multi-Navigate** patterns with VBM→MST→A→B→C→Z cascades:

| Pattern | Domains Using It | Max Depth |
|---------|-----------------|-----------|
| VBM→MST→A→Z | RBC (6 sheets) | 4 |
| VBM→MST→B→Z | TRS (14 sheets) | 4 |
| MST→A→B→Z | RBL, RBD, RBB | 4 |
| MST→A→B→C→Z | BBK (deepest at 5 levels), RPB | 5 |
| A→B→Z | MVB, HRS, RIS | 3 |
| A→B | MCS (underbuilt) | 2 |
| BOF→A→B→C→Z | NWR | 5 |

### Known Production Gaps (Mar 2026)

| Gap | Type | Status per Part 6 |
|-----|------|-------------------|
| BTS (Tech) — Tech Master, CRM, Core banking | Forward-reference engines | Part 6: "placeholder, no sheet yet" — valid |
| Finance | iframe only | No GNM structure expected — reporting function |
| 7 degenerate sheets (bbk-111/112/113/4, hrs-mps, mvb-541/542) | Zero data columns | Part 7 checklist violations — need re-extraction |
| rpb-10 / rpb-10a | Exact duplicate | Data entry error |
| sub-mst-wb | Orphaned (in registry, not in hierarchy) | Needs wiring or removal |
| MCS underbuilt | Only 1 child (mcs-plc) | Part 6 defines SSC→CDO cascade — not implemented in BOD |

### BOD TypeScript Data Format

bod-nextjs serializes GNM sheets as TypeScript `GnmSheet` objects:

```typescript
interface GnmSheet {
  id: string;        // '{prefix}-{number}' e.g. 'rbc-11'
  title: string;     // sheet display title with level suffix e.g. '(Z)'
  badge: string;     // 3-letter code
  domain: string;    // 'MF' | 'BO' | 'SP'
  minWidth: string;  // CSS min-width
  colgroup: string[]; // column widths
  headerCells: GnmCell[];
  rows: GnmRow[];    // z-shdr + z-zhdr + data + All + Common
}
```

Hierarchy managed in `gnm-hub-data.ts`: `gnmSubOrder` (display order), `gnmSubMeta` (metadata), `gnmChildSheets` (parent→children tree), `gnmParentSheet` (derived reverse lookup).

Navigation managed in `gnm-custom-links.ts`: `cellToSub` (BMA cell → sub-sheet ID), `cellToIframe` (BMA cell → iframe URL), `cellIframeLinks` (sheet-specific cell → URL).

---

