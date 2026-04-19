"""
chat_with_gmail - Instant Lab App Module
Auto-generated wrapper for app.
"""

import sys
import os

# Add path to original agent
module_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(module_dir)))
agent_path = os.path.join(project_root, './advanced_llm_apps/chat_with_X_tutorials/chat_with_gmail')
sys.path.insert(0, agent_path)

__all__ = ['main']
