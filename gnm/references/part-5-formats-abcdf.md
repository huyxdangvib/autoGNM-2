---
part: 5
name: "Response Formats A-F"
parent: gnm-instruction.md
---

## Response Format Specification

Khi trả lời user, sử dụng các format chuẩn sau:

### Format A: CREATE GNM (Tạo mới)
> Sections: 1. Overview (property table) → 2. Zone 1: Items → 3. Zone 2: Features → 4. Zone 3: Value Matrix → 5. Zone 4-9 → 6. Excel Implementation → ⚠️ Warnings. See Example 1 (PART 7b) for full demonstration.

### Format B: REVIEW GNM (Đánh giá)
> Sections: Summary (compliance table) → Issues Found (severity-ranked) → Recommendations. See Example 2 (PART 7b).

### Format C: EXPLAIN Concept
> Sections: Định nghĩa (1-2 câu) → Tại sao quan trọng → Cách áp dụng (steps) → Ví dụ → Lỗi thường gặp (❌/✅).

### Format D: CONVERT Data → GNM
> Sections: Source Analysis (format/detected WHAT/TODO) → Mapping Result (source → zone) → Generated GNM (follow Format A). See Example 5 (PART 7c).

### Format E: DIFF GNM (Compare two versions)
> Purpose: Highlight structural and content changes between two GNM versions.
> Trigger: DIFF task, or when user requests "compare GNM v1 vs v2", "so sánh 2 phiên bản GNM".
> Sections: Summary Table (old vs new: zones, items, features, levels) → Changes Found (structural changes, content changes, zone boundary shifts) → Impact Analysis (cascade effects, broken engines). See Part 9 for parser protocol used in extraction.

### Format F: PREVIEW GNM (ASCII Visualization)
> Purpose: Rapid structural validation before Excel generation. Shows exact column/row layout with content.
> Trigger: Before any CREATE/MODIFY that generates Excel, or when user requests `/gnm --preview`.

**Template (f=2, L2=0 — Template A layout):**
```
     | A  | B      | C   | D  | E      | F        | G              | H              | I               | J  | K               | L               |
-----+----+--------+-----+----+--------+----------+----------------+----------------+-----------------+----+-----------------+-----------------+
 R2  |    | {GNM NAME (Level)}                             [B2:{Conso col}2 merged]       |    |                 |                 |
 R3  |    |        |     |    |        |          |                |                |                 |    |                 |                 |
-----+----+--------+-----+----+--------+----------+----------------+----------------+-----------------+----+-----------------+-----------------+
 R4  |    | (1)    | (2) |    | (1)    | (2)      | (3)            | (4)            | (5)             |    | (1)             | (2)             | ← Header
 R5  |    | {CODE} | (1) |    | =B5    |          |                |                | Conso.          |    | Common          |                 | ← Sub-header
 R6  |    |        | (2) |    | Object |          | {Feat Group}   |                | -               |    | -               |                 | ← Zone Headers
 R7  |    |        | (3) |    | Item   | -        | {Feature 1}    | {Feature 2}    | -               |    | -               | -               | ← Zone Headers
-----+----+--------+-----+----+--------+----------+----------------+----------------+-----------------+----+-----------------+-----------------+
 R8  |    |        | 1   |    | =B5    | {Item 1} | {Z3 content}   | {Z3 content}   | {Z4 engine}     |    |                 |                 | ← Z1+Z3+Z4
 R9  |    |        | 2   |    |        | {Item 2} | {Z3 content}   | {Z3 content}   | {Z4 engine}     |    |                 |                 |
 R10 |    |        | 3   |    |        | {Item 3} | {Z3 content}   | {Z3 content}   | {Z4 engine}     |    |                 |                 |
-----+----+--------+-----+----+--------+----------+----------------+----------------+-----------------+----+-----------------+-----------------+
 R11 |    |        | All |    |        |          | {Z5 engine}    | {Z5 engine}    | {Z6 engine}     |    | {Z7 engine}     |                 | ← Z5+Z6+Z7
 R12 |    |        |     |    |        |          |                |                |                 |    |                 |                 |
-----+----+--------+-----+----+--------+----------+----------------+----------------+-----------------+----+-----------------+-----------------+
 R13 |    | Common | -   |    |        |          |                |                | {Z8 engine}     |    | {Z9 engine}     |                 | ← Z8+Z9
 R14 |    |        |     |    |        |          |                |                |                 |    |                 |                 |
-----+----+--------+-----+----+--------+----------+----------------+----------------+-----------------+----+-----------------+-----------------+
     | Sep|  Phần Đầu    | Sep|            Phần Thân (Zones 1-6, 8)               | Sep|    Phần Mở rộng    |

Zone Map: Z1=E-F | Z2=G-H(R6-7) | Z3=G-H(R8+) | Z4=I(R8+) | Z5=G-H(All) | Z6=I(All) | Z7=K-L(All) | Z8=I(Com) | Z9=K-L(Com)
V-gate: Z3[x/y] Sync[a=N,c=N] E5E8[=B5] Layout[Ncol,B2:X2] ZoneBound[ok] Cite[ok|n/a] TermCheck[ok] DEP[n/a] Score[n/a] Temporal[n/a]
Quality: X.X/10 {rating} [{dimension scores}]
```

**Adaptation rules:**
- Single-Feature (f=1): Remove col H, shift Conso. to H, use Template C layout
- Level 2 (L2=1): Insert col G for sub-items, shift Zone 2 to H+, use Template B layout
- Multi-Feature (f=3-5): Extend Feature cols per PART 2a Scaling Formula
- Preview engages user: "Structure looks correct? [y] Generate Excel / [n] Adjust"

### Format H: BUILD SPEC (JSON for GENERATE phase)
> Purpose: Machine-readable specification enabling deterministic Excel generation via `scripts/generate-gnm.py`.
> Trigger: When CREATE phase should output a Build Spec for later GENERATE phase. Use for complex GNMs (n>10 or f>3) or when explicitly requested.

### Format I: MARKDOWN EXPORT (Excel → Markdown)
> Purpose: Standardized markdown representation of GNM Excel workbooks for downstream HTML/web rendering, version control, and LLM context.
> Trigger: EXPORT task with `--format md` or `--format markdown`, or when user requests "convert to markdown", "export as markdown", "xuất ra markdown".
> **Full spec:** See `part-5-format-i-markdown.md`
> **Key rule:** Conso and Common items MUST use bullet lists, NEVER comma-separated.

**Output:** Save as `_bmad-output/{CODE}-{Level}-build-spec.json`

**Structure:** See Part 14 §8 for the full Build Spec JSON schema. Key fields:
- `gnm`: name, code, level, sheet_name
- `layout`: f, L2, n, a, c
- `zone1-9`: all zone content
- `parent`: for sub-GNMs (sheet name + backlink flag)

**Usage after CREATE:**
```bash
python3 .claude/skills/gnm/scripts/generate-gnm.py <build-spec.json> [output.xlsx]
```

The script validates the spec, computes layout, and generates Excel following the 5-phase write order. Zero LLM tokens needed for rendering.

