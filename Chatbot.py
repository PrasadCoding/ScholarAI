import streamlit as st
from io import BytesIO
import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# Load OpenAI API key from environment variable or .env file
import os
os.environ["OPENAI_API_KEY"] = "your-openai-key"  # Replace with env loading in production

# --- Styling and Layout ---
col1, col2 = st.columns([4, 1])
with col1:
    st.title("ScholarAI")
with col2:
    on = st.toggle("🌗")

if on:
    theme_color = "#2C3E50"
    font_color = "#ECF0F1"
    user_bg = "#34495E"
    bot_bg = "#1ABC9C"
else:
    theme_color = "#ECF0F1"
    font_color = "#2C3E50"
    user_bg = "#BDC3C7"
    bot_bg = "#3498DB"

st.markdown(f"""
<style>
    .stApp {{ background-color: {theme_color}; color: {font_color}; }}
    .message-box {{
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
        max-width: 75%;
    }}
    .user-msg {{ background-color: {user_bg}; align-self: flex-end; }}
    .bot-msg {{ background-color: {bot_bg}; align-self: flex-start; }}
</style>
""", unsafe_allow_html=True)

# --- RAG Pipeline Functions ---
def extract_text_from_pdf(file_obj):
    doc = fitz.open(stream=file_obj, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def split_text(text, chunk_size=500, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.create_documents([text])

def create_vector_store(documents):
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore

def build_conversational_chain(vectorstore):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    conversation = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3}),
        memory=memory
    )
    return conversation

# --- Check for uploaded PDF ---
if "uploaded_pdf" not in st.session_state:
    st.warning("⚠️ Please upload a PDF on the upload page first.")
else:
    # --- Initialize chat and process PDF only once ---
    if "conversation_chain" not in st.session_state:
        st.info("⏳ Processing PDF and building AI assistant...")
        pdf_file = st.session_state["uploaded_pdf"]
        pdf_bytes = pdf_file.read()
        text = extract_text_from_pdf(BytesIO(pdf_bytes))
        documents = split_text(text)
        vectorstore = create_vector_store(documents)
        st.session_state.conversation_chain = build_conversational_chain(vectorstore)
        st.session_state.chat_history = []

    # --- Chat UI ---
    st.markdown("#### Ask a question about your PDF")

    user_input = st.text_input("Type your question here...", key="user_input")

    if user_input:
        # Get response from the RAG pipeline
        response = st.session_state.conversation_chain.invoke({"question": user_input})
        bot_reply = response["answer"]

        # Store in chat history
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("bot", bot_reply))

    # --- Display Chat Bubbles ---
    for speaker, msg in st.session_state.chat_history:
        css_class = "user-msg" if speaker == "user" else "bot-msg"
        st.markdown(f'<div class="message-box {css_class}">{msg}</div>', unsafe_allow_html=True)
