from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)

import os

class DocumentLoader:
    def load_document(self, file_path):
        
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == ".pdf":
            loader = PyPDFLoader(file_path)
        elif file_extension == ".txt":
            loader = TextLoader(file_path, encoding="utf-8")
        elif file_extension == ".docx":
            loader = Docx2txtLoader(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")

        document = loader.load()

        return document