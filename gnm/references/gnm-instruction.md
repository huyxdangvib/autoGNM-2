---
name: gnm-builder
description: GNM/MFM Excel strategy template builder. Trigger on GNM, MFM, WHAT-TODO, 9-zone, Excel strategy matrix, Engine format, zone placement, VIB strategy visualization, GNM training, GNM preview. Vietnamese triggers: "bảng GNM", "ma trận WHAT-TODO", "bảng phân tích chiến lược", "bảng chiến lược kinh doanh". Actions: create, review, modify, explain, convert, delete/archive, preview, diff, train, export.
version: "5.13.0"
author: VIB Strategy Office
updated: 2026-04-21
model_target: Claude Opus 4+
structure: multi-file (19 parts)
gnm_root: "references"
deployment: skill
language_policy: "Bilingual by design — English for technical terms (Zone, Engine, Value, Level, Conso.) + Vietnamese for explanations and user-facing output."
---

> **Directory convention:** All part files live in `references/` alongside this orchestrator. Each part may have multiple sub-files — load all `part-N-*.md` for a given part number.

# GNM Excel Builder — Orchestrator

> System prompt specification for Claude to assist with GNM creation and validation.
> Load this file + `gnm-instruction-layer.md` first, then parts per Task-Type Matrix.

---

## Part Catalog

20 parts across 57 sub-files. Load all `part-N-*.md` for a given part number.

| Part | File(s) | Content | When to Load | Tokens |
|------|---------|---------|--------------|--------|
| **Orch.** | `gnm-instruction.md` | Loading protocol, task matrix | Always | ~2,500 |
| **Layer** | `gnm-instruction-layer.md` | Role, thinking, V-gate, responses | Always | ~2,000 |
| 1 | `part-1-*.md` (5) | Identity, thinking, rules, quality | Always | ~6,100 |
| 1b | `part-1b-relevance-engine.md` | Framework relevance | CREATE only | ~1,940 |
| 1c | `part-1c-*.md` (2) | Framework catalog — 124 items | CREATE only | ~3,500 |
| 2a | `part-2a-structure-core.md` | Dynamic Row, Column Layout, Zone Headers | CREATE/MODIFY/CONVERT | ~2,500 |
| 2b | `part-2b-*.md` (3) | Visual Templates, Section Details | Defer to Excel output | ~7,000 |
| 3a | `part-3a-*.md` (6) | Core Zones 1-3, Temporal, Scoring | Most tasks | ~9,000 |
| 3b | `part-3b-*.md` (2) | Engine & Referral Zones 4-9 | On-demand | ~4,500 |
| 4 | `part-4-*.md` (2) | Colors, borders, positioning | Defer to Excel output | ~6,240 |
| 5 | `part-5-*.md` (7) | Formulas, formats, write order, export, markdown | CREATE/MODIFY/CONVERT/EXPORT | ~4,200 |
| 6 | `part-6-*.md` (6) | VIB business context, domain | If VIB domain | ~3,067 |
| 7 | `part-7-*.md` (2) | Mistakes, checklist, validation | Always | ~2,200 |
| 7b | `part-7b-*.md` (3) | 5 Core few-shot examples | Always | ~5,800 |
| 7c | `part-7c-*.md` (7) | 8 Extended examples | Specialized tasks | ~8,200 |
| 8 | `part-8-quality-scorecard.md` | 10-Dimension Quality Scorecard | PREVIEW/DIFF/post-V-gate | ~2,500 |
| 9 | `part-9-*.md` (3) | GNM Excel Parser Protocol | REVIEW/DIFF | ~3,000 |
| 10 | `part-10-cascade-dag-engine.md` | Cascade DAG Engine | CASCADE | ~2,000 |
| 11 | `part-11-*.md` (2) | Interactive Training Mode | TRAIN | ~2,000 |
| 12 | `part-12-session-memory.md` | Session Memory & Feedback Loop | Cross-session | ~1,000 |
| 13 | `part-13-excel-generation.md` | Excel canonical styles, HYPERLINKs | Defer to Excel output | ~500 |
| 14 | `part-14-excel-generation-playbook.md` | Consolidated Excel playbook + Build Spec | GENERATE task only | ~3,000 |

---

## Loading Protocol

> **Path resolution:** All part files live in `references/`. Resolve as `references/part-N-name.md`.

### Always Load (every task)
- **Orchestrator** + **Instruction Layer** — always loaded first
- **Part 1** — System role, thinking process, critical rules
- **Part 7** — Validation checklist (consult before ANY output)
- **Part 7b** — 5 Core Few-Shot Examples (consult before ANY output)

### Task-Type Loading Matrix

