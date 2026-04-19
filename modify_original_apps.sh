#!/bin/bash

# Script to modify original app files to use API key modal instead of text inputs

echo "=== Modifying original apps to use API key modal ==="

# Function to update an app
update_original_app() {
    local app_file="$1"
    local app_name="$2"
    local api_keys="$3"  # Comma-separated list of required keys

    if [ ! -f "$app_file" ]; then
        echo "SKIP: $app_file not found"
        return
    fi

    echo "Updating original: $app_file"

    # Backup original file
    cp "$app_file" "${app_file}.backup"

    # Add modal import
    sed -i '1a import sys\nimport os\n\n# Import API key modal\nsys.path.insert(0, os.path.join(os.path.dirname(__file__), '\''../../../'\''))\nfrom api_key_modal import configure_api_keys' "$app_file"

    # Replace text input patterns with modal
    # This is a simplified approach - would need more sophisticated patterns for different apps

    # For OpenAI API key inputs
    sed -i 's/openai_api_key = st\.text_input(".*OpenAI.*API.*Key.*", type="password")/# API keys configured via modal/' "$app_file"

    # For other common patterns
    sed -i 's/serp_api_key = st\.text_input(".*SerpAPI.*", type="password")/# API keys configured via modal/' "$app_file"
    sed -i 's/google_api_key = st\.text_input(".*Google.*API.*", type="password")/# API keys configured via modal/' "$app_file"

    # Add modal configuration near the top
    sed -i 's/st\.title(/# Configure API keys\napi_modal = configure_api_keys("'"$app_name"'")\n\nst.title(/' "$app_file"

    # Add key retrieval
    sed -i 's/^openai_api_key =/# openai_api_key = api_modal.get_key("OPENAI_API_KEY")/' "$app_file"
    sed -i 's/^serp_api_key =/# serp_api_key = api_modal.get_key("SERPAPI_API_KEY")/' "$app_file"

    echo "  ✓ Modified $app_file"
}

# Update key starter apps
update_original_app "starter_ai_agents/ai_travel_agent/travel_agent.py" "AI Travel Agent" "OPENAI_API_KEY,SERPAPI_API_KEY"
update_original_app "starter_ai_agents/ai_meme_generator_agent_browseruse/ai_meme_generator_agent.py" "AI Meme Generator" "OPENAI_API_KEY"
update_original_app "starter_ai_agents/ai_blog_to_podcast_agent/blog_to_podcast_agent.py" "AI Blog to Podcast" "OPENAI_API_KEY"

echo "=== Original app modifications complete ==="
echo "Note: This is a basic modification - individual apps may need custom integration"