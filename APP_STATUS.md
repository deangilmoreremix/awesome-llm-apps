# App Status Guide

## Status Definitions

| Status | Description | Requirements |
|--------|-------------|--------------|
| **ready** | Can run now with API keys | Has main.py, all deps installed, secrets configured |
| **advanced** | Needs extra services/packages | MCP servers, local setup, or specialized APIs |
| **external** | Exposed in hub before full embed | Working app but may need custom deployment |

## App Structure

```
app_modules/
└── instant_lab/
    └── {app_name}/
        ├── __init__.py          # Package marker
        └── app/
            ├── main.py          # Entry point with main() function
            └── .streamlit/
                └── secrets.toml # Required secrets (optional)
```

## Quick Setup

1. Copy `.streamlit/secrets.toml` to each app's `.streamlit/secrets.toml`
2. Fill in your API keys
3. Apps marked "ready" should run immediately

## Secrets Required by App Type

| Secret | Apps That Need It |
|--------|-------------------|
| OPENAI_API_KEY | OpenAI-powered apps, research agents |
| GOOGLE_API_KEY | Gemini-powered apps, Google AI |
| GEMINI_API_KEY | Breakup recovery, multimodal agents |
| SERPAPI_API_KEY | Travel agent, web research |
| ANTHROPIC_API_KEY | Claude-powered apps |
| GITHUB_TOKEN | GitHub MCP agent |
| NOTION_TOKEN | Notion MCP agent |

## Current App Status

Run `python check_apps.py` to verify all registered apps have proper implementations.