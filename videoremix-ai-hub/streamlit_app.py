import streamlit as st

st.set_page_config(
    page_title="VideoRemix AI Hub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

home = st.Page("pages/00_Home.py", title="Home", icon="🏠")
instant = st.Page("pages/01_Instant_Lab.py", title="Instant Lab", icon="⚡")
revenue = st.Page("pages/02_Revenue_Engine.py", title="Revenue Engine", icon="💰")
creative = st.Page("pages/03_Creative_Studio.py", title="Creative Studio", icon="🎬")
workforce = st.Page("pages/04_AI_Workforce.py", title="AI Workforce", icon="🤖")
voice = st.Page("pages/05_Voice_Command_Center.py", title="Voice Command Center", icon="🎤")
control = st.Page("pages/06_Control_Center.py", title="Control Center", icon="🧠")
knowledge = st.Page("pages/07_Knowledge_Engine.py", title="Knowledge Engine", icon="📚")
builder = st.Page("pages/08_Builder_Lab.py", title="Builder Lab", icon="🧪")
settings = st.Page("pages/09_Settings.py", title="Settings", icon="⚙️")

pg = st.navigation(
    {
        "VideoRemix AI Hub": [
            home,
            instant,
            revenue,
            creative,
            workforce,
            voice,
            control,
            knowledge,
            builder,
            settings,
        ]
    }
)

pg.run()