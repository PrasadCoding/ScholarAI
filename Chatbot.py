import streamlit as st

# Retrieve theme settings from session state
if "theme_color" in st.session_state and "font_color" in st.session_state:
    theme_color = st.session_state["theme_color"]
    font_color = st.session_state["font_color"]
else:
    theme_color = "#ECF0F1"
    font_color = "#2C3E50"

# Apply theme styles
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

# Page title
st.title("Chatbot")

# Chat input field
prompt = st.chat_input("Say something")

# Display user input (for now, no response logic)
if prompt:
    st.write(f"**You:** {prompt}")
