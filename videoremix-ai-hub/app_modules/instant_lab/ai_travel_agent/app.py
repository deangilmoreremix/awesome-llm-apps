import streamlit as st


def main() -> None:
    st.write("## ✈️ AI Travel Agent")
    destination = st.text_input("Destination")
    days = st.number_input("Days", min_value=1, max_value=30, value=3)
    vibe = st.selectbox("Trip style", ["Luxury", "Budget", "Adventure", "Family", "Business"])

    if st.button("Build Itinerary"):
        if not destination.strip():
            st.warning("Please enter a destination.")
            return

        st.success("Trip itinerary created.")
        for day in range(1, int(days) + 1):
            st.write(f"**Day {day}:** {destination} • {vibe} plan")