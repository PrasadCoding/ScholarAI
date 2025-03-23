import streamlit as st

# Toggle Button for Theme
dark_mode = st.toggle("🌗 Toggle Dark Mode", value=True)

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
        </style>
    """, unsafe_allow_html=True)
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
        </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Upload Paper", "Ask Questions"])

st.title("📚 AI Research Assistant")

if page == "Home":
    st.write("Welcome to the AI Research Assistant!")
elif page == "Upload Paper":
    uploaded_file = st.sidebar.file_uploader("Upload a PDF", type="pdf")
    if uploaded_file:
        st.success("PDF Uploaded Successfully! (Processing will be added soon)")
elif page == "Ask Questions":
    st.write("Ask questions about the uploaded paper!")
