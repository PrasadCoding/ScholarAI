import streamlit as st

# Create a row layout for the title and toggle switch
col1, col2 = st.columns([8, 1])  # Adjust column width ratios

with col1:
    st.title("📚 AI Research Assistant")

with col2:
    dark_mode = st.toggle("🌗", value=True)  # Empty text keeps only emoji

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


