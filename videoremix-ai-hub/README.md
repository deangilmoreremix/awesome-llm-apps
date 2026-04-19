# VideoRemix AI Hub

A single Streamlit multipage hub that loads many AI apps from one catalog.

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy to Streamlit Community Cloud

1. Push this folder to GitHub
2. In Streamlit Community Cloud, select this repo
3. Main file path: `streamlit_app.py`

## How apps are loaded

- Register apps in `data/app_catalog.json`
- Create each module in `app_modules/<hub>/<tool_name>/app.py`
- Each module must expose `main()`

## Current starter modules

- **Instant Lab** / AI Meme Generator
- **Instant Lab** / AI Travel Agent
- **Creative Studio** / AI Blog to Podcast

The remaining catalog items are scaffolded as placeholders so the whole UI is navigable now.