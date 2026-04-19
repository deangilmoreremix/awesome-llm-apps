import streamlit as st


def main() -> None:
    st.write("## 😂 AI Meme Generator")
    topic = st.text_input("Enter a meme topic", placeholder="Cold outreach, startup life, agencies...")
    tone = st.selectbox("Tone", ["Funny", "Savage", "Relatable", "Professional"])

    if st.button("Generate Meme Idea"):
        if not topic.strip():
            st.warning("Please enter a topic.")
            return

        st.success("Meme generated.")
        st.write(f"**Top Text:** When the client says '{topic}'")
        st.write(f"**Bottom Text:** And you switch into {tone.lower()} mode instantly.")