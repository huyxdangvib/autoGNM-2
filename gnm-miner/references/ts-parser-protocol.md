---
name: ts-parser-protocol
version: "1.0.0"
parent: SKILL.md
---

# TypeScript GnmSheet Parser Protocol

## Overview

Parses TypeScript `GnmSheet` data files into structured GNM zone data. This protocol treats each `.ts` file as a serialized GNM AST (Abstract Syntax Tree).

## GnmSheet Interface

```typescript
interface GnmCell { text: string; className?: string; style?: Record<string,string>; colspan?: number; href?: string; iframeSrc?: string; dangerousHtml?: string; }
interface GnmRow { className?: string; cells: GnmCell[]; }
interface GnmSheet { id: string; title: string; badge: string; domain: string; minWidth: string; colgroup: string[]; headerCells: GnmCell[]; rows: GnmRow[]; externalLink?: string; }
```

## Row Classification Rules

Rows are classified by their cell classNames:

| Row Type | Detection Rule | Zone Mapping |
|----------|---------------|-------------|
| **Super-header** | First cell has `z-shdr` | Badge row (Row 1) |
| **Zone header** | First data cell has `z-zhdr` | Zone 2 labels (Rows 2-3) |
| **Data row** | Cells contain `z-l0`, `z-l1`, `z-l2` | Zone 1 items + Zone 3 values |
| **All row** | Index cell text = `'All'` | Zone 4-7 (Conso + extensions) |
| **Common row** | First cell text = `'Common'` | Zone 8-9 |
| **Terminator** | Index cell text = `'-'` | End of data |

## Column Classification Rules

Columns are classified by position and colgroup width:

| Column | Position | colgroup Width | Content |
|--------|----------|---------------|---------|
| **Index 1** | 0 | `42px` | Badge or label |
| **Index 2** | 1 | `28px` | Row number |
| **Separator** | 2 | `4px` | Visual divider |
| **Zone 1 (L0)** | 3 | `80px` | Category/Object |
| **Zone 1 (L1)** | 4 | `100px` | Item name |
| **Zone 2-3** | 5..N-3 | `''` (flex) | Features × Values |
| **Separator** | N-2 | `4px` | Visual divider |
| **Common 1** | N-1 | `''` (flex) | Extension col 1 |
| **Common 2** | N | `''` (flex) | Extension col 2 |

**Conso column:** The last flex column before the second separator.

## Zone 2 Feature Extraction

Features are extracted from Row 3 (second z-zhdr row):

```
Row 3 cells[5..N-3] where className includes 'z-zhdr' and style.fontWeight = '600'
→ Each non-empty text = one Feature name
```

**Colspan handling:** When a Row 2 cell has `colspan > 1`, it groups multiple Row 3 features under a temporal or organizational header (e.g., "2026 Q1 Goal & Performance" spanning 4 columns).

## Zone 3 Value Classification

Each `z-l2` cell is classified by content:

| Pattern | Classification | Example |
|---------|---------------|---------|
| Numeric (with commas/dots) | **KPI Value** | `'17,700'`, `'95.06%'` |
| Text with `data-ref` in dangerousHtml | **Cross-reference link** | `'Secured Lending Growth (1.1)'` |
| `'Y'` | **Boolean marker** | Feature applicability |
| `'-'` | **Explicit empty** | Not applicable |
| `''` (empty string) | **Blank** | No data |
| Text with `backgroundColor` | **Traffic-light KPI** | Performance indicator |
| Text with `color: '#dc3545'` | **Negative value** | Red accounting convention |

## Degenerate Sheet Detection

A sheet is **degenerate** if:
1. All colgroup entries are `'4px'` (only separators, no data width)
2. Zero cells with className `z-l2` exist
3. The sheet renders as an empty grid with only badge and headers

Degenerate sheets typically represent Excel charts/images that couldn't be tabularly extracted.

## Hierarchy Metadata Extraction

From `gnm-hub-data.ts`:

```typescript
// Parse these exports:
gnmSubOrder: string[]                           // Display order
gnmSubMeta: Record<string, SubGnmMeta>          // {name, code, sheet, domain}
gnmChildSheets: Record<string, string[]>        // Parent→children
gnmParentSheet: Record<string, string>           // Derived child→parent
```

**Tree building algorithm:**
1. Find root sheets (in gnmSubOrder but NOT in gnmParentSheet)
2. Recursively traverse gnmChildSheets to build tree
3. Annotate each node with depth, domain, and sheet count

## Build Spec Output Format

When extracting to Build Spec (for `/gnm` GENERATE consumption):

```yaml
code: RBC
level: Z
title: "RB+ GOAL & PERFORMANCE 2026"
domain: MF
source: gnm-rbc-1z.ts
items:
  - { l0: "RPC", l1: "Growth", l2: "Lending" }
  - { l0: "", l1: "", l2: "Card & UPL" }
features:
  - { name: "Net Growth", col: 6 }
  - { name: "2026", col: 7, group: "Yearly Goal" }
  - { name: "YoY", col: 8, group: "Yearly Goal" }
values:
  - { row: 1, col: 7, text: "17,700" }
  - { row: 1, col: 10, text: "95.06%", style: { backgroundColor: "#a0cf7e" } }
conso:
  - { row: 1, text: "Secured Lending Growth (1.1)", ref: "rbc-11" }
common:
  - { zone: 7, text: "Goal & Performance (1)", ref: "rbc-1z" }
```
