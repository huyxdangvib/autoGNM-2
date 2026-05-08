---
part: 12
name: "Session Memory & Feedback Loop"
parent: gnm-instruction.md
---


<part12_session_memory>

# PART 12: SESSION MEMORY & FEEDBACK LOOP

> **TL;DR:** Enables cross-session learning by recording GNM creation history, user corrections, quality trends, and recurring issues. Stores in repo memory for persistent access. Feeds back into future sessions to pre-warn about known issues and adapt to user preferences.

> **When to use:** Automatically after every GNM output (CREATE, MODIFY, CASCADE). Consult at session start to load user patterns.


## Memory Storage

### Location
```
/memories/repo/gnm-history.json     # GNM creation history
/memories/repo/gnm-preferences.md   # User preferences and patterns
```

### GNM History Schema

```json
{
  "version": "1.0",
  "entries": [
    {
      "id": "gnm-001",
      "date": "2026-03-16",
      "task_type": "CREATE",
      "topic": "Wholesale Banking Lending",
      "code": "WBL",
      "level": "B",
      "domain": "vib",
      "quality_score": 8.2,
      "dimension_scores": {
        "structural": 9, "taxonomy": 7, "flow": 8,
        "density": 9, "naming": 8, "cascade": 10,
        "decoding": 7, "domain": 9, "scope": 8, "action": 8
      },
      "vgate_issues": [],
      "user_corrections": [
        {
          "type": "zone1_rename",
          "before": "Working Cap",
          "after": "Working Capital Loans",
          "reason": "More specific naming"
        }
      ],
      "frameworks_accepted": ["customer_management", "operational_excellence"],
      "frameworks_rejected": ["disruption"],
      "sheets_created": 1,
      "cascade_depth": 0
    }
  ]
}
```

## Recording Protocol

### After CREATE/MODIFY

1. Record entry with topic, code, level, domain
2. Run Quality Scorecard → store all 10 dimension scores
3. If user makes corrections → record before/after/reason
4. Record which framework recommendations were accepted vs rejected
5. Append to `/memories/repo/gnm-history.json`

### After CASCADE

1. Record root entry + all child sheets
2. Store cascade DAG structure
3. Record per-sheet quality scores + aggregate
4. Store build order and timing

### After REVIEW

1. Record reviewed file metadata
2. Store issues found + user agreement (accepted fix vs rejected)
3. Track recurring issue patterns

## Feedback Retrieval

### At Session Start

When GNM skill activates, check for existing history:

```python
def load_gnm_history():
    history = read('/memories/repo/gnm-history.json')
    if not history:
        return None
    
    insights = {
        'total_gnms': len(history['entries']),
        'avg_quality': mean([e['quality_score'] for e in history['entries']]),
        'weak_dimensions': find_consistently_low(history),
        'common_corrections': aggregate_corrections(history),
        'preferred_frameworks': rank_frameworks(history),
        'recurring_issues': find_recurring_vgate_issues(history)
    }
    return insights
```

### Pre-Warning System

Before output, check history for known patterns:

| Pattern | Detection | Pre-Warning |
|---------|-----------|-------------|
| **Low taxonomy scores** | Avg taxonomy < 7 across 3+ GNMs | "⚠️ Taxonomy quality has been a recurring area — double-check MECE and perspective consistency" |
| **Repeated corrections** | Same type of correction 3+ times | "💡 Based on past sessions, you prefer [X] over [Y] — applying that preference" |
| **Framework preference** | Consistently rejected framework category | Suppress that framework from recommendations |
| **Domain patterns** | 80%+ GNMs are VIB domain | Auto-load Part 6 without explicit domain detection |

## User Preferences

### Auto-Detected Preferences

| Preference | Detection Logic | Application |
|------------|----------------|-------------|
| **Naming style** | Track user corrections to engine names | Apply preferred naming patterns |
| **Level defaults** | Most common level per topic type | Suggest default level |
| **Feature patterns** | Commonly used Zone 2 features | Pre-populate feature suggestions |
| **Detail level** | User usually expands/contracts from suggestion | Adjust Zone 3 detail density |
| **Language** | Primary language of corrections | Set response language default |

### Manual Preferences

Store in `/memories/repo/gnm-preferences.md`:

```markdown
# GNM Preferences

## Naming
- Prefer full descriptive names over abbreviations
- Always include business unit prefix (e.g., "RB" for Retail Banking)

## Structure
- Default Level: B for new topics
- Default features: 2 (moderate complexity)
- Always include PCSS MR for commercial banking topics

## Style
- Expanded Quality Scorecard for scores < 8.0
- Compact V-gate line for scores ≥ 8.0
- Preview before Excel generation (always)
```

## Quality Trend Tracking

### Trend Report (on request)

```
## GNM Quality Trend

Period: Last 30 days | GNMs analyzed: 12

### Overall Trend
Score: 6.8 → 7.5 → 8.2 (↑ improving)

### Dimension Trends
| Dimension | 30d ago | 15d ago | Current | Trend |
|-----------|---------|---------|---------|-------|
| Taxonomy | 5 | 6 | 7 | ↑ |
| Flow | 7 | 7 | 8 | ↑ |
| Decoding | 5 | 6 | 7 | ↑ |
| Naming | 8 | 8 | 8 | → |
| Density | 6 | 8 | 9 | ↑ |

### Top Recurring Issues
1. Mixed PCSS perspectives in Zone 1 (fixed 3x)
2. Incoherent axis — items from different decoding methods mixed (fixed 2x)

### Recommendations
- Focus on: Taxonomy Quality (still lowest dimension)
- Consider: Training Mode Phase 2 exercises for MECE practice + Axis Decoding exercise
```

## Privacy & Data Handling

- History is stored locally in repo memory only — never transmitted
- No personal data stored — only GNM structural metadata
- User can clear history: "clear GNM history" or delete memory files
- History entries are text only — no Excel file content stored

---

> **📌 Retrieval Signpost:** For Quality Scorecard dimensions → PART 8. For V-gate checks → orchestrator. For training recommendation → PART 11. For memory system → workspace `/memories/repo/`.
