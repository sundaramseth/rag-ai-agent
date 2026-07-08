from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

class VectorStore:

    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    def create_vectorstore(self, chunks):
        vector_db = FAISS.from_documents(
            documents=chunks,
            embedding=self.embeddings
        )

        vector_db.save_local(
            folder_path="vectorstore",
            index_name="faiss_index"
        )

        return vector_db
    
    def load_vectorstore(self):

        db = FAISS.load_local(
            folder_path="vectorstore",
            embeddings=self.embeddings,
            allow_dangerous_deserialization=True
        )

        return db
        
    def get_retriever(self, db):

        retriever = db.as_retriever(
            search_type="mmr", #MMR (Max Marginal Relevance) tries to retrieve relevant but diverse chunks.
            search_kwargs={
                "k": 3,
                "fetch_k": 10
            }
        )
        return retriever