import streamlit as st
import os
import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

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


# === Step 1: Extract text from PDF ===
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")  # accepts file-like object
    text = ""
    for page in doc:
        text += page.get_text()
    return text


# === Step 2: Split text into chunks ===
def split_text(text, chunk_size=500, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.create_documents([text])

# === Step 3: Create embeddings and store in FAISS ===
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


if "uploaded_pdf" in st.session_state:
    pdf_file = st.session_state["uploaded_pdf"]
    text = extract_text_from_pdf(pdf_file)
    documents = split_text(text)
    vectorstore = create_vector_store(documents)
    conversation_chain = build_conversational_chain(vectorstore)
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
        response = conversation_chain.invoke({"question": prompt})
    
        response = f"Bot: {response["answer"]}"
        with st.chat_message("assistant"):
            st.markdown(f"<span style='color:{font_color}'>{response}</span>", unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": response})
    
else:
    pass





