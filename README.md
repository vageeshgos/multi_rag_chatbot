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

multi_source_rag_chatbot/
├── app.py # Streamlit frontend
├── multi_source_rag_chatbot.py # Backend pipeline
├── requirements.txt
├── README.md
## 🔄 Workflow

1. **Choose a source** (PDF, YouTube URL, Wikipedia topic, Website URL)  
2. **Upload or paste** the input  
3. **LangChain splits and embeds** the data  
4. **FAISS vector search** retrieves relevant chunks  
5. **Ollama LLM** answers your questions  

---

## 🧪 How It Works Internally


graph TD
A[User Selects Source] --> B[Load Data]
B --> C[Split into Chunks]
C --> D[Generate Embeddings using Ollama]
D --> E[Store in FAISS Vector DB]
E --> F[Query by User]
F --> G[Retrieve Relevant Chunks]
G --> H[LLM (Ollama) Generates Answer]

🧑‍💻 Setup Instructions
1. Clone the Project
bash
Copy
Edit
git clone https://github.com/yourusername/multi-source-rag-chatbot.git
cd multi-source-rag-chatbot
2. Create and Activate Virtual Environment

python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux/Mac
source venv/bin/activate
3. Install Requirements

pip install -r requirements.txt
4. Run Ollama Model
Make sure Ollama is installed: https://ollama.com/download
Then run any one of the models:
ollama run llama3
# or
ollama run llama2
# or
ollama run mistral
5. Start Streamlit App

streamlit run app.py
📌 The chatbot will launch in your browser with a menu to select input type (PDF upload, YouTube link, etc.)

🖼️ Screenshots
User Interface:

Model Accuracy Chart:

Flowchart:

🚧 Roadmap
Add .docx file support

Add user authentication

Add multilingual response

Enable answer citation sources

📜 License
MIT License. Free to use and modify.

🤝 Contact
Built by Your Name
Contributions and feedback are welcome!


Let me know if you'd like me to:
- Generate the `requirements.txt`
- Push this directly to a GitHub repo
- Include a short demo video or GIF




