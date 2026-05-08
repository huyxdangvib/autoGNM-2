# Question Tree — AI-leading, lazy-first interview (MVP, L1)

> **Core principle:** The AI does the work. The user confirms or corrects. Whenever the AI can plausibly guess an answer from prior context, it pre-populates and asks for confirmation rather than asking the question open-ended. Humans are lazy by design — the skill maximizes that.
>
> The user provides domain knowledge. The AI provides everything else: structure, vocabulary, defaults, candidate alternatives. The 8 push-back triggers from `pushback-triggers.md` are applied by the AI **to its own batch outputs before showing them** (self-check). User overrides go through 2-step re-confirmation only when they violate structure.

The interview computes the next phase by inspecting which spec fields are still missing. Render triggers are marked **[RENDER]** — call `bash scripts/render.sh` after the user's answer is written back.

---

## Phase 0 — Boot

On `/gnm-interview` invocation:
1. If `workspace/spec.json` exists, ask: "Resume previous session, or start fresh?" Archive old to `workspace/archive/{timestamp}-spec.json` if fresh.
2. Otherwise, create empty spec stub with `schema_version: "gnm-interview/1.0"`, `gnm.level: 1`, `gnm.is_final: true`.
3. Tell user: "Mình sẽ tự đề xuất cấu trúc GNM dựa trên một câu mô tả ngắn của bạn. Bạn confirm/sửa từng bước. Live `.xlsx` ở `workspace/current.xlsx`."

---

## Phase 1 — Bootstrap

> **B1 is unconditional and always fires first.** Never infer language from chat context, never skip on resume.

### B1 — Language

- "English or Tiếng Việt?"
- enum `en` / `vi` → `session.lang`

### B2-batch — Topic + identity

Ask one question for the topic:
- EN: "What's this GNM about? Just a short phrase or sentence is fine."
- VI: "GNM này về cái gì? Một cụm hoặc một câu ngắn là đủ."

User answers (e.g. "Finance DataMart"). AI then **proposes purpose + code + name in a single batch**:

```
Mình suggest:
  • Tên đầy đủ:  Finance DataMart
  • Code:        FDM    (alts: FDT, FDD)
  • Purpose:     Finance DataMart là kho dữ liệu tài chính tập trung
                 phục vụ báo cáo quản trị và phân tích.

Confirm hết, hay sửa cái nào? (vd "code: FDT" / "rewrite purpose: ...")
```

User options:
- `ok` → all three accepted
- "code: FDT" → swap code only
- "rewrite purpose: …" → user supplies new purpose
- "rewrite name: …" → user supplies new name
- "redo all" → AI re-proposes with different angle

Self-check: code matches `^[A-Z]{3}$`, name ≤ 60 chars, purpose ≥ 5 words.

**Spec fields:** `gnm.purpose`, `gnm.code`, `gnm.name`, `gnm.sheet_name` (derived as `"{code} (L1)"`).

After confirm: tell user "L1 (root); cascade là v2." No render yet (renderer needs `n ≥ 1`, `f ≥ 1`).

---

## Phase 2 — Domain discovery (AI guesses, user confirms)

Goal: gather enough context to propose Z1 lens + items + Z2 flow + features. The AI **leads with confidence-ranked guesses**, not open-ended questions.

> **Framing rule:** lock the **intended audience** first (D0), then frame everything downstream in that audience's language. Exec audience → business / monetization lens. Practitioner audience → capability / teaching / workflow lens. Operator audience → process / value-stream lens. Customer audience → outcome / job-to-be-done lens. Don't default to monetization framing for non-business audiences. See `good-gnm-distilled.md` § "audience axiom".

### D0 — Audience (lead with guess)

Format:
```
Mình đoán GNM này dành cho:
  ✓ Exec / business owner          (đọc để ra quyết định P&L)
  · Practitioner (dev / analyst)   (đọc để học hoặc làm)
  · Operator / ops team            (đọc để vận hành quy trình)
  · Customer / external user       (đọc để hiểu outcome)

Đúng không? Hay khác?
```

Audience drives every framing decision below. If audience changes mid-session, AI must re-propose Z1 lens / Z2 flow under the new audience.

**Spec field:** `session.audience` (one of: `exec`, `practitioner`, `operator`, `customer`, or free-text).

### D1 — Value mechanism (lead with guess)

