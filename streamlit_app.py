import streamlit as st

col1, col2 = st.columns([4, 1])
with col1:
    st.title("ScholarAI")
with col2:
    on = st.toggle("🌗")

if on:
    theme_color = "#2C3E50"
    font_color = "#ECF0F1"
else:
    theme_color = "#ECF0F1"
    font_color = "#2C3E50"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {theme_color};
        color: {font_color};
    }}
    </style>
    """, 
    unsafe_allow_html=True
)
