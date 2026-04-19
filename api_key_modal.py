"""
API Key Configuration Modal Component
Reusable modal for configuring API keys across all apps
"""

import streamlit as st
import json
import os
from typing import Dict, List, Optional

class APIKeyModal:
    """Modal component for API key configuration"""

    def __init__(self, app_name: str = "AI Agent"):
        self.app_name = app_name
        self.modal_key = f"api_modal_{app_name.replace(' ', '_').lower()}"
        self.keys_key = f"api_keys_{app_name.replace(' ', '_').lower()}"

    def get_required_keys(self) -> Dict[str, Dict]:
        """Define required API keys for different app types"""
        # This can be customized per app
        return {
            "OPENAI_API_KEY": {
                "label": "OpenAI API Key",
                "description": "Required for GPT models",
                "placeholder": "sk-...",
                "required": True
            },
            "GOOGLE_API_KEY": {
                "label": "Google API Key",
                "description": "Required for Gemini models",
                "placeholder": "AIza...",
                "required": False
            },
            "ANTHROPIC_API_KEY": {
                "label": "Anthropic API Key",
                "description": "Required for Claude models",
                "placeholder": "sk-ant-...",
                "required": False
            },
            "SERPAPI_API_KEY": {
                "label": "SerpAPI Key",
                "description": "Required for web search functionality",
                "placeholder": "your-serpapi-key",
                "required": False
            }
        }

    def load_keys_from_session(self) -> Dict[str, str]:
        """Load API keys from session state"""
        return st.session_state.get(self.keys_key, {})

    def save_keys_to_session(self, keys: Dict[str, str]):
        """Save API keys to session state"""
        st.session_state[self.keys_key] = keys

    def has_required_keys(self) -> bool:
        """Check if all required keys are configured"""
        keys = self.load_keys_from_session()
        required_keys = [k for k, v in self.get_required_keys().items() if v["required"]]

        return all(keys.get(key) for key in required_keys)

    def show_modal(self):
        """Show the API key configuration interface"""
        # Don't show configuration if keys are already configured
        if self.has_required_keys():
            # Show a small indicator that keys are configured
            if st.button("🔑 API Keys Configured ✓", help="Click to reconfigure API keys"):
                st.session_state[f"{self.modal_key}_show_config"] = True
        else:
            # Show configuration button if keys are missing
            if st.button(f"🔑 Configure {self.app_name} API Keys", type="primary"):
                st.session_state[f"{self.modal_key}_show_config"] = True

        # Show configuration form if requested
        if st.session_state.get(f"{self.modal_key}_show_config", False):
            self.show_config_form()

    def show_config_form(self):
        """Show the configuration form"""
        st.markdown(f"""
        ## 🔑 Configure {self.app_name}

        This app requires API keys to function. Please configure the keys below:

        **Note:** Your keys are stored securely in your browser session and are not saved to our servers.
        """)

        with st.form(f"api_keys_form_{self.modal_key}"):
            keys_config = self.get_required_keys()
            current_keys = self.load_keys_from_session()

            updated_keys = {}

            # Create input fields for each required key
            for key_name, key_info in keys_config.items():
                label = f"{key_info['label']}"
                if key_info['required']:
                    label += " *"

                value = current_keys.get(key_name, "")
                updated_keys[key_name] = st.text_input(
                    label=label,
                    value=value,
                    type="password",
                    placeholder=key_info['placeholder'],
                    help=key_info['description'],
                    key=f"{self.modal_key}_{key_name}"
                )

            # Action buttons
            col1, col2, col3 = st.columns(3)

            with col1:
                save_submitted = st.form_submit_button("💾 Save Keys", type="primary")

            with col2:
                reset_submitted = st.form_submit_button("🔄 Reset Keys")

            with col3:
                cancel_submitted = st.form_submit_button("❌ Cancel")

            if save_submitted:
                self.save_keys_to_session(updated_keys)
                st.success("✅ API keys saved successfully!")
                st.session_state[f"{self.modal_key}_show_config"] = False
                st.rerun()

            elif reset_submitted:
                self.save_keys_to_session({})
                st.info("🔄 Keys reset. Please enter new keys.")
                st.rerun()

            elif cancel_submitted:
                st.session_state[f"{self.modal_key}_show_config"] = False
                st.rerun()

        # Help section
        with st.expander("🔗 How to get API keys"):
            st.markdown("""
            ### 🔑 API Key Sources

            **OpenAI API Key:**
            - Visit [OpenAI Platform](https://platform.openai.com/api-keys)
            - Create a new API key
            - Copy the key (starts with `sk-`)

            **Google API Key:**
            - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
            - Create a new API key
            - Copy the key (starts with `AIza`)

            **Anthropic API Key:**
            - Visit [Anthropic Console](https://console.anthropic.com/)
            - Create a new API key
            - Copy the key (starts with `sk-ant-`)

            **SerpAPI Key:**
            - Visit [SerpAPI](https://serpapi.com/)
            - Sign up for an account
            - Get your API key
            """)

    def get_key(self, key_name: str) -> Optional[str]:
        """Get a specific API key"""
        keys = self.load_keys_from_session()
        return keys.get(key_name)

    def get_all_keys(self) -> Dict[str, str]:
        """Get all configured API keys"""
        return self.load_keys_from_session()


# Convenience function for easy integration
def configure_api_keys(app_name: str = "AI Agent") -> APIKeyModal:
    """Create and return an API key modal for an app"""
    modal = APIKeyModal(app_name)
    modal.show_modal()
    return modal</content>
<parameter name="filePath">/workspace/0c85e0dc-1244-40ab-8f84-e11668f857da/sessions/agent_e5f1c028-f00b-43e8-8dde-5cf11e8e8e3f/api_key_modal.py