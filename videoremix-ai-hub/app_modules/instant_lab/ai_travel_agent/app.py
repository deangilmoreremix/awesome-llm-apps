import streamlit as st


def main() -> None:
    st.write("## ✈️ AI Travel Agent")
    destination = st.text_input("Destination")
    days = st.number_input("Number of days", min_value=1, max_value=30, value=3)
    vibe = st.selectbox("Trip vibe", ["Luxury", "Budget", "Adventure", "Family", "Business"])

    if st.button("Build Trip Plan"):
        if not destination.strip():
            st.warning("Please enter a destination.")
            return

        st.success("Trip plan created.")
        for day in range(1, int(days) + 1):
            st.write(f"**Day {day}:** Explore {destination} with a {vibe.lower()} itinerary.")