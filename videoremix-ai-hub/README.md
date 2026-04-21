# VideoRemix AI Hub

A unified Streamlit interface for browsing and launching 100+ AI apps from the Awesome LLM Apps collection.

## Features

- **Browse by Hub**: Explore apps organized into categories like Instant Lab, Revenue Engine, Creative Studio, etc.
- **Smart Filtering**: Filter by status (ready/advanced), tags, and featured apps.
- **One-Click Launch**: Launch any compatible app in a new browser tab/window.
- **Live Status**: Automatically detects available apps and their readiness.

## Local Setup (Required for Full Functionality)

The hub requires local execution to launch apps directly. Follow these steps:

### Prerequisites
- Python 3.8+
- Git
- Internet connection for API-dependent apps

### Installation
```bash
git clone https://github.com/deangilmoreremix/awesome-llm-apps.git
cd awesome-llm-apps/videoremix-ai-hub
pip install -r requirements.txt
```

### Running the Hub
```bash
streamlit run streamlit_app.py
```

### Launching Apps
- Click "Launch App" on any card
- Apps open in new browser tabs automatically
- No additional setup needed for most apps

## Architecture

This is a **multi-page Streamlit application** with:
- Main dashboard with app grid
- Category-specific pages (Instant Lab, Revenue Engine, etc.)
- Integrated app launcher using subprocess
- Expandable app details with "Learn More" sections

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