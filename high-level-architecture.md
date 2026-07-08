                Upload PDF
                     │
                     ▼
            Document Loader
                     │
                     ▼
            Text Splitter (Chunking)
                     │
                     ▼
          Embedding Model
                     │
                     ▼
              FAISS Vector DB
                     │
────────────────────────────────────
                     │
               User Question
                     │
                     ▼
          Embed User Question
                     │
                     ▼
          Similarity Search
             (Top 3 Chunks)
                     │
                     ▼
          Prompt Construction
                     │
                     ▼
                  Gemini LLM
                     │
                     ▼
             Final Grounded Answer




#embedding
User Question

↓

Embedding

↓

FAISS

↓

Top 3 Similar Chunks

↓

Gemini