# GNM Skill — Architecture

> Maintainer reference for the 3-layer file architecture. Not loaded at runtime — for humans only.

---

## File Hierarchy

```
gnm/
├── SKILL.md                    ← L1: Router (entry point, ~80 lines)
├── ARCHITECTURE.md             ← This file (not loaded at runtime)
├── evals/
│   └── evals.json              ← 25 test cases for skill evaluation
├── gnm-workspace/              ← Eval run outputs (not committed)
└── references/                 ← All knowledge files
    ├── gnm-instruction.md      ← L2a: Orchestrator (loading protocol, task matrix)
    ├── gnm-instruction-layer.md← L2b: Instruction Layer (behavioral spec)
    ├── CHANGELOG.md            ← Version history
    └── part-*.md (56 files)    ← L3: Knowledge Base (20 parts)
```

## Three Layers

```
┌─────────────────────────────────────────────────────┐
│  L1: SKILL.md (Router)                              │
│  • Triggers skill activation via description        │
│  • Points to references/ — no logic of its own      │
│  • Part catalog table (what to load)                 │
│  • Activation workflow (7 steps)                     │
│  • Security & communication rules                   │
│  • ⚠️ DO NOT MODIFY note for Excel files            │
├─────────────────────────────────────────────────────┤
│  L2a: gnm-instruction.md (Orchestrator)             │  ← ALWAYS loaded
│  • Part Loading Protocol (which files for which task)│
│  • Task-Type Loading Matrix (12 task types)          │
│  • Token budget & loading instructions               │
│  • Shared protocols (checkpoint, challenge signal)   │
│                                                      │
│  L2b: gnm-instruction-layer.md (Instruction Layer)  │  ← ALWAYS loaded
│  • Role & communication traits                       │
│  • 8-step thinking process                           │
│  • V-gate (10 checks, 3-tier: PASS/CONDITIONAL/FAIL)│
│  • Response by Intent (CREATE/REVIEW/MODIFY/etc.)    │
│  • 11 Critical Rules & Priority Hierarchy            │
│  • Output style, error template, overflow strategy   │
│  • Validation & evaluation metrics                   │
├─────────────────────────────────────────────────────┤
│  L3: part-*.md (56 files, 20 parts)                 │  ← Loaded on-demand
│  • Domain knowledge, rules, examples, templates     │
│  • Each part has own frontmatter version             │
│  • Loaded per Task-Type Matrix in L2a               │
│  • DRY: cross-refs replace duplicated content        │
└─────────────────────────────────────────────────────┘
```

## Layer Responsibilities (SSOT)

| Concern | Owner | NOT in |
|---------|-------|--------|
| Trigger description, scope boundary | L1 (SKILL.md) | L2a, L2b |
| Part catalog & token estimates | L1 (SKILL.md) + L2a | — |
| Which parts to load per task type | L2a (orchestrator) | L1, L2b |
| Token budget, loading instructions | L2a (orchestrator) | L1 |
| How Claude behaves (role, thinking, V-gate) | L2b (instruction layer) | L2a |
| Response formats per intent | L2b (instruction layer) | L2a |
| Critical Rules definitions | L3 (Part 1) | L2a, L2b (summary only) |
| Zone structure, formulas, styling | L3 (Parts 2-5) | L2a, L2b |
| Domain context (VIB) | L3 (Part 6) | L2a, L2b |
| Domain engine templates (Zone 5-9) | L3 (Part 3b) | L2a, L2b |
| Examples | L3 (Parts 7b, 7c) | L2a, L2b |

**Key rule:** L2b summarizes critical rules but NEVER defines them — Part 1 is authoritative. If L2b and Part 1 conflict, Part 1 wins.

## Task-Type Loading Flow

```
User request
    │
    ▼
┌──────────┐    ┌───────────┐    ┌──────────────┐
│ L1: SKILL │───►│ L2a: Orch │───►│ L2b: Layer   │
│ (triggers)│    │ (loading) │    │ (behavior)   │
└──────────┘    └─────┬─────┘    └──────────────┘
                      │
              Step 1: Classify task
                      │
                      ▼
              ┌───────────────┐
              │ Task-Type     │
              │ Loading Matrix│
              └───────┬───────┘
                      │
         ┌────────────┼────────────┐
         ▼            ▼            ▼
    ┌─────────┐  ┌─────────┐  ┌─────────┐
    │ Always  │  │ + Task  │  │ + VIB   │
    │ 1,7,7b  │  │ specific│  │ domain  │
    └─────────┘  └─────────┘  └─────────┘
                      │
                      ▼
              8-step thinking → V-gate → Output
```

