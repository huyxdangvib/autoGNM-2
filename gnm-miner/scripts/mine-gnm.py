#!/usr/bin/env python3
"""mine-gnm.py — Extract GNM data from TypeScript GnmSheet files to Build Spec JSON.

Usage:
    python mine-gnm.py <data-dir> [--output <output-dir>] [--domain <prefix>] [--format json|yaml]

Examples:
    python mine-gnm.py ./src/data/                          # Mine all sheets
    python mine-gnm.py ./src/data/ --domain rbc             # Mine RBC domain only
    python mine-gnm.py ./src/data/ --output ./build-specs/  # Custom output dir
"""

import argparse
import json
import re
import sys
from pathlib import Path


def parse_gnm_sheet(filepath: Path) -> dict | None:
    """Parse a TypeScript GnmSheet file into structured data."""
    content = filepath.read_text(encoding="utf-8")

    # Extract sheet metadata
    id_match = re.search(r"id:\s*'([^']+)'", content)
    title_match = re.search(r"title:\s*'([^']+)'", content)
    badge_match = re.search(r"badge:\s*'([^']+)'", content)
    domain_match = re.search(r"domain:\s*'([^']+)'", content)
    min_width_match = re.search(r"minWidth:\s*'([^']+)'", content)

    if not id_match:
        return None

    # Extract colgroup
    colgroup_match = re.search(r"colgroup:\s*\[([^\]]+)\]", content)
    colgroup = []
    if colgroup_match:
        colgroup = re.findall(r"'([^']*)'", colgroup_match.group(1))

    # Count data columns (non-separator flex columns)
    data_cols = sum(1 for w in colgroup if w == "")
    sep_cols = sum(1 for w in colgroup if w == "4px")
    is_degenerate = data_cols == 0

    # Count z-l2 cells (Zone 3 values)
    z_l2_count = len(re.findall(r"className:\s*'z-l2'", content))

    # Count data rows (rows with z-l0 or z-l1)
    data_row_count = len(re.findall(r"className:\s*'z-l[01]'", content))

    # Extract cross-references
    cross_refs = re.findall(r'data-ref="([^"]+)"', content)
    sheet_refs = re.findall(r'data-sheet="([^"]+)"', content)

    # Check for iframe links
    iframe_links = re.findall(r"iframeSrc:\s*'([^']+)'", content)

    # Extract text content from z-l2 cells for KPI detection
    z_l2_texts = re.findall(r"\{\s*text:\s*'([^']*)'[^}]*className:\s*'z-l2'", content)
    has_numeric = any(re.match(r"^[\d,.\-()%]+$", t.strip()) for t in z_l2_texts if t.strip())
    has_boolean = any(t.strip() == "Y" for t in z_l2_texts)

    # Detect traffic-light styling
    has_traffic_light = "backgroundColor" in content and "z-l2" in content

    # Classify pattern
    if is_degenerate:
        pattern = "degenerate"
    elif has_numeric and has_traffic_light:
        pattern = "kpi-performance"
    elif has_numeric:
        pattern = "kpi-data"
    elif has_boolean:
        pattern = "boolean-matrix"
    elif cross_refs or sheet_refs:
        pattern = "navigation-board"
    else:
        pattern = "strategy-content"

    return {
        "id": id_match.group(1),
        "title": title_match.group(1) if title_match else "",
        "badge": badge_match.group(1) if badge_match else "",
        "domain": domain_match.group(1) if domain_match else "",
        "minWidth": min_width_match.group(1) if min_width_match else "",
        "file": filepath.name,
        "colgroup": colgroup,
        "dataColumns": data_cols,
        "separatorColumns": sep_cols,
        "isDegenerate": is_degenerate,
        "z_l2_count": z_l2_count,
        "dataRowCount": data_row_count,
        "crossRefs": cross_refs,
        "sheetRefs": sheet_refs,
        "iframeLinks": iframe_links,
        "pattern": pattern,
    }


def parse_hub_data(filepath: Path) -> dict:
    """Parse gnm-hub-data.ts for hierarchy metadata."""
    content = filepath.read_text(encoding="utf-8")

    # Extract gnmSubOrder
    order_match = re.search(
        r"gnmSubOrder\s*=\s*\[(.*?)\]", content, re.DOTALL
    )
    sub_order = []
    if order_match:
        sub_order = re.findall(r"'([^']+)'", order_match.group(1))

    # Extract gnmSubMeta
    meta = {}
    meta_entries = re.findall(
        r"'([^']+)':\s*\{\s*name:\s*'([^']*)',\s*code:\s*'([^']*)',\s*sheet:\s*([^,]+),\s*domain:\s*'([^']*)'\s*\}",
        content,
    )
    for entry_id, name, code, sheet, domain in meta_entries:
        meta[entry_id] = {
            "name": name.strip(),
            "code": code,
            "sheet": sheet.strip().strip("'"),
            "domain": domain,
        }

    # Extract gnmChildSheets
    children = {}
    child_entries = re.findall(
        r"'([^']+)':\s*\[([^\]]+)\]", content[content.find("gnmChildSheets") :]
    )
    for parent, child_str in child_entries:
        kids = re.findall(r"'([^']+)'", child_str)
        if kids:
            children[parent] = kids

    return {"subOrder": sub_order, "subMeta": meta, "childSheets": children}


