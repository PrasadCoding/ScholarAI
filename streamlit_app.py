import streamlit as st
import os
import fitz 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import time

# --- Sidebar ---
with st.sidebar:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("Navigation")
    with col2:
        on = st.toggle("🌗")
    
    if on:
        theme_color = "#2C3E50"
        font_color = "#ECF0F1"
    else:
        theme_color = "#ECF0F1"
        font_color = "#2C3E50"
    # st.title("Navigation")
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
    st.title("ScholarAI")
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
    


# elif page == "Chatbot":
#     os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
    
#     st.title("Ask Your Paper")
    
#     # Apply custom CSS for background and font color
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-color: {theme_color};
#             color: {font_color};
#         }}
#         .stMarkdown, .stTextInput, .stChatInput {{
#             color: {font_color} !important;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )
    
    
#     # === Step 1: Extract text from PDF ===
#     def extract_text_from_pdf(pdf_file):
#         pdf_file.seek(0)  # 🔥 Reset the pointer to the beginning
#         doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
#         text = ""
#         for page in doc:
#             text += page.get_text()
#         return text
    
    
    
#     # === Step 2: Split text into chunks ===
#     def split_text(text, chunk_size=500, chunk_overlap=100):
#         splitter = RecursiveCharacterTextSplitter(
#             chunk_size=chunk_size,
#             chunk_overlap=chunk_overlap
#         )
#         return splitter.create_documents([text])
    
#     # === Step 3: Create embeddings and store in FAISS ===
#     def create_vector_store(documents):
#         embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
#         vectorstore = FAISS.from_documents(documents, embeddings)
#         return vectorstore
    
#     def build_conversational_chain(vectorstore):
#         llm = ChatOpenAI(model_name="gpt-3.5-turbo")
#         memory = ConversationBufferMemory(
#             memory_key="chat_history",
#             return_messages=True
#         )
#         conversation = ConversationalRetrievalChain.from_llm(
#             llm=llm,
#             retriever=vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3}),
#             memory=memory
#         )
#         return conversation
    
    
#     # === After defining all your functions ===
    
#     if "uploaded_pdf" in st.session_state:
#         pdf_file = st.session_state["uploaded_pdf"]
    
#         if "vectorstore" not in st.session_state:
#             text = extract_text_from_pdf(pdf_file)
#             documents = split_text(text)
#             st.session_state["vectorstore"] = create_vector_store(documents)
    
#         vectorstore = st.session_state["vectorstore"]
    
#         if "conversation_chain" not in st.session_state:
#             st.session_state["conversation_chain"] = build_conversational_chain(vectorstore)
    
#         conversation_chain = st.session_state["conversation_chain"]
    
#         # Initialize chat history if needed
#         if "messages" not in st.session_state:
#             st.session_state.messages = []
    
#         # Display previous chat messages
#         for message in st.session_state.messages:
#             with st.chat_message(message["role"]):
#                 st.markdown(f"<span style='color:{font_color}'>{message['content']}</span>", unsafe_allow_html=True)
    
#         # Handle new user prompt
#         if prompt := st.chat_input("Ask me something about your PDF"):
#             st.chat_message("user").markdown(f"<span style='color:{font_color}'>{prompt}</span>", unsafe_allow_html=True)
#             st.session_state.messages.append({"role": "user", "content": prompt})
    
#             # 🔍 Bot response
#             response = conversation_chain.invoke({"question": prompt})
#             response_text = f"Bot: {response['answer']}"
    
#             with st.chat_message("assistant"):
#                 st.markdown(f"<span style='color:{font_color}'>{response_text}</span>", unsafe_allow_html=True)
    
#             st.session_state.messages.append({"role": "assistant", "content": response_text})
    
