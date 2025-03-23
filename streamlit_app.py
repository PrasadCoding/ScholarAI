import streamlit as st

# Set default theme (Light theme color first)
theme_color = "#ECF0F1"

# Create a theme toggle button on the right side
theme_toggle = st.checkbox("Switch to Dark Theme", value=False, key="theme_toggle")

# Change theme color based on toggle
if theme_toggle:
    theme_color = "#34495E"  # Dark theme color

# Apply custom background color based on theme
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
