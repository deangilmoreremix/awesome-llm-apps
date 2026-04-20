import json
import os
from pathlib import Path

# Load the catalog
catalog_path = Path(__file__).parent / "data" / "app_catalog.json"
with open(catalog_path, "r") as f:
    apps = json.load(f)

# Repo root
repo_root = Path(__file__).parent.parent

for app in apps:
    source_path = app.get("source_path")
    if not source_path:
        continue
    full_path = repo_root / source_path
    if not full_path.exists():
        print(f"Source path does not exist: {full_path}")
        continue
    py_files = list(full_path.glob("*.py"))
    # Exclude key_utils.py and local_*.py
    candidates = [f for f in py_files if not f.name.startswith("key_utils") and not f.name.startswith("local_")]
    if len(candidates) == 1:
        main_file = candidates[0].name
    elif len(candidates) > 1:
        # Try to find one that looks like the id
        id_base = app["id"].replace("ai_", "")
        for c in candidates:
            if id_base in c.name or c.name.replace("_agent", "").replace(".py", "") == id_base:
                main_file = c.name
                break
        else:
            # Pick the first or largest
            main_file = sorted(candidates, key=lambda x: x.stat().st_size, reverse=True)[0].name
    else:
        main_file = None
    if main_file:
        app["main_file"] = main_file
        print(f"Set {app['id']} main_file to {main_file}")
    else:
        print(f"No main file found for {app['id']}")

# Save back
with open(catalog_path, "w") as f:
    json.dump(apps, f, indent=2)