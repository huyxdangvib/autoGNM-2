---
name: mine-workflow
version: "1.0.0"
parent: SKILL.md
---

# MINE Workflow — 6-Step GNM Extraction Protocol

## Overview

The MINE workflow extracts GNM data from TypeScript `GnmSheet` codebases, producing structured reports and Build Specs. Designed for projects like bod-nextjs where GNM sheets are serialized as TypeScript data files.

## Prerequisites

- Target directory contains `gnm-*.ts` files following `GnmSheet` interface
- `gnm-sheet-registry.ts` exists (central import map)
- `gnm-hub-data.ts` exists (hierarchy metadata)

---

## Step 1: Discovery

**Goal:** Find all GNM data files and infrastructure files.

**Actions:**
1. Glob for `gnm-*.ts` in target `src/data/` directory
2. Categorize files:
   - **Infrastructure:** `gnm-sheet-registry.ts`, `gnm-hub-data.ts`, `gnm-custom-links.ts`
   - **Data sheets:** All other `gnm-*.ts` files
   - **Sub-boards:** Files matching `gnm-sub-*.ts`
3. Count total files by prefix (e.g., bbk: 15, cpf: 15)
4. Read `package.json` for project context (framework, name)

**Output:** File inventory with counts by prefix.

---

## Step 2: Hierarchy Extraction

**Goal:** Build the complete parent-child tree from hub data.

**Actions:**
1. Read `gnm-hub-data.ts` and extract:
   - `gnmSubOrder` — ordered list of all sheet IDs
   - `gnmSubMeta` — metadata per sheet (name, code, sheet number, domain)
   - `gnmChildSheets` — parent→children mapping
   - `gnmParentSheet` — derived reverse lookup
2. Build tree structure from root (typically `bma-board` or hub sheet)
3. Calculate max depth per branch
4. Identify root entry points (sheets with no parent)
5. Read `gnm-custom-links.ts` for navigation mappings

**Output:** Full hierarchy tree with depth annotations.

---

## Step 3: Content Extraction

**Goal:** Parse each sheet's Zone 1-9 content.

**Actions per sheet:**
1. Parse `GnmSheet` structure: id, title, badge, domain, minWidth
2. Extract column layout from `colgroup` array
3. Parse header rows (z-shdr, z-zhdr) for Zone 2 feature names
4. Parse data rows for:
   - Zone 1: Items from `z-l0`, `z-l1` cells
   - Zone 2: Features from header row 3 (`z-zhdr` with `fontWeight: '600'`)
   - Zone 3: Values from `z-l2` cells (text, style, dangerousHtml)
   - Zone 4: Conso column (second-to-last before separator)
   - Zone 5-9: All/Common rows content
5. Detect data patterns:
   - **KPI sheets:** Cells with numeric values + traffic-light backgroundColor
   - **Strategy boards:** Cells with cross-ref links (`data-ref` or `data-sheet`)
   - **Boolean matrices:** Cells with "Y" markers
   - **Gantt timelines:** Consecutive cells with same backgroundColor
   - **Degenerate sheets:** All columns are 4px separators (no data width)

**Token optimization:** For MINE task, extract summary (row count, column count, data patterns) not full cell-by-cell content. Full extraction only for EXTRACT task on single domain.

**Output:** Per-sheet content summary with pattern classification.

---

## Step 4: Quality Scan

**Goal:** Run Part 7-equivalent checklist against each sheet.

**Actions per sheet:**
1. **Column layout check:** Verify colgroup has data columns (not all 4px separators)
2. **Zone 3 density:** Count z-l2 cells vs total data cells → density percentage
3. **Cross-reference integrity:** Verify all `data-ref` and `data-sheet` links resolve to existing sheet IDs
4. **Header consistency:** Verify z-shdr → z-zhdr → data row structure
5. **All/Common sync:** Verify All row exists and Common footer row exists
6. **Duplicate detection:** Compare sheets by content hash for exact duplicates

**Severity classification:**
- **FAIL:** Zero data columns (degenerate), exact duplicate
- **WARN:** Zone 3 density < 30%, broken cross-references
- **INFO:** Missing Conso content, sparse navigation boards

**Output:** Quality audit table with per-sheet pass/warn/fail.

---

## Step 5: Gap Detection

**Goal:** Compare extracted hierarchy against GNM/MFM knowledge (Part 6).

**Actions:**
1. Load `/gnm` skill's Part 6 VBM cascade as reference
2. Compare:
   - Hub items that have no sub-sheet links (forward-reference engines)
   - Domains present in Part 6 but missing from codebase (e.g., BTS, Finance)
   - Cascade depth patterns vs Part 6 expected patterns
   - Support function taxonomy (Service/Control/Revenue Enabler) compliance
3. Cross-reference domain coverage matrix
4. Identify orphaned sheets (in registry but not in hierarchy)
5. Flag degenerate sheets per Part 7 standards

**Output:** Gap analysis with severity ratings and Part 6 cross-references.

---

## Step 6: Report Generation

**Goal:** Produce the final mining report and optional Build Specs.

**Report structure:**
```markdown
# GNM Comprehensive Mining Report — {Project Name}
## 1. Project Overview (table: total sheets, hub, domains, source files)
## 2. Architecture (9-zone grid description)
## 3. Domain Inventory (MF/BO/SP breakdown with sheet counts)
## 4. Hub Structure (BMA or root board matrix)
## 5. Hierarchy Tree (full ASCII tree)
## 6. Content Patterns (data types, zone usage, styling)
## 7. Key KPI Data (top-level metrics from Z-level sheets)
## 8. Cross-References (navigation links, iframe embeds)
## 9. Infrastructure Files (registry, hub data, custom links)
## 10. Quality Audit Results (pass/warn/fail per sheet)
## 11. Gap Analysis (cross-referenced with Part 6)
## 12. Summary Statistics
## 13. Unresolved Questions
```

**Build Spec output** (optional, for EXTRACT task):
```yaml
code: {BADGE}
level: {A|B|C|Z}
title: {TITLE}
domain: {MF|BO|SP}
items: [{name, level, children}]
features: [{name, type}]
values: [{row, col, text, style}]
```

**File naming:** `plans/reports/gnm-mining-{YYMMDD}-{HHMM}-{slug}.md`

---

## Parallelization Strategy

For large codebases (100+ sheets):
- **Step 1-2:** Single agent (infrastructure files are small)
- **Step 3:** Parallelize by domain prefix — one agent per prefix
- **Step 4:** Can run alongside Step 3 per-sheet
- **Step 5:** Single agent (needs full hierarchy context)
- **Step 6:** Single agent (needs all prior outputs)

**Token budget per agent:** ~50K for discovery + hierarchy, ~30K per domain extraction.

---

## Round-Trip Validation (Optional Step 7)

When Build Specs are generated:
1. Feed Build Spec to `/gnm` GENERATE → produces Excel
2. Run `extract-gnm-to-ts.py` on Excel → produces new TypeScript
3. Diff original TypeScript vs regenerated TypeScript
4. Report any data loss or transformation errors

This validates the full pipeline: TypeScript → Build Spec → Excel → TypeScript.
