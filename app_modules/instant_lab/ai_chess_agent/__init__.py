"""
ai_chess_agent - Instant Lab App Module
Auto-generated wrapper for app.
"""

import sys
import os

# Add path to original agent
module_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(module_dir)))
agent_path = os.path.join(project_root, './advanced_ai_agents/autonomous_game_playing_agent_apps/ai_chess_agent')
sys.path.insert(0, agent_path)

__all__ = ['main']
