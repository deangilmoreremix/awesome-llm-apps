"""
Test the API key modal component
"""

import streamlit as st
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from api_key_modal import configure_api_keys

st.title("🧪 API Key Modal Test")

st.markdown("This is a test page for the API key modal component.")

# Test the modal
api_modal = configure_api_keys("Test App")

# Show current key status
st.subheader("Current API Key Status")
keys = api_modal.get_all_keys()
for key_name, key_value in keys.items():
    masked_value = "***" + key_value[-4:] if key_value else "Not set"
    st.write(f"{key_name}: {masked_value}")

if api_modal.has_required_keys():
    st.success("✅ All required API keys are configured!")
else:
    st.warning("⚠️ Some required API keys are missing.")