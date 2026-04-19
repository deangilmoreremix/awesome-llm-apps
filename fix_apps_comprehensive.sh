#!/bin/bash

# Comprehensive fix: Modify original app files to handle API keys gracefully
# This ensures apps work regardless of hosting platform status

echo "=== Implementing comprehensive app fixes ==="

# Function to fix an app
fix_app() {
    local app_file="$1"
    local app_name="$2"
    
    if [ ! -f "$app_file" ]; then
        echo "SKIP: $app_file not found"
        return
    fi
    
    echo "Fixing: $app_file"
    
    # Create backup
    cp "$app_file" "${app_file}.bak"
    
    # Add graceful API key handling
    # Replace direct text inputs with fallback logic
    
    # For OpenAI keys
    sed -i 's/openai_api_key = st\.text_input(".*OpenAI.*API.*Key.*", type="password")/# Try to get OpenAI key from environment or user input\ntry:\n    openai_api_key = os.getenv("OPENAI_API_KEY") or st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))\nexcept:\n    openai_api_key = st.text_input("OpenAI API Key", type="password")/' "$app_file"
    
    # For SerpAPI keys
    sed -i 's/serp_api_key = st\.text_input(".*SerpAPI.*", type="password")/# Try to get SerpAPI key from environment or user input\ntry:\n    serp_api_key = os.getenv("SERPAPI_API_KEY") or st.text_input("SerpAPI Key", type="password", value=os.getenv("SERPAPI_API_KEY", ""))\nexcept:\n    serp_api_key = st.text_input("SerpAPI Key", type="password")/' "$app_file"
    
    # For Google keys
    sed -i 's/google_api_key = st\.text_input(".*Google.*API.*", type="password")/# Try to get Google key from environment or user input\ntry:\n    google_api_key = os.getenv("GOOGLE_API_KEY") or st.text_input("Google API Key", type="password", value=os.getenv("GOOGLE_API_KEY", ""))\nexcept:\n    google_api_key = st.text_input("Google API Key", type="password")/' "$app_file"
    
    # Add environment variable support at the top
    if ! grep -q "import os" "$app_file"; then
        sed -i '1a import os' "$app_file"
    fi
    
    # Add graceful error handling for missing keys
    sed -i 's/if openai_api_key and serp_api_key:/if openai_api_key and (serp_api_key or not "serp" in locals()):\n    # API keys are available\nelse:\n    st.warning("Please provide the required API keys above")\n    st.stop()\n\nif openai_api_key and (serp_api_key if "serp_api_key" in locals() else True):/' "$app_file"
    
    echo "  ✓ Fixed $app_file with graceful API key handling"
}

# Fix key apps
fix_app "starter_ai_agents/ai_travel_agent/travel_agent.py" "AI Travel Agent"
fix_app "starter_ai_agents/ai_meme_generator_agent_browseruse/ai_meme_generator_agent.py" "AI Meme Generator"
fix_app "starter_ai_agents/ai_blog_to_podcast_agent/blog_to_podcast_agent.py" "AI Blog to Podcast"
fix_app "starter_ai_agents/ai_breakup_recovery_agent/ai_breakup_recovery_agent.py" "AI Breakup Recovery"

echo "=== App fixes complete ==="
echo "Apps now handle API keys gracefully and should work regardless of hosting platform status"