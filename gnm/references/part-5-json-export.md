---
part: 5
name: "Multi-Format Export & JSON Schema"
parent: gnm-instruction.md
---

## Multi-Format Export (GNM → Structured Data)

> **Purpose:** While Excel remains the primary medium for GNM, a structured data representation enables version control (diffable), web dashboard rendering, API integration, and programmatic validation. This section defines the canonical JSON schema for GNM export.

### Export Task Type

**Task keyword:** `EXPORT` — converts an existing GNM (Excel or spec) into structured JSON.

**When to use:**
- Version-controlling GNM evolution in git (JSON is diffable, Excel is not)
- Rendering GNM in web dashboards or presentation tools
- Programmatic validation of GNM rules (CI/CD pipeline)
- Transferring GNM structure between systems

### GNM JSON Schema

```json
{
  "$schema": "gnm-v1",
  "metadata": {
    "name": "VIB Business Model",
    "code": "VBM",
    "level": "A",
    "version": "1.0",
    "created": "2026-03-16",
    "temporal_state": null,
    "author": "Strategy Office"
  },
  "zone1": {
    "object": "Business Unit",
    "item": "Division",
    "items": [
      { "id": 1, "level1": "Retail Banking", "level2": null },
      { "id": 2, "level1": "Wholesale Banking", "level2": null }
    ]
  },
  "zone2": {
    "feature_group": "Businesses & Functions strategies",
    "features": [{ "name": "-", "weight": null }]
  },
  "zone3": {
    "matrix": [
      {
        "item_id": 1, "feature": "-", "type": "engine",
        "value": null,
        "engine": { "name": "Retail Banking Business", "code": "RBB", "level": "A", "sheet": "RBB (A)" },
        "dependencies": [], "score": null, "citation": null
      }
    ]
  },
  "zone4": { "engines": [{ "item_id": 1, "name": "RB Consolidation", "code": "RBC", "level": "Z" }] },
  "zone5": { "engines": [] },
  "zone6": { "engines": [] },
  "zone7": { "engines": [] },
  "zone8": { "engines": [] },
  "zone9": { "engines": [] },
  "cascade": { "parent": null, "children": ["RBB (A)", "WBB (A)"] }
}
```

### Schema Rules

| Field | Required | Notes |
|-------|----------|-------|
| `metadata.code` | Yes | Must match B5 |
| `metadata.level` | Yes | A/B/C/Z/Z1 |
| `metadata.temporal_state` | No | `null`, `"as-is"`, `"to-be"`, or `"delta"` |
| `zone3.matrix[].type` | Yes | `"value"`, `"engine"`, `"value+engine"`, or `"empty"` (→ "-") |
| `zone3.matrix[].dependencies` | No | Array of `"CODE(L)"` strings, max 2 |
| `zone3.matrix[].score` | No | Numeric score if scoring methodology used |
| `zone3.matrix[].citation` | No | `"[^n]"` or `"[EST]"` for Z-level quantitative data |
| `zone2.features[].weight` | No | Float 0.0-1.0, sum must = 1.0 if present |

### Response Format E: EXPORT GNM
> Sections: Source GNM identification → Schema validation → JSON output → Render options (Excel rebuild / web view / diff).

### Bidirectional Conversion

| Direction | Command | Notes |
|-----------|---------|-------|
| **Excel → JSON** | `EXPORT` | Extract structure from Excel into JSON schema |
| **JSON → Excel** | `CONVERT` (from JSON) | Rebuild Excel from JSON, applying Write Order |

> **Excel remains primary:** JSON export is a secondary representation. If JSON and Excel conflict, Excel is the source of truth.
