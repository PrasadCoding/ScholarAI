import streamlit as st

# Set default theme (Light theme color first)
theme_color = "#ECF0F1"  # Light theme color

# Add a toggle switch on the top right for theme selection
col1, col2 = st.columns([3, 1])  # Create two columns
with col2:
    # Toggle theme with a radio button
    theme_toggle = st.radio("", ["Light", "Dark"], index=0, key="theme_toggle", horizontal=True)

# Change theme color based on toggle selection
if theme_toggle == "Dark":
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

# Title
st.title("📚 AI Research Assistant")
