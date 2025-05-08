# import streamlit as st

# pg = st.navigation(["Home.py", "Chatbot.py"])
# pg.run()

import streamlit as st
import os
import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain



# st.set_page_config(page_title="Research Paper RAG Chatbot", page_icon="📚", layout="wide")

# --- Sidebar ---
with st.sidebar:
    st.title("Navigation")
    st.markdown("---")
    
    page = st.radio(
        "Navigate", 
        ["Home", "Chatbot", "Paper Summary", "What is RAG?", "FAQ", "About"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.caption("Empowering research, one question at a time.")

# --- Pages ---
if page == "Home":
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
        </style>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown('#')
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
    
    st.markdown("###")
    st.markdown("""<div style="font-size: 18px; color: {font_color};">Upload a PDF</div>""", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type="pdf")
    
    if uploaded_file:
        st.session_state["uploaded_pdf"] = uploaded_file
    
    st.write("")
    
    st.markdown("""
        <style>
        div.stButton > button {
            color: #2C3E50;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True)
    
    if st.button("Go to Chat 💬"):
        if "uploaded_pdf" in st.session_state:
            st.switch_page("Chatbot.py")
        else:
            st.warning("📄 Please upload a PDF before proceeding.")

elif page == "Chatbot":
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
        pdf_file.seek(0)  # 🔥 Reset the pointer to the beginning
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
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
    
    
    # === After defining all your functions ===
    
    if "uploaded_pdf" in st.session_state:
        pdf_file = st.session_state["uploaded_pdf"]
    
        if "vectorstore" not in st.session_state:
            text = extract_text_from_pdf(pdf_file)
            documents = split_text(text)
            st.session_state["vectorstore"] = create_vector_store(documents)
    
        vectorstore = st.session_state["vectorstore"]
    
        if "conversation_chain" not in st.session_state:
            st.session_state["conversation_chain"] = build_conversational_chain(vectorstore)
    
        conversation_chain = st.session_state["conversation_chain"]
    
        # Initialize chat history if needed
        if "messages" not in st.session_state:
            st.session_state.messages = []
    
        # Display previous chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(f"<span style='color:{font_color}'>{message['content']}</span>", unsafe_allow_html=True)
    
        # Handle new user prompt
        if prompt := st.chat_input("Ask me something about your PDF"):
            st.chat_message("user").markdown(f"<span style='color:{font_color}'>{prompt}</span>", unsafe_allow_html=True)
            st.session_state.messages.append({"role": "user", "content": prompt})
    
            # 🔍 Bot response
            response = conversation_chain.invoke({"question": prompt})
            response_text = f"Bot: {response['answer']}"
    
            with st.chat_message("assistant"):
                st.markdown(f"<span style='color:{font_color}'>{response_text}</span>", unsafe_allow_html=True)
    
            st.session_state.messages.append({"role": "assistant", "content": response_text})
    
    else:
        st.warning("Please upload a PDF from the homepage to begin.")

elif page == "Paper Summary":
    st.title("📄 Paper Summary")
    st.write("""
    Once a paper is uploaded, a brief **summary** will be generated here:
    - **Title**
    - **Authors**
    - **Abstract**
    - **Key Points**
    """)
    st.info("Upload a paper in the Chatbot section to see the summary here!")

elif page == "What is RAG?":
    st.title("🧠 What is Retrieval-Augmented Generation (RAG)?")
    st.write("""
    **Retrieval-Augmented Generation (RAG)** is a powerful technique where the model first **retrieves relevant documents** and then **generates answers** based on them.
    
    It combines the best of both worlds:
    - **Retrieval** ensures factual grounding.
    - **Generation** ensures fluent, understandable answers.
    
    This helps the model stay accurate and avoid hallucination — critical when answering about research papers!
    """)
    st.image("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/rag/rag-architecture.png", width=700)
    st.caption("Image source: Hugging Face")

elif page == "FAQ":
    st.title("❓ Frequently Asked Questions")
    st.write("""
    **Q: Can I upload any PDF?**  
    A: Ideally, the PDF should be a research paper with text (not scanned images).
    
    **Q: How is the answer generated?**  
    A: The app uses Retrieval-Augmented Generation (RAG) to fetch content from the uploaded paper and answer based on that.
    
    **Q: Will it hallucinate?**  
    A: Much less than a normal chatbot, because it uses your uploaded paper as the base.
    """)

elif page == "About":
    st.title("👨‍💻 About This Project")
    st.write("""
    Built as a part of a **research assistant project**, this app aims to make research papers easier to explore.
    
    **Technologies Used**:
    - Streamlit
    - OpenAI / Hugging Face models
    - Retrieval-Augmented Generation (RAG)
    
    **Created by**: [Your Name](https://www.linkedin.com/in/yourprofile/)
    """)
