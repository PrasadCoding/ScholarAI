import streamlit as st

# Set default theme (Light theme color first)
theme_color = "#ECF0F1"

# Toggle to switch between themes
theme_toggle = st.checkbox("Switch to Dark Theme")

if theme_toggle:
    theme_color = "#34495E"  # Dark theme color

# Set the page title and style based on theme color
st.markdown(
    f"""
    <style>
    .title {{
        color: {theme_color};
        font-size: 50px;
        font-weight: bold;
    }}
    </style>
    """, 
    unsafe_allow_html=True
)

# Display the title
st.markdown('<p class="title">📚 AI Research Assistant</p>', unsafe_allow_html=True)
