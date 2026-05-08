---
part: 7c
name: "Examples: Taxonomy & Convert"
parent: gnm-instruction.md
---


<part7c_extended_examples>

# PART 7c: EXTENDED FEW-SHOT EXAMPLES (ON-DEMAND)

> **TL;DR:** 8 task-specific examples: TAXONOMY, CONVERT, CASCADE, VGATE_FAILURE, SINGLE_FEATURE_CREATE, DELETE_ARCHIVE, REVIEW_VIB, DELETE_CASCADE_MULTI. Load alongside Part 7b when working on these specific task types.

> **Retrieval Signpost:** For core examples (CREATE, REVIEW, MODIFY, EXPLAIN, AMBIGUOUS) -> PART 7b. For validation logic, mistakes, checklists -> PART 7. For critical rules -> PART 1. For structure core (Column Layout, Dynamic Rows) -> PART 2a. For templates & section details -> PART 2b. For core zones (1-3) -> PART 3a. For engine zones (4-9) -> PART 3b.


## Extended Examples

<examples>
<example type="TAXONOMY_VIOLATION">

### Example 3: Taxonomy Violation Detection

**User Input:**
> "Zone 1 cua toi: Level 1 = Corporate Bond, Government Bond. Level 2 = Short-term, Long-term"

**Expected Response:**
```
## TAXONOMY VIOLATION DETECTED

**Van de:**
- Level 1: Bond Type (Corporate, Government) -- chieu "Loai trai phieu"
- Level 2: Tenor (Short-term, Long-term) -- chieu "Ky han"
- -> **Khong cung taxonomy!**

**Tai sao sai:**
Level 1 va Level 2 phai co quan he cha-con thuc su, cung chieu phan loai.
"Short-term" khong phai con cua "Corporate Bond", ma la mot chieu phan loai khac.

**Giai phap:**

**Option A: Giu Bond Type lam chinh**
| Level 1 | Level 2 |
|---------|----------|
| Corporate Bond | Investment Grade |
|  | High Yield |
| Government Bond | Treasury |
|  | Municipal |

**Option B: Tenor lam Feature (Zone 2)**
- Zone 1 (WHAT): Corporate Bond, Government Bond
- Zone 2 (TODO): Short-term Mgmt, Long-term Mgmt
- -> Tenor tro thanh goc nhin phan tich, khong phai Item

Ban muon chon approach nao?
```

</example>

---

<example type="CONVERT">

### Example 5: CONVERT Request -> Response

**User Input:**
> "Toi co bang du lieu san pham bao hiem nhan tho: Term Life, Whole Life, Endowment. Can chuyen thanh GNM voi goc nhin Product Development va Distribution."

**Expected Response:**
```
<thinking>
Step 1: Request Type = CONVERT (chuyen du lieu thanh GNM)
Step 2: Parameters:
- Topic: Life Insurance Products
- Detected WHAT: 3 products (Term Life, Whole Life, Endowment)
- Detected TODO: 2 perspectives (Product Development, Distribution)
- Level: B (can Engines cho tung san pham)
- Level 2: No (3 products dong cap)

Step 2.5: Quote rules:
- PART 1, Critical Rule #1: "Zone 3 khong bao gio de o trong"
- PART 3a, Zone 2: "Features phai la HANH DONG hoac GOC NHIN" -> Product Dev & Distribution = TODO
- PART 2a, Column Layout: Khong Level 2 -> Zone 2 = G-H, Conso. = I

Step 3: Validate
- 3 products x 2 features = 6 Zone 3 cells -> deu can Engines (Level B)
- WHAT vs TODO: Products = WHAT, Dev/Distribution = TODO
- All & Common: 2 dong moi cum (default)
</thinking>

<answer>
## CONVERT TO GNM: Life Insurance Products

### Source Analysis
| Attribute | Value |
|-----------|-------|
| Source format | List (3 products + 2 perspectives) |
| Detected WHAT | Term Life, Whole Life, Endowment |
| Detected TODO | Product Development, Distribution |
| Suggested Level | B (moi product x perspective can Engine drill-down) |

### Mapping Result
| Source Element | -> GNM Zone | Rationale |
|----------------|-----------|----------|
| Term Life, Whole Life, Endowment | Zone 1 (Items, cot F) | 3 san pham = WHAT can phan tich |
| Product Development | Zone 2 (Feature 1, cot G) | Goc nhin phat trien = TODO |
| Distribution | Zone 2 (Feature 2, cot H) | Goc nhin phan phoi = TODO |

### Generated GNM

> **Note:** Generated GNM follows Format A (CREATE) structure -- same as Example 1. Key specifics below:

| Property | Value |
|----------|-------|
| Ten GNM | LIFE INSURANCE PRODUCTS (B) |
| Ma GNM | LIP |
| WHAT (Zone 1) | Term Life, Whole Life, Endowment (cot E-F) |
| TODO (Zone 2) | Product Dev, Distribution (cot G-H) |
| Level 2 | No |

**Zone 3 (Value Matrix):**
| Item | Product Dev | Distribution |
|------|------------|-------------|
| Term Life | Term Product Design TPD(Z) | Term Distribution Strategy TDS(Z) |
| Whole Life | WL Product Engineering WPE(Z) | WL Channel Management WCM(Z) |
| Endowment | Endowment Product Design EPD(Z) | Endowment Sales Framework ESF(Z) |

**Zone 4-9 (compact):** Zone 4 Conso. at col I. All (rows 11-12): Zone 5 at G-H, Zone 6 at I, Zone 7 at K-L (n=3, a=2, c=2). Common (rows 13-14): Zone 8 at I, Zone 9 at K-L.

**Excel:** Sheet=`LIP (B)`, E5=`=B5`, E8=`=B5`, B2 Merge=B2:I2
</answer>
```

</example>

---

<example type="CASCADE">

