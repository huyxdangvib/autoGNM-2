# Question Tree — canonical interview sequence (MVP, L1)

The interview follows a fixed sequence. The AI computes the next question by inspecting which fields in `workspace/spec.json` are still missing or empty. Render triggers are marked **[RENDER]** — call `bash scripts/render.sh` after the user's answer is written back.

Wording below is a starting template; adapt to user's tone. EN and VI both shown for the questions the user actually sees.

---

## Phase 0 — Boot

On `/gnm-interview` invocation:
1. If `workspace/spec.json` exists, ask: "Resume previous session, or start fresh?" If fresh, archive the old one to `workspace/archive/{timestamp}-spec.json`.
2. Otherwise, create a new empty spec stub with `schema_version: "gnm-interview/1.0"` and `gnm.level: 1, gnm.is_final: true`.
3. Tell the user: "I'll ask one question at a time and we'll build the GNM together. Your live `.xlsx` updates after each meaningful answer in `workspace/current.xlsx`."

---

## Phase 1 — Bootstrap (B1–B4)

| # | EN | VI | Validation | Spec field |
|---|---|---|---|---|
| B1 | "English or Tiếng Việt?" | (same) | enum `en` / `vi` | `session.lang` |
| B2 | "What's this GNM about, in one sentence?" | "GNM này nói về điều gì, tóm tắt một câu?" | reject < 5 words or vague placeholders | `gnm.purpose` |
| B3 | "3-letter uppercase code? (e.g. ESD, MRC)" | "Mã 3 ký tự viết hoa? (ví dụ: ESD, MRC)" | regex `^[A-Z]{3}$`; if 4+ chars given, propose 2 truncations | `gnm.code` |
| B4 | "Full GNM name? (becomes the title cell)" | "Tên đầy đủ của GNM? (sẽ thành ô tiêu đề)" | non-empty, ≤ 60 chars | `gnm.name` |

After B4 → **[RENDER]** empty shell. Tell user: "This is L1 (root). Cascade to deeper levels is v2."

---

## Phase 2 — Zone 1 (Items)

### Z1.1 — count

- **EN:** "How many items on the WHAT axis? (typically 2–7)"
- **VI:** "Bao nhiêu hạng mục trên trục WHAT? (thường 2–7)"
- **Validation:** int ≥ 1
- **Push-back:** trigger #8 if `n=1`; soft challenge if `n > 9`
- **Field:** `layout.n`

### Z1.2 — names

- **EN:** "List the {n} items, one per line."
- **VI:** "Liệt kê {n} hạng mục, mỗi dòng một mục."
- **Validation:** count matches n
- **Push-back:** trigger #2 (verbs), trigger #7 (mixed perspective)
- **Field:** `zone1.items[].l1`

### Z1.3 — perspective

- **EN:** "What perspective ties these together? (product line / customer segment / lifecycle stage / channel / region / …)"
- **VI:** "Lăng kính chung của các hạng mục là gì? (dòng sản phẩm / phân khúc khách hàng / giai đoạn vòng đời / kênh / khu vực / …)"
- **Validation:** non-empty
- **Field:** `zone1.perspective`

### Z1.4 — confirm

- **EN:** "Confirm Zone 1: {item list}. Proceed?"
- **VI:** "Xác nhận Zone 1: {danh sách}. Tiếp tục?"
- **On yes:** **[RENDER]** Zone 1 stub.

---

## Phase 3 — Zone 2 (Features)

### Z2.1 — count

- **EN:** "How many features on the TODO axis? (1–5)"
- **VI:** "Bao nhiêu tính năng trên trục TODO? (1–5)"
- **Validation:** int 1..5
- **Push-back:** trigger #4 if `f=1`
- **Field:** `layout.f`

### Z2.2 — names

- **EN:** "List the {f} features."
- **VI:** "Liệt kê {f} tính năng."
- **Validation:** count matches f
- **Push-back:** trigger #5 (WHAT-not-TODO), trigger #3 (mirror items)
- **Field:** `zone2.features`

### Z2.3 — feature group header

- **EN:** "What's the feature group name? (header for the TODO axis — e.g. 'Operations', 'Annual Calendar')"
- **VI:** "Tên nhóm tính năng? (tiêu đề trục TODO — ví dụ 'Vận hành', 'Lịch năm')"
- **Validation:** non-empty
- **Field:** `zone2.feature_group`
- **On answer:** **[RENDER]** Z1 + Z2 frame, empty Z3.

---

## Phase 4 — Zone 3 (Cells, n × f)

Loop over each cell `(i, j)` in row-major order.

For each cell:

- **EN:** "*{item_i}* × *{feature_j}* — what value or engine goes here?
  - Free text for a value
  - `engine: <name>` for a hyperlink-style engine
  - `skip` to leave as `—`
  - `…` to come back later"
- **VI:** "*{item_i}* × *{feature_j}* — giá trị hoặc engine ở đây là gì?
  - Văn bản tự do để nhập giá trị
  - `engine: <tên>` cho engine tham chiếu
  - `skip` để để trống `—`
  - `…` để quay lại sau"
- **Validation:** non-empty after re-prompt; reject `…` at finalize
- **Push-back:** trigger #1 (empty), trigger #6 (vague engine)
- **Field:** `zone3[i][j]`