Format:
```
Mình đoán {topic} tạo ra value chủ yếu qua:
  ✓ Cost reduction       (tự động hoá / efficiency)
  ✓ Speed to insight     (quyết định nhanh hơn = outcomes tốt hơn)
  · Risk reduction       (tránh tổn thất / regulatory)
  · Revenue uplift       (revenue mới / pricing power)
  · New market access    (capability mở segments mới)

Đúng không? Hay đổi cái nào? (vd "không có cost reduction, có thêm revenue uplift")
```

✓ = AI's guess (1–3 marked); · = alternates (user can promote).

User options: `ok`, "thêm X / bỏ Y", "redo guess".

### D2 — Outcome metrics (only if D1 was thin)

If D1 answer was a single mechanism or vague, ask D2 to sharpen — same lead-with-guess format:
```
Outcome chính có lẽ là:
  ✓ Time-to-report       (rút ngắn report cycle)
  ✓ Decision accuracy    (giảm sai số trong forecast/budget)
  · Compliance coverage  (rủi ro audit findings)

Đúng không?
```

**Stop after D1 (or D1+D2 max).** Don't drag — the propose step is where real iteration happens.

**Spec impact:** AI writes `session.domain_notes` (free string) summarizing the value mechanisms locked in.

---

## Phase 3 — Zone 1 (two-level batch propose)

Rows decompose as *lens → items*. Lens first because it's debatable in one phrase; bad lens means re-doing items.

### Phase 3.1 — Row lens (propose with primary + alternates)

Candidate lenses (filter by audience locked at D0):

| Lens | Audience fit | Use when |
|---|---|---|
| **P&L lever** | exec | Topic touches revenue / cost / risk on a financial statement |
| **Monetization technique** | exec | Topic is a capability with multiple ways to convert into money |
| **Revenue-impact area** | exec | Topic spans business units or product lines that each generate revenue |
| **Value-chain stage** | exec / operator | Horizontal capability supporting upstream/downstream |
| **Customer-value pillar** | exec / customer | Customer-facing; value emerges across segments |
| **Capability area** | practitioner | Roadmap / learning topic; rows are skills or domains to master |
| **Concept cluster** | practitioner | Teaching / education topic; rows are concept families |
| **Workflow stage** | practitioner / operator | Day-to-day work decomposes into stages |
| **Process / value-stream stage** | operator | Operational topic decomposes into Acquire→…→Recover or similar |
| **Outcome / JTBD** | customer | External-facing; rows are customer jobs-to-be-done |

AI picks recommended lens(es) based on `session.audience` first, then `session.domain_notes`. Show 1 ✓ recommended + 2 alternates. If audience is `practitioner`, never recommend "P&L lever" as primary.

Format:
```
Frame các dòng theo lens:
  ✓ P&L lever            (recommended — domain notes nói về cost-to-serve, NIM, fee income)
  · Monetization technique
  · Value-chain stage

OK với P&L lever, hay đổi sang alt?
```

User options: `ok`, "dùng monetization technique", "propose lens khác".

**Spec field:** `zone1.perspective`.

### Phase 3.2 — Row items (batch propose)

After lens locks, AI proposes 4–6 items as a batch:

```
Dưới lens "P&L lever", 4 dòng:
  1. NIM optimization
  2. Fee income visibility
  3. Cost-to-serve reduction
  4. Risk-weighted asset efficiency

Confirm hết, hay sửa? (vd "đổi 2 thành 'Liquidity cost'", "thêm 'Capital efficiency'", "redo all")
```

