import json
import os

with open('/workspaces/awesome-llm-apps/videoremix-ai-hub/data/app_catalog.json', 'r') as f:
    apps = json.load(f)

issues = []

for app in apps:
    source_path = os.path.join('/workspaces/awesome-llm-apps', app['source_path'])
    if not os.path.isdir(source_path):
        issues.append(f"Missing directory: {app['source_path']} for app {app['id']}")
    elif 'main_file' in app and app['main_file']:
        main_file_path = os.path.join(source_path, app['main_file'])
        if not os.path.isfile(main_file_path):
            issues.append(f"Missing main_file: {app['main_file']} in {app['source_path']} for app {app['id']}")

for issue in issues:
    print(issue)