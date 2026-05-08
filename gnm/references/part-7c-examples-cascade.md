---
part: 7c
name: "Examples: Cascade"
parent: gnm-instruction.md
---

### Example 8: Multi-Sheet CASCADE (A->B->Z)

**User Input:**
> "Create a 3-sheet cascade for Retail Banking Lending: RBL(A) overview, then Mortgage sub-GNM MTG(B), then Mortgage Pricing detail MTG(Z)."

**Expected Response (abbreviated -- focus on cascade-specific elements):**

```
<thinking>
Step 1: Request Type = CREATE (multi-sheet cascade)
Step 2: Parameters:
- Cascade: RBL(A) -> MTG(B) -> MTP(Z)
- Sheet 1: RBL(A) -- Level A, Single-Feature "Lending Products", 3 items (Mortgage, Auto, Business Loan)
- Sheet 2: MTG(B) -- Level B, 2 Features (Origination, Servicing), 3 items (Fixed Rate, Variable Rate, Split)
- Sheet 3: MTP(Z) -- Level Z, 2 Features (Pricing Model, Margin Analysis), 3 items (Fixed, Variable, Split)

Step 2.5: Quote rules:
- PART 1, Critical Rule #2: "E5 = B5 = E8" on EVERY sheet
- PART 1, Critical Rule #8: "Sub-GNM phai co back-link o A1"
- PART 5, Write Order: "Moi Phase phai hoan thanh tren TAT CA sheets truoc khi chuyen Phase"

Step 4.5: Self-verify
- 3 sheets x (E5=B5 + E8=B5) = 6 formulas needed
- 2 sub-GNMs x A1 back-link = 2 back-link formulas
- Sheet 1 Zone 3 engines -> Sheet 2, Sheet 2 Zone 3 engines -> Sheet 3
</thinking>

<answer>
## CASCADE: RBL(A) -> MTG(B) -> MTP(Z)

### Sheet 1: RBL (A) -- Retail Banking Lending
| Property | Value |
|----------|-------|
| Sheet name | `RBL (A)` |
| A1 | (empty -- root GNM, no back-link) |
| B5 | RBL |
| E5 | `=B5` |
| E8 | `=B5` |

**Zone 3 (Single-Feature, col G):**
| Item (F) | Lending Products (G) | Conso. (H) |
|----------|---------------------|-------------|
| Mortgage | =HYPERLINK("#'MTG (B)'!B2", "Mortgage Lending MTG(B)") | Mortgage Playbook MTP(Z) |
| Auto | Auto Lending Strategy ALS(B) | Auto Playbook ALP(Z) |
| Business Loan | Business Loan Framework BLF(B) | BL Playbook BLP(Z) |

### Sheet 2: MTG (B) -- Mortgage Lending
| Property | Value |
|----------|-------|
| Sheet name | `MTG (B)` |
| **A1** | `=HYPERLINK("#'RBL (A)'!A1", "<<")` |
| B5 | MTG |
| E5 | `=B5` |
| E8 | `=B5` |

**Zone 3 (2 Features, cols G-H):**
| Item (F) | Origination (G) | Servicing (H) | Conso. (I) |
|----------|----------------|---------------|-------------|
| Fixed Rate | =HYPERLINK("#'MTP (Z)'!B2", "Fixed Rate Pricing MTP(Z)") | Fixed Servicing Model FSM(Z) | Fixed Rate Guide FRG(Z) |
| Variable Rate | Variable Pricing Engine VPE(Z) | Variable Servicing VSM(Z) | Variable Rate Guide VRG(Z) |
| Split | Split Product Design SPD(Z) | Split Servicing SSM(Z) | Split Product Guide SPG(Z) |

### Sheet 3: MTP (Z) -- Fixed Rate Pricing
| Property | Value |
|----------|-------|
| Sheet name | `MTP (Z)` |
| **A1** | `=HYPERLINK("#'MTG (B)'!A1", "<<")` |
| B5 | MTP |
| E5 | `=B5` |
| E8 | `=B5` |

**Zone 3 (Level Z = Values, cols G-H):**
| Item (F) | Pricing Model (G) | Margin Analysis (H) | Conso. (I) |
|----------|-------------------|---------------------|-------------|
| Fixed 1Y | Base rate + 2.5% spread, floor 8.5% | NIM target 3.2%, COF 5.3% [EST] | - |
| Fixed 3Y | Base rate + 3.0% spread, floor 9.0% | NIM target 3.5%, COF 5.5% [EST] | - |
| Fixed 5Y | Base rate + 3.5% spread, floor 9.5% | NIM target 3.8%, COF 5.7% [EST] | - |

> [EST] tags on margin figures -- benchmarks pending treasury confirmation.

### Write Order for 3-Sheet Cascade
```python
sheets = ['RBL (A)', 'MTG (B)', 'MTP (Z)']

# Phase 1: Data on ALL sheets first
for s in sheets: write_data(s)

# Phase 2: Formulas on ALL sheets (E5=B5, E8=B5, HYPERLINKs, back-links)
for s in sheets: write_formulas(s)

# Phase 3-5: Borders then formatting on ALL sheets
for s in sheets: set_section_medium_border(s)
for s in sheets: set_cluster_thin_border(s)
for s in sheets: set_formatting(s)  # wrap text + autofit
```

### Cascade Validation Checklist
- [ ] Every sheet: E5 = `=B5`, E8 = `=B5` (formula, not static)
- [ ] RBL(A) A1: empty (root -- no parent)
- [ ] MTG(B) A1: `=HYPERLINK("#'RBL (A)'!A1", "<<")`
- [ ] MTP(Z) A1: `=HYPERLINK("#'MTG (B)'!A1", "<<")`
- [ ] RBL(A) Zone 3 G8: HYPERLINK points to `MTG (B)` sheet
- [ ] MTG(B) Zone 3 G8: HYPERLINK points to `MTP (Z)` sheet
- [ ] Forward-reference engines (ALS, BLF) noted -- sheets not yet created
</answer>
```

</example>

---

<example type="VGATE_FAILURE">

