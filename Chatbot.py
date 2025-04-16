import streamlit as st
import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import os

# Load API key from Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# UI Title
st.title("📄 Chat with your PDF")

# === Theme toggle (optional) ===
col1, col2 = st.columns([4, 1])
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
    </style>
    """, unsafe_allow_html=True
)

# === PDF Upload ===
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

@st.cache_data(show_spinner="Extracting and indexing PDF...")
def process_pdf(file):
    # Step 1: Extract text
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    # Step 2: Chunk it
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = splitter.create_documents([text])

    # Step 3: Create vectorstore
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

if uploaded_file:
    vectorstore = process_pdf(uploaded_file)

    # === Initialize the conversation chain ===
    if "conversation" not in st.session_state:
        llm = ChatOpenAI(model_name="gpt-3.5-turbo")
        memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        st.session_state.conversation = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3}),
            memory=memory
        )
        st.session_state.messages = []

    # === Display chat messages ===
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # === Input area ===
    if prompt := st.chat_input("Ask your PDF anything..."):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = st.session_state.conversation.invoke({"question": prompt})
        answer = response["answer"]

        with st.chat_message("assistant"):
            st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
