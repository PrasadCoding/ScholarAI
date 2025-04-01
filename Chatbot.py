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
    .chat-container {{
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: {theme_color};
        padding: 10px;
        border-top: 1px solid {font_color};
    }}
    .chat-container input {{
        width: 100%;
        padding: 10px;
        border: 1px solid {font_color};
        border-radius: 8px;
        font-size: 16px;
        background-color: {theme_color};
        color: {font_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Chat input field at the bottom
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
prompt = st.text_input("How can I help you today?")
st.markdown('</div>', unsafe_allow_html=True)

# Display user input (for now, no response logic)
if prompt:
    st.write(f"**You:** {prompt}")
