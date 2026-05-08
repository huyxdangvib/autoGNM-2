# gnm-interview — Architecture

> Maintainer reference. Not loaded at runtime.

## File hierarchy

```
gnm-interview/
├── SKILL.md                # L1: entry, description triggers, activation workflow
├── ARCHITECTURE.md         # this file
├── references/             # L2: knowledge — loaded once at session start
│   ├── question-tree.md            # canonical question sequence (EN + VI)
│   ├── pushback-triggers.md        # 8 trigger rules with citations
│   ├── pushback-protocol.md        # 4-step re-confirmation flow
│   ├── good-gnm-distilled.md       # what makes a GNM good (drives fuzzy judgement)
│   ├── build-spec-schema.md        # JSON Schema for the spec
│   ├── level-taxonomy.md           # integer-level + is_final rules
│   └── glossary-vi.md              # VI translations + tone notes
├── scripts/                # L3: deterministic rendering
│   ├── generate-gnm.py     # forked from gnm/scripts/generate-gnm.py
│   └── render.sh           # wrapper — atomic rename, file-lock safe
└── workspace/              # runtime, gitignored
    ├── spec.json           # live Build Spec — single source of truth
    ├── transcript.md       # append-only Q&A log
    └── current.xlsx        # latest render — user keeps this open
```

## State model

```
┌─────────────────────────┐
│   user message          │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  AI: read spec.json     │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  determine next question│  ← state machine: which fields are missing?
│  (question-tree.md)     │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  ask user               │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│  validate answer        │  ← regex / range / push-back triggers
└──────────┬──────────────┘
           │
     fail? │ pass?
           │
   ┌───────┘
   ▼                ▼
 push-back        write to spec.json
 protocol         (read-modify-write)
   │                │
   │                ▼
   │           render trigger?
   │                │
   │           yes  │  no
   │                ▼
   │           bash render.sh
   │                │
   ▼                ▼
   loop back ←──────┘
```

## Data flow per turn

1. **Read** `workspace/spec.json` — full snapshot of session state
2. **Compute** next question from field-fill state (question-tree.md §state machine)
3. **Ask** one question
4. **Validate** answer:
   - Mechanical: regex, range, count
   - Triggers: 8 push-back rules from pushback-triggers.md
5. If trigger fires → 4-step protocol from pushback-protocol.md
6. **Write** answer back to `spec.json` (the entire field, not a delta)
7. **Render** if a structure-changing field flipped (see [RENDER] markers in question-tree.md)
8. **Append** Q&A to `transcript.md`

## Render integration

Trigger points (≈ 20 renders for a typical 4×3 GNM):
- End of bootstrap (B4) — empty shell
- End of Zone 1 (Z1.4) — items column populated
- End of Zone 2 (Z2.3) — feature row populated, empty Z3
- End of each Z3 row — Z3 partial
- After each Z4 entry — Conso engine populated
- After each Z5/Z7/Z9 row, Z6/Z8 entry — aggregation rows
- Finalize (F1) — final renamed file

Invocation: `bash scripts/render.sh [spec.json] [out.xlsx]`. Defaults to `workspace/spec.json` → `workspace/current.xlsx`. Atomic rename via `current.next.xlsx` so an Excel-open file doesn't corrupt the save.

Partial-spec rule: before any cell-level render, AI auto-pads `zone3` with `"…"` and `zone4` with `""` so `validate_spec` passes. Placeholders render as light-gray cells. Final render rejects `…`.

## Decoupling from `/gnm`

The skill is **runtime-self-contained**:
- No imports or path references into `gnm/`
- `good-gnm-distilled.md` is hand-curated, not a symlink
- `scripts/generate-gnm.py` is a fork, not a wrapper

This is deliberate. The legacy `/gnm` skill uses A/B/C/D/E/F/G/Z letter levels; the interview uses integer levels + `is_final`. Until `/gnm` migrates, the two skills produce equivalent-but-different schemas. The fork header points back to the upstream divergence point so a future rebase is mechanical.

## Forked-script change inventory

Diff from `gnm/scripts/generate-gnm.py`:

| Site | Change | Why |
|---|---|---|
| Header docstring | Note divergence + upstream pointer | Maintainability |
| `level_suffix(level, is_final, lang)` | New helper | EN/VI suffix formatting |
| `filename_suffix(level, is_final)` | New helper | `L{n}` / `L{n}F` naming |
| `validate_spec` L112–124 | Integer 1..12 check + bool `is_final` check | Schema replacement |
| `write_data` B2 cell | Use `level_suffix` | New B2 text format |
| `write_data` end | Stamp `B1 = "⚠ N rule overrides logged"` if `warnings` present | Push-back surfacing |
| `apply_formatting` | `B1` warning style (`WARN_FONT`) | Consistency |
| `generate_gnm` filename | Use `filename_suffix` | New filename format |
| `generate_gnm` sheet name | Use `filename_suffix` (no `F` flag for tab) | Excel 31-char tab limit |

Total ~30 lines net new. Validation behavior tightened (rejects letter levels); rendering output identical apart from B2 text and filename.

## V2 — cascade

Cascade adds:
- A `parent` field on the spec, populated when the user starts a sub-sheet
- A different bootstrap question: "new root or cascade child?"
- Multi-sheet write order in `generate_gnm` — process all sheets phase-by-phase, not sheet-by-sheet (per Part 14 §7)
- Backlink HYPERLINKs in A1 cells of child sheets (already supported in script via `parent.backlink`)

The schema reserves the `parent` field today so v2 doesn't break v1 specs.

## Maintenance rules

1. **Never duplicate rules between references and SKILL.md.** SKILL.md points; references define.
2. **Keep the script fork diff small (≤ 30 lines).** Document any new divergence in this file's "Forked-script change inventory".
3. **Workspace is per-user.** If shared deployment ever happens, move workspace to `~/.claude/gnm-interview/workspace/`.
4. **Never write VIB domain content into references.** Domain knowledge belongs in the user's head; the skill only knows structure.
5. **Bilingual content sync.** When updating an EN prompt in `question-tree.md` or `pushback-protocol.md`, update the VI sibling in the same edit.

---

*v1.0.0 — initial scaffolding. For maintainers only.*
