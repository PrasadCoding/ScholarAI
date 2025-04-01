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
        position: relative;
        transform: translateY(650%);
        width: 100%;
        
       
    }}
    </style>
    """, 
    unsafe_allow_html=True
)

# Chat input field
prompt = st.text_input("", placeholder = "How can I help you!")

if "uploaded_pdf" in st.session_state:
    pdf_file = st.session_state["pdf_file"]
    st.write(f"PDF file '{pdf_file.name}' is accessible in Chatbot page.")
else:
    st.write("No PDF uploaded yet.")


