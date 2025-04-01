import streamlit as st

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
    .  .stChatInput {{
        background-color: {theme_color} !important;
        border: 1px solid {font_color} !important;
        border-radius: 8px !important;
    }}
    .stChatInput input {{
        background-color: {theme_color};
        border: 1px solid {font_color};
        color: {font_color};
        border-radius: 8px;
        padding: 8px;
        font-size: 16px;
    }}
    .stChatInput div {{
        background-color: {theme_color};
        border: 1px solid {font_color};
        border-radius: 8px;
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
