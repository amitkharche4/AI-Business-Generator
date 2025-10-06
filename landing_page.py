
import streamlit as st
import json

st.title("Automated $1K/Week Business Generator")

try:
    with open("latest_ideas.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    st.warning("No ideas generated yet. Run the generator first!")
    data = []

for item in data:
    st.subheader(item['idea'])
    st.write(f"**Market Score:** {item['market_score']}/10")
    st.write("**Assets:**")
    st.write(item['assets'])
    st.markdown("---")
