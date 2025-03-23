import streamlit as st

# Create a row layout for the title and toggle switch
col1, col2 = st.columns([8, 1])  # Adjust column width ratios

with col1:
    st.title("📚 AI Research Assistant")

with col2:
    dark_mode = st.toggle(" ", value=True)  # Empty text keeps only emoji

# Apply Theme Based on Selection
if dark_mode:
    st.markdown("""
        <style>
            body, .stApp {
                background-color: #0e1117;
                color: white;
            }
            [data-testid="stSidebar"] {
                background-color: #161a23;
                color: white;
            }
            .st-bf { transform: translateY(-3px); }  /* Adjust switch position */
        </style>
    """, unsafe_allow_html=True)
    col2.markdown("🌙")  # Moon emoji for dark mode
else:
    st.markdown("""
        <style>
            body, .stApp {
                background-color: white;
                color: black;
            }
            [data-testid="stSidebar"] {
                background-color: #f0f2f6;
                color: black;
            }
            .st-bf { transform: translateY(-3px); }  /* Adjust switch position */
        </style>
    """, unsafe_allow_html=True)
    col2.markdown("☀️")  # Sun emoji for light mode

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Upload Paper", "Ask Questions"])

if page == "Home":
    st.write("Welcome to the AI Research Assistant!")
elif page == "Upload Paper":
    uploaded_file = st.sidebar.file_uploader("Upload a PDF", type="pdf")
    if uploaded_file:
        st.success("PDF Uploaded Successfully! (Processing will be added soon)")
elif page == "Ask Questions":
    st.write("Ask questions about the uploaded paper!")
