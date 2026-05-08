# Question Tree — domain-driven interview (MVP, L1)

> **Core principle:** The AI never asks the user structural questions ("how many items?", "list the features"). Those assume the user already knows GNM. Instead the AI asks **domain questions** ("who uses this? what work happens here?"), then **proposes the GNM structure itself** and lets the user confirm, edit, or push back.
>
> The user's job is domain knowledge. The AI's job is structure. The 8 push-back triggers from `pushback-triggers.md` apply to the AI's own proposals (the AI must self-check before showing a proposal) and to user overrides of valid structure.

The interview computes the next question by inspecting which spec fields are still missing. Render triggers are marked **[RENDER]** — call `bash scripts/render.sh` after the user's answer is written back.

---

## Phase 0 — Boot

On `/gnm-interview` invocation:
1. If `workspace/spec.json` exists, ask: "Resume previous session, or start fresh?" Archive old to `workspace/archive/{timestamp}-spec.json` if fresh.
2. Otherwise, create empty spec stub with `schema_version: "gnm-interview/1.0"`, `gnm.level: 1`, `gnm.is_final: true`.
3. Tell user: "I'll ask about your domain, then propose the GNM structure. Live `.xlsx` updates at `workspace/current.xlsx`."

---

## Phase 1 — Bootstrap (B1–B4)

Short identifying questions only. No structure yet.

| # | EN | VI | Validation | Spec field |
|---|---|---|---|---|
| B1 | "English or Tiếng Việt?" | (same) | enum `en` / `vi` | `session.lang` |
| B2 | "What's this GNM about, in one sentence?" | "GNM này nói về điều gì, tóm tắt một câu?" | reject < 5 words; if vague, suggest a candidate sentence and let user accept | `gnm.purpose` |
| B3 | "3-letter uppercase code? (e.g. FDM, MRC)" | "Mã 3 ký tự viết hoa? (ví dụ: FDM, MRC)" | regex `^[A-Z]{3}$`; if longer, propose 2 truncations | `gnm.code` |
| B4 | "Full GNM name? (becomes the title cell)" | "Tên đầy đủ của GNM? (sẽ thành ô tiêu đề)" | non-empty, ≤ 60 chars | `gnm.name` |

After B4: tell user "L1 (root); cascade is v2." No render yet — renderer needs `n ≥ 1` and `f ≥ 1`.

---

## Phase 2 — Domain discovery (D-questions)

The AI asks 2–4 open-ended questions to gather enough context to propose Zone 1 + Zone 2 confidently.

> **Framing rule:** every D-question must orient toward **business value / monetization** — how this thing helps the business make money, save money, reduce risk, or open new markets. Never frame around audience ("who uses it?"), org ("which team owns it?"), or operational lens ("what's the tech stack?"). A GNM is a strategy tool; org-based framing produces an org chart, not a strategy.

Templates (all monetization-framed):

| Template | Use when |
|---|---|
| "How does this {topic} help the business make money — directly or indirectly? Where's the value created?" | Always — opens the monetization angle |
| "Which revenue, cost, or risk levers does this touch?" | When B2 was abstract |
| "If you had to defend this in a board meeting, what's the business-value pitch?" | When the user is stuck — forces the strategic frame |
| "What's the monetization mechanism — revenue uplift, cost reduction, risk reduction, or new revenue stream?" | After the first answer, to sharpen |
| "What outcomes signal this is working? What numbers move?" | Helps surface features (TODO axis) as outcome-driving actions |

**Anti-templates — never use these:**
- ❌ "Who's the audience? Who reads this?" → A GNM is a *standardized language* — audience is always "everyone, by design". The question is conceptually meaningless. Asking it produces persona-targeted items that defeat the universal-legibility purpose.
- ❌ "Which teams own this?" → produces org-chart items
- ❌ "What's the tech stack / data flow?" → produces operational items
- ❌ "How is it organized today?" → bakes in the existing structure instead of designing one

The audience/team/tech may come up implicitly in the user's answers — that's fine — but the AI's organizing axis must be business-value, not org or audience.

Stop asking when the AI can propose Z1+Z2 under monetization framing. Typical: 2 questions, sometimes 3, rarely 4.

