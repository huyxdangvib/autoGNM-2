---
part: 2b
name: "Visual Templates A/B/C"
parent: gnm-instruction.md
---


<part2b_templates_details>

# PART 2b: TEMPLATES & SECTION DETAILS

> **TL;DR:** PART 2b chua 3 Visual Templates (A: 5 cot Multi-Feature, B: 6 cot co Level 2, C: 4 cot Single-Feature) va Section Details (Ten GNM, Phan Dau, Phan Than, Phan Mo rong). Load on-demand khi generating Excel output.

> **Retrieval Signpost:** For Dynamic Row Formula, Column Layout Constraint, Zone Headers Cell Map -> see PART 2a. For core zones (1-3) -> PART 3a. For engine zones (4-9) -> PART 3b. For styling -> PART 4.


## Visual Templates (3 Layouts)

### Template A - Khong co Level 2, Multi-Feature (5 cot Phan Than):

> **B2 Merge Range:** B2 : Col(G+L2+f) — tuc merge den het cot Conso. Xem Bang tra cuu nhanh o Column Layout Constraint (PART 2a) cho exact col letter. Merge KHONG bao gom cot Separator va Phan Mo rong.

```
     | A  | B    | C   | D  | E      | F    | G         | H         | I       | J  | K       | L   |
-----+----+------+-----+----+--------+------+-----------+-----------+---------+----+---------+-----+
 R2  |    | EXAMPLE LIBRARY (B)  [merged B2:I2]                                  |    |         |     |
-----+----+------+-----+----+--------+------+-----------+-----------+---------+----+---------+-----+
 R3  |    | (empty row - khong su dung)                                                                        |
-----+----+------+-----+----+--------+------+-----------+-----------+---------+----+---------+-----+
 R4  |    | (1)  | (2) |    | (1)    | (2)  | (3)       | (4)       | (5)     |    | (1)     | (2) | <- Header
 R5  |    | EXL  | (1) |    | =B5    |      |           |           | Conso.  |    | Common  |     | <- Sub-header
 R6  |    |      | (2) |    | Object |      | Dev       |           | -       |    | -       |     | <- Zone Headers
 R7  |    |      | (3) |    | Item   | -    | Feature1  | Feature2  | -       |    | -       | -   | <- Zone Headers
-----+----+------+-----+----+--------+------+-----------+-----------+---------+----+---------+-----+
 R8  |    |      | 1   |    | =B5    | Corp | Engine    | Value     | Engine  |    |         |     | <- Zone 1,3,4 (E8=B5)
 R9  |    |      | 2   |    |        | SME  | Val+Engine| Engine    | Engine  |    |         |     | <- Zone 3: Value/Engine/Val+Engine
 R10 |    |      | 3   |    |        | FI   | Value     | Value     | Engine  |    |         |     |
-----+----+------+-----+----+--------+------+-----------+-----------+---------+----+---------+-----+
 R11 |    |      | All |    |        |      | Zone 5    | Zone 5    | Zone 6  |    | Zone 7  |     | <- All cluster
 R12 |    |      |     |    |        |      |           |           |         |    |         |     |
-----+----+------+-----+----+--------+------+-----------+-----------+---------+----+---------+-----+
 R13 |    |Common| -   |    |        |      |           |           | Zone 8  |    | Zone 9  |     | <- Common cluster
 R14 |    |      |     |    |        |      |           |           |         |    |         |     |
-----+----+------+-----+----+--------+------+-----------+-----------+---------+----+---------+-----+
     |Sep |Phan Dau    |Sep |      Phan Than (Zones 1-6,8)           |Sep | Phan Mo rong    |
```

