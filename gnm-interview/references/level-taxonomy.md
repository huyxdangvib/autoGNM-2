# Level Taxonomy — integer scheme + `is_final`

The `gnm-interview` skill replaces the legacy A/B/C/D/E/F/G/Z letter scheme with two fields on `gnm`:

| Field | Type | Semantics |
|---|---|---|
| `level` | `int` 1..12 | Cascade depth. Root sheet is always **1**; each cascade child is `parent.level + 1`. |
| `is_final` | `bool` | `true` if no further cascade is planned beneath this sheet. |

## Why integers, not letters

Letters (A/B/C/...) implied a fixed taxonomy with semantic baggage per letter (A = enterprise root, Z = leaf measurement, D = decomposition hub). In practice cascades go arbitrarily deep, and the legacy scheme had no clean answer past G. Integers make depth explicit and unambiguous; `is_final` separately captures the leaf-or-not flag that letters used to bundle in.

## Automatic derivation

Levels are **automatic, not user-declared.**

- **Root sheet (no parent):** `level = 1`
- **Cascade child:** `level = parent.level + 1`

The interview never asks "what level is this?" — it derives it from cascade context.

In MVP scope the interview only builds a **root sheet**, so `level` is always `1` and `is_final` is always `true`.

## `is_final` semantics

- `true` — author has declared this sheet is a leaf (no cascade deeper from it). Affects filename (adds `F`) and B2 suffix (adds `— Final` / `— Cuối`).
- `false` — sheet is a non-leaf in a cascade; deeper sheets exist or are planned.

A sheet at the deepest natural level can still be `is_final: false` if the author hasn't decided yet. Only flip to `true` when committing.

## Filename convention

| Case | Pattern | Example |
|---|---|---|
| Non-final | `{code}-L{level}-gnm.xlsx` | `ESD-L3-gnm.xlsx` |
| Final | `{code}-L{level}F-gnm.xlsx` | `ESD-L1F-gnm.xlsx` |

The `F` is a single-character flag — keeps filenames stable and sortable.

## B2 cell suffix convention

The B2 title cell contains `{name} {suffix}`, where suffix is:

| Lang | Non-final | Final |
|---|---|---|
| `en` | `(L{level})` | `(L{level} — Final)` |
| `vi` | `(L{level})` | `(L{level} — Cuối)` |

Examples:
- `Enterprise Sales Desk (L1 — Final)`
- `Risk Operations (L3)` (mid-cascade, non-final)
- `Mortgage Pricing (L7 — Cuối)` (Vietnamese, deep leaf)

## Sheet name convention

`{code} (L{level})` — capped at 31 characters per Excel's hard limit. The `F` flag is omitted from the sheet tab to keep tabs short.

## Migration note

The legacy `/gnm` skill still uses A/B/C/Z. The interview skill is a clean break:
- The forked `scripts/generate-gnm.py` rejects letter levels with a clear error.
- Cross-references to legacy Part 6/Part 9 rules that reason about letters need translation when adapting them.
- A future `/gnm` migration can rebase onto this scheme; until then, the two skills produce different but equally-valid Excel structures.

## V2 — cascade

When cascade ships, the bootstrap question becomes:

> "Is this a new root GNM, or a cascade child of an existing sheet?"

If child: user supplies parent code + parent level; interview derives `level = parent + 1`. The `parent` field on the spec is populated, and the renderer adds an A1 backlink to the parent sheet.

`is_final` stays user-declared even with cascade — it's a future-intent flag, not a structural one.
