import streamlit as st
from shared.app_registry import APP_CATALOG
from shared.filters import filter_apps_by_search


st.title("🚀 VideoRemix AI Hub")
st.write("Launch all your AI tools from one Streamlit hub.")

search = st.text_input("Search apps")

filtered = filter_apps_by_search(APP_CATALOG, search)

st.subheader("Featured Apps")

cols = st.columns(3)
for i, app in enumerate(filtered[:3]):
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"### {app['name']}")
            st.write(app["description"])
            st.caption(app["hub"])