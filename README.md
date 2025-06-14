# ⚡ EV-GPT

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Google AI](https://img.shields.io/badge/Google%20AI-Gemini%201.5-orange)](https://ai.google.dev/)

> 🚗 Your intelligent assistant for Electric Vehicle information, powered by Google's Generative AI and advanced document retrieval.

## 🌟 Overview

EV-GPT is a sophisticated question-answering system that leverages Google's Generative AI to provide detailed insights about electric vehicles. By creating a vector database from PDF and TXT documents, it enables powerful semantic search and Q&A capabilities. The system features a modern Streamlit web interface that delivers context-aware responses about electric vehicles based on comprehensive documentation.

## ✨ Features

- 📄 **Smart Document Processing**
  - Multi-threaded PDF and TXT file handling
  - Efficient document chunking with configurable parameters
  - Automatic metadata extraction

- 🤖 **Advanced AI Integration**
  - Powered by Google's Gemini 1.5 Flash model
  - Vector embedding using text-embedding-004
  - Expert automotive analysis with context-aware responses

- 🔍 **Intelligent Search**
  - Persistent vector storage with ChromaDB
  - Source document tracking and display
  - Semantic search capabilities

- 💻 **User-Friendly Interface**
  - Modern Streamlit web interface
  - Real-time response generation
  - Source document visualization

## 🛠️ Prerequisites

- Python 3.8 or higher
- Google API key for Generative AI services (Gemini and Embeddings)
- Sufficient disk space for document storage and vector database

## 📥 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/EV-GPT.git
cd EV-GPT
```

2. **Create and activate virtual environment**
```bash
# For Linux/Mac
python -m venv evgpt-venv
source evgpt-venv/bin/activate

# For Windows
python -m venv evgpt-venv
evgpt-venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure API Key**
Add your Google API key to both `setup_vector_db.py` and `app.py`:
```python
os.environ["GOOGLE_API_KEY"] = "your-api-key-here"
```

## 🚀 Usage

1. **Prepare Documents**
   - Add EV-related documents (PDF/TXT) to the `data` directory
   - Organize in subdirectories (e.g., `manuals/`, `reviews/`)

2. **Create Vector Database**
```bash
python setup_vector_db.py
```

3. **Launch Application**
```bash
python app.py
```

4. **Access Web Interface**
   - Open browser at `http://localhost:8501`
   - Enter your EV-related questions
   - View AI responses with source documents

## 📁 Project Structure

```
EV-GPT/
├── 📂 data/               # Document storage
│   ├── 📂 manuals/       # EV manuals
│   └── 📂 reviews/       # EV reviews
├── 📂 db/                # Vector database
├── 📂 evgpt-venv/       # Virtual environment
├── 📄 setup_vector_db.py # Database setup
├── 📄 app.py            # Streamlit application
├── 📄 requirements.txt   # Dependencies
└── 📄 README.md         # Documentation
```

## 🔧 Technical Details

- **Framework**: LangChain for RAG implementation
- **Document Processing**: RecursiveCharacterTextSplitter
- **Vector Storage**: ChromaDB
- **AI Model**: Google Gemini 1.5 Flash
- **Web Interface**: Streamlit
- **Performance**: Multi-threaded processing

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💬 Support

Need help? Here's how to reach us:

- 📧 Create an issue in the GitHub repository
- 💡 Check existing issues for similar problems
- 📚 Review the documentation for common solutions

---

<div align="center">
Made with ❤️ by Nizar
</div>
