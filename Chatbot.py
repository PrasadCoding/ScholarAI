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
   .stTextInput {{
        position: fixed;
        bottom: 10px;
        left: 50%;
        transform: translateX(-50%);
        width: 60%;
    }}
    </style>
    """, 
    unsafe_allow_html=True
)

# Chat input field
prompt = st.text_input("How can I help you today?")

# Display user input
if prompt:
    st.write(f"**You:** {prompt}")
