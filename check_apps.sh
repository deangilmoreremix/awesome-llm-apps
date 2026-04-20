#!/bin/bash

# List of filtered URLs
urls=(
"advanced_ai_agents/multi_agent_apps/devpulse_ai/"
"advanced_ai_agents/multi_agent_apps/ai_home_renovation_agent"
"awesome_agent_skills/self-improving-agent-skills/"
"starter_ai_agents/ai_blog_to_podcast_agent/"
"starter_ai_agents/ai_breakup_recovery_agent/"
"starter_ai_agents/ai_data_analysis_agent/"
"starter_ai_agents/ai_medical_imaging_agent/"
"starter_ai_agents/ai_meme_generator_agent_browseruse/"
"starter_ai_agents/ai_music_generator_agent/"
"starter_ai_agents/ai_travel_agent/"
"starter_ai_agents/gemini_multimodal_agent_demo/"
"starter_ai_agents/mixture_of_agents/"
"starter_ai_agents/xai_finance_agent/"
"starter_ai_agents/openai_research_agent/"
"starter_ai_agents/web_scraping_ai_agent/"
"advanced_ai_agents/multi_agent_apps/ai_home_renovation_agent"
"advanced_ai_agents/multi_agent_apps/devpulse_ai/"
"advanced_ai_agents/single_agent_apps/ai_deep_research_agent/"
"advanced_ai_agents/multi_agent_apps/agent_teams/ai_vc_due_diligence_agent_team"
"advanced_ai_agents/single_agent_apps/research_agent_gemini_interaction_api"
"advanced_ai_agents/single_agent_apps/ai_consultant_agent"
"advanced_ai_agents/single_agent_apps/ai_system_architect_r1/"
"advanced_ai_agents/multi_agent_apps/ai_financial_coach_agent/"
"advanced_ai_agents/single_agent_apps/ai_movie_production_agent/"
"advanced_ai_agents/single_agent_apps/ai_investment_agent/"
"advanced_ai_agents/single_agent_apps/ai_health_fitness_agent/"
"advanced_ai_agents/multi_agent_apps/product_launch_intelligence_agent"
"advanced_ai_agents/single_agent_apps/ai_fraud_investigation_agent/"
"advanced_ai_agents/single_agent_apps/ai_journalist_agent/"
"advanced_ai_agents/multi_agent_apps/ai_mental_wellbeing_agent/"
"advanced_ai_agents/single_agent_apps/ai_meeting_agent/"
"advanced_ai_agents/multi_agent_apps/ai_self_evolving_agent/"
"advanced_ai_agents/multi_agent_apps/agent_teams/ai_sales_intelligence_agent_team"
"advanced_ai_agents/multi_agent_apps/ai_news_and_podcast_agents/"
"advanced_ai_agents/multi_agent_apps/trust_gated_agent_team/"
"advanced_ai_agents/autonomous_game_playing_agent_apps/ai_3dpygame_r1/"
"advanced_ai_agents/autonomous_game_playing_agent_apps/ai_chess_agent/"
"advanced_ai_agents/autonomous_game_playing_agent_apps/ai_tic_tac_toe_agent/"
"advanced_ai_agents/multi_agent_apps/agent_teams/ai_competitor_intelligence_agent_team/"
"advanced_ai_agents/multi_agent_apps/agent_teams/ai_finance_agent_team/"
"advanced_ai_agents/multi_agent_apps/agent_teams/ai_game_design_agent_team/"
"advanced_ai_agents/multi_agent_apps/agent_teams/ag2_adaptive_research_team/"
"advanced_ai_agents/multi_agent_apps/agent_teams/ai_legal_agent_team/"
"advanced_ai_agents/multi_agent_apps/agent_teams/ai_recruitment_agent_team/"
"advanced_ai_agents/multi_agent_apps/agent_teams/ai_real_estate_agent_team"
"advanced_ai_agents/multi_agent_apps/agent_teams/ai_services_agency/"
"advanced_ai_agents/multi_agent_apps/agent_teams/ai_teaching_agent_team/"
"advanced_ai_agents/multi_agent_apps/agent_teams/multimodal_coding_agent_team/"
"advanced_ai_agents/multi_agent_apps/agent_teams/multimodal_design_agent_team/"
"advanced_ai_agents/multi_agent_apps/agent_teams/multimodal_uiux_feedback_agent_team/"
"/advanced_ai_agents/multi_agent_apps/agent_teams/ai_travel_planner_agent_team/"
"voice_ai_agents/ai_audio_tour_agent/"
"voice_ai_agents/customer_support_voice_agent/"
"voice_ai_agents/voice_rag_openaisdk/"
"mcp_ai_agents/browser_mcp_agent/"
"mcp_ai_agents/github_mcp_agent/"
"mcp_ai_agents/notion_mcp_agent"
"mcp_ai_agents/ai_travel_planner_mcp_agent_team"
"mcp_ai_agents/multi_mcp_agent_router/"
"rag_tutorials/agentic_rag_embedding_gemma"
"rag_tutorials/agentic_rag_with_reasoning/"
"rag_tutorials/ai_blog_search/"
"rag_tutorials/autonomous_rag/"
"rag_tutorials/contextualai_rag_agent/"
"rag_tutorials/corrective_rag/"
"rag_tutorials/deepseek_local_rag_agent/"
"rag_tutorials/gemini_agentic_rag/"
"rag_tutorials/hybrid_search_rag/"
"rag_tutorials/llama3.1_local_rag/"
"rag_tutorials/local_hybrid_search_rag/"
"rag_tutorials/local_rag_agent/"
"rag_tutorials/rag-as-a-service/"
"rag_tutorials/rag_agent_cohere/"
"rag_tutorials/rag_chain/"
"rag_tutorials/rag_database_routing/"
"rag_tutorials/vision_rag/"
"rag_tutorials/rag_failure_diagnostics_clinic/"
"rag_tutorials/knowledge_graph_rag_citations/"
"awesome_agent_skills/self-improving-agent-skills/"
"awesome_agent_skills/academic-researcher/"
"awesome_agent_skills/code-reviewer/"
"awesome_agent_skills/content-creator/"
"awesome_agent_skills/data-analyst/"
"awesome_agent_skills/debugger/"
"awesome_agent_skills/decision-helper/"
"awesome_agent_skills/deep-research/"
"awesome_agent_skills/editor/"
"awesome_agent_skills/email-drafter/"
"awesome_agent_skills/fact-checker/"
"awesome_agent_skills/fullstack-developer/"
"awesome_agent_skills/meeting-notes/"
"awesome_agent_skills/project-planner/"
"awesome_agent_skills/python-expert/"
"awesome_agent_skills/sprint-planner/"
"awesome_agent_skills/strategy-advisor/"
"awesome_agent_skills/technical-writer/"
"awesome_agent_skills/ux-designer/"
"awesome_agent_skills/visualization-expert/"
"advanced_llm_apps/llm_apps_with_memory_tutorials/ai_arxiv_agent_memory/"
"advanced_llm_apps/llm_apps_with_memory_tutorials/ai_travel_agent_memory/"
"advanced_llm_apps/llm_apps_with_memory_tutorials/llama3_stateful_chat/"
"advanced_llm_apps/llm_apps_with_memory_tutorials/llm_app_personalized_memory/"
"advanced_llm_apps/llm_apps_with_memory_tutorials/local_chatgpt_with_memory/"
"advanced_llm_apps/llm_apps_with_memory_tutorials/multi_llm_memory/"
"advanced_llm_apps/chat_with_X_tutorials/chat_with_github/"
"advanced_llm_apps/chat_with_X_tutorials/chat_with_gmail/"
"advanced_llm_apps/chat_with_X_tutorials/chat_with_pdf/"
"advanced_llm_apps/chat_with_X_tutorials/chat_with_research_papers/"
"advanced_llm_apps/chat_with_X_tutorials/chat_with_substack/"
"advanced_llm_apps/chat_with_X_tutorials/chat_with_youtube_videos/"
"advanced_llm_apps/llm_optimization_tools/toonify_token_optimization/"
"advanced_llm_apps/llm_optimization_tools/headroom_context_optimization/"
"advanced_llm_apps/llm_finetuning_tutorials/gemma3_finetuning/"
"advanced_llm_apps/llm_finetuning_tutorials/llama3.2_finetuning/"
"ai_agent_framework_crash_course/google_adk_crash_course/"
"ai_agent_framework_crash_course/openai_sdk_crash_course/"
)