**[RENDER]** after every full row (every f cells filled).

---

## Phase 5 — Zone 4 (Conso engines, n)

Loop over each item.

- **EN:** "For row *{item_i}*, what's the consolidated engine? (one engine summarizing all features for that row, ≤ 50 chars)"
- **VI:** "Cho dòng *{item_i}*, engine tổng hợp là gì? (một engine tóm gọn cả {f} tính năng, tối đa 50 ký tự)"
- **Validation:** non-empty
- **Push-back:** trigger #6 (vague). Custom check: must differ from any Z3 cell in that row — if identical, "Is row *{item_i}* really just feature *{feature_j}*?"
- **Field:** `zone4[i]`

**[RENDER]** after each Z4 entry.

---

## Phase 6 — Zones 5–9 (Aggregation rows, optional)

Tell user: "Now the All / Common aggregation rows. These are skippable — type `skip` to leave a cell blank. Defaults are 2 'All' rows and 2 'Common' rows."

Defaults: `layout.a = 2`, `layout.c = 2`.

### Z5 — All cluster × feature columns (a × f)

For each row r in 1..a, for each feature j in 1..f:
- **EN:** "All-cluster row {r} × *{feature_j}*: aggregation engine? (or `skip`)"
- **VI:** "Dòng All số {r} × *{feature_j}*: engine tổng hợp? (hoặc `skip`)"
- **Field:** `zone5[r-1][j-1]`

### Z6 — All cluster × Conso col (a)

For each row r in 1..a:
- **EN:** "All-cluster row {r}: overall conso engine? (or `skip`)"
- **VI:** "Dòng All số {r}: engine tổng hợp toàn diện? (hoặc `skip`)"
- **Field:** `zone6[r-1]`

### Z7 — All cluster × extended (Mở rộng) cols (a × 2)

For each row r in 1..a:
- **EN:** "All-cluster row {r}: extended engines [left, right]? (or `skip`)"
- **VI:** "Dòng All số {r}: engine mở rộng [trái, phải]? (hoặc `skip`)"
- **Field:** `zone7[r-1]` as `[left, right]`

### Z8 — Common cluster × Conso col (c)

For each row r in 1..c:
- **EN:** "Common-cluster row {r}: parent / peer reference engine? (or `skip`)"
- **VI:** "Dòng Common số {r}: engine tham chiếu cha/ngang hàng? (hoặc `skip`)"
- **Field:** `zone8[r-1]`

### Z9 — Common cluster × extended cols (c × 2)

For each row r in 1..c:
- **EN:** "Common-cluster row {r}: other common engines [left, right]? (or `skip`)"
- **VI:** "Dòng Common số {r}: engine common khác [trái, phải]? (hoặc `skip`)"
- **Field:** `zone9[r-1]` as `[left, right]`

**[RENDER]** after each row of Z5/Z7/Z9 (per-row, not per-cell). Z6 and Z8 render after each entry.

---

## Phase 7 — Finalize (F1)

- **EN:** "Done. Final render? [Y/n]"
- **VI:** "Xong. Render bản cuối? [Y/n]"
- **On yes:**
  1. Reject if any `zone3` cell is `…` (placeholder) — list the cells.
  2. **[RENDER]** to `workspace/{code}-L{level}F-gnm.xlsx`.
  3. Save `transcript.md` to same directory as the final .xlsx.
  4. Print summary: warnings count, file path, sheet name.

---

## Editing / backtracking

User can interrupt at any phase:

- **"Change Zone 1 item 2 to X"** → AI edits `zone1.items[1].l1`, runs **[RENDER]**, asks "Engines in row 2 still valid? (Z3 row 2: {cells})". If user wants to redo Z3 for that row, loop back into Phase 4 for `(i=1, j=0..f-1)`.
- **"Change f to 4"** → AI extends `zone2.features` (asks for the new feature name), pads `zone3[*]` with `…`, rerenders, then loops back into Phase 4 to fill the new column.
- **"Change n to 3"** (was 4) → AI asks which item to drop, removes it from `zone1.items`, `zone3`, `zone4`, rerenders.
- **"Show me what you have"** → render current spec, list field-fill status: `Z1 ✓ Z2 ✓ Z3 partial (5/12 cells) Z4 ✗ Z5–9 ✗`.

---

## Field-fill state machine (for AI's question-picking logic)

The AI determines the next question by inspecting spec fields in this priority order:

1. `session.lang` empty → B1
2. `gnm.purpose` empty → B2
3. `gnm.code` empty → B3
4. `gnm.name` empty → B4
5. `layout.n` empty → Z1.1
6. `zone1.items` length < n → Z1.2
7. `zone1.perspective` empty → Z1.3
8. `layout.f` empty → Z2.1
9. `zone2.features` length < f → Z2.2
10. `zone2.feature_group` empty → Z2.3
11. any `zone3[i][j]` is null/`…` → Phase 4 loop
12. any `zone4[i]` is null → Phase 5 loop
13. user hasn't been offered Z5–9 yet → Phase 6 entry
14. user typed `done` or all Z5–9 cells answered/skipped → F1

Skipping forward: user can say "go to Z3" — AI auto-fills missing prior fields with sensible defaults (and asks "is that OK?") then jumps to Z3.
