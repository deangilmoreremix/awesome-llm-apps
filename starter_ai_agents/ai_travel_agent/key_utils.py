import streamlit as st

def get_api_key(provider: str) -> str:
    """
    Get API key for a given provider, prompting user if not already stored in session state.

    Args:
        provider: The name of the API provider (e.g., "OpenAI", "Claude", "ElevenLabs")

    Returns:
        str: The API key entered by the user
    """
    session_key = f"{provider.lower()}_api_key"

    if session_key not in st.session_state:
        st.session_state[session_key] = ""

    key = st.text_input(
        f"Enter {provider} API Key",
        type="password",
        value=st.session_state[session_key],
        key=f"{provider}_key_input"
    )

    # Update session state if key has changed
    if key != st.session_state[session_key]:
        st.session_state[session_key] = key

    return key