### Template B - Co Level 2 (6 cot Phan Than):
```
     | A  | B    | C   | D  | E      | F    | G      | H         | I         | J       | K  | L       | M   |
-----+----+------+-----+----+--------+------+--------+-----------+-----------+---------+----+---------+-----+
 R2  |    | EXAMPLE LIBRARY (B)                                                                              |
-----+----+------+-----+----+--------+------+--------+-----------+-----------+---------+----+---------+-----+
 R3  |    | (empty row - khong su dung)                                                                               |
-----+----+------+-----+----+--------+------+--------+-----------+-----------+---------+----+---------+-----+
 R4  |    | (1)  | (2) |    | (1)    | (2)  | (3)    | (4)       | (5)       | (6)     |    | (1)     | (2) | <- Header
 R5  |    | EXL  | (1) |    | =B5    |      |        |           |           | Conso.  |    | Common  |     | <- Sub-header
 R6  |    |      | (2) |    | Object |      |        | Dev       |           | -       |    | -       |     | <- Zone Headers
 R7  |    |      | (3) |    | Item   | -    | -      | Feature1  | Feature2  | -       |    | -       | -   | <- Zone Headers
-----+----+------+-----+----+--------+------+--------+-----------+-----------+---------+----+---------+-----+
 R8  |    |      | 1   |    | =B5    | Corp |LargeCap| Engine    | Value     | Engine  |    |         |     | <- Zone 1,3,4 (E8=B5)
 R9  |    |      | 2   |    |        |      |Mid-tier| Val+Eng   | Engine    | Engine  |    |         |     | <- Zone 3: Value/Engine/Val+Engine
 R10 |    |      | 3   |    |        | SME  | -      | Value     | Value     | Engine  |    |         |     |
 R11 |    |      | 4   |    |        | FI   | Bank   | Value     | Value     | Engine  |    |         |     |
 R12 |    |      | 5   |    |        |      | NBFI   | Value     | Value     | Engine  |    |         |     |
-----+----+------+-----+----+--------+------+--------+-----------+-----------+---------+----+---------+-----+
 R13 |    |      | All |    |        |      |        | Zone 5    | Zone 5    | Zone 6  |    | Zone 7  |     | <- All cluster
 R14 |    |      |     |    |        |      |        |           |           |         |    |         |     |
-----+----+------+-----+----+--------+------+--------+-----------+-----------+---------+----+---------+-----+
 R15 |    |Common| -   |    |        |      |        |           |           | Zone 8  |    | Zone 9  |     | <- Common cluster
 R16 |    |      |     |    |        |      |        |           |           |         |    |         |     |
-----+----+------+-----+----+--------+------+--------+-----------+-----------+---------+----+---------+-----+
     |Sep |Phan Dau    |Sep |         Phan Than (Zones 1-6,8)                          |Sep | Phan Mo rong    |
```

### Template C - Single-Feature, khong co Level 2 (4 cot Phan Than):
```
     | A  | B    | C   | D  | E      | F        | G                    | H         | I  | J       | K   |
-----+----+------+-----+----+--------+----------+----------------------+-----------+----+---------+-----+
 R2  |    | EXAMPLE LIBRARY (B)  [merged B2:H2]                                      |    |         |     |
-----+----+------+-----+----+--------+----------+----------------------+-----------+----+---------+-----+
 R3  |    | (empty row)                                                                                   |
-----+----+------+-----+----+--------+----------+----------------------+-----------+----+---------+-----+
 R4  |    | (1)  | (2) |    | (1)    | (2)      | (3)                  | (4)       |    | (1)     | (2) | <- Header
 R5  |    | KBS  | (1) |    | =B5    |          |                      | Conso.    |    | Common  |     | <- Sub-header
 R6  |    |      | (2) |    | Object |          | Strategy Development | -         |    | -       |     | <- Zone Headers
 R7  |    |      | (3) |    | Item   | -        | -                    | -         |    | -       | -   | <- Zone Headers
-----+----+------+-----+----+--------+----------+----------------------+-----------+----+---------+-----+
 R8  |    |      | 1   |    | =B5    | Business | Engine               |           |    |         |     | <- Zone 1,3 (E8=B5)
 R9  |    |      | 2   |    |        |          | Engine               |           |    |         |     | <- Zone 3: 1 Engine per Item
 R10 |    |      | 3   |    |        |          | Engine               |           |    |         |     |
 R11 |    |      | 4   |    |        | Channel  | Engine               |           |    |         |     |
 R12 |    |      | 5   |    |        |          | Engine               |           |    |         |     |
-----+----+------+-----+----+--------+----------+----------------------+-----------+----+---------+-----+
 R13 |    |      | All |    |        |          | Zone 5               | Zone 6    |    | Zone 7  |     | <- All cluster
 R14 |    |      |     |    |        |          |                      |           |    |         |     |
-----+----+------+-----+----+--------+----------+----------------------+-----------+----+---------+-----+
 R15 |    |Common| -   |    |        |          |                      | Zone 8    |    | Zone 9  |     | <- Common cluster
 R16 |    |      |     |    |        |          |                      |           |    |         |     |
-----+----+------+-----+----+--------+----------+----------------------+-----------+----+---------+-----+
     |Sep |Phan Dau    |Sep |      Phan Than (Zones 1-6,8)              |Sep | Phan Mo rong    |
```

> **Luu y Template C:** Zone 2 chi co 1 cot (G), Zone 3 cung 1 cot (G), Conso. o H. Zone 4 (Conso.) dong vai tro "chieu TODO thu 2" cho cross-cutting Engines.

> **Scaling beyond 2 Features (f=3..5):** Khong co template visual san cho f>2. Ap dung **Scaling Formula** o Column Layout Constraint (PART 2a) de tinh column positions. Moi Feature them vao -> them 1 cot 200px cho Zone 2/3, Conso. va Separator shift +1. Bang tra cuu nhanh: f=3 -> Phan Than 6 cot (E-J, khong L2) hoac 7 cot (E-K, co L2); f=5 -> Phan Than 8 cot (E-L, khong L2) hoac 9 cot (E-M, co L2).

---

<section_details>

