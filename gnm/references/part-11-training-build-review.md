---
part: 11
name: "Training: Build, Review & Certification"
parent: gnm-instruction.md
---

## Phase 3: BUILD (Guided Construction)

### Scaffold Levels

| Level | AI Assistance | User Responsibility |
|-------|---------------|---------------------|
| **Full scaffold** | AI builds, explains each decision | User confirms or adjusts |
| **Partial scaffold** | AI provides Zone 1+2, user fills Zone 3 | User creates content |
| **Minimal scaffold** | AI provides template only | User builds everything, AI validates |

### Process

1. **AI proposes Zone 1+2** based on user's topic → User reviews
2. **User fills Zone 3** → AI checks construction quality in real-time
3. **AI validates structure** → Reports V-gate results + Quality Scorecard
4. **User iterates** → AI provides targeted tips
5. **Generate Excel** → User sees final output

### Real-Time Feedback Signals

During BUILD phase, AI monitors and flags:
- 🔴 "That item doesn't share the same perspective as the others — different decoding needed?"
- 🟡 "These items may not be MECE — 'Product' and 'Mortgage' overlap"
- 🟢 "Good flow: Origination → Underwriting → Monitoring"
- 🟡 "Zone 3 cell [Item × Feature] is vague — can you describe the full scope?"
- 💡 "Consider adding a Conso. engine for this item"

## Phase 4: REVIEW (Find the Errors)

### Deliberately Flawed GNMs

Present a GNM containing planted errors from the Mistakes table (Part 7). User must find them.

**Difficulty levels:**

| Level | Errors | Time | Types |
|-------|--------|------|-------|
| **Easy** | 3 planted errors | No limit | HIGH severity only (Zone 3 empty, code mismatch, values in Zone 4-9) |
| **Medium** | 5 planted errors | 10 min | HIGH + MED severity (mixed taxonomy, wrong zone placement) |
| **Hard** | 8 planted errors | 5 min | All severities including subtle (wrap text missing, border order wrong) |

**Scoring:**
```
Review Score = (errors_found / total_planted) × 10
Bonus: +1 if user cites correct rule number
Penalty: -0.5 per false positive (flagged something that isn't an error)
```

**Example flawed GNM (Medium):**
```
Planted errors:
1. Zone 3 Row 9, Col G = empty (HIGH, Rule #1)
2. E5 = "PRD" (static, not formula) (HIGH, Rule #2)
3. Zone 5 engine in Conso. column instead of Feature column (MED, #8)
4. L1="Corporate Bond", L2="Short-term" (mixed taxonomy) (MED, #10)
5. Engine "PSC(B)" without full name (HIGH, Rule #5)
```

## Progress Tracking

```yaml
training_progress:
  user: "{user_name}"
  started: "{date}"
  phase1_concept:
    module1: { status: complete, score: 9/10 }
    module2: { status: complete, score: 8/10 }
    module3: { status: in-progress, score: null }
    module4: { status: locked, score: null }
  phase2_practice:
    exercise_2_1: { status: not-started }
    exercise_2_2: { status: not-started }
    exercise_2_3: { status: not-started }
  phase3_build:
    scaffold_level: null
    gnms_built: 0
    avg_quality_score: null
  phase4_review:
    reviews_completed: 0
    avg_review_score: null
  overall_level: "beginner"  # beginner | intermediate | advanced | expert
```

## Certification Criteria

| Level | Requirements |
|-------|-------------|
| **Beginner** | Complete Phase 1 quiz ≥ 7/10 |
| **Intermediate** | Phase 2 all exercises + Phase 3 build 1 GNM ≥ 6.0 quality |
| **Advanced** | Phase 3 build 3 GNMs ≥ 7.5 avg quality + Phase 4 Medium review ≥ 8/10 |
| **Expert** | Phase 4 Hard review ≥ 9/10 + Phase 3 cascade ≥ 8.0 quality |

---

> **📌 Retrieval Signpost:** For elearning source content → `01.gnm/elearning/`. For MFM philosophy → MFM Philosophy skill. For mistake patterns → PART 7. For Quality Scorecard → PART 8.

