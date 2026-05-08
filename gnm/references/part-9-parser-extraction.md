---
part: 9
name: "Parser: Boundary Detection & Extraction"
parent: gnm-instruction.md
---

### Step 3: Dynamic Row Boundary Detection

```python
def detect_rows(ws, conso_col):
    # Find content rows: start at row 8, scan until "All" label in column C
    content_start = 8
    row = 8
    items = []
    while row < 200:  # Safety limit
        c_val = ws.cell(row=row, column=3).value  # Column C
        if c_val and str(c_val).strip().lower() == 'all':
            all_start = row
            break
        if c_val is not None:
            items.append(row)
        row += 1
    
    n = len(items)  # Item count
    
    # Find Common start: scan from all_start
    row = all_start
    while row < 200:
        b_val = ws.cell(row=row, column=2).value  # Column B
        if b_val and str(b_val).strip().lower() == 'common':
            common_start = row
            break
        row += 1
    
    a = common_start - all_start      # All row count
    
    # Find end: scan from common_start until empty
    row = common_start
    while row < 200:
        has_content = any(
            ws.cell(row=row, column=c).value is not None
            for c in range(2, conso_col + 3)
        )
        if not has_content:
            end_row = row - 1
            break
        row += 1
    
    c = end_row - common_start + 1  # Common row count
    
    return {
        'n': n, 'a': a, 'c': c,
        'content_start': content_start,
        'content_end': content_start + n - 1,
        'all_start': all_start,
        'all_end': all_start + a - 1,
        'common_start': common_start,
        'common_end': common_start + c - 1
    }
```

### Step 4: Zone Content Extraction

```python
def extract_zones(ws, cols, rows):
    ast = {
        'zone1': {'items': []},
        'zone2': {'feature_group': ws.cell(row=6, column=cols['features'][0]['col']).value,
                   'features': [f['name'] for f in cols['features']]},
        'zone3': {'matrix': []},
        'zone4': {'engines': []},
        'zone5': {'engines': []},
        'zone6': {'engines': []},
        'zone7': {'engines': []},
        'zone8': {'engines': []},
        'zone9': {'engines': []}
    }
    
    # Zone 1: Items (col F, optionally G)
    for r in range(rows['content_start'], rows['content_end'] + 1):
        item = {
            'row': r,
            'level1': ws.cell(row=r, column=6).value,  # Col F
            'level2': ws.cell(row=r, column=7).value if cols['has_level2'] else None
        }
        ast['zone1']['items'].append(item)
    
    # Zone 3: Value Matrix (feature cols × content rows)
    for r in range(rows['content_start'], rows['content_end'] + 1):
        for f in cols['features']:
            cell = ws.cell(row=r, column=f['col'])
            cell_type = _classify_cell(cell)  # engine|value|value+engine|empty
            ast['zone3']['matrix'].append({
                'row': r, 'col': f['col'],
                'item': ws.cell(row=r, column=6).value,
                'feature': f['name'],
                'content': cell.value,
                'type': cell_type,
                'has_hyperlink': cell.value and '=HYPERLINK' in str(cell.value)
            })
    
    # Zone 4: Conso column (content rows)
    for r in range(rows['content_start'], rows['content_end'] + 1):
        cell = ws.cell(row=r, column=cols['conso_col'])
        if cell.value:
            ast['zone4']['engines'].append({
                'row': r, 'content': cell.value,
                'item': ws.cell(row=r, column=6).value
            })
    
    # Zone 5: All rows × Feature columns
    for r in range(rows['all_start'], rows['all_end'] + 1):
        for f in cols['features']:
            cell = ws.cell(row=r, column=f['col'])
            if cell.value:
                ast['zone5']['engines'].append({
                    'row': r, 'col': f['col'],
                    'feature': f['name'], 'content': cell.value
                })
    
    # Zone 6: All rows × Conso column
    for r in range(rows['all_start'], rows['all_end'] + 1):
        cell = ws.cell(row=r, column=cols['conso_col'])
        if cell.value:
            ast['zone6']['engines'].append({'row': r, 'content': cell.value})
    
    # Zone 7: All rows × Extension columns (after Conso separator)
    ext_start = cols['conso_col'] + 2  # skip separator col
    for r in range(rows['all_start'], rows['all_end'] + 1):
        col = ext_start
        while col <= ext_start + 5:  # scan extension columns
            cell = ws.cell(row=r, column=col)
            if cell.value:
                ast['zone7']['engines'].append({'row': r, 'col': col, 'content': cell.value})
            col += 1
    
    # Zone 8: Common rows × Conso column
    for r in range(rows['common_start'], rows['common_end'] + 1):
        cell = ws.cell(row=r, column=cols['conso_col'])
        if cell.value:
            ast['zone8']['engines'].append({'row': r, 'content': cell.value})
    
    # Zone 9: Common rows × Extension columns
    for r in range(rows['common_start'], rows['common_end'] + 1):
        col = ext_start
        while col <= ext_start + 5:
            cell = ws.cell(row=r, column=col)
            if cell.value:
                ast['zone9']['engines'].append({'row': r, 'col': col, 'content': cell.value})
            col += 1
    
    return ast
```

