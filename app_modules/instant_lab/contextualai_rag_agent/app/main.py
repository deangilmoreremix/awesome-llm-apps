"""
Main entry point for contextualai_rag_agent - Instant Lab App
This module is loaded by the hosting platform to run the agent.
"""

import sys
import os

# Ensure proper path resolution
module_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(module_dir))))

# Add the original agent directory to path
agent_path = os.path.join(project_root, './rag_tutorials/contextualai_rag_agent')


def main():
    """Entry point that runs the Streamlit application."""
    import subprocess
    
    # Get the agent script path
    agent_script = os.path.join(agent_path, 'contextualai_rag_agent.py')
    
    # Run the Streamlit app
    subprocess.run(['streamlit', 'run', agent_script])


if __name__ == '__main__':
    main()
