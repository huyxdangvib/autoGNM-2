---
part: 2b
name: "Section Details: Header & Phần Đầu"
parent: gnm-instruction.md
---

## Section Details

### 1. Ten GNM

**Muc dich:** The hien chu de chinh cua GNM, giup nguoi doc nhanh chong nhan biet noi dung ma GNM muon truyen tai.

| Thuoc tinh | Gia tri |
|------------|---------|
| **Vi tri** | O B2 |
| **Ten Sheet Excel** | `Ma GNM (Level)`  -  VD: `PRD (A)`, `GEL (B)`, `MTZ (Z)`  |
| **Cach the hien** | Ten ngan gon (toi da 50 ky tu), viet in hoa, BAT BUOC kem Level o cuoi (vd: `PRD (A), MTZ (Z)`) |
| **Dinh dang** | Font Myriad Pro, 14pt, in dam (Bold), nen #FFFFFF, chu #000000, no wrap text |
| **Merge Range** | B2 merge tu B2 den cot cuoi Phan Than (VD: B2:H2 khi 4 cot Single-Feature, B2:I2 khi 5 cot, B2:J2 khi 6 cot). **Khi them/bot cot -> cap nhat merge range tuong ung** |

**GNM Levels:**

| Level | Zone 3 Content | Mo ta |
|-------|----------------|-------|
| **A, B, C...** | Engines (da la Value) | GNM cau truc/dieu huong - Zone 3 chua **Engines** voi ten du nghia (VD: `Service Catalog SVC (B)`) |
| **Z** | Values chi tiet | GNM chi tiet/thuc thi - Zone 3 chua Values truc tiep; co the co Engines dang Z1, Z2... |

> **! QUAN TRONG:** Engine DA LA Value — ten mang nghia, max 50 chars. Xem **Engine** trong Terminology (PART 1).

**Vi du:**
- `CORPORATE BOND BUSINESS (A)` -> Sheet: `CBB (A)`
- `PRODUCT DEVELOPMENT (B)` -> Sheet: `PRD (B)`
- `MORTGAGE PRODUCT (Z)` -> Sheet: `MTG (Z)`

---

### 2. Phan Dau

**Muc dich:** Dong vai tro nhu **bang dinh vi (index)**, giup hoach dinh cau truc va noi dung cua toan bo GNM. Phan Dau cho biet GNM se co bao nhieu Items, bao nhieu yeu to All va Common.

**Cau truc:** Luon la bang 2 cot x nhieu hang

#### 2.1 Cum Header (Row 4):
- **O B4:** Chua label `(1)`
- **O C4:** Chua label `(2)`
- **Styling:** Nen #0070C0, chu trang #FFFFFF, top left align, no wrap text

#### 2.2 Cum Sub-header (Rows 5-7):
Dinh nghia cau truc phan cap cua Zone 1:
- **B5:** Ma GNM (3 ky tu viet tat, in hoa - VD: GEX, PRB)
- **C5:** Label `(1)` - tuong ung voi Ma GNM (nhap `-1`)
- **C6:** Label `(2)` - tuong ung voi Object (nhap `-2`)
- **C7:** Label `(3)` - tuong ung voi Item (nhap `-3`)
- **B6, B7:** De trong
- **Number Format C5:C7:** Decimal places = 0, Negative numbers = (1234)

**Styling:**
- **Cot B (B5:B7):** Nen #FFFFFF (trang), chu #000000
- **Cot C (C5:C7):** Nen #DDEBF7 (xanh nhat), chu #000000

#### 2.3 Cum Content (Rows 8+):
- **Cot B (1):** De trong
- **Cot C (2):** Danh so tuan tu 1, 2, 3... tuong ung voi so DONG trong Zone 1 (moi dong = 1 to hop Level 1 + Level 2)
- **Styling:** Nen #FFFFFF, chu den #000000

#### 2.4 Cum All (Rows dong, sau Content):
- **Muc dich:** Danh dau khu vuc danh cho cac yeu to ap dung cho TAT CA items
- **Vi tri bat dau:** Row = 8 + n (n = so items trong Content)
- **So dong:** Toi thieu 2 rows, **tang them khi can nhieu Engines hon** (VD: 3 Engines Zone 5 -> 3 dong All)
- **Cach xac dinh so dong:** Dem so Engines nhieu nhat trong Zone 5/6/7 -> do la so dong All can thiet

**Quy tac dien o trong Cum All (Phan Dau):**

| O | Dong | Noi dung | Bat buoc |
|---|------|----------|----------|
| **B** (cot 1) | Tat ca dong All | De trong | Yes |
| **C** (cot 2) | Dong dau tien | Label **"All"** (nhan co dinh) | Yes |
| **C** (cot 2) | Cac dong sau | De trong | Yes |

> **[!] QUAN TRONG - Bien All:** Dong dau tien cua Cum All phai co **Thin Top Border o o C** (KHONG co Top Border o o B) de phan cach voi Cum Content phia tren.

**Dong bo bat buoc Cum All -> Zones (cung so dong):**

