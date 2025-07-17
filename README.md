# 🧠 Multi-Source RAG Chatbot (PDF, Web, Wiki, YouTube) with Streamlit

A powerful, production-ready **Retrieval-Augmented Generation (RAG)** chatbot built using **LangChain**, **Ollama (LLaMA2, LLaMA3, Mistral)**, and **Streamlit**. It allows users to upload PDFs or enter URLs from **websites, YouTube videos, or Wikipedia** to ask natural language questions and get accurate AI-generated answers.

---

## 🚀 Features

- 📄 Upload **PDFs or Word documents**
- 🌐 Load and query from **websites**, **YouTube transcripts**, and **Wikipedia**
- 🧠 Powered by **Ollama + LLaMA / Mistral**
- 🔍 Built-in **vector search** using FAISS
- 🎛️ Streamlit-based user interface
- ✅ Plug-and-play architecture — easy to extend

---

## 📌 Use Cases

1. **Document Intelligence**  
   Upload policy documents, resumes, manuals, etc. and ask questions directly.

2. **Multi-Source AI Research Assistant**  
   Combine knowledge from a website, a video, and a document for a complete AI-powered Q&A.

---

## ⚙️ Tech Stack

| Component     | Tool/Library       |
|---------------|--------------------|
| LLM           | Ollama (LLaMA2, LLaMA3, Mistral) |
| Framework     | LangChain          |
| UI            | Streamlit          |
| Embedding     | OllamaEmbeddings   |
| Vector Store  | FAISS              |
| PDF Parsing   | PyPDFLoader        |
| Web Loader    | WebBaseLoader      |
| Wiki/YouTube  | WikipediaLoader, YoutubeLoader |

---

## 📊 Model Accuracy Comparison (Internal Test Dataset)

| Model   | Accuracy (%) |
|---------|--------------|
| LLaMA 2 | 83%          |
| LLaMA 3 | 89%          |
| Mistral | 85%          |

---

## 📂 Folder Structure

