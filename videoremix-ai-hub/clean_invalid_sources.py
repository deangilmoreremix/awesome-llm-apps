import json
from pathlib import Path

# Load the catalog
catalog_path = Path(__file__).parent / "data" / "app_catalog.json"
with open(catalog_path, "r") as f:
    apps = json.load(f)

repo_root = Path(__file__).parent.parent

filtered_apps = []
for app in apps:
    source_path = app.get("source_path")
    if source_path:
        full_path = repo_root / source_path
        if full_path.exists():
            filtered_apps.append(app)
        else:
            print(f"Removing app {app['id']} with invalid source_path: {source_path}")
    else:
        filtered_apps.append(app)  # keep if no source_path

# Save back
with open(catalog_path, "w") as f:
    json.dump(filtered_apps, f, indent=2)

print(f"Kept {len(filtered_apps)} apps, removed {len(apps) - len(filtered_apps)}")