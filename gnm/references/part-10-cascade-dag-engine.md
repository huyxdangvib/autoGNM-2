---
part: 10
name: "Cascade DAG Engine"
parent: gnm-instruction.md
---


<part10_cascade_engine>

# PART 10: CASCADE DAG ENGINE

> **TL;DR:** Dependency-aware construction engine for enterprise GNM cascades (3-50+ sheets). Builds a DAG (Directed Acyclic Graph), validates structure, produces topological build order, and tracks progress. Replaces ad-hoc cascade construction with deterministic orchestration.

> **When to use:** CASCADE task type, or CREATE with `cascade_children` in Build Spec, or any request involving 3+ linked GNM sheets.


## Cascade Specification

### Input Format

```yaml
cascade:
  root: "VBM (A)"                    # Root GNM (Level A)
  nodes:
    - code: VBM
      level: A
      children: [RBB, ONW, HRS, VRS, MCS_A, HAGT, GNM, VES, BFS, VOS, RSS, RST]
    - code: RBB
      level: A
      children: [RBL, RBF, RBC, RBB_Banca]
    - code: RBL
      level: B
      children: [MTG, ATL, BLN]
    - code: MTG
      level: Z
      children: []                    # Leaf node
    - code: WBB
      level: A
      children: [CBB, TFB]
  domain: vib
```

### Auto-Inference

If user provides only root topic + scope, infer cascade structure:
1. Identify organizational layers (A→B→Z from Part 1)
2. Map layers to GNM levels (A→B→Z)
3. Use VIB Business Basic Units (Part 6) for domain-specific expansion
4. Present inferred cascade for user confirmation before building

## DAG Construction

### Step 1: Build Adjacency List

```python
def build_dag(cascade_spec):
    dag = {}
    for node in cascade_spec['nodes']:
        code = f"{node['code']} ({node['level']})"
        dag[code] = {
            'children': [resolve_code(c) for c in node['children']],
            'level': node['level'],
            'status': 'pending'
        }
    return dag
```

### Step 2: Validate DAG Integrity

| Check | Rule | Action on Fail |
|-------|------|----------------|
| **No cycles** | DFS cycle detection — no node should be its own ancestor | Abort + report cycle path |
| **No orphans** | Every non-root node must have exactly 1 parent | Report orphan nodes, suggest parent |
| **Level consistency** | Parent level ≥ child level (A>B>C>Z>Z1) | Warn if child level > parent level |
| **Back-link reachability** | Every child sheet can navigate back to parent via `<<` | Auto-fix: generate back-link formulas |
| **No duplicate codes** | Each code appears at most once per level | Abort + report duplicates |
| **Max depth** | Cascade depth ≤ 5 levels | Warn if deeper (suggest splitting into separate workbooks) |

```python
def validate_dag(dag):
    issues = []
    
    # Cycle detection (DFS)
    visited, rec_stack = set(), set()
    def has_cycle(node):
        visited.add(node)
        rec_stack.add(node)
        for child in dag[node]['children']:
            if child not in visited:
                if has_cycle(child):
                    return True
            elif child in rec_stack:
                issues.append(f"CYCLE: {node} → {child}")
                return True
        rec_stack.discard(node)
        return False
    
    for node in dag:
        if node not in visited:
            has_cycle(node)
    
    # Orphan detection
    all_children = set()
    for node in dag:
        all_children.update(dag[node]['children'])
    root = [n for n in dag if n not in all_children]
    if len(root) != 1:
        issues.append(f"Expected 1 root, found {len(root)}: {root}")
    
    return issues
```

### Step 3: Topological Sort (Build Order)

```python
def topological_sort(dag):
    """Returns build order: leaves first, root last.
    Uses out-degree (child count) as dependency: a node is 'ready' only
    after ALL its children have been built."""
    out_degree = {}
    for node in dag:
        children_in_dag = [c for c in dag[node]['children'] if c in dag]
        out_degree[node] = len(children_in_dag)
    
    queue = [n for n in out_degree if out_degree[n] == 0]
    build_order = []
    while queue:
        node = queue.pop(0)
        build_order.append(node)
        for potential_parent in dag:
            if node in dag[potential_parent]['children']:
                out_degree[potential_parent] -= 1
                if out_degree[potential_parent] == 0:
                    queue.append(potential_parent)
    
    return build_order  # Leaves first → Root last
```

**Build strategy:** Build leaves first so parent sheets can immediately create valid HYPERLINK formulas to existing child sheets.

### Step 4: Generate Build Plan

```
## Cascade Build Plan: VBM (A)
Total sheets: 12 | Levels: A(3), B(3), Z(6) | Max depth: 4

### Build Order (bottom-up):
| # | Sheet | Level | Parent | Children | Status |
|---|-------|-------|--------|----------|--------|
| 1 | MTG (Z) | Z | RBL (B) | — | ⬜ pending |
| 2 | ATL (Z) | Z | RBL (B) | — | ⬜ pending |
| 3 | BLN (Z) | Z | RBL (B) | — | ⬜ pending |
| 4 | RBL (B) | B | RBB (A) | MTG, ATL, BLN | ⬜ pending |
| ... | ... | ... | ... | ... | ... |
| 12 | VBM (A) | A | — (root) | RBB, WBB, TRS, BNW | ⬜ pending |

### Cross-Sheet Links:
| From | Zone | To | Formula |
|------|------|----|---------|
| RBL (B) | Z3/R8/G | MTG (Z) | =HYPERLINK("#'MTG (Z)'!B2","Mortgage MTG(Z)") |
| RBB (A) | Z3/R8/G | RBL (B) | =HYPERLINK("#'RBL (B)'!B2","RB Lending RBL(B)") |
| ... | ... | ... | ... |
```

## Energy Checkpoints

For cascades with 5+ sheets, insert checkpoints:

| After Sheet # | Checkpoint |
|---------------|------------|
| 3 | "Completed 3/{total} sheets: {list}. Ready to continue?" |
| 6 | "Halfway: 6/{total} sheets done. Cascade structure verified. Continue?" |
| 9 | "Almost there: 9/{total}. {remaining} sheets left." |
| Final | "All {total} sheets complete. Running cascade validation..." |

## Cascade Validation (Post-Build)

After all sheets are built, run cascade-wide checks:

| # | Check | How |
|---|-------|-----|
| 1 | **All HYPERLINKs resolve** | Every `=HYPERLINK("#'Sheet'!...")` points to existing sheet |
| 2 | **All back-links valid** | Every sub-GNM A1 has `=HYPERLINK("#'Parent'!A1","<<")` |
| 3 | **No orphan sheets** | Every sheet is reachable from root |
| 4 | **Engine name consistency** | Same engine is named identically across all sheets |
| 5 | **Code uniqueness** | No duplicate codes within same level |
| 6 | **Level hierarchy** | No child with higher level than parent |

## Output Format

```
Cascade: VBM(A) → 12 sheets | Depth: 4 | Build: bottom-up
DAG: ✅ No cycles | ✅ No orphans | ✅ Level-consistent
Progress: [████████████] 12/12 complete
Links: 18 HYPERLINKs verified | 11 back-links verified
Quality: Avg 8.4/10 across 12 sheets
```

---

> **📌 Retrieval Signpost:** For cascade patterns (Multi-A, Single-A) → PART 1. For Level-to-Scope Mapping → PART 1. For HYPERLINK formulas → PART 5. For Write Order → PART 5.
