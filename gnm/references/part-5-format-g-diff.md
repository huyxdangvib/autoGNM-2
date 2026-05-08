---
part: 5
name: "Format G: DIFF"
parent: gnm-instruction.md
---


### Format G: DIFF / Compare GNMs
> Purpose: Side-by-side comparison of two GNMs or before/after states. Used for As-Is/To-Be and version tracking.
> Trigger: User provides two GNMs for comparison, or MODIFY shows before/after.

**Output structure:**
```
## GNM DIFF: {GNM_A} vs {GNM_B}

### Structural Comparison
| Aspect | {GNM_A} | {GNM_B} | Delta |
|--------|---------|---------|-------|
| Items | 3 | 5 | +2 added |
| Features | 2 | 2 | unchanged |
| Level | B | B | unchanged |
| Zone 3 density | 5/6 (83%) | 9/10 (90%) | +7% |

### Zone 1 Changes
| Item | {GNM_A} | {GNM_B} | Change |
|------|---------|---------|--------|
| Working Capital | ✅ present | ✅ present | unchanged |
| Medium-Long Term | ✅ present | ✅ present | unchanged |
| LC UPAS | ✅ present | ❌ removed | [RETIRE] |
| Trade Finance | ❌ absent | ✅ added | [NEW] |
| Structured Finance | ❌ absent | ✅ added | [NEW] |

### Zone 3 Cell Changes
| Item × Feature | {GNM_A} | {GNM_B} | Tag |
|---------------|---------|---------|-----|
| Trade Fin × Origination | — | TF Origination TFO(Z) | [NEW] |
| LC UPAS × Risk Mgmt | Trade Risk TRA(Z) | — | [RETIRE] |
| Working Cap × Origination | WC Orig WCO(Z) | WC Origination Process WCO(Z) | [GAP] name update |

### Quality Comparison
| Dimension | {GNM_A} | {GNM_B} | Delta |
|-----------|---------|---------|-------|
| Total | 7.5/10 | 8.2/10 | +0.7 |
```

---

**Energy Checkpoints (for complex multi-sheet GNMs):**
When building a cascade with 3+ sheets, insert an energy checkpoint after every 3rd sheet:
"We've completed [N] sheets so far: [list]. [N] remaining. The cascade is taking shape — ready to continue?"
This prevents user fatigue during large GNM construction sessions.

---