| Phan | Vung can dien | Zone tuong ung | Noi dung |
|------|--------------|----------------|----------|
| **Phan Dau** (B-C) | O C = "All" + rong | Index cho Zone 5-7 | Chi label, khong co Engine |
| **Phan Than** - Zone 1 columns | Cung rows, cot E-F (hoac E-G) | Khong co zone | **De trong hoan toan** |
| **Phan Than** - Zone 2-3 columns | Cung rows, cot Feature | **Zone 5** | Engines (Vertical Consolidation) |
| **Phan Than** - Cot Conso. | Cung rows, cot cuoi Than | **Zone 6** | Engines (Common of 3,4,5) |
| **Phan Mo rong** | Cung rows, 2 cot Mo rong | **Zone 7** | Engines (Common of 3,4,5,6) |

> **Quy tac dong bo All/Common:** So dong moi Cum trong Phan Dau **PHAI BANG** Phan Than va Phan Mo rong. Xem chi tiet kiem tra -> **All & Common Sync Validation** (PART 7).

#### 2.5 Cum Common (Rows dong, sau All):
- **Muc dich:** Danh dau khu vuc danh cho nguon luc noi bo va ben ngoai
- **Vi tri bat dau:** Row = 8 + n + a (n = so items, a = so dong All)
- **So dong:** Toi thieu 2 rows, **tang them khi can nhieu Engines hon** (VD: 4 Engines Zone 8/9 -> 4 dong Common)
- **Cach xac dinh so dong:** Dem so Engines nhieu nhat trong Zone 8/9 -> do la so dong Common can thiet

**Quy tac dien o trong Cum Common (Phan Dau):**

| O | Dong | Noi dung | Bat buoc |
|---|------|----------|----------|
| **B** (cot 1) | Dong dau tien | Label **"Common"** (nhan co dinh) | Yes |
| **B** (cot 1) | Cac dong sau | De trong | Yes |
| **C** (cot 2) | Dong dau tien | Dau **"-"** | Yes |
| **C** (cot 2) | Cac dong sau | De trong | Yes |

> **[!] QUAN TRONG - Bien Common:** Dong dau tien cua Cum Common phai co **Thin Top Border o ca o B va C** de phan cach voi Cum All phia tren.

**Dong bo bat buoc Cum Common -> Zones (cung so dong):**

| Phan | Vung can dien | Zone tuong ung | Noi dung |
|------|--------------|----------------|----------|
| **Phan Dau** (B-C) | B="Common"+rong, C="-"+rong | Index cho Zone 8-9 | Chi label, khong co Engine |
| **Phan Than** - Zone 1-3 columns | Cung rows, cot E den Feature cuoi | Khong co zone | **De trong hoan toan** |
| **Phan Than** - Cot Conso. | Cung rows, cot cuoi Than | **Zone 8** | Engines (Internal Referral) |
| **Phan Mo rong** | Cung rows, 2 cot Mo rong | **Zone 9** | Engines (External Referral) |

> **Dong bo:** Ap dung cung quy tac nhu Cum All o tren -> PART 7 All & Common Sync Validation.

---

#### Tong hop: Cau truc Row dong cho Cum All & Common

**Vi du cu the (3 items, 2 All rows, 2 Common rows):**

```
Phan Dau (B-C)        | Phan Than (Zone cols)          | Phan Mo rong (2 cot)
-----------------------+--------------------------------+----------------------
R8:  |    | 1          | Zone1 | Zone3 | Zone3 | Zone4  |
R9:  |    | 2          | Zone1 | Zone3 | Zone3 | Zone4  |
R10: |    | 3          | Zone1 | Zone3 | Zone3 | Zone4  |
-----+----+------------+-------+-------+-------+--------+----------------------  <- Thin Top Border
R11: |    | All        |(rong) |Zone 5 |Zone 5 |Zone 6  | Zone 7  |
R12: |    |            |(rong) |       |       |        |         |
-----+----+------------+-------+-------+-------+--------+----------------------  <- Thin Top Border
R13: |Common| -         |(rong) |(rong) |(rong) |Zone 8  | Zone 9  |
R14: |    |            |(rong) |(rong) |(rong) |        |         |
```

**Quy tac KHONG duoc vi pham:**
1. **Zone 5** chi nam o khu vuc All, cung cot Zone 2-3 — KHONG nam o cot Zone 1 hoac Conso.
2. **Zone 6** chi nam o khu vuc All, cot Conso. — KHONG nam o cot Zone 2-3
3. **Zone 7** chi nam o khu vuc All, Phan Mo rong — KHONG nam o Phan Than
4. **Zone 8** chi nam o khu vuc Common, cot Conso. — KHONG nam o cot Zone 2-3
5. **Zone 9** chi nam o khu vuc Common, Phan Mo rong — KHONG nam o Phan Than
6. **Khu vuc trong bat buoc:** Zone 1 columns trong All rows va Zone 1-3 columns trong Common rows PHAI de trong

> **VBM Practical Note:** VBM(A) now uses separate All and Common sections (updated Mar 2026). All row contains Zone 5 engines (VMI, VES) in feature columns and Zone 7 engines (VIB Goal → HAGT, GNM → BFS) in extension. Common row contains Org. structure (VOS) in feature columns and External stakeholders in extension (Zone 9). Some compact A-level GNMs may still merge All and Common — this is acceptable when referral engines are few.

---

