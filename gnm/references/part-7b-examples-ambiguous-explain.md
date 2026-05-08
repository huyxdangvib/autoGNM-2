---
part: 7b
name: "Examples: AMBIGUOUS & EXPLAIN"
parent: gnm-instruction.md
---

### Example 6: AMBIGUOUS Request -> Proceed with World-Class Assumptions

**User Input:**
> "Tao GNM cho ngan hang so"

**Expected Response:**
```
<thinking>
Step 1: Request Type = CREATE
Step 2: Extract Parameters:
- Topic: "Ngan hang so" (Digital Banking) -- broad topic, missing Level/Items/Features
- Apply Assumption Framework (PART 5, Error Handling):
  - Level: A (topic rong -> tong quan)
  - WHAT: Classification Decoding -> Digital Banking channels la phan loai world-class pho bien nhat (Mobile Banking, Internet Banking, Open Banking/API)
  - TODO: Component-Based Decoding (BSC-inspired) -> Development + Operations la 2 perspectives cot loi cho digital transformation theo McKinsey/Gartner best practices
  - Level 2: No (3 channels dong cap)

Step 2.3: Framework Relevance (Relevance Engine -- Part 1b):
- GNM Type: Business/Product -> strategic_analysis=1.3, market_analysis=1.3, business_model=1.2
- Level: A -> strategic x1.5, operational x0.5, execution x0.3
- Top 3 scores:
  - strategic_analysis = 1.3 x 1.5 = **1.95**
  - market_analysis = 1.3 x 1.5 = **1.95**
  - business_model = 1.2 x 1.5 = **1.80**
- Recommended frameworks: strategic_analysis, market_analysis, business_model
- Zone mapping: Zone 1 Items from market segments, Zone 2 Features from business model dimensions

Step 2.5: Quote rules:
- PART 5, §Thiếu thông tin bắt buộc — Proceed with Assumptions: "Khi user cung cấp topic nhưng thiếu parameters, KHÔNG dừng lại hỏi. Chủ động tạo GNM với assumptions dựa trên Modern World-Class Best Practices"
- PART 3a, Zone 1: "Classification Decoding co the dung tai Zone 1 de xac dinh Items"
- PART 3a, Zone 2: "Features phai la HANH DONG hoac GOC NHIN" -> Development & Operations = TODO
- PART 1, Critical Rule #4: "Zone 4-9 CHI chua Engines"

Step 3: Validate
- 3 items x 2 features = 6 Zone 3 cells -> Level A = mostly Engines
- WHAT vs TODO: Channels = WHAT, Dev/Ops = TODO
- All/Common: 2 dong moi cum (default)

Step 4.5: Self-verify
- Zone 3: all 6 cells filled
- E5=B5, E8=B5 (formula)
- All sync: 2 rows x 3 phan
- Common sync: 2 rows x 3 phan
</thinking>

<answer>
## GNM SPECIFICATION: DIGITAL BANKING (A)

### Assumptions (Modern World-Class Best Practices)
| Parameter | Assumed Value | Rationale | Adjust? |
|-----------|--------------|-----------|--------|
| Level | A (tong quan) | Topic rong, can bird's-eye view truoc khi drill-down | Edit |
| WHAT (Items) | Mobile Banking, Internet Banking, Open Banking/API | Classification Decoding: 3 digital channels theo Gartner Digital Banking Framework | Edit |
| TODO (Features) | Development, Operations | BSC-inspired: Build (Dev) + Run (Ops) la 2 tru cot digital transformation | Edit |
| Level 2 | No | 3 channels dong cap, chua can chi tiet hoa | Edit |

> Neu assumptions khong phu hop, chi can noi "doi Items thanh X" hoac "dung Level B" -- toi se dieu chinh ngay.

> **Note:** GNM body follows Format A (CREATE) -- same structure as Example 1. Key specifics:

| Property | Value |
|----------|-------|
| Ten GNM | DIGITAL BANKING (A) |
| Ma GNM | DIG |
| WHAT (Zone 1) | Mobile Banking, Internet Banking, Open Banking/API (cot E-F) |
| TODO (Zone 2) | Development, Operations (cot G-H) |

**Zone 3 (Value Matrix):**
| Item | Development | Operations |
|------|------------|------------|
| Mobile Banking | Mobile App Engineering MAE(B) | Mobile Ops & Monitoring MOM(B) |
| Internet Banking | Web Platform Development WPD(B) | Web Ops & Security WOS(B) |
| Open Banking/API | API Platform & Integration API(B) | API Gateway Operations AGO(B) |

**Zone 4-9 (compact):** Zone 4 Conso. at col I. All (rows 11-12): Zone 5 at G-H, Zone 6 at I, Zone 7 at K-L (n=3, a=2, c=2). Common (rows 13-14): Zone 8 at I, Zone 9 at K-L.

**Excel:** Sheet=`DIG (A)`, E5=`=B5`, E8=`=B5`, B2 Merge=B2:I2
</answer>
```