**Spec impact:** the AI writes `session.domain_notes` summarizing **business-value mechanisms** learned. This drives the propose step.

---

## Phase 3 — Zone 1 (propose → confirm)

The AI proposes:
- **Items** (4–7 by default) — concrete nouns framed by **business-value lens** (revenue impact area, monetization mechanism, value-chain stage). Never by audience or org.
- **Perspective** (one phrase) — must name a *value lens*: e.g. "monetization technique", "revenue-impact area", "business-value pillar", "P&L lever". Not "team", "audience", "data domain" (these are operational).

> **Self-check before proposing:** if the proposed items would just as easily appear on an org chart or audience map, redo the proposal under monetization framing. Example: for "AI & Data" department — wrong: {Research, Productization, Deployment}; right: {Revenue Uplift via Personalization, Cost Reduction via Automation, Risk Reduction via Fraud Detection, New AI-as-a-Service Revenue}.

Format:
```
Mình đề xuất Zone 1 (trục WHAT):

  Perspective: data domain
  Items:
    1. {item}
    2. {item}
    3. {item}
    4. {item}

Bạn confirm, sửa (vd "đổi item 2 thành X"), hay muốn mình propose lại?
```

User options:
- `ok` / `confirm` → write to spec, **[RENDER]** Z1 stub
- "đổi {N} thành {X}" → swap one item
- "thêm {Y}" / "bỏ {N}" → add/remove
- "propose lại với perspective {Z}" → AI re-proposes
- "let me list myself" → AI accepts user's list, but applies pushback triggers #2 (verbs) and #7 (mixed perspective) to the user's list