Self-check before showing:
- **Lens-consistent** — every item is a clean instance of the locked lens
- No verb-items (trigger #2)
- 2 ≤ count ≤ 7 (trigger #8)
- Coherent under the lens (trigger #7)
- Not the same taxonomy AI plans for Z2 (trigger #3)

If lens makes good items hard to enumerate (< 3 candidates), AI proposes a different lens — that's a signal the lens is wrong.

After confirm → **[RENDER]** Z1 stub.

**Spec fields:** `layout.n`, `zone1.items[].l1`.

---

## Phase 4 — Zone 2 (two-level batch propose)

Same pattern: pick a flow, then enumerate stages.

### Phase 4.1 — Column flow (propose with primary + alternates)

Candidate flows:

| Flow | Stages (typical) | Use when |
|---|---|---|
| **Value-creation arc** | Discover → Activate → Measure → Optimize | Capability surfaces value; needs a closed loop |
| **Customer journey** | Acquire → Convert → Retain → Expand | Customer-facing, monetization through CLV |
| **P&L stages** | Plan → Earn → Cost → Risk-adjust | Financial outcome decomposition |
| **Decision loop** | Surface → Decide → Act → Measure | Information / analytics / decision-support topics |
| **Strategic pillars** | Strategy → Execution → Control | High-level governance topics |

Format:
```
Cột theo flow:
  ✓ Decision loop        (recommended — FDM là analytics/decision-support)
  · Value-creation arc
  · P&L stages

OK?
```

**Spec field:** `zone2.feature_group`.

### Phase 4.2 — Column features (batch propose)

```
Theo flow "Decision loop", 4 cột:
  1. Surface insights
  2. Inform decisions
  3. Drive actions
  4. Measure impact

Confirm hết, hay sửa?
```

Self-check:
- **Flow-consistent** — features are stages of the locked flow
- f in 2..5 (trigger #4 — never f=1)
- Verbs/perspectives, not nouns (trigger #5)
- Not mirror of items (trigger #3)
- Ordered direction (the LIST has a flow)

After confirm → **[RENDER]** Z1 + Z2 frame, empty Z3.

**Spec fields:** `layout.f`, `zone2.features`.

---

## Phase 5 — Zone 3 (batch fill the entire matrix)

> **Default mode: batch fill.** AI fills the entire `n × f` matrix in one shot using domain notes, then shows the user the matrix for review. User edits cells they disagree with. Cell-by-cell mode is a fallback when user requests it ("walk me through cell by cell").

Format:
```
Mình điền sẵn Z3 (4 dòng × 4 cột). Bạn review và sửa cell nào không OK:

                  Surface       Inform         Drive          Measure
                  insights      decisions      actions        impact
  NIM             Daily NIM    NIM driver     Margin         NIM trend
  optimization    dashboard    decomposition  reset trigger  scorecard
  Fee income      Fee anomaly  Cross-sell     Campaign       Fee
  visibility      monitor      target setter  activation     attribution
  Cost-to-serve   Unit cost    Process ROI    Automation     Cost-trend
  reduction       trends       ranker         pipeline       savings monitor
  RWA efficiency  RWA          Capital        Reweight       RWA-NIM
                  consumption  reallocation   playbook       reconciliation

Cells nào không OK? (vd "[2,3]: Campaign launcher CMP", "redo row 3", "skip [3,2]")
Confirm tất cả: `ok`
```

Cell content types AI picks from:
- **Value** — quantitative or qualitative content (`"15.5%"`, `"Daily"`, `"Lead capture flow"`)
- **Engine** — named referent in `[Full Name] CODE` format (`"Fraud Detection Engine FDE"`)
- **`—`** — explicit non-applicability (when AI judges no plausible content)
- **`…`** — placeholder (rare; only when domain context too thin)

Self-check before showing:
- No empty cells (trigger #1) — every cell has content or explicit `—`
- No vague engines (`System`, `Tool`, `Process` standalone — trigger #6)
- Engine names ≤ 50 chars (trigger #6)

User options:
- `ok` → all cells accepted, **[RENDER]** full matrix
- `[i,j]: <new content>` → edit one cell
- `redo row N` → AI re-proposes that row
- `redo column N` → AI re-proposes that column
- `redo all` → AI re-proposes whole matrix with different angle
- `walk me through` → switch to cell-by-cell mode for this phase

In cell-by-cell mode (fallback): AI proposes one cell at a time, "for *{item} × {feature}*, suggest: `{content}`. OK / sửa / skip?".

**[RENDER]** after every batch update (or every cell in cell-by-cell mode).

**Spec field:** `zone3[i][j]`.

---

## Phase 6 — Zone 4 (batch propose Conso engines)

```
Mình điền sẵn Conso engines (1 engine cho mỗi dòng):

  1. NIM optimization        →  NIM Optimizer NIO
  2. Fee income visibility   →  Fee Intelligence Engine FIE
  3. Cost-to-serve reduction →  Cost Engine CSE
  4. RWA efficiency          →  RWA Engine RWE

Confirm hết, hay sửa? (vd "1: Margin Engine MGE")
```

Self-check:
- Each Conso ≠ any single Z3 cell in that row (forces aggregation)
- ≤ 50 chars, self-descriptive (trigger #6)

After confirm → **[RENDER]**.

**Spec field:** `zone4[i]`.

---

## Phase 7 — Zones 5–9 (batch propose with skip-defaults)

Tell user: *"Bây giờ aggregation rows (All / Common). Mình đề xuất sẵn — bạn confirm/sửa/skip từng cell."*

Defaults: `layout.a = 2`, `layout.c = 2`. Mark `· skip` where AI has no plausible guess; `✓ {engine}` where it does.

Single batch covering all 5 zones:
```
All cluster (rows 1–2):
  Z5 (per feature col):
    Row 1: ✓ Insight Aggregator IGA   ✓ Decision Engine DCE   ✓ Action Hub ACH    ✓ Measurement Engine MSE
    Row 2: · skip                     · skip                  · skip              · skip
  Z6 (Conso col):
    Row 1: ✓ Finance DataMart Conso FDC
    Row 2: · skip
  Z7 (extended cols, [left, right]):
    Row 1: ✓ Strategy Hub STR / · skip
    Row 2: · skip / · skip

Common cluster (rows 1–2):
  Z8 (Conso col):
    Row 1: ✓ Enterprise Data EDM
    Row 2: · skip
  Z9 (extended cols, [left, right]):
    Row 1: ✓ Org Chart ORG / · skip
    Row 2: · skip / · skip

Confirm hết / sửa cell nào / `skip all` / `redo`?
```

User options: `ok`, `[Z6 row 1]: <new>`, `skip all`, `redo`, etc.

After confirm → **[RENDER]**.

---

## Phase 8 — Finalize (F1)

- *"Render bản cuối? [Y/n]"*
- On yes:
  1. Reject if any `zone3` cell is `…`. List the cells.
  2. **[RENDER]** to `workspace/{code}-L{level}F-gnm.xlsx`.
  3. Save `transcript.md` next to the final .xlsx.
  4. Print: warnings count, file path, sheet name.

---

## Editing / backtracking

User can interrupt at any phase:

- **"Change item 2 to X"** → AI edits `zone1.items[1].l1`, **[RENDER]**, asks "Z3 row 2 still valid? Cells: {list}". User confirms or asks AI to re-propose just that row.
- **"Add a feature 'Quality'"** → AI extends `zone2.features`, pads `zone3[*]` with `…`, **[RENDER]**, propose-loops the new column in batch.
- **"Drop item 2"** → AI removes from `zone1.items`, `zone3`, `zone4`, **[RENDER]**.
- **"Show me what you have"** → render current spec, list field-fill status: `Z1 ✓ Z2 ✓ Z3 partial (5/12) Z4 ✗ Z5–9 ✗`.
- **"Re-propose Z2"** → AI re-runs Phase 4 with current domain notes.
- **"Walk me through cell by cell"** during Phase 5 → switch to per-cell mode for the rest of Z3.

---

## Push-back direction (inverted vs structural-questions model)

Old model: user gives raw answer, AI checks against rules, pushes back.

New model:
- **AI's batch output** is self-checked against all 8 triggers BEFORE being shown. The AI never proposes a structural violation.
- **User overrides** that violate triggers go through 2-step re-confirmation (e.g. user says "make item 'Manage Reports'" — AI fires trigger #2, asks for re-confirm, logs warning if user insists).
- **User pushes back on AI's proposal** ("redo all", "use different lens") → AI iterates without warning log. Not a logged warning — just iteration.

The `warnings[]` log is reserved for user-overridden rule violations only.

---

## Field-fill state machine

The AI determines the next phase by inspecting these fields in priority order:

1. `session.lang` empty → B1
2. `gnm.purpose` OR `gnm.code` OR `gnm.name` empty → B2-batch (one ask, batch propose)
3. `session.domain_notes` empty/insufficient → Phase 2 (D1, then optional D2)
4. `zone1.perspective` empty → Phase 3.1 (propose row lens)
5. `layout.n == 0` → Phase 3.2 (batch propose row items)
6. `zone2.feature_group` empty → Phase 4.1 (propose column flow)
7. `layout.f == 0` → Phase 4.2 (batch propose column features)
8. any `zone3[i][j]` is null/`…` → Phase 5 (batch fill matrix)
9. any `zone4[i]` is null → Phase 6 (batch propose Conso)
10. user hasn't been offered Z5–9 yet → Phase 7 (batch propose aggregation)
11. user typed `done` or all Z5–9 cells answered/skipped → F1

User can jump phases ("go to Z3") — AI auto-fills missing prior fields with batch proposals + asks "OK?" before jumping.

If user rejects a lens at 3.1 or flow at 4.1, AI clears the dependent enumeration (`zone1.items` / `zone2.features`) before re-proposing. Lens/flow is upstream of items.
