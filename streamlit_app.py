import streamlit as st
from streamlit_navigation_bar import st_navbar

st.set_page_config(page_title="ScholarAI", initial_sidebar_state="collapsed")

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

# Ensuring navbar renders once
if "page" not in st.session_state:
    st.session_state.page = st_navbar(pages, styles=styles)
else:
    st.session_state.page = st_navbar(pages, styles=styles)

st.write(f"### {st.session_state.page}")

# Page Content Based on Selection
if st.session_state.page == "Home":
    st.markdown("""
        <div style="text-align: center;">
            <h3><b>Welcome to ScholarAI!</b></h3>
            <p style="font-size: 18px;">
                ScholarAI is an AI-powered research assistant designed to help you with research papers. 
                Upload a paper, and ScholarAI will assist you in answering questions, summarizing key points, 
                and analyzing content.
            </p>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "Library":
    st.write("📚 Welcome to the Library!")

elif st.session_state.page == "Tutorials":
    st.write("📖 Explore our Tutorials!")

elif st.session_state.page == "Development":
    st.write("🛠️ Development Section!")

elif st.session_state.page == "Download":
    st.write("⬇️ Download Resources!")

# Sidebar Content
with st.sidebar:
    st.write("Sidebar Content")
