import streamlit as st


def main() -> None:
    st.write("## 🎙️ AI Blog to Podcast")
    title = st.text_input("Blog title")
    content = st.text_area("Paste blog content", height=220)

    if st.button("Convert to Podcast Outline"):
        if not title.strip() or not content.strip():
            st.warning("Please add a title and content.")
            return

        st.success("Podcast outline created.")
        st.write("### Episode Hook")
        st.write(f"Today we're breaking down: {title}")

        st.write("### Main Talking Points")
        st.write("1. The core idea")
        st.write("2. Why it matters")
        st.write("3. Actionable takeaways")

        st.write("### Closing CTA")
        st.write("Invite listeners to learn more or subscribe.")