| Task Type | Always | + Load | + If VIB domain | + On demand |
|-----------|--------|--------|-----------------|-------------|
| **CREATE** | 1, 2a, 7, 7b | 1b, 1c, 3a, 5 | 6 | 2b, 3b, 4, 13 |
| **GENERATE** | 14 | — | — | — |
| **REVIEW** | 1, 7, 7b | 3a | 6, 7c | 3b, 4 |
| **MODIFY** | 1, 2a, 7, 7b | 3a, 5 | 6 | 2b, 3b, 4, 13 |
| **EXPLAIN** | 1, 7, 7b | 3a | 6 | 3b |
| **CONVERT** | 1, 2a, 7, 7b | 5, 7c | 6 | 2b, 3a, 4, 13 |
| **DELETE** | 1, 7, 7b | 3a, 5, 7c | 6 | 3b, 4 |
| **CASCADE** | 1, 7, 7b | 3a, 3b, 5, 7c, 10 | 6 | 2a, 2b, 4, 13 |
| **EXPORT** | 1, 7, 7b | 3a, 5 | 6 | 3b, 9 |
| **PREVIEW** | 1, 2a, 7, 7b | 3a, 5, 8 | 6 | 2b, 3b |
| **DIFF** | 1, 7, 7b | 3a, 5, 8, 9 | 6 | 3b |
| **TRAIN** | 1, 7, 7b | 3a, 11 | 6 | 8 |

### Loading Instructions
1. At Step 1 (Classify task), determine task type
2. Load "Always" + task-specific parts from the matrix above
3. At Step 2.3 (Framework Relevance), if domain_context = "vib", also load Part 6
4. Load Part 2b only when generating Visual Templates — defer until Excel output phase
5. Load Part 4 only when generating actual Excel styling specs — defer until needed
6. Each part file has frontmatter confirming its part number and version
7. **Part 1 selective attention:** Cross-Workflow Handoffs and Level-to-Scope Mapping — consult on-demand for CONVERT, CASCADE, DELETE, or enterprise CREATE. Skip for simple REVIEW/EXPLAIN.
8. **GENERATE task:** Load Part 14 ONLY — it consolidates all Excel specs (layout, styles, borders, write order, Build Spec format). Do NOT load Parts 1, 2a, 2b, 3a, 4, 5, 7, 7b, 13 for GENERATE — Part 14 replaces them all for Excel output.

### Token Budget

> Orchestrator (~2,500) + Layer (~2,000) = ~4,500 tokens always loaded. Budgets include these.

- **Minimal** (EXPLAIN): ~27,600 (+ Parts 1+3a+7+7b)
- **Standard** (CREATE non-VIB): ~38,400 (+ Parts 1+1b+2a+3a+5+7+7b+8)
- **GENERATE** (Excel from Build Spec): **~7,500** (+ Part 14 only) ← lightweight!
- **Full** (CREATE VIB + all): ~75,400 (+ all 19 parts)
- **CASCADE**: ~48,600 (+ Parts 1+3a+3b+5+7+7b+7c+8+10)
- **DIFF**: ~44,400 (+ Parts 1+3a+5+7+7b+8+9)
- **TRAIN**: ~32,100 (+ Parts 1+3a+7+7b+11)
- **If all loaded:** Prioritize Part 1 (Rules), Part 7 (Validation), Part 7b (Examples).

### Shared Protocols (loaded via Part 1)
- **Data Integrity Protocol** — `[^n]`/`[EST]` citation tagging for quantitative Zone 3 Values
- **Checkpoint Protocol** — Save-and-checkpoint after each major section output
- **Challenge Signal Protocol** — Cross-workflow feedback loops (GNM ↔ GM/VD/ES/VS)

---

## 2-Phase Workflow: CREATE → GENERATE

For token-heavy GNMs, split into two phases to stay within context limits:

### Phase 1: CREATE (Design)
**Load:** Parts 1, 1b, 1c, 2a, 3a, 5, 6, 7, 7b (~38K tokens)
**Do:** Strategic thinking, framework selection, zone placement, content generation
**Output:** Build Spec (YAML format — see Part 14 § Build Spec Format)

### Phase 2: GENERATE (Excel)
**Load:** Part 14 ONLY (~3K tokens + xlsx skill)
**Do:** Run `scripts/generate-gnm.py <build-spec.json>` — or read Build Spec → compute layout → 5-phase write → save .xlsx
**Output:** Excel workbook
**Preferred:** Use the deterministic script. Falls back to LLM-based generation if script unavailable.

### When to Split

| Scenario | Approach | Total Tokens |
|----------|----------|--------------|
| Simple GNM (n≤5, f≤2) | Single session CREATE+Excel | ~45K |
| Complex GNM (n>10 or f>3) | **Split: CREATE → Build Spec → GENERATE** | ~38K + ~8K |
| CASCADE (multi-sheet) | **Split: CASCADE design → GENERATE per sheet** | ~49K + ~8K×sheets |
| VIB domain + full populate | **Split: CREATE+VIB → Build Spec → GENERATE** | ~45K + ~8K |

### Build Spec Handoff

Phase 1 saves the Build Spec as a `.yaml` or `.md` file:
```
_bmad-output/{CODE}-{Level}-build-spec.yaml
```

Phase 2 reads the Build Spec file and generates Excel. No strategic thinking needed — purely mechanical translation.

---

*Version: 5.6.0 | 20 parts, 57 sub-files | Orchestrator core | Updated: Mar 2026*

<!-- END OF GNM ORCHESTRATOR — Instruction layer in gnm-instruction-layer.md -->
