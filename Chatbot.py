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
   .stTextInput {{
        position: relative;
        transform: translateY(650%);
        width: 100%;
        
       
    }}
    </style>
    """, 
    unsafe_allow_html=True
)

# Chat input field
prompt = st.text_input("", placeholder = "How can I help you!")

if "uploaded_pdf" in st.session_state:
    pdf_file = st.session_state["uploaded_pdf"]
    st.write(f"PDF file '{pdf_file.name}' is accessible in Chatbot page.")
else:
    st.write("No PDF uploaded yet.")


def process_pdf(pdf_file):
    """Extracts text from the uploaded PDF, splits it into chunks, and stores embeddings in FAISS."""
    
    # Extract text from the PDF
    raw_text = ""
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        raw_text += page.extract_text()

    # Split text into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    text_chunks = text_splitter.split_text(raw_text)

    # Generate embeddings and store them in FAISS
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(texts=text_chunks, embedding=embeddings)

    return vector_store

processed_file = process_pdf(pdf_file)
st.write(processed_file)

