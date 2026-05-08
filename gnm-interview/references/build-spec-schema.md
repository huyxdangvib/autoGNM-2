# Build Spec — JSON Schema (gnm-interview/1.0)

The Build Spec is the single source of truth across interview turns. The AI reads, mutates, and writes it back to `workspace/spec.json` after every answered question. The renderer (`scripts/generate-gnm.py`) consumes it to produce the live `.xlsx`.

## Required top-level keys

```jsonc
{
  "schema_version": "gnm-interview/1.0",
  "gnm":      { ... },   // identity + level
  "session":  { ... },   // runtime metadata (lang)
  "layout":   { ... },   // structural dimensions
  "zone1":    { ... },   // WHAT axis (items)
  "zone2":    { ... },   // TODO axis (features)
  "zone3":    [...],     // n × f matrix of values/engines
  "zone4":    [...],     // n consolidation engines
  "zone5":    [...],     // optional: All cluster × feature cols
  "zone6":    [...],     // optional: All cluster × Conso col
  "zone7":    [...],     // optional: All cluster × extended cols
  "zone8":    [...],     // optional: Common cluster × Conso col
  "zone9":    [...],     // optional: Common cluster × extended cols
  "warnings": [...],     // logged rule overrides (push-back acks)
  "parent":   { ... }    // optional: cascade backlink (v2)
}
```

## Field reference

### `gnm`

| Field | Type | Constraint |
|---|---|---|
| `code` | string | `^[A-Z]{3}$` — exactly 3 uppercase letters |
| `name` | string | non-empty, ≤ 60 chars |
| `purpose` | string | one-sentence summary, ≥ 5 words |
| `level` | int | `1..12` (MVP: always `1`) |
| `is_final` | bool | true if no further cascade planned (MVP: always `true`) |
| `sheet_name` | string | derived `"{code} (L{level})"`, capped 31 chars |

### `session`

| Field | Type | Values |
|---|---|---|
| `lang` | string | `"en"` or `"vi"` — drives B2 final-suffix wording (`Final` vs `Cuối`) |
| `domain_notes` | string | free-text summary the AI builds during Phase 2 (Domain Discovery); drives propose-step for Z1/Z2/Z3 |

### `layout`

| Field | Type | Range | Meaning |
|---|---|---|---|
| `f` | int | 1..5 | feature count (TODO axis width) |
| `L2` | int | 0 or 1 | 1 if Zone 1 has a level-2 sub-grouping column |
| `n` | int | ≥ 1 | item count (WHAT axis height) |
| `a` | int | ≥ 2 | All-cluster row count |
| `c` | int | ≥ 2 | Common-cluster row count |

### `zone1`

```jsonc
{
  "perspective": "channel",            // free text from Z1.3
  "items": [
    { "l1": "Inbound",  "l2": null },  // l2 is null when layout.L2 == 0
    { "l1": "Outbound", "l2": null }
  ]
}
```

`zone1.items.length` MUST equal `layout.n`. If `layout.L2 == 1`, every item MUST have a non-null `l2`.

### `zone2`

```jsonc
{
  "feature_group": "Operations",
  "features": ["Origination", "Risk", "Reporting"]
}
```

`zone2.features.length` MUST equal `layout.f`.

### `zone3`

`n × f` matrix. Each cell is either:
- a string (value or engine name)
- an object `{ "text": "...", "sheet": "..." }` for HYPERLINK to a sub-sheet
- `"—"` for an explicit user skip
- `"…"` for an in-progress placeholder (auto-padded by AI; rejected at finalize)

```jsonc
"zone3": [
  ["Lead capture flow",     "Fraud screening",         "Daily call volume"],
  ["Outbound dialer",       "Compliance script check", "Conversion rate"],
  ["Callback queue SLA",    "—",                       "Callback hit rate"],
  ["IVR menu config",       "Disclosure recording",    "IVR completion %"]
]
```

### `zone4`

Length-`n` array. Each entry is the consolidated engine for the row (string or HYPERLINK object).

### `zone5`

Up to `layout.a` rows. Each row is an array of `f` engines (one per feature column). Use `""` for blank cells.

```jsonc
"zone5": [
  ["All-channel origination ACO", "All-channel risk ACR", "All-channel reporting ACP"],
  ["", "", ""]
]
```

### `zone6`

Up to `layout.a` strings — the All-cluster Conso engine per row.

### `zone7`

Up to `layout.a` `[left, right]` pairs — the All-cluster extended (Mở rộng) engines.

### `zone8`

Up to `layout.c` strings — the Common-cluster Conso engine per row.

### `zone9`

Up to `layout.c` `[left, right]` pairs — the Common-cluster extended engines.

### `warnings`

Array of override records, written by the push-back protocol on user re-confirmation:

```jsonc
{ "trigger": 5, "field": "zone2.features[2]", "value": "Cards", "user_ack": true }
```

The renderer stamps `⚠ N rule overrides logged` into cell `B1` if any are present.

### `parent` (v2 — cascade)

Reserved. Out of scope for MVP.

```jsonc
{ "sheet": "VBM (L1)", "backlink": true }
```

## Renderer-enforced invariants

`scripts/generate-gnm.py::validate_spec` checks (rejects with exit code 1 + stderr if any fail):

- `gnm.code` matches `^[A-Z]{3}$`
- `gnm.level` is `int` in `1..12`
- `gnm.is_final` is `bool`
- `layout.f` in `1..5`, `layout.n ≥ 1`, `layout.a ≥ 2`, `layout.c ≥ 2`
- `zone1.items.length == layout.n`
- `zone2.features.length == layout.f`
- `zone3.length == layout.n` and every row has length `layout.f`
- `zone4.length == layout.n`
- `zone5.length ≤ layout.a`, `zone9.length ≤ layout.c`
- If `layout.L2 == 1`, every item has a non-null `l2`

## Filename convention

- Non-final: `{code}-L{level}-gnm.xlsx` (e.g. `ESD-L1-gnm.xlsx`)
- Final: `{code}-L{level}F-gnm.xlsx` (e.g. `ESD-L1F-gnm.xlsx`)

## B2 cell convention

- EN, non-final: `"{name} (L{level})"`
- EN, final: `"{name} (L{level} — Final)"`
- VI, final: `"{name} (L{level} — Cuối)"`

## Example: minimal valid spec

See `workspace/sample-spec.json` for a full example. Minimum spec for a renderable L1 sheet (n=2, f=1):

```jsonc
{
  "schema_version": "gnm-interview/1.0",
  "gnm": { "code": "DMO", "name": "Demo", "purpose": "Smallest valid GNM",
           "level": 1, "is_final": true, "sheet_name": "DMO (L1)" },
  "session": { "lang": "en" },
  "layout": { "f": 1, "L2": 0, "n": 2, "a": 2, "c": 2 },
  "zone1": { "perspective": "—", "items": [{"l1":"A","l2":null},{"l1":"B","l2":null}] },
  "zone2": { "feature_group": "—", "features": ["—"] },
  "zone3": [["—"],["—"]],
  "zone4": ["—","—"],
  "zone5": [], "zone6": [], "zone7": [], "zone8": [], "zone9": [],
  "warnings": []
}
```
