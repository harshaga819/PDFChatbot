# 📄 PDF Chatbot using LangChain & RAG

![Python](https://img.shields.io/badge/Python-3.x-blue)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-green)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-orange)
![Gemini](https://img.shields.io/badge/LLM-Gemini_2.5_Flash-blueviolet)

A **Retrieval-Augmented Generation (RAG)** based PDF Chatbot that allows users to upload a PDF and ask questions in natural language. Instead of relying on general knowledge, the chatbot retrieves relevant information from the uploaded document and generates responses strictly based on its content.

The project is built using the latest **LangChain ecosystem**, **LCEL (LangChain Expression Language)**, **ChromaDB**, **HuggingFace Embeddings**, **Google Gemini 2.5 Flash**, and **Streamlit**.

---

# ✨ Features

- Upload any PDF document
- Automatic PDF parsing using PyPDFLoader
- Intelligent text chunking with RecursiveCharacterTextSplitter
- Semantic search using HuggingFace Embeddings
- Vector storage using ChromaDB
- Context-aware question answering with Gemini 2.5 Flash
- Answers generated only from the uploaded document
- Built using modern LangChain LCEL architecture
- Interactive Streamlit web application
- Clean, modular and easy-to-understand codebase

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Framework | LangChain |
| Pipeline | LCEL (LangChain Expression Language) |
| Embedding Model | sentence-transformers/all-MiniLM-L6-v2 |
| Vector Database | ChromaDB |
| LLM | Google Gemini 2.5 Flash |
| UI | Streamlit |
| PDF Loader | PyPDFLoader |

---

# 🏗️ Architecture

```text
                    PDF Upload
                         │
                         ▼
                  PyPDFLoader
                         │
                         ▼
      RecursiveCharacterTextSplitter
                         │
                         ▼
         HuggingFace Embeddings
                         │
                         ▼
                  ChromaDB
                         │
                         ▼
            Similarity Retriever
                         │
                         ▼
          Prompt Template (LCEL)
                         │
                         ▼
            Gemini 2.5 Flash LLM
                         │
                         ▼
                Generated Answer
```

---

# ⚙️ Project Workflow

1. **Upload PDF** – The user uploads a PDF document through the Streamlit interface.

2. **Document Loading** – The PDF is loaded using **PyPDFLoader**.

3. **Text Chunking** – The document is split into smaller chunks using **RecursiveCharacterTextSplitter**.

4. **Embedding Generation** – Each chunk is converted into vector embeddings using **sentence-transformers/all-MiniLM-L6-v2**.

5. **Vector Storage** – The embeddings are stored in **ChromaDB**.

6. **User Query** – The user asks a question related to the uploaded document.

7. **Semantic Retrieval** – Relevant chunks are retrieved using similarity search.

8. **Response Generation** – Gemini 2.5 Flash generates an answer strictly from the retrieved context.

---

# 📷 Application Screenshots

## Home Page

Initial interface of the application.

![Home](images/Screenshot%202026-06-30%20234839.png)

---

## Select a PDF

Choose the PDF that you want to chat with.

![Select PDF](images/Screenshot%202026-06-30%20234906.png)

---

## Indexing the PDF

The application processes the document by chunking the text, generating embeddings and storing them in ChromaDB.

![Indexing](images/Screenshot%202026-06-30%20234916.png)

---

## PDF Indexed Successfully

After indexing is complete, the chatbot is ready to answer questions.

![Indexed](images/Screenshot%202026-07-01%20000211.png)

---

## Ask Questions

Ask questions in natural language and receive context-aware answers.

![Question Answer](images/Screenshot%202026-07-01%20000239.png)

---

## Continue the Conversation

Continue asking multiple questions without re-indexing the document.

![Conversation](images/Screenshot%202026-07-01%20000313.png)

---

# 📂 Project Structure

```text
PDFChatbot/
│
├── app.py
├── chat.py
├── config.py
├── pdf_index.py
├── utils.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── uploaded.pdf
│
├── chroma_db/
│
├── images/
│   ├── Screenshot 2026-06-30 234839.png
│   ├── Screenshot 2026-06-30 234906.png
│   ├── Screenshot 2026-06-30 234916.png
│   ├── Screenshot 2026-07-01 000211.png
│   ├── Screenshot 2026-07-01 000239.png
│   └── Screenshot 2026-07-01 000313.png
│
└── PDF_Chatbot.ipynb
```

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/harshaga819/PDFChatbot.git
cd PDFChatbot
```

## Create a Virtual Environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser at:

```
http://localhost:8501
```

---

# 📒 Jupyter Notebook

The repository also includes **PDF_Chatbot.ipynb**, which demonstrates the complete development process of the project before integrating it into the Streamlit application.

The notebook covers:

- PDF loading
- Document chunking
- Embedding generation
- ChromaDB vector creation
- Retriever implementation
- Prompt engineering
- End-to-end RAG pipeline

---

# 🎯 What I Learned

- Retrieval-Augmented Generation (RAG)
- LangChain Expression Language (LCEL)
- Semantic Search
- Vector Databases
- Embedding Models
- Prompt Engineering
- Context-based Question Answering
- Streamlit Application Development
- Building modular AI applications

---

# 🚀 Future Improvements

- Multi-document support
- Conversational memory
- Hybrid Search
- Source citations with page numbers
- Document summarization
- Docker support
- Cloud deployment
- User authentication

---

# 🙌 Acknowledgements

- LangChain
- Google Gemini
- HuggingFace
- ChromaDB
- Streamlit

---

# 👨‍💻 Author

**Harsh Agarwal**

- GitHub: https://github.com/harshaga819
- LinkedIn: https://www.linkedin.com/in/harshaga819

---

## ⭐ Support

If you found this project useful, consider giving it a **Star** on GitHub.