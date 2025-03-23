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

st.markdown(f"""
# Welcome to ScholarAI!
   
ScholarAI is an AI-powered research assistant designed to help you with your research papers. You can upload a research paper, and ScholarAI will assist you in answering questions, summarizing key points, or analyzing the paper's content. It’s like having a virtual assistant for your academic needs!

**Key Features:**
- Upload and analyze research papers.
- Get answers to your questions about the paper.
- Receive summaries and insights on key points.

This app aims to support students, researchers, and academics in navigating and understanding research papers more efficiently.
""")