## V-gate Classification (v5.5)

```
┌─────────────────────────────────────────────┐
│  V-gate Result (10 checks)                  │
├─────────────────────────────────────────────┤
│  PASS          │ All 10 checks ok/n/a       │
│  CONDITIONAL   │ Checks 1-4 pass +          │
│                │ 1 non-critical warning      │
│  FAIL          │ Any of 1-4 fails OR        │
│                │ 2+ non-critical fail        │
└─────────────────────────────────────────────┘
Checks 1-4 = structural core (Z3, Sync, E5/E8, Layout)
Checks 5-10 = non-critical (Citation, Term, Boundary, Dep, Score, Temporal)
```

## DRY Cross-Reference Map (v5.5)

Content that was deduplicated — single source with cross-references:

| Content | SSOT Location | Files that cross-ref |
|---------|--------------|---------------------|
| Cascade Patterns (Multi-A, Single-A, A→Z) | `part-1-system-role.md` | `part-1-rules-priority.md`, `part-1-identity-thinking.md` |
| Level-to-Scope Mapping | `part-1-system-role.md` | `part-1-rules-priority.md` |
| Quick Reference Card + Zone Summary | `part-1-system-role.md` | `part-1-identity-thinking.md` |
| Critical Rules (1-11) scope | `part-1-rules-priority.md` | `part-1-construction-quality.md` (Q1-Q8 different scope) |
| Zone 5-9 domain templates | `part-3b-zones5-9-referral.md` | (new, no cross-refs needed) |

## Version Tracking

| File | Version field | Bump when |
|------|--------------|-----------|
| `gnm-instruction.md` | Frontmatter `version` + footer | System-wide changes, file restructuring |
| `gnm-instruction-layer.md` | Frontmatter `version` + footer | Behavioral changes (thinking, V-gate, rules) |
| `part-*.md` | Frontmatter `version` | That specific part's content changes |
| `SKILL.md` | Title heading `v5.x.x` | Any release |
| `CHANGELOG.md` | Header note + entry table | Every release |

**Convention:** Orchestrator version = system release version. Part versions may lag — that's by design. Only bump a part when its content actually changes.

## Maintenance Rules

1. **Never duplicate behavioral content in L2a** — the v5.2.2 split moved all behavioral spec to L2b. The orchestrator (L2a) owns only loading protocol and task matrix.
2. **L1 summarizes, L2/L3 define** — SKILL.md can reference rules but must not define them. Pointers, not copies.
3. **File merging threshold** — if two sub-files for the same part total <250 lines, merge them into one. If a single file exceeds 200 lines, consider splitting. **⚠️ Exception: DO NOT MODIFY Excel-related files** (Part 13, Part 14, `generate-gnm.py`) — they require full detail (styles, layout, formulas, write order) in continuous form for correct `.xlsx` output. Do not split, compress, summarize, or restructure these files. Exempt from file-size and token-optimization rules.
4. **File naming** — `part-{N}-{descriptive-slug}.md` with kebab-case. Multi-file parts use `part-{N}-*.md` glob pattern.
5. **After any structural change** — update: (a) sub-file count in L2a footer + L2b long_context_strategy, (b) Part catalog table in L1, (c) CHANGELOG entry.
6. **Version sync** — on release, bump L2a frontmatter+footer, L2b frontmatter+footer, L1 title, CHANGELOG header. Don't bump parts that didn't change.
7. **DRY enforcement** — before adding content to Part 1 files, check the Cross-Reference Map above. If the content exists elsewhere, add a cross-ref link instead of duplicating.

## Eval Infrastructure (v5.5)

```
evals/
└── evals.json          ← 25 test cases, 12 task types, 10 quality dimensions

gnm-workspace/          ← Created during eval runs (not committed to git)
└── iteration-N/
    └── eval-{name}/
        └── with_skill/
            ├── outputs/    ← Skill output files
            ├── timing.json ← Token count, duration
            └── grading.json← Assertion pass/fail results
```

**Eval targets:** V-gate ≥90%, Quality avg ≥7.5, Zone 3 density ≥60%, Construction Quality ≥85%
**Last eval (2026-03-16):** 3/25 run — 100% pass rate, 8.5 avg quality

---

*Updated: v5.5 (2026-03-16) | For maintainers only — not loaded at runtime*
