import streamlit as st

# Set up the layout of the page with the title and a toggle button for theme
st.set_page_config(page_title="ScholarAI", layout="wide")

# Create columns for title and toggle switch
col1, col2 = st.columns([6, 1])
with col1:
    st.title("ScholarAI")
with col2:
    # Create a toggle switch using checkbox
    theme_toggle = st.checkbox("🌙 Dark Mode", value=False)

# Set the background color based on the toggle state
if theme_toggle:
    st.markdown(
        """
        <style>
        .reportview-container {
            background-color: #2C3E50;
            color: white;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        .reportview-container {
            background-color: #ECF0F1;
            color: black;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

# Main content of the page
st.write("Welcome to ScholarAI! Toggle between Dark and Light themes using the switch.")
