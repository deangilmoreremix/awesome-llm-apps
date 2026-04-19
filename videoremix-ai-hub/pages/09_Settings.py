import streamlit as st

st.title("⚙️ Settings")
st.write("Use Streamlit secrets for API keys.")
st.code(
    """
# .streamlit/secrets.toml
OPENAI_API_KEY="your-key"
GOOGLE_API_KEY="your-key"
ANTHROPIC_API_KEY="your-key"
""",
    language="toml",
)