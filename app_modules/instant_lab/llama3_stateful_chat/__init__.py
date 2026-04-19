"""
llama3_stateful_chat - Instant Lab App Module
Auto-generated wrapper for app.
"""

import sys
import os

# Add path to original agent
module_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(module_dir)))
agent_path = os.path.join(project_root, './advanced_llm_apps/llm_apps_with_memory_tutorials/llama3_stateful_chat')
sys.path.insert(0, agent_path)

__all__ = ['main']
