#!/usr/bin/env bash
# Serve workspace/ over HTTP so the live HTML preview is reachable
# at http://localhost:PORT/current.html. The HTML auto-refreshes every
# 2 seconds, so you just leave the tab open while the interview runs.
#
# Usage: bash serve.sh [port]
# Default port: 8765 (avoids common dev-server collisions)

set -e

PORT="${1:-8765}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
WORKSPACE="$ROOT/workspace"

if [ ! -d "$WORKSPACE" ]; then
  echo "❌ Workspace not found: $WORKSPACE" >&2
  exit 2
fi

echo "GNM live preview"
echo "  → http://localhost:$PORT/current.html"
echo "  serving $WORKSPACE"
echo "  Ctrl-C to stop"
echo ""

cd "$WORKSPACE"
exec python3 -m http.server "$PORT" --bind 127.0.0.1
