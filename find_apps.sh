#!/bin/bash

# Find all directories with Python files that are likely apps
find . -type d \( \
    -path "./starter_ai_agents/*" -o \
    -path "./advanced_ai_agents/*" -o \
    -path "./rag_tutorials/*" -o \
    -path "./awesome_agent_skills/*" -o \
    -path "./mcp_ai_agents/*" -o \
    -path "./voice_ai_agents/*" -o \
    -path "./advanced_llm_apps/*" \
\) | while read dir; do
    # Skip certain subdirectories
    if [[ "$dir" == *"/node_modules"* ]] || [[ "$dir" == *"/__pycache__"* ]] || [[ "$dir" == *"/.git"* ]]; then
        continue
    fi
    
    # Check if directory has Python files
    if find "$dir" -maxdepth 1 -name "*.py" | grep -q .; then
        echo "$dir"
    fi
done | sort
