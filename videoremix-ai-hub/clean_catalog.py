import json
from pathlib import Path

# Load the catalog
catalog_path = Path(__file__).parent / "data" / "app_catalog.json"
with open(catalog_path, "r") as f:
    apps = json.load(f)

repo_root = Path(__file__).parent.parent

for app in apps:
    if "main_file" in app:
        source_path = app.get("source_path")
        if source_path:
            full_path = repo_root / source_path / app["main_file"]
            if not full_path.exists():
                print(f"Removing invalid main_file for {app['id']}: {app['main_file']}")
                del app["main_file"]

# Save back
with open(catalog_path, "w") as f:
    json.dump(apps, f, indent=2)