def build_tree(hub_data: dict) -> dict:
    """Build hierarchy tree from hub data."""
    children_map = hub_data["childSheets"]
    all_children = set()
    for kids in children_map.values():
        all_children.update(kids)

    # Find roots (in order but not a child of anything)
    roots = [sid for sid in hub_data["subOrder"] if sid not in all_children]

    def build_node(sid: str, depth: int = 0) -> dict:
        meta = hub_data["subMeta"].get(sid, {})
        node = {"id": sid, "depth": depth, **meta, "children": []}
        for child_id in children_map.get(sid, []):
            node["children"].append(build_node(child_id, depth + 1))
        return node

    return {"roots": [build_node(r) for r in roots]}


def run_audit(sheets: list[dict], hub_data: dict) -> list[dict]:
    """Run quality audit on parsed sheets."""
    results = []
    seen_content = {}

    for sheet in sheets:
        issues = []
        status = "PASS"

        # S1: Column layout
        if sheet["isDegenerate"]:
            issues.append({"severity": "FAIL", "code": "S1", "msg": "Zero data columns (degenerate)"})
            status = "FAIL"

        # D1: Zone 3 density
        if sheet["z_l2_count"] == 0 and not sheet["isDegenerate"]:
            issues.append({"severity": "WARN", "code": "D1", "msg": "No z-l2 data cells"})
            if status == "PASS":
                status = "WARN"

        # H1: Registered in order
        if sheet["id"] not in hub_data["subOrder"] and sheet["id"] != "bma-board":
            issues.append({"severity": "WARN", "code": "H4", "msg": "Not in gnmSubOrder (orphaned)"})
            if status == "PASS":
                status = "WARN"

        # H5: Duplicate detection (simple content hash)
        content_key = f"{sheet['z_l2_count']}:{sheet['dataRowCount']}:{sheet['dataColumns']}"
        if content_key in seen_content and sheet["z_l2_count"] > 0:
            other = seen_content[content_key]
            issues.append({
                "severity": "WARN",
                "code": "H5",
                "msg": f"Potential duplicate of {other}",
            })
            if status == "PASS":
                status = "WARN"
        seen_content[content_key] = sheet["id"]

        results.append({"id": sheet["id"], "status": status, "issues": issues})

    return results


def main():
    parser = argparse.ArgumentParser(description="Mine GNM TypeScript data files")
    parser.add_argument("data_dir", help="Path to src/data/ directory")
    parser.add_argument("--output", "-o", default=".", help="Output directory")
    parser.add_argument("--domain", "-d", help="Filter by domain prefix (e.g., rbc)")
    parser.add_argument("--format", "-f", choices=["json", "yaml"], default="json")
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    if not data_dir.exists():
        print(f"Error: {data_dir} does not exist", file=sys.stderr)
        sys.exit(1)

    # Step 1: Discovery
    gnm_files = sorted(data_dir.glob("gnm-*.ts"))
    infra_files = {"gnm-sheet-registry.ts", "gnm-hub-data.ts", "gnm-custom-links.ts"}
    data_files = [f for f in gnm_files if f.name not in infra_files]

    if args.domain:
        data_files = [f for f in data_files if f.name.startswith(f"gnm-{args.domain}") or f.name.startswith(f"gnm-sub-{args.domain}")]

    print(f"Found {len(data_files)} data files in {data_dir}")

    # Step 2: Parse hub data
    hub_path = data_dir / "gnm-hub-data.ts"
    hub_data = parse_hub_data(hub_path) if hub_path.exists() else {"subOrder": [], "subMeta": {}, "childSheets": {}}
    print(f"Hub: {len(hub_data['subOrder'])} ordered, {len(hub_data['subMeta'])} with metadata")

    # Step 3: Parse all sheets
    sheets = []
    for f in data_files:
        parsed = parse_gnm_sheet(f)
        if parsed:
            sheets.append(parsed)
    print(f"Parsed {len(sheets)} sheets")

    # Step 4: Build tree
    tree = build_tree(hub_data)

    # Step 5: Run audit
    audit = run_audit(sheets, hub_data)
    pass_count = sum(1 for a in audit if a["status"] == "PASS")
    warn_count = sum(1 for a in audit if a["status"] == "WARN")
    fail_count = sum(1 for a in audit if a["status"] == "FAIL")
    print(f"Audit: {pass_count} pass, {warn_count} warn, {fail_count} fail")

    # Step 6: Output
    result = {
        "project": str(data_dir),
        "totalSheets": len(sheets),
        "sheets": sheets,
        "hierarchy": tree,
        "audit": audit,
        "summary": {
            "byDomain": {},
            "byPattern": {},
            "degenerate": [s["id"] for s in sheets if s["isDegenerate"]],
            "auditPass": pass_count,
            "auditWarn": warn_count,
            "auditFail": fail_count,
        },
    }

    # Compute summaries
    for s in sheets:
        domain = s["domain"]
        result["summary"]["byDomain"][domain] = result["summary"]["byDomain"].get(domain, 0) + 1
        pattern = s["pattern"]
        result["summary"]["byPattern"][pattern] = result["summary"]["byPattern"].get(pattern, 0) + 1

    out_file = output_dir / "gnm-mine-result.json"
    out_file.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Output: {out_file}")


if __name__ == "__main__":
    main()
