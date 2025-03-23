import streamlit as st

col1, col2 = st.columns([4, 1])
with col1:
    st.title("ScholarAI")
with col2:
    on = st.toggle("🌗")

if on:
    theme_color = "#2C3E50"  
else:
    theme_color = "#ECF0F1"


st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {theme_color};
    }}
    </style>
    """, 
    unsafe_allow_html=True
)