#     else:
#         st.warning("Please upload a PDF from the homepage to begin.")
elif page == "Chatbot":
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
    
    st.title("Ask Your Paper")
    
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
    
    # === File Upload ===
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf", key="pdf_upload")
    
    if uploaded_file:
        # If a new file is uploaded, reset the chat history and conversation chain
        st.session_state["uploaded_pdf"] = uploaded_file
        st.session_state["messages"] = []  # Clear previous chat history
        st.session_state.pop("vectorstore", None)  # Remove previous vectorstore if exists
        st.session_state.pop("conversation_chain", None)  # Remove previous conversation chain if exists
        
        # Extract text and create new vector store and conversation chain
        text = extract_text_from_pdf(uploaded_file)
        documents = split_text(text)
        st.session_state["vectorstore"] = create_vector_store(documents)
        vectorstore = st.session_state["vectorstore"]
        
        st.session_state["conversation_chain"] = build_conversational_chain(vectorstore)
        conversation_chain = st.session_state["conversation_chain"]

        st.session_state["file_uploaded"] = True  # Mark that a file has been uploaded

    if "uploaded_pdf" in st.session_state:
        # Proceed with chat if file is uploaded
        st.title("Chatbot")
        
        vectorstore = st.session_state["vectorstore"]
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
        # Display message if no file uploaded
        if "file_uploaded" not in st.session_state or not st.session_state["file_uploaded"]:
            st.warning("Please upload a PDF to begin.")

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
    
    # Page title and introductory text
    st.title("RAG in Action")
    
    # RAG explanation
    st.markdown("""
    Retrieval-Augmented Generation (RAG) combines information retrieval and natural language generation to provide more accurate and context-aware responses.
    
    ### Here's how it works:

    - **Retrieve**: Find the most relevant parts of your PDF.
    - **Augment**: Combine them with your question for richer context.
    - **Generate**: Create a precise, context-aware answer.
    """)
    
    # Embedding the YouTube animation video
    st.markdown("""
    ### Watch a quick animation to see how RAG works!
    """)
    
    st.video("https://www.youtube.com/watch?v=QL_pnuEM-gE")  # Replace with your video URL

    st.subheader("Process Overview")
        

    # Tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["Upload →", "Chunk →", "Embed →", "Retrieve →", "Augment →", "Generate"]
    )
    
    with tab1:
        st.subheader("Step 1: Upload Document")  # <-- Changed to subheader
        st.write("""
        The document is uploaded in any format (PDF, TXT, etc.), and the text is extracted for further processing.
        
        **Example Document**:
        ```
        The DeepTransformer model is a new architecture proposed for enhancing deep learning tasks such as NLP. 
        It improves on traditional transformer models by using multi-layered attention mechanisms and dynamic token embeddings.
        ```
        """)
    
    with tab2:
        st.subheader("Step 2: Chunking")
        st.write("""
        The document is split into smaller, meaningful chunks.
    
        **Example Chunks**:
        ```
        - Chunk 1: "Introduction to DeepTransformer, a new model for NLP tasks."
        - Chunk 2: "DeepTransformer improves traditional transformer models using multi-layered attention mechanisms."
        - Chunk 3: "Our experiments show that DeepTransformer outperforms state-of-the-art models on NLP tasks."
        ```
        """)
    
    with tab3:
        st.subheader("Step 3: Embedding")
        st.write("""
        Each chunk is transformed into a high-dimensional vector embedding that captures the semantic meaning of the text.
        
        **Example**:
        ```
        Chunk 1 Embedding: [0.12, -0.45, 0.78, 0.56, ...]
        Chunk 2 Embedding: [0.21, -0.33, 0.65, 0.47, ...]
        Chunk 3 Embedding: [0.19, -0.49, 0.74, 0.50, ...]
        ```
        The vectors help compare text based on meaning.
        """)
    
    with tab4:
        st.subheader("Step 4: Retrieval")
        st.write("""
        A user query is compared with the embeddings of the chunks to retrieve the most relevant ones.
        
        **Example Query**: "What method is proposed?"
        
        **Retrieved Chunks**:
        ```
        - Chunk 2: "DeepTransformer improves traditional transformer models using multi-layered attention mechanisms."
        - Chunk 3: "Our experiments show that DeepTransformer outperforms state-of-the-art models on NLP tasks."
        ```
        These chunks are the most relevant to the user's query.
        """)
    
    with tab5:
        st.subheader("Step 5: Augmentation")
        st.write("""
        The retrieved chunks are combined with the user’s query to form a rich context for the language model.
        
        **Augmented Input**:
        ```
        Context:
        "DeepTransformer improves traditional transformer models using multi-layered attention mechanisms."
        
        Question:
        "What method is proposed?"
        ```
        This helps the language model generate a more accurate and context-aware answer.
        """)
    
    with tab6:
        st.subheader("Step 6: Generate Answer")
        st.write("""
        The augmented context and query are sent to a language model, which generates a detailed answer.
        
        **Example Output**:
        ```
        "The paper proposes DeepTransformer, a new transformer-based model designed to improve NLP tasks by using multi-layered attention mechanisms and dynamic token embeddings."
        ```
        The model's response is based on the context and the query.
        """)

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
