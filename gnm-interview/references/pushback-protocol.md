# Push-back Protocol — 2-step re-confirmation

When a trigger from `pushback-triggers.md` fires, the AI follows this 4-step flow uniformly. The user can override any rule, but only after explicit re-confirmation, and only with a logged warning.

## The 4 steps

### Step 1 — Name the rule + cite the user's evidence

State the GNM rule in one sentence. Quote the specific value the user gave. Do not lecture.

> "GNM rule: Zone 2 features must be TODO verbs, not WHAT nouns. You wrote `Cards` as feature 3 — `Cards` is a noun-product."

### Step 2 — Propose 2 concrete alternatives

Always offer two. Specific, not abstract. The user can pick either, write their own, or override.

> "Try: (a) `Issuance` if you mean creating cards, (b) `Settlement` if you mean clearing. Or move `Cards` to Zone 1 and pick a new TODO verb."

### Step 3 — If the user insists on the original answer

Restate the rule one more time, ask for explicit confirmation:

> "Heard you. To confirm: you want `Cards` as a Zone 2 feature, even though it's a WHAT noun? This will be logged as a rule override. Reply `yes` (or `có`) to proceed."

The user MUST reply `yes` / `có` (case-insensitive). Anything else returns to Step 2.

### Step 4 — On confirmation: log + stamp

Append to `spec.warnings[]`:

```json
{ "trigger": 5, "field": "zone2.features[2]", "value": "Cards", "user_ack": true }
```

The renderer reads `warnings[]` and stamps `⚠ N rule overrides logged` into cell `B1`. The flow proceeds to the next question.

---

## Bilingual rule statements

Indexed by trigger # from `pushback-triggers.md`.

### Trigger 1 — Empty Z3 cell

- **EN:** "Every WHAT × TODO intersection must have content — Critical Rule #1."
- **VI:** "Mỗi giao điểm WHAT × TODO phải có nội dung — đây là Nguyên tắc cốt lõi #1."

### Trigger 2 — Items are verbs

- **EN:** "Zone 1 items are nouns. *{item}* reads as an action."
- **VI:** "Hạng mục Zone 1 phải là danh từ. *{item}* nghe như một hành động."

### Trigger 3 — Z1 ≡ Z2 taxonomy

- **EN:** "Items and features look like the same taxonomy. Identity Matrix is only valid if deliberate."
- **VI:** "Hạng mục và tính năng có vẻ dùng cùng một phân loại. Identity Matrix chỉ hợp lệ khi cố ý."

### Trigger 4 — Single feature

- **EN:** "Multi-feature (2–5) is the default. Single feature collapses the matrix structure."
- **VI:** "Mặc định là nhiều tính năng (2–5). Một tính năng làm mất cấu trúc ma trận."

### Trigger 5 — Z2 entry is WHAT

- **EN:** "*{feature}* is a noun. Features must be verbs/perspectives."
- **VI:** "*{feature}* là danh từ. Tính năng phải là động từ/góc nhìn."

### Trigger 6 — Vague / long engine

- **EN (vague):** "*{name}* is too generic. Engine names must be self-descriptive, ≤ 50 chars."
- **EN (long):** "*{name}* is {N} chars; max is 50."
- **VI (vague):** "*{name}* quá chung chung. Tên engine cần tự mô tả, tối đa 50 ký tự."
- **VI (long):** "*{name}* dài {N} ký tự; tối đa 50."

### Trigger 7 — Mixed perspective

- **EN:** "Your items mix perspectives. Pick one lens for the whole list."
- **VI:** "Hạng mục của bạn trộn nhiều góc nhìn. Hãy chọn một lăng kính chung."

### Trigger 8 — n=1 degenerate

- **EN:** "GNM needs ≥ 2 items — otherwise it's a list, not a matrix."
- **VI:** "GNM cần ≥ 2 hạng mục — nếu không thì đó là danh sách, không phải ma trận."

---

## Vietnamese tone notes

Direct translation of the English flow can sound abrupt. Soften with:

- Open with `Mình hơi lăn tăn rằng...` ("I'm a little hesitant that...") instead of bare rule statement.
- Replace `Are you sure?` with `Bạn có chắc không?` (gentler) rather than `Bạn chắc chắn không?` (formal-blunt).
- Use `nhé` particle on counter-questions: `Mình thử như này nhé:` ("Let's try this:") softens the prescriptive tone.
- Avoid `Phải` ("must") in user-facing rule statements; prefer `nên` ("should") in the soft frame, then escalate to `phải` only at the explicit re-confirm step.

The native-tone review is flagged as an open risk — see plan §10. The wording above is a starting point, not a finished translation.

---

## When NOT to push back

- **Trigger 1** when user says `skip` explicitly: that's a documented absence, not a rule violation. Record `—` and move on.
- **Trigger 6** when the user gives an engine name in `[Full Name] CODE` format that fits ≤ 50 chars and isn't on the vague-blacklist: accept silently.
- **Trigger 7** when the AI is genuinely uncertain (this is fuzzy detection): err toward acceptance, log internal uncertainty in `transcript.md` rather than asking the user.
- Any trigger after the user has already overridden it on this exact field in the same session: do not re-fire. Track in `spec.warnings[]`.

---

## Override cap (informal)

If a single session accumulates `len(warnings) ≥ 3`, the AI should ask:

> "I've logged 3 rule overrides so far. Want to step back and review the structure, or keep going?"

This is a soft check, not a hard block. User can keep going. Logged in transcript.
