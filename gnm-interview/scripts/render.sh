#!/usr/bin/env bash
# Render the live spec.json to workspace/current.xlsx with atomic-rename
# so we never corrupt a file the user has open in Excel.
#
# Usage: bash render.sh [spec.json] [out.xlsx]
# Defaults: workspace/spec.json -> workspace/current.xlsx

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

SPEC="${1:-$ROOT/workspace/spec.json}"
OUT="${2:-$ROOT/workspace/current.xlsx}"
TMP="${OUT%.xlsx}.next.xlsx"

if [ ! -f "$SPEC" ]; then
  echo "❌ Spec file not found: $SPEC" >&2
  exit 2
fi

python3 "$SCRIPT_DIR/generate-gnm.py" "$SPEC" "$TMP"

# Atomic rename — if user has $OUT open in Excel on macOS, mv usually still
# succeeds (the open handle keeps the old inode); on Windows mv fails.
XLSX_FAILED=0
if mv -f "$TMP" "$OUT" 2>/dev/null; then
  echo "→ $OUT"
else
  echo "⚠️  Could not replace $OUT — likely open in Excel."
  echo "   Latest render is at: $TMP"
  echo "   Close $OUT and run: mv -f \"$TMP\" \"$OUT\""
  XLSX_FAILED=1
fi

# HTML live preview — render-html.py does its own atomic write.
HTML_OUT="${OUT%.xlsx}.html"
if python3 "$SCRIPT_DIR/render-html.py" "$SPEC" "$HTML_OUT" >/dev/null; then
  echo "→ $HTML_OUT"
fi

if [ "$XLSX_FAILED" = "1" ]; then
  exit 3
fi
