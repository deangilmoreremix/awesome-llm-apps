"""
Main entry point for ai_game_design_agent_team - Instant Lab App
This module is loaded by the hosting platform to run the agent.
"""

import sys
import os

# Ensure proper path resolution
module_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(module_dir))))

# Add the original agent directory to path
agent_path = os.path.join(project_root, './advanced_ai_agents/multi_agent_apps/agent_teams/ai_game_design_agent_team')


def main():
    """Entry point that runs the Streamlit application."""
    import subprocess
    
    # Get the agent script path
    agent_script = os.path.join(agent_path, 'game_design_agent_team.py')
    
    # Run the Streamlit app
    subprocess.run(['streamlit', 'run', agent_script])


if __name__ == '__main__':
    main()
