"""
AI Breakup Recovery Agent - Instant Lab App Module
This module provides the main() function for the hosted application.
"""

import sys
import os

# Add the parent directory to sys.path to access the original agent code
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../../starter_ai_agents/ai_breakup_recovery_agent'))

# Import the main application
from ai_breakup_recovery_agent import *  # noqa: F401, F403

# Re-export key items for the app module interface
__all__ = ['st', 'Agent', 'initialize_agents']