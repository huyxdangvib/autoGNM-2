---
name: quality-audit
version: "1.0.0"
parent: SKILL.md
---

# Quality Audit Protocol — TypeScript GnmSheet

Adapted from GNM Skill Part 7 Pre-Submission Checklist for TypeScript codebases.

## Audit Checks

### Structure Checks (CRITICAL)

| # | Check | Rule | Detection |
|---|-------|------|-----------|
| S1 | **Column layout valid** | colgroup must have flex columns (not all `4px`) | Count `''` entries in colgroup > 0 |
| S2 | **Header rows present** | Must have z-shdr (row 1) + z-zhdr (rows 2-3) | Check first 3 rows' classNames |
| S3 | **Data rows exist** | Must have ≥1 row with z-l0/z-l1/z-l2 cells | Scan for className matches |
| S4 | **All row present** | Must have row where index cell = 'All' | Scan index column |
| S5 | **Common row present** | Must have row where first cell = 'Common' | Scan first column |
| S6 | **Separator columns** | Must have exactly 2 separator columns (4px) | Count `4px` in colgroup = 2 |

### Data Integrity Checks (HIGH)

| # | Check | Rule | Detection |
|---|-------|------|-----------|
| D1 | **Zone 3 density** | z-l2 cells should be > 30% non-empty | Count non-empty z-l2 / total z-l2 |
| D2 | **Cross-ref integrity** | All `data-ref` and `data-sheet` links resolve | Check refs against gnmSubMeta keys |
| D3 | **Badge consistency** | badge field matches z-shdr row badge text | Compare sheet.badge vs rows[0].cells[0].text |
| D4 | **Domain valid** | domain is 'MF', 'BO', or 'SP' | Enum check |
| D5 | **ID format** | id matches `{prefix}-{suffix}` pattern | Regex: `/^[a-z]+-[a-z0-9]+$/` |

### Hierarchy Checks (MEDIUM)

| # | Check | Rule | Detection |
|---|-------|------|-----------|
| H1 | **Registered in order** | Sheet ID exists in gnmSubOrder | Lookup in array |
| H2 | **Has metadata** | Sheet ID exists in gnmSubMeta | Lookup in record |
| H3 | **Parent exists** | If in gnmChildSheets as child, parent sheet exists | Verify parent ID in registry |
| H4 | **No orphans** | Sheet is in registry AND in gnmSubOrder | Cross-check both structures |
| H5 | **No duplicates** | No two sheets share identical content | Content hash comparison |

### Format Checks (LOW)

| # | Check | Rule | Detection |
|---|-------|------|-----------|
| F1 | **Title has level** | title ends with `(A)`, `(B)`, `(C)`, `(Z)`, or `(D)` | Regex: `/\([ABCZD]\)\s*$/` |
| F2 | **minWidth valid** | minWidth is CSS value like '1100px' | Regex: `/^\d+px$/` |
| F3 | **Consistent cell count** | All rows have same number of cells (±colspan) | Compare cell counts |

## Severity Classification

| Level | Criteria | Action |
|-------|----------|--------|
| **FAIL** | Any S1-S6 fails | Sheet is structurally broken — needs rebuild |
| **HIGH** | D1-D5 violation | Data quality issue — needs fix |
| **MEDIUM** | H1-H5 violation | Hierarchy issue — needs wiring |
| **LOW** | F1-F3 violation | Format issue — cosmetic fix |

## Degenerate Sheet Report

When S1 fails (all columns are separators), generate:

```
❌ DEGENERATE: {sheet.id} ({sheet.title})
   Reason: Zero data columns — colgroup = [{widths}]
   Impact: Renders as empty table with badge only
   Fix: Re-extract from source Excel or convert to iframe embed
```

## Duplicate Sheet Report

When H5 detects identical content:

```
⚠️ DUPLICATE: {sheet1.id} ↔ {sheet2.id}
   Diff: Only id and export name differ
   Fix: Remove one from gnmSubOrder, gnmSubMeta, gnmChildSheets, and registry
```

## Audit Output Format

```markdown
## Quality Audit Results

| Sheet ID | S | D | H | F | Status | Issues |
|----------|---|---|---|---|--------|--------|
| rbc-1z | ✅ | ✅ | ✅ | ✅ | PASS | — |
| bbk-111 | ❌ | — | ✅ | ⚠️ | FAIL | S1: zero data columns |
| rpb-10a | ✅ | ✅ | ⚠️ | ✅ | WARN | H5: duplicate of rpb-10 |

Summary: {pass} pass, {warn} warn, {fail} fail out of {total} sheets
```
