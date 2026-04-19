#!/bin/bash

# Comprehensive script to update all apps to use API key modal

echo "=== Updating all apps to use API key modal ==="

# Function to update an app file
update_app_file() {
    local file_path="$1"
    local app_name="$2"

    if [ ! -f "$file_path" ]; then
        echo "SKIP: $file_path not found"
        return
    fi

    echo "Updating: $file_path"

    # Add imports if not present
    if ! grep -q "from api_key_modal import configure_api_keys" "$file_path"; then
        # Find streamlit import and add after it
        sed -i '/import streamlit as st/a import sys\nimport os\n\n# Import API key modal\nsys.path.insert(0, os.path.join(os.path.dirname(__file__), '\''../../../'\''))\ntry:\n    from api_key_modal import configure_api_keys\nexcept ImportError:\n    configure_api_keys = None' "$file_path"
    fi

    # Replace common API key input patterns
    # This is a simplified approach - would need more sophisticated pattern matching for complex cases

    echo "  ✓ Added imports to $file_path"
}

# Update the key "Ready" apps mentioned by user
update_app_file "starter_ai_agents/ai_travel_agent/travel_agent.py" "AI Travel Agent"
update_app_file "starter_ai_agents/ai_meme_generator_agent_browseruse/ai_meme_generator_agent.py" "AI Meme Generator"
update_app_file "starter_ai_agents/ai_blog_to_podcast_agent/blog_to_podcast_agent.py" "AI Blog to Podcast"

echo "=== Manual updates needed for complex API key patterns ==="
echo "The following apps need manual updates:"
echo "- starter_ai_agents/ai_breakup_recovery_agent/ai_breakup_recovery_agent.py"
echo "- And many others with complex API key handling"

echo "=== Update script complete ==="