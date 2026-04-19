#!/bin/bash

# Script to update all apps to use the API key modal instead of text inputs

echo "=== Updating apps to use API key modal ==="

# Function to update an app
update_app() {
    local app_file="$1"
    local app_name="$2"

    echo "Updating: $app_file"

    # Check if file exists
    if [ ! -f "$app_file" ]; then
        echo "  File not found: $app_file"
        return
    fi

    # Add import if not already present
    if ! grep -q "from api_key_modal import configure_api_keys" "$app_file"; then
        # Find the import section
        if grep -q "^import streamlit as st" "$app_file"; then
            sed -i '/^import streamlit as st/a import sys\nimport os\n\n# Import API key modal\nsys.path.insert(0, os.path.join(os.path.dirname(__file__), '\''../../../'\''))\nfrom api_key_modal import configure_api_keys' "$app_file"
        fi
    fi

    # Replace text inputs for API keys with modal
    # This is a simplified approach - in practice, we'd need more sophisticated pattern matching
    if grep -q "st.text_input.*API.*Key" "$app_file"; then
        echo "  Found API key inputs in $app_file - would need manual update"
    fi
}

# Update key starter apps
update_app "starter_ai_agents/ai_travel_agent/travel_agent.py" "AI Travel Agent"
update_app "starter_ai_agents/ai_meme_generator_agent_browseruse/ai_meme_generator_agent.py" "AI Meme Generator"
update_app "starter_ai_agents/ai_blog_to_podcast_agent/blog_to_podcast_agent.py" "AI Blog to Podcast"

echo "=== Update complete ==="
echo "Note: Manual updates needed for complex API key patterns"