---
part: 5
name: "Write Order Protocol"
parent: gnm-instruction.md
---

## ⚠️ Excel Write Order Protocol (BẮT BUỘC)

> **[!] CRITICAL:** Khi tạo GNM trong Excel (qua code, script, hoặc hướng dẫn thủ công), **PHẢI tuân thủ thứ tự ghi sau**. Vi phạm thứ tự sẽ gây ra: border bị ghi đè, formula bị mất, cấu trúc sai.

### 5-Phase Execution Sequence

```
Phase 1: STRUCTURE & DATA        ← Ghi tất cả nội dung trước
Phase 2: FORMULAS                 ← Ghi formulas SAU data
Phase 3: SECTION MEDIUM BORDERS   ← Viền ngoài section trước  
Phase 4: CLUSTER THIN BORDERS     ← Overlay thin borders SAU CÙNG
Phase 5: FORMATTING & WRAP TEXT   ← Alignment, wrap text, row autofit CUỐI CÙNG
```

| Phase | Thao tác | Chi tiết | Tại sao thứ tự này? |
|-------|----------|----------|---------------------|
| **1. Data** | Ghi toàn bộ labels, values, engines cho **mọi sheet** | B2 (Tên), B4:C4 (Header), B5 (Mã GNM), C5:C7 (nhãn), C8+ (numbering), All/Common labels, Zone 1-9 content | Data phải có trước khi áp format |
| **2. Formulas** | Ghi tất cả formulas cho **mọi sheet** | `E5=B5`, `E8=B5`, `C8=ROW()-ROW($C$7)`, HYPERLINK formulas, back-link `<<` tại A1 | Formula ghi SAU data để reference ô đã có giá trị. Nếu ghi trước → bị data ghi đè |
| **3. Medium Borders** | Áp dụng Medium border bao quanh **section** cho mọi sheet | Phần Đầu: B4:C[end], Phần Thân: E4:[Conso][end], Phần Mở rộng: 2 cột | Medium border đặt khung ngoài. Áp dụng TRƯỚC thin |
| **4. Thin Borders** | Overlay Thin top border cho All/Common cho mọi sheet | All-Đầu: chỉ ô C (KHÔNG B). All-Thân & Mở rộng: toàn bộ cols. Common-tất cả: toàn bộ cols (kể cả B) | Thin ghi SAU CÙNG để **overlay** lên medium — không bị ghi đè ngược |
| **5. Formatting** | Áp dụng Alignment + Wrap Text + Row Autofit cho mọi sheet | Content areas (rows 6+): wrap_text=True, top-left align, indent=1. Headers/Sub-headers (rows 4-5): wrap_text=False. B2/A1: wrap_text=False, indent=0. Sau khi set wrap text, gọi autofit row height để rows tự động giãn theo nội dung | Formatting cuối cùng để không bị các phase trước ghi đè. Wrap text + autofit đảm bảo mọi nội dung hiển thị đầy đủ |

### Tại sao phải tuân thủ thứ tự?

| Lỗi thực tế | Nguyên nhân gốc | Cách phòng |
|--------------|-----------------|------------|
| All thin top border bị mất | Medium border (Phase 3) ghi đè thin nếu thin ghi trước | Thin luôn ở Phase 4 (sau Medium) |
| Common thin top border bị mất | Tương tự — medium ghi đè thin | Thin luôn ở Phase 4 |
| Section medium border bị phá | Thin border ghi đè một phần medium khi không đúng layer | Medium (Phase 3) trước, Thin (Phase 4) overlay |
| E8 = trống trên một số sheets | Data ghi đè formula `=B5` khi Phase 1 chạy sau Phase 2 | Data (Phase 1) trước, Formulas (Phase 2) sau |
| Nội dung bị cắt / tràn sang ô bên | Wrap text không được bật cho content areas | Phase 5 (Formatting): wrap_text=True cho rows 6+, autofit row height |

### Ví dụ Implementation

```python
# ❌ SAI — xử lý từng sheet hoàn chỉnh → border/formula conflict
for sheet in sheets:
    write_data(sheet)
    write_formulas(sheet)      # formula có thể bị data của sheet khác ghi đè
    set_medium_border(sheet)   # medium ghi trước
    set_thin_border(sheet)     # thin overlay — nhưng nếu medium chạy lại sẽ mất

# ✅ ĐÚNG — 5 phases tuần tự qua TẤT CẢ sheets
for sheet in sheets:           # Phase 1
    write_data(sheet)

for sheet in sheets:           # Phase 2
    write_formulas(sheet)      # E5=B5, E8=B5, HYPERLINKs

for sheet in sheets:           # Phase 3
    set_section_medium_border(sheet)

for sheet in sheets:           # Phase 4
    set_cluster_thin_border(sheet)  # overlay — luôn sau medium

for sheet in sheets:           # Phase 5
    set_formatting(sheet)      # alignment, wrap text, row autofit
```

> **Quy tắc vàng:** Mỗi Phase phải hoàn thành trên **TẤT CẢ sheets** trước khi chuyển Phase. KHÔNG xử lý từng sheet hoàn chỉnh rồi chuyển sheet.

</write_order>

---

