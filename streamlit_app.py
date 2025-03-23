import streamlit as st

# Toggle switch for changing theme
toggle = st.sidebar.radio("Select Theme", ("Dark", "Light"))

# Set background color based on theme selection
if toggle == "Dark":
    st.markdown(
        """
        <style>
        .reportview-container {
            background-color: #2C3E50;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        .reportview-container {
            background-color: #ECF0F1;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

# Title with toggle switch on the same line
col1, col2 = st.columns([6, 1])
with col1:
    st.title("ScholarAI")
with col2:
    st.radio("", ("🌙 Dark", "🌞 Light"), key="theme", index=0, horizontal=True)

# Main content
st.write("Welcome to ScholarAI! Toggle between Dark and Light themes using the switch.")
