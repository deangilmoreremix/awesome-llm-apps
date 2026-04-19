#!/usr/bin/env bash
base="/workspace/0c85e0dc-1244-40ab-8f84-e11668f857da/sessions/agent_e5f1c028-f00b-43e8-8dde-5cf11e8e8e3f"
mapfile -t paths < <(grep -oP '\([^)]*\)' "$base/README.md" | grep '/$' | sed 's/(//;s/)//' | sort -u)
missing=()
for p in "${paths[@]}"; do
  if [ -d "$base/$p" ]; then
    echo "OK: $p"
  else
    echo "MISSING: $p"
    missing+=("$p")
  fi
done
echo "==========="
echo "Total listed: ${#paths[@]}"
echo "Missing: ${#missing[@]}"
if [ ${#missing[@]} -gt 0 ]; then
  printf 'Missing paths:\n%s\n' "${missing[@]}"
fi
