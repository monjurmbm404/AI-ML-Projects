# 📚 AI/ML Project 02 — PDF RAG Chatbot

An AI-powered chatbot that allows users to upload PDF documents and ask questions. The system retrieves relevant content from the documents and generates accurate answers using a Retrieval-Augmented Generation (RAG) pipeline.

---

## 🚀 Features

- 📄 **PDF Upload Support**
  Upload multiple PDF files and extract their content automatically

- 🔍 **Semantic Search (RAG)**
  Finds the most relevant text chunks using embeddings

- 💬 **Chat Interface**
  Ask natural language questions about your documents

- 🧠 **Context-Aware Answers**
  Answers are generated strictly from uploaded PDF content

- ⚡ **Fast & Interactive UI**
  Built with Streamlit for a smooth chat experience

- 📊 **Context Transparency**
  Option to view retrieved chunks and similarity scores

---

## 🎥 Demo & Explanation Video

Watch the full explanation and live demo of the project:

👉 [https://youtu.be/ixrdDO0114M](https://youtu.be/ixrdDO0114M)

**What the video covers:**

- Project overview
- How RAG works (Embeddings + Retrieval + LLM)
- Live demo (upload → ask → answer)
- Code walkthrough

---

## 🧠 Tech Stack

- **Python**
- **Streamlit**
- **Sentence Transformers** (`all-MiniLM-L6-v2`)
- **NumPy**
- **PyPDF2**
- **Groq API / Gemini API / OpenAI-compatible APIs**
- **Requests**

---

## 🏗️ How It Works

```
User Uploads PDFs
        ↓
   Text Extraction (PyPDF2)
        ↓
   Text Chunking
        ↓
 Embedding Generation (MiniLM)
        ↓
   Vector Store (In-Memory)
        ↓
User Question → Embedding
        ↓
 Cosine Similarity Search
        ↓
 Top-K Relevant Chunks
        ↓
 Prompt Construction
        ↓
   LLM (Groq / Gemini)
        ↓
     Final Answer
```

---

## 📁 Project Structure

```
AI-ML-Projects/
└── AI-ML-Project 02 PDF RAG Chatbot/
  ├── app.py           # Streamlit UI (chat interface)
  ├── rag_logic.py     # Core RAG pipeline (PDF → chunks → embeddings → retrieval)
  ├── requirements.txt
  ├── .env.example
```

---

## ⚙️ Installation Guide

### 1. Clone the repository

```bash
git clone https://github.com/monjurBakthMazumder/AI-ML-Projects.git
cd "AI-ML-Projects/AI-ML-Project 02 PDF RAG Chatbot"
```

---

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

⚠️ Note:

- You can also use:
  - `GEMINI_API_KEY`
  - `GOOGLE_API_KEY`

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧪 Usage

1. Upload one or more PDF files
2. Adjust settings (chunk size, overlap, top-k retrieval)
3. Ask a question in the chat
4. Get:
   - 💬 AI-generated answer
   - 📄 Source-backed explanation
   - 📊 Retrieved context (optional)

---

## 📌 Use Cases

- 📖 Study from PDF books/notes
- 📑 Research paper Q&A
- 🧠 Quick revision from large documents
- 📚 Knowledge extraction from reports

---

## ⚠️ Limitations

- Works only with **text-based PDFs** (no OCR for scanned images)
- In-memory vector store (not persistent)
- Large PDFs may increase processing time
- Requires internet connection for LLM API
- Answer quality depends on retrieved chunks

---

## 🔮 Future Improvements

- Persistent vector database (FAISS / Chroma)
- OCR support for scanned PDFs
- Chat history memory (long-term context)
- Highlight answers inside PDF
- Multi-language support
- Deploy on cloud (Streamlit Cloud / Docker)

---

## 💡 Why This Project?

Many students and professionals struggle to quickly extract information from large PDF documents. This project solves that problem by combining semantic search with LLMs, allowing users to interact with documents conversationally.

---

## 🧾 Sample Interaction

**Question:**

```
What is the main topic of this document?
```

**Answer:**

```
The document primarily discusses...
```

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