</example>

---

<example type="EXPLAIN">

### Example 7: EXPLAIN Request -> Response

**User Input:**
> "Zone 4 la gi? Tai sao can?"

**Expected Response:**
```
<thinking>
Step 1: Request Type = EXPLAIN
Step 2: Topic = Zone 4 (Horizontal Consolidation)
Step 2.5: Quote rules:
- PART 3b, Zone 4: "Horizontal consolidation of Zone 3 -- CHI chua Engines"
- PART 1, Critical Rule #4: "Zone 4-9 CHI chua Engines"
- PART 1, Critical Rule #3: "Conso. luon la cot cuoi cung"
</thinking>

<answer>
## ZONE 4: HORIZONTAL CONSOLIDATION

### Dinh nghia (1-2 cau)
Zone 4 la **cot Conso. (Consolidation)** -- cot cuoi cung cua Phan Than. No tong hop theo **chieu ngang** (horizontal) cua Zone 3, tao lien ket den GNM con cho tung Item.

### Tai sao quan trong
Hinh dung Zone 3 nhu mot bang lon Items x Features. Zone 4 la cot **tong ket hang** -- nhung thay vi cong so, no chua **Engines** (links) den GNM con tong hop playbook/guide cho tung Item.

### Cach ap dung
1. Xac dinh moi Item can playbook/guide tong hop hay khong
2. Neu can -> tao Engine: `[Ten day du] MaGNM (Level)`
3. Dat Engine vao cot Conso., cung hang voi Item

### Vi du
| Item | Feature 1 | Feature 2 | **Conso. (Zone 4)** |
|------|----------|----------|---------------------|
| Working Capital | WCO(Z) | WCR(Z) | **Working Capital Playbook WCP(Z)** |

### Loi thuong gap
- Sai: Dat Values (so lieu, text) vao Zone 4 -> Zone 4 CHI chua Engines
- Sai: Conso. o giua Phan Than -> Conso. LUON o cot cuoi
- Dung: Engine name du nghia: `Working Capital Playbook WCP(Z)` -- nguoi doc hieu ngay

Ban muon tim hieu them ve Zone 5 (Vertical Consolidation) khong?
</answer>
```

</example>

</examples>

---

> **For additional examples** — see Part 7c (`references/part-7c-*.md`) for task-specific examples: TAXONOMY, CONVERT, CASCADE, VGATE_FAILURE, SINGLE_FEATURE_CREATE, DELETE_ARCHIVE, REVIEW_VIB, DELETE_CASCADE_MULTI.

> **End of Part 7b (Core Examples) v4.11.4** — 5 core examples loaded. For any rule clarification, PART 1 is authoritative. For structure specs, PART 2a (core) / PART 2b (templates) is SSOT. For zone definitions, PART 3a/3b. Always run V-gate before output.

