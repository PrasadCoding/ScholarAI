import streamlit as st
from streamlit_navigation_bar import st_navbar

st.set_page_config(initial_sidebar_state="collapsed")

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

pages = ["Home", "Library", "Tutorials", "Development", "Download"]
styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

page = st_navbar(pages, styles=styles)

if page == "Home":
    st.markdown(f"""
    <div style="text-align: center;">
        <h3 style="font-weight: bold; color: {font_color};">Welcome to ScholarAI!</h3>
    </div>

    <div style="text-align: center; font-size: 18px; color: {font_color};">
        ScholarAI is an AI-powered research assistant designed to help you with your research papers. 
        You can upload a research paper, and ScholarAI will assist you in answering questions, summarizing 
        key points, or analyzing the paper's content. It’s like having a virtual assistant for your academic needs!
    </div>
    """, unsafe_allow_html=True)

    st.markdown("###")
    st.markdown(f"""<div style="font-size: 18px; color: {font_color};">Upload a PDF</div>""", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type="pdf")

elif page == "Library":
    st.write("This is the Library Page.")

elif page == "Tutorials":
    st.write("This is the Tutorials Page.")

elif page == "Development":
    st.write("This is the Development Page.")

elif page == "Download":
    st.write("This is the Download Page.")

with st.sidebar:
    st.write("Sidebar")