Self-check before proposing (AI must apply triggers to its own proposal):
- **Business-value framing** — items name P&L levers, monetization mechanisms, or revenue-impact areas (NOT teams, NOT audiences, NOT tech components)
- No verb-items (trigger #2)
- 2 ≤ count ≤ 7 (trigger #8)
- Coherent perspective (trigger #7) — perspective is a value lens
- Not the same taxonomy AI plans to use for Z2 (trigger #3)

If the AI can't satisfy these, it asks one more D-question (monetization-framed) instead of proposing.

**Spec fields:** `layout.n`, `zone1.items[].l1`, `zone1.perspective`.

---

## Phase 4 — Zone 2 (propose → confirm)

Same model. AI proposes:
- **Features** (2–4 by default — single-feature is legacy)
- **Feature group** (header, e.g. "Operations", "Data Lifecycle")

Format:
```
Mình đề xuất Zone 2 (trục TODO):

  Feature group: Data Lifecycle
  Features: Ingestion → Modeling → Consumption

Confirm/sửa/propose lại?
```

Self-check before proposing:
- **Value-creation framing** — features are actions/phases that *translate items to business outcomes* (e.g. Discover → Activate → Measure → Optimize; Acquire → Convert → Retain → Expand). NOT technical lifecycle (Ingestion → Modeling → Storage), NOT org phases (Plan → Build → Run).
- f ≥ 2 (trigger #4 — never propose f=1)
- Features are verbs/perspectives, not nouns (trigger #5)
- Features aren't mirror of items (trigger #3)
- Features form a coherent business-value flow (value-creation arc, customer journey, P&L stages)

User confirm → **[RENDER]** Z1 + Z2 frame, empty Z3.

**Spec fields:** `layout.f`, `zone2.features`, `zone2.feature_group`.

---

## Phase 5 — Zone 3 (propose where possible, ask where not)

Loop over each cell `(i, j)` in row-major order. For each cell:

1. **AI tries to propose first.** If the AI has a plausible guess from domain notes (e.g. for `Finance DataMart × Modeling`, plausible guess "Star schema design"), propose it: *"Cho {item} × {feature}, mình đề xuất: `{proposed value or engine}`. Confirm/sửa/skip?"*
2. **If AI has no plausible guess**, ask: *"Cho {item} × {feature}, ô này nên là gì? (giá trị, engine: tên, hoặc skip để để '—')"*
3. User options:
   - `ok` / confirm
   - free text → overwrite proposal
   - `engine: <name>` → recorded as engine
   - `skip` → recorded as `—`
   - `…` → placeholder, comes back later

Self-check on every proposal:
- No vague engine names (trigger #6: not `System`, `Tool`, `Process` standalone)
- ≤ 50 chars

**[RENDER]** after every full row (every f cells filled).

**Spec field:** `zone3[i][j]`.

---

## Phase 6 — Zone 4 (propose Conso engines)

For each item i, the AI proposes the consolidated engine for that row:

> "Cho dòng *{item_i}*, engine tổng hợp: `{proposed engine}`. Confirm/sửa?"

Self-check:
- Differs from any single Z3 cell in that row
- ≤ 50 chars, self-descriptive (trigger #6)

User confirm → **[RENDER]**.

**Spec field:** `zone4[i]`.

---

## Phase 7 — Zones 5–9 (propose with skip-default)

The AI tells user: *"Bây giờ đến các dòng aggregation (All / Common). Mình sẽ đề xuất từng ô — bạn confirm, sửa, hoặc skip để để trống."*

Defaults: `layout.a = 2`, `layout.c = 2`.

Loop in this order, per cell, AI proposes (or marks "no plausible proposal — skip?"):

| Phase | Position | AI proposal source |
|---|---|---|
| Z5 | All-cluster row 1, per feature column | aggregate engine for that feature |
| Z5 | All-cluster row 2, per feature column | secondary aggregate or empty |
| Z6 | All-cluster row 1, Conso column | overall conso engine |
| Z6 | All-cluster row 2, Conso column | usually empty |
| Z7 | All-cluster row 1, extended cols | lateral references (strategy/org) |
| Z8 | Common-cluster row 1, Conso col | parent/peer reference |
| Z9 | Common-cluster row 1, extended cols | other common refs |

When AI has no plausible guess, ask: *"Common row 1 — engine tham chiếu cha/peer? (skip để bỏ qua)"*.

**[RENDER]** after each row of Z5/Z7/Z9; after each Z6/Z8 entry.

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

- **"Change item 2 to X"** → AI edits `zone1.items[1].l1`, **[RENDER]**, asks "Z3 row 2 still valid? Cells: {list}". User confirms or asks AI to re-propose.
- **"Add a feature 'Quality'"** → AI extends `zone2.features`, pads `zone3[*]` with `…`, **[RENDER]**, then propose-loops the new column.
- **"Drop item 2"** → AI removes from `zone1.items`, `zone3`, `zone4`, **[RENDER]**.
- **"Show me what you have"** → render current spec, list field-fill status: `Z1 ✓ Z2 ✓ Z3 partial (5/12) Z4 ✗ Z5–9 ✗`.
- **"Re-propose Z2"** → AI re-runs Phase 4 with current domain notes.

---

## Push-back direction (inverted vs structural-questions model)

Old model: user gives raw answer, AI checks against rules, pushes back.

New model:
- **AI's proposal** is self-checked against all 8 triggers BEFORE being shown. The AI never proposes a structural violation.
- **User overrides** still trigger the 2-step re-confirmation (e.g. user says "I want item: 'Manage Reports'" — AI fires trigger #2, asks for re-confirm, logs warning if user insists).
- **User pushes back on AI's proposal** → AI asks one more domain question and re-proposes. Not a logged warning — just iteration.

The `warnings[]` log is reserved for user-overridden rule violations only.

---

## Field-fill state machine

The AI determines the next phase by inspecting these fields in priority order:

1. `session.lang` empty → B1
2. `gnm.purpose` empty → B2
3. `gnm.code` empty → B3
4. `gnm.name` empty → B4
5. `session.domain_notes` empty/insufficient → Phase 2 (D-questions)
6. `layout.n == 0` → Phase 3 (propose Z1)
7. `layout.f == 0` → Phase 4 (propose Z2)
8. any `zone3[i][j]` is null/`…` → Phase 5 (per-cell propose-or-ask)
9. any `zone4[i]` is null → Phase 6 (propose Conso)
10. user hasn't been offered Z5–9 yet → Phase 7 entry
11. user typed `done` or all Z5–9 cells answered/skipped → F1

User can jump phases ("go to Z3") — AI auto-fills missing prior fields with proposals + asks "OK?" before jumping.
