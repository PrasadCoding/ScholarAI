import streamlit as st

# Initialize theme settings if not in session state
if "theme_color" not in st.session_state:
    st.session_state["theme_color"] = "#ECF0F1"  # Default light theme
    st.session_state["font_color"] = "#2C3E50"  # Default font color for light theme

# Theme toggle
col1, col2 = st.columns([4, 1])
with col1:
    st.title("Chatbot")
with col2:
    on = st.toggle("🌗", value=("theme_color" in st.session_state and st.session_state["theme_color"] == "#2C3E50"))

# Update theme based on toggle
if on:
    st.session_state["theme_color"] = "#2C3E50"  # Dark theme
    st.session_state["font_color"] = "#ECF0F1"  # Light font for dark theme
else:
    st.session_state["theme_color"] = "#ECF0F1"  # Light theme
    st.session_state["font_color"] = "#2C3E50"  # Dark font for light theme

# Apply theme styles
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {st.session_state["theme_color"]};
        color: {st.session_state["font_color"]};
    }}
    </style>
    """, 
    unsafe_allow_html=True
)

# Chat input field
prompt = st.chat_input("Say something")

# Display user input (for now, no response logic)
if prompt:
    st.write(f"**You:** {prompt}")
