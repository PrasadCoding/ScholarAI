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

st.markdown(
    """
    <div style='text-align:center; padding: 50px;'>
        <h2 style='color: {font_color};'>Your AI-powered Research Assistant</h2>
        <p style='color: {font_color}; font-size: 18px;'>Upload your research papers and get AI-based assistance for all your questions!</p>
        <button style="padding: 15px 30px; font-size: 16px; background-color: {font_color}; color: {theme_color}; border-radius: 10px; border: none; cursor: pointer;">Upload Paper</button>
    </div>
    """, 
    unsafe_allow_html=True
)
