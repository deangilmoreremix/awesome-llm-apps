import streamlit as st


def main() -> None:
    st.write("## 🎙️ AI Blog to Podcast")
    title = st.text_input("Blog title")
    content = st.text_area("Paste the blog content", height=220)

    if st.button("Convert"):
        if not title.strip() or not content.strip():
            st.warning("Please enter both a title and content.")
            return

        st.success("Podcast outline created.")
        st.write("### Hook")
        st.write(f"Today we're breaking down: {title}")

        st.write("### Segment 1")
        st.write("Key idea and why it matters.")

        st.write("### Segment 2")
        st.write("Examples, implications, and takeaways.")

        st.write("### CTA")
        st.write("Invite listeners to subscribe or explore the next step.")