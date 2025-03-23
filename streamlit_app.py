import streamlit as st

col1, col2 = st.columns([4, 1])
with col1:
    st.title("ScholarAI")
with col2:
    on = st.toggle("🌗")

if on:
    theme_color = "#2C3E50"  # Dark theme background
    font_color = "#ECF0F1"   # Light text for dark theme
    sidebar_color = "#34495E"  # Darker sidebar color
else:
    theme_color = "#ECF0F1"  # Light theme background
    font_color = "#2C3E50"   # Dark text for light theme
    sidebar_color = "#BDC3C7"  # Lighter sidebar color

# Apply background color for the main page and sidebar
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {theme_color};
        color: {font_color};
    }}
    .st-emotion-cache-6qob1r e1tphpha8 {{
        background-color: {sidebar_color};
    }}
    </style>
    """, 
    unsafe_allow_html=True
)

# Main page content
st.markdown(f"""
<div style="text-align: center;">
    <h3 style="font-weight: bold; color: {font_color};">Welcome to ScholarAI!</h3>
</div>

<div style="text-align: center; font-size: 18px; color: {font_color};">
    ScholarAI is an AI-powered research assistant designed to help you with your research papers. 
    You can upload a research paper, and ScholarAI will assist you in answering questions, summarizing 
    key points, or analyzing the paper's content. It’s like having a virtual assistant for your academic needs!
</div>
""", unsafe_allow_html=True)

# File uploader section
st.markdown("###")
st.markdown("""<div style="font-size: 18px; color: {font_color};">Upload a PDF</div>""", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type="pdf")
