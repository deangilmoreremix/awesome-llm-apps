# VideoRemix AI Hub

A unified Streamlit interface for browsing and launching 100+ AI apps from the Awesome LLM Apps collection.

## Features

- **Browse by Hub**: Explore apps organized into categories like Instant Lab, Revenue Engine, Creative Studio, etc.
- **Smart Filtering**: Filter by status (ready/advanced), tags, and featured apps.
- **One-Click Launch**: Launch any compatible app in a new browser tab/window.
- **Live Status**: Automatically detects available apps and their readiness.

## Run locally

```bash
git clone https://github.com/deangilmoreremix/awesome-llm-apps.git
cd awesome-llm-apps/videoremix-ai-hub
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy to Streamlit Community Cloud

1. Push this folder to GitHub
2. In Streamlit Community Cloud, select this repo
3. Main file path: `streamlit_app.py`

## How apps are launched

Apps are launched externally using `subprocess` to run `streamlit run <main_file>` in the app's source directory. This ensures each app runs in its own process without conflicts.

- Apps are registered in `data/app_catalog.json` with metadata including source paths.
- The system automatically detects the main Python file for Streamlit apps.
- Non-Streamlit apps or complex multi-agent systems show appropriate error messages.
- All launch buttons work reliably for compatible apps.

## Supported App Types

- ✅ **Streamlit Apps**: Direct launch support
- ⚠️ **Agent Teams/Multi-Agent**: May require manual setup (run individually)
- ❌ **Non-Streamlit Frameworks**: Not launchable via hub (run from source directory)

For apps not launchable via the hub, follow the individual README instructions in their source directories.