missing_dirs=()
missing_main_files=()

for url in "${urls[@]}"; do
    # Normalize: remove leading / and trailing /
    normalized=$(echo "$url" | sed 's|^/||; s|/$||')
    
    # Check if in catalog
    if grep -q "\"source_path\": \"$normalized\"" videoremix-ai-hub/data/app_catalog.json; then
        # Check directory
        dir_path="/workspaces/awesome-llm-apps/$normalized"
        if [ ! -d "$dir_path" ]; then
            missing_dirs+=("$dir_path")
        fi
        
        # Check main_file
        main_file=$(grep -A10 "\"source_path\": \"$normalized\"" videoremix-ai-hub/data/app_catalog.json | grep -o '"main_file": "[^"]*"' | sed 's/"main_file": "\([^"]*\)"/\1/')
        if [ -n "$main_file" ]; then
            file_path="$dir_path/$main_file"
            if [ ! -f "$file_path" ]; then
                missing_main_files+=("$file_path")
            fi
        fi
    fi
done

# Special check for hub quick start
hub_app_py="/workspaces/awesome-llm-apps/videoremix-ai-hub/streamlit_app.py"
hub_req="/workspaces/awesome-llm-apps/videoremix-ai-hub/requirements.txt"

hub_status="valid"
if [ ! -f "$hub_app_py" ]; then
    hub_status="missing streamlit_app.py"
elif [ ! -f "$hub_req" ]; then
    hub_status="missing requirements.txt"
else
    if [ ! -s "$hub_req" ]; then
        hub_status="requirements.txt is empty"
    fi
fi

# Output
echo "Missing directories:"
for dir in "${missing_dirs[@]}"; do
    echo "$dir"
done

echo "Missing main files:"
for file in "${missing_main_files[@]}"; do
    echo "$file"
done

echo "Hub quick start status: $hub_status"