---
part: 3a
name: "Pattern Validity Rules"
parent: gnm-instruction.md
---

## Pattern Validity Rules

Rules for validating non-obvious GNM patterns that might appear incorrect but are structurally valid.

### Enterprise as Zone 2 Feature (Not Just Zones 5-9)

**Default rule:** Enterprise-wide content goes to Zones 5-9 (All/Common).

**Exception:** At B-level, Enterprise CAN be a Zone 2 feature column alongside BL columns (RB, WB, TRS) when Enterprise items are **active capability engines** the leader develops in parallel with BL strategies.

| Where Enterprise Goes | When |
|----------------------|------|
| **Zones 5-9 only** (All/Common) | Enterprise = governance/infrastructure (organizational concern) |
| **Zone 2 feature column** | Enterprise = **strategic capability engines** actively developed alongside BL strategies |

**Rule of thumb:** If Enterprise engines have their own Z-sheets with WHAT x TODO decomposition → they deserve a feature column. If they're just references/policies → Zones 5-9.

**Example — CRD(B):** Enterprise column contains IFRS9 Model, Concentration Framework, Rating Methodology, Stress Testing, Collections Strategy, Enterprise CRAS. These are active capability investments, not just governance.

---

### Feature Group Naming

Feature Group name (Row 6) should immediately tell the reader what decision the GNM supports.

| Name | Signal | Verdict |
|------|--------|---------|
| "Development" | Vague — development of what? | Ambiguous |
| "Credit Portfolio Strategy" | Portfolio allocation view | Clear for strategy GNM |
| "Credit Risk by Business" | Risk per division | Clear for operational view |
| "Credit Risk Appetite" | Focus on limits/targets | Clear if CRAS-focused |

**Rule:** Prefer self-evident names over generic ones. "Development" requires context; "Credit Portfolio Strategy" is self-evident.

---

### 3-Level Cascade Constraint (A->B->Z)

| Level | Content | Rule |
|-------|---------|------|
| A | All Engines -> B | Navigation only |
| B | Mix of Engines -> Z + Values | Strategy — where the leader makes trade-offs |
| Z | **All Values** | Terminal node — specific numbers, thresholds, SLAs, frequencies |

**Optimization:** Many "Z-sheets" can be written as Values directly in B-level Zone 3. Only create Z-sheet when content needs its own WHAT x TODO decomposition.

Target: ~20 sheets total per function cascade (not 40+).

---
