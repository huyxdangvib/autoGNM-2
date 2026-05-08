---
part: 2b
name: "Section Details: Phần Thân & Mở Rộng"
parent: gnm-instruction.md
---

### 3. Phan Than

**Muc dich:** La khu vuc chinh de trinh bay ma tran WHAT x TODO, noi the hien moi quan he giua cac chu the (Items) va cac hanh dong/tinh nang (Features).

**Cau truc:** Gom nhieu cot va hang, duoc chia thanh cac Zones chuc nang (Zone 1-6, 8)

#### Cum Header (Row 4):
- **E4 tro di:** Danh so cot tuan tu `(1)`, `(2)`, `(3)`... (so cot phu thuoc so Features va co Level 2 hay khong)
- **Phan Than f+L2+3 cot** (xem Scaling Formula PART 2a). VD: f=1,L2=0 -> 4 cot (E-H); f=2,L2=0 -> 5 cot (E-I); f=2,L2=1 -> 6 cot (E-J)
- **Styling:** Nen #0070C0, chu trang #FFFFFF, top left align, no wrap text

#### Cum Sub-header (Row 5):
- **E5:** Ma GNM (dung formula `=B5` de dong bo voi Phan Dau)
- **Cot giua:** De trong
- **Cot cuoi:** Nhan **Conso.** (Consolidation - cot hop nhat)
- **Styling:** Nen #DDEBF7, chu den #000000

> **Luu y:** Vi tri cot Conso. thay doi: H5 (Single-Feature, khong L2) hoac I5 (Multi-Feature, khong L2) hoac J5 (co L2)

#### Cum Zone Headers (Rows 6-7):
- **Zone 1 headers:** E6-F7 (mac dinh) hoac E6-G7 (khi co Level 2)
- **Zone 2 headers:** 1-2 cot sau Zone 1 (Feature labels)
- **Zone 4 headers:** Cot cuoi, rows 6-7 luon la nhan "-" co dinh
- **Styling:** Nen #DDEBF7, chu den #000000

> **Vi du:** Single-Feature: Zone 1 = E-F, Zone 2 = G, Conso = H. Khong co Level 2: Zone 1 = E-F, Zone 2 = G-H, Conso = I. Co Level 2: Zone 1 = E-G, Zone 2 = H-I, Conso = J.

#### Cac Zones trong Phan Than:
| Zone | Vung | Chuc nang |
|------|------|-----------|
| Zone 1 | 2-3 cot dau tien (E-F hoac E-G) | Chieu WHAT - Level 0 (Ma GNM) + Level 1 (Item) + Level 2 (neu can chi tiet hoa) |
| Zone 2 | Dong tren cung (sau Zone 1) | Chieu TODO - danh sach Features |
| Zone 3 | Giao diem Item x Feature | Ma tran gia tri chinh |
| Zone 4 | Cot Conso. (cot cuoi) | Horizontal consolidation of Zone 3 - Engine only - Item-level consolidation or Decoding topics |
| Zone 5 | Khu vuc All (cung cot Zone 2-3) | Vertical consolidation of Zone 3 - Engine only - Feature-level consolidation or Decoding topics |
| Zone 6 | All x Conso. | Common matters of Zone 3, 4, 5 - Engine only |
| Zone 8 | Khu vuc Common (cot Conso.) | Internal functions interaction - Referral to others' GNM |

---

### 4. Phan Mo rong

**Muc dich:** Mo rong pham vi cua GNM ra khoi ma tran WHAT x TODO, ket noi voi boi canh dau vao va he sinh thai ben ngoai.

**Cau truc:** Luon la bang 2 cot x nhieu hang (so hang bang Phan Than)

#### Cum Header (Row 4):
- Cot 1: Label `(1)` — Vi tri: K4 (khong Level 2) hoac L4 (co Level 2)
- Cot 2: Label `(2)` — Vi tri: L4 (khong Level 2) hoac M4 (co Level 2)
- **Styling:** Nen #0070C0, chu trang #FFFFFF, top left align, no wrap text

#### Cum Sub-header (Rows 5-7):

| Row | Cot 1 (K hoac L) | Cot 2 (L hoac M) |
|-----|-------------------|-------------------|
| **5** | "Common" (nhan co dinh) | (trong) |
| **6** | "-" | (trong) |
| **7** | "-" | "-" |

- **Styling:** Nen #DDEBF7, chu den #000000

> **Luu y:** Vi tri cot Phan Mo rong thay doi dong: K-L (khong Level 2) hoac L-M (co Level 2)

#### Content Rows (Rows 8 den Row cuoi Item):
> **QUY TAC BAT BUOC:** Phan Mo rong o cac rows tuong ung voi Zone 3 content (tu Row 8 den Row cuoi Item) **PHAI de trong hoan toan**. Chi co khu vuc All (Zone 7) va Common (Zone 9) moi chua Engines.

| Rows | Noi dung | Ly do |
|------|----------|-------|
| **Row 8 -> Row (7+n)** | **De trong** | Phan Mo rong khong co zone tuong ung voi Zone 3 o cac content rows |
| **All rows** | Zone 7 — Engines | Common matters of Zone 3, 4, 5, 6 |
| **Common rows** | Zone 9 — Engines | Extended functions interaction |

#### Cac Zones trong Phan Mo rong:
| Zone | Vung | Chuc nang |
|------|------|-----------|
| Zone 7 | All x Mo rong (2 cot) | Common matters of Zone 3, 4, 5, 6 - Engine only |
| Zone 9 | Common x Mo rong (2 cot) | Extended functions interaction - Referral to others' GNM |

---

</section_details>

> **Retrieval Signpost:** For Dynamic Row Formula, Column Layout Constraint, Zone Headers Cell Map -> see **PART 2a** (`references/part-2a-structure-core.md`). For core zones -> PART 3a. For engine zones -> PART 3b.

