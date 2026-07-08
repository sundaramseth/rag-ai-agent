import streamlit as st
print("Streamlit version:System  Running", st.__version__)

import os
from loaders.document_loader import DocumentLoader
from rag import RAGPipeline
from vectorstore.faiss_store import VectorStore
from agent import (
    DocumentSearchTool,
    AIAgent
)

# Page Configuration
st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 AI Document Assistant")
st.caption("Upload a document and ask questions using RAG + AI Agent")

# Sidebar
with st.sidebar:
    st.header("📂 Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a PDF, DOCX or TXT file",
        type=["pdf", "docx", "txt"]
    )

    st.divider()

    st.markdown("### Settings")

    top_k = st.slider(
        "Number of Retrieved Chunks",
        min_value=1,
        max_value=10,
        value=3
    )

    temperature = st.slider(
        "Temperature",
        0.0,
        1.0,
        0.2
    )

# Main Section
st.subheader("💬 Ask Your Question")

question = st.text_input(
    "Enter your question",
    placeholder="Example: What is the leave policy?"
)

ask = st.button(
    "Ask AI",
    type="primary",
    use_container_width=True
)

if ask:

    if uploaded_file is None:
        st.warning("Please upload a document first.")

    elif question == "":
        st.warning("Please enter a question.")

    else:

        st.success("Thinking... This may take a few seconds depending on the document size and complexity.")

        upload_dir = "uploads"
        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(upload_dir, uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # load the document using DocumentLoader
        document_loader = DocumentLoader()
        document = document_loader.load_document(file_path)

        # chunk the document using RAGPipeline
        rag_pipeline = RAGPipeline()
        chunks = rag_pipeline.chunk_documents(document)

        vector_store = VectorStore()

        db = vector_store.create_vectorstore(chunks)

        st.success("Vector Store Created Successfully!")

        st.success(f"Pages Loaded : {len(document)}")

        st.success(f"Chunks Created : {len(chunks)}")

        with st.expander("View First Chunk"):
            st.write(chunks[0].page_content)

        with st.expander("View Second Chunk"):
            if len(chunks) > 1:
                st.write(chunks[1].page_content)


        retriever = vector_store.get_retriever(db)

        results = retriever.invoke(question)

        st.subheader("Retrieved Chunks")


        for i, doc in enumerate(results):

            st.markdown(f"### Chunk {i+1}")

            st.write(doc.page_content[:500])

            st.divider()

        # generate answer using RAGPipeline
        tool = DocumentSearchTool(
            retriever
        ).get_tool()

        agent = AIAgent([tool])

        result = agent.ask(question)
        #answer = rag_pipeline.generate_answer(results, question)
        st.subheader("🤖 AI Answer")
        st.write(result["answer"])
