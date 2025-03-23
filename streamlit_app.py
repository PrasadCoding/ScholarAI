import streamlit as st

# Initialize session state for theme
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True  # Default: Dark Mode

# Custom CSS for Dark and Light Mode
dark_theme = """
<style>
    body {
        background-color: #202020;
        color: #F0F0F0;
    }
    .stApp {
        background-color: #202020;
        color: #F0F0F0;
    }
    .stButton, .stRadio, .stTextInput, .stFileUploader {
        background-color: #2E2E2E;
        color: #F0F0F0;
    }
    .stButton:hover, .stRadio:hover, .stTextInput:hover, .stFileUploader:hover {
        background-color: #3C3C3C;
    }
</style>
"""

light_theme = """
<style>
    body {
        background-color: #FFFFFF;
        color: #000000;
    }
    .stApp {
        background-color: #FFFFFF;
        color: #000000;
    }
    .stButton, .stRadio, .stTextInput, .stFileUploader {
        background-color: #F1F1F1;
        color: #000000;
    }
    .stButton:hover, .stRadio:hover, .stTextInput:hover, .stFileUploader:hover {
        background-color: #E0E0E0;
    }
</style>
"""

# Layout: Title and Toggle Button on the same line with 🌗 emoji
col1, col2 = st.columns([8, 1])

with col1:
    st.title("📚 AI Research Assistant")

with col2:
    st.session_state.dark_mode = st.toggle("🌗", value=st.session_state.dark_mode, key="theme_toggle")

# Apply the selected theme using CSS
if st.session_state.dark_mode:
    st.markdown(dark_theme, unsafe_allow_html=True)
else:
    st.markdown(light_theme, unsafe_allow_html=True)

# Home page content
st.write("Welcome to the **AI Research Assistant**! Use the toggle to switch themes.")
