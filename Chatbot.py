import streamlit as st
import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import os

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

col1, col2 = st.columns([4, 1])
with col1:
    st.title("Ask Your Paper")
with col2:
    on = st.toggle("🌗", key="theme_toggle")

# Set colors based on toggle
if on:
    theme_color = "#2C3E50"  # dark background
    font_color = "#ECF0F1"   # light text
else:
    theme_color = "#ECF0F1"  # light background
    font_color = "#2C3E50"   # dark text

# Apply custom CSS for background and font color
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {theme_color};
        color: {font_color};
    }}
    .stMarkdown, .stTextInput, .stChatInput {{
        color: {font_color} !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(f"<span style='color:{font_color}'>{message['content']}</span>", unsafe_allow_html=True)

# React to user input
if prompt := st.chat_input("What is up?"):
    st.chat_message("user").markdown(f"<span style='color:{font_color}'>{prompt}</span>", unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    with st.chat_message("assistant"):
        st.markdown(f"<span style='color:{font_color}'>{response}</span>", unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": response})

