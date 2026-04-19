"""
Main entry point for AI Breakup Recovery Agent - Instant Lab App
This module is loaded by the hosting platform to run the agent.
"""

import sys
import os

# Ensure proper path resolution
module_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(module_dir))))

# Add the original agent directory to path
agent_path = os.path.join(project_root, 'starter_ai_agents', 'ai_breakup_recovery_agent')
sys.path.insert(0, agent_path)


def main():
    """Entry point that runs the Streamlit application."""
    import subprocess
    import os
    
    # Get the agent script path
    agent_script = os.path.join(agent_path, 'ai_breakup_recovery_agent.py')
    
    # Run the Streamlit app
    subprocess.run(['streamlit', 'run', agent_script])


if __name__ == '__main__':
    main()