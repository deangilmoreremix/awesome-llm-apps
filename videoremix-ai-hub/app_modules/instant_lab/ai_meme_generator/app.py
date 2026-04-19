import streamlit as st


def main() -> None:
    st.write("## 😂 AI Meme Generator")
    topic = st.text_input("Topic", placeholder="Cold outreach, startup life, agencies...")
    tone = st.selectbox("Tone", ["Funny", "Savage", "Relatable", "Professional"])

    if st.button("Generate Meme"):
        if not topic.strip():
            st.warning("Please enter a topic.")
            return

        st.success("Meme concept generated.")
        st.write(f"**Top text:** When the client says '{topic}'")
        st.write(f"**Bottom text:** And you instantly switch into {tone.lower()} mode.")