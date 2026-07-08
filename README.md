# 🤖 AI Document Assistant (RAG + AI Agent)

An intelligent AI-powered Document Assistant built using **Python, LangChain, Google Gemini, FAISS, Hugging Face Embeddings, and Streamlit**.

Upload one or more PDF documents and ask natural language questions. The application retrieves the most relevant document chunks using semantic search and generates accurate answers using Google's Gemini LLM.

---

## 🚀 Live Demo

> Add your deployed Streamlit URL here

```
https://rag-ai-agentgit-chr5m2pdpc3eqcfodnuh5b.streamlit.app/
```

---

# ✨ Features

- 📄 Upload PDF documents
- 🧠 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic Search using FAISS
- 🤖 Google Gemini 2.5 Flash Integration
- 📚 HuggingFace Sentence Transformer Embeddings
- 💬 Conversational Question Answering
- ⚡ AI Agent powered document search
- 🎯 Context-aware responses
- 🌐 Streamlit Web Interface
- ☁️ Deployed on Streamlit Cloud

---

# 🏗️ Architecture

```
                 User Uploads PDF
                        │
                        ▼
              Document Loader
                        │
                        ▼
             Text Chunking
                        │
                        ▼
      HuggingFace Embeddings
                        │
                        ▼
             FAISS Vector Store
                        │
        Similarity Search (Top-K)
                        │
                        ▼
             Retrieved Context
                        │
                        ▼
        Prompt + Google Gemini
                        │
                        ▼
               Final Answer
```

---

# 🛠 Tech Stack

### Backend

- Python
- LangChain
- LangChain Community
- LangChain Google GenAI

### LLM

- Google Gemini 2.5 Flash

### Embeddings

- sentence-transformers/all-MiniLM-L6-v2

### Vector Database

- FAISS

### Frontend

- Streamlit

### Document Processing

- PyPDF
- Docx2txt

---

# 📂 Project Structure

```
rag-ai-agent/
│
├── agent.py
├── app.py
├── config.py
├── llm.py
├── prompts.py
├── rag.py
├── requirements.txt
│
├── loaders/
│   └── document_loader.py
│
├── vectorstore/
│   └── faiss_store.py
│
├── tests/
│   └── test_gemini.py
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/rag-ai-agent.git

cd rag-ai-agent
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

You can generate a Gemini API key from:

https://aistudio.google.com/apikey

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🧪 Example Workflow

1. Upload PDF document(s)

2. Click Process Documents

3. Wait until vector database is created

4. Ask your question

Example

```
Summarize this document.

```

```
What are the key responsibilities?

```

```
Explain Chapter 5.

```

```
What technologies are used?

```

---

# 📸 Screenshots

## Home Page



---

## Upload Documents

> <img width="372" height="425" alt="image" src="https://github.com/user-attachments/assets/3813f628-986e-47ac-9bbd-5712aa5bbc38" />


---

## Chat Interface

> <img width="1912" height="911" alt="image" src="https://github.com/user-attachments/assets/272363f8-6b8d-424a-b849-46dc502a99ec" />


---

# ⚡ How It Works

### Step 1

Upload PDF document(s)

↓

### Step 2

Extract text using PyPDF

↓

### Step 3

Split into semantic chunks

↓

### Step 4

Generate embeddings

↓

### Step 5

Store embeddings inside FAISS

↓

### Step 6

Retrieve relevant chunks

↓

### Step 7

Send retrieved context to Gemini

↓

### Step 8

Return accurate answer

---

# 📦 Dependencies

- LangChain
- Google Gemini
- FAISS
- HuggingFace Embeddings
- Streamlit
- PyPDF
- Sentence Transformers

---

# Future Improvements

- Conversation Memory
- Chat History
- Multi-file Support
- Source Citations
- Streaming Responses
- Authentication
- User Workspace
- Persistent Vector Database
- Docker Support
- REST API
- Hybrid Search
- Re-ranking
- Voice Input
- OCR Support
- Image Question Answering

---

# 👨‍💻 Author

**Sundaram Seth**

Python Developer | AI Engineer | Full Stack Developer

GitHub:
https://github.com/sundaramseth

LinkedIn:
https://linkedin.com/in/sundaramseth

Portfolio:
https://sundaramsethweb.web.app/

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

# 📄 License

This project is licensed under the MIT License.

Feel free to use, modify, and contribute.
