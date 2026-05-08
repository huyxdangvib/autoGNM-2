# Vietnamese Glossary — gnm-interview

Bilingual mapping for user-facing terms. Technical anchors (Zone, Engine, Level, Conso) stay in English per VIB convention; domain language follows user's choice.

## Structural terms

| English | Tiếng Việt | Notes |
|---|---|---|
| GNM | GNM | Untranslated — proper noun |
| Zone (1–9) | Zone (1–9) | Untranslated |
| Item | Hạng mục | Zone 1 row label |
| Feature | Tính năng | Zone 2 column label |
| Feature group | Nhóm tính năng | Zone 2 header (row 6) |
| Engine | Engine / Cỗ máy | Prefer "engine" in technical contexts; "cỗ máy" only in introductory copy |
| Value | Giá trị | Zone 3 cell content (numeric/text) |
| Conso. (Consolidated) | Conso. | Untranslated — column header in Excel |
| All cluster | Cụm All | Aggregation rows |
| Common cluster | Cụm Common | Aggregation rows |
| Mở rộng (extended) | Mở rộng | Already Vietnamese in canonical layout |
| Phần Đầu | Phần Đầu | Already Vietnamese |
| Phần Thân | Phần Thân | Already Vietnamese |
| Cascade | Cascade / phân cấp | "Cascade" preferred in technical text |
| Sheet | Sheet / trang | "Sheet" in workbook context |
| Sub-sheet | Sheet con | |
| Backlink | Liên kết ngược | |
| HYPERLINK | HYPERLINK | Untranslated — Excel formula name |
| Override | Bỏ qua quy tắc | Literally "skip the rule" |
| Final / leaf | Cuối / lá | "Cuối" in B2 suffix; "lá" in conceptual text |

## Action verbs (interview prompts)

| English | Tiếng Việt |
|---|---|
| List | Liệt kê |
| Confirm | Xác nhận |
| Skip | Bỏ qua / `skip` |
| Resume | Tiếp tục |
| Start fresh | Bắt đầu mới |
| Go back / change | Quay lại / thay đổi |
| Render | Render / vẽ lại |
| Done | Xong |
| Are you sure? | Bạn có chắc không? |

## Push-back softeners

Use these to keep the 4-step flow polite in Vietnamese:

| Function | Phrase |
|---|---|
| Soft hesitation opener | `Mình hơi lăn tăn rằng…` |
| Soft suggestion | `Mình thử như này nhé:` |
| Re-confirm | `Bạn có chắc không?` (gentler than `Bạn chắc chắn không?`) |
| Logging notice | `Mình sẽ ghi lại như một lần bỏ qua quy tắc.` |
| Acknowledge override | `Đã ghi nhận. Tiếp tục nhé.` |

## Status labels (transcript / state messages)

| English | Tiếng Việt |
|---|---|
| In progress | Đang tiến hành |
| Completed | Hoàn thành |
| Skipped | Đã bỏ qua |
| Pending | Đang chờ |
| Override logged | Đã ghi nhận bỏ qua quy tắc |

## What stays English

- Zone numbers and Z1/Z2/Z3 codes
- Engine codes (`ESD`, `ACO`, `LCW`)
- File extensions, formula names (`HYPERLINK`, `=ROW()`)
- The `L{n}` / `L{n}F` filename and B2 suffix flags (only the word "Final" → "Cuối" changes between EN and VI)
- "Conso.", "All", "Common" cell-label text in the rendered Excel (these are Excel column/row labels, not user prose)
