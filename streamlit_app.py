import streamlit as st

# Initialize session state for theme
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True  # Default: Dark Mode

# Create layout with title and toggle switch on the same line
col1, col2 = st.columns([8, 1])

with col1:
    st.title("📚 AI Research Assistant")

with col2:
    if st.toggle(" ", value=st.session_state.dark_mode, key="theme_toggle"):
        st.session_state.dark_mode = True  # Enable dark mode
    else:
        st.session_state.dark_mode = False  # Enable light mode
    st.experimental_rerun()  # Reload app to apply theme

# Apply Theme Dynamically
theme = "dark" if st.session_state.dark_mode else "light"

# Display message
st.write(f"Current Theme: **{theme.capitalize()} Mode**")

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Upload Paper", "Ask Questions"])

if page == "Home":
    st.write("Welcome to the AI Research Assistant!")
elif page == "Upload Paper":
    uploaded_file = st.sidebar.file_uploader("Upload a PDF", type="pdf")
    if uploaded_file:
        st.success("PDF Uploaded Successfully! (Processing will be added soon)")
elif page == "Ask Questions":
    st.write("Ask questions about the uploaded paper!")
