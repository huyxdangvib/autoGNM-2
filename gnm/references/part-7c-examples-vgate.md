---
part: 7c
name: "Examples: V-Gate Failure"
parent: gnm-instruction.md
---

### Example 9: V-Gate Failure + Correction Protocol

**Scenario:** During a CREATE for "NPL Workout Strategy WOR(B)" with 3 items and 2 features, Step 4.5 catches a zone boundary error.

**Step 4.5 V-gate (FAILED):**
```
V-gate: Z3[6/6] Sync[a=2=2=2,c=2=2=2] E5E8[ok] Layout[5col] ZoneBound[FAIL] Cite[n/a] TermCheck[ok]
```

**Error detected:** Zone 5 engine placed in Conso. column (I11) instead of Feature columns (G11-H11).

**Step 4.5b Correction Protocol:**
1. **Identify:** Rule violated = PART 3b, Zones 5-9 table: "Zone 5: Vertical Consolidation -- Cluster: All -- Vi tri cot: Zone 2-3 cols"
2. **Root-cause:** Step 4 generated Zone 5 engine `NPL Recovery Standards NRS(Z)` in Conso. col instead of Feature col
3. **Fix at root:** Move `NPL Recovery Standards NRS(Z)` from I11 (Conso.) to G11 (Feature col 1). Place Zone 6 engine `Workout Governance Framework WGF(Z)` in I11 (Conso.) where it belongs.
4. **Re-run ALL checks:**
   - Z3[6/6] | Sync[2=2=2] | E5E8[ok] | Layout[5col] | ZoneBound[ok] | Cite[n/a]
5. All checks pass on 2nd run.

**Corrected V-gate:**
```
V-gate: Z3[6/6] Sync[a=2=2=2,c=2=2=2] E5E8[ok] Layout[5col] ZoneBound[ok] Cite[n/a] TermCheck[ok]
```

> This example demonstrates the correction protocol catching and fixing a common zone placement error before it reaches the user.

</example>

---

<example type="SINGLE_FEATURE_CREATE">

