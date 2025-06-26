# ⚡ EV-GPT 🚗

### *Your AI-Powered Electric Vehicle Expert*

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Google AI](https://img.shields.io/badge/Google%20AI-Gemini%201.5-orange?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)

---

> 🎯 **Transform your EV research with AI-powered insights!**  
> 🧠 Powered by Google's cutting-edge Gemini 1.5 Flash model  
> 🔍 Advanced document retrieval with semantic search  
> ⚡ Lightning-fast responses with context-aware analysis

---

## 🎨 What Makes EV-GPT Special?

| 🚀 **Speed** | 🧠 **Intelligence** | 🎯 **Accuracy** | 🔒 **Security** |
|:-------------:|:------------------:|:----------------:|:---------------:|
| ⚡ Sub-second responses | 🤖 State-of-the-art AI | 📊 Data-driven insights | 🔐 AWS-secured secrets |
| 🚗 Real-time processing | 🧩 Context-aware analysis | 📈 Expert automotive knowledge | 🛡️ Production-ready |

---

## ✨ Core Features

### 🤖 **AI-Powered Intelligence**

| Feature | Description | 🎯 Benefit |
|---------|-------------|------------|
| **🧠 Google Gemini 1.5 Flash** | Latest language model | Expert-level automotive analysis |
| **🔤 Text Embedding 004** | High-quality vectors | Precise semantic understanding |
| **🎯 Context-Aware Responses** | Smart document retrieval | Accurate, relevant answers |
| **🚗 EV-Specialized Knowledge** | Automotive expertise | Industry-specific insights |

### 📄 **Smart Document Processing**
- 🎯 **Multi-format Magic** - PDF & TXT files handled seamlessly
- ⚡ **Lightning Processing** - Multi-threaded for speed
- 🧩 **Intelligent Chunking** - Context-preserving text splitting
- 📊 **Metadata Extraction** - Automatic source tracking

### 🔍 **Advanced Search & Retrieval**
- 🗄️ **Vector Database** - ChromaDB for lightning-fast search
- 🧠 **RAG Architecture** - Retrieval-Augmented Generation
- 📚 **Source Attribution** - Transparent reference display
- 🎯 **Semantic Understanding** - Beyond keyword matching

### 💻 **Beautiful Web Interface**
- 🎨 **Modern Streamlit UI** - Clean, responsive design
- ⚡ **Real-time Magic** - Instant response generation
- 📖 **Source Visualization** - Clear reference materials
- 🎯 **User-Friendly** - Intuitive question-answering

### ☁️ **Enterprise-Grade Infrastructure**
- 🔐 **AWS Integration** - Secure secret management
- 🐳 **Docker Ready** - Containerized deployment
- 🛡️ **Production Strong** - Robust error handling
- 🔒 **Security First** - Environment isolation

---

## 🛠️ Technology Stack

| 🧠 **AI & ML** | 🗄️ **Database** | 🌐 **Web Framework** | ☁️ **Cloud** |
|:---------------:|:----------------:|:-------------------:|:-------------:|
| ![Google Gemini](https://img.shields.io/badge/Google%20Gemini-1.5%20Flash-orange?style=flat&logo=google) | ![ChromaDB](https://img.shields.io/badge/ChromaDB-vector%20db-blue?style=flat) | ![Streamlit](https://img.shields.io/badge/Streamlit-web%20app-red?style=flat&logo=streamlit) | ![AWS](https://img.shields.io/badge/AWS-Secrets%20Manager-orange?style=flat&logo=amazonaws) |
| ![LangChain](https://img.shields.io/badge/LangChain-RAG%20framework-yellow?style=flat) | ![SQLite](https://img.shields.io/badge/SQLite-persistence-green?style=flat&logo=sqlite) | ![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=flat&logo=python) | ![Docker](https://img.shields.io/badge/Docker-containerization-blue?style=flat&logo=docker) |

---

## 🚀 Quick Start Guide

### 📋 Prerequisites
- 🐍 Python 3.11+ 
- 🔑 Google API key
- ☁️ AWS account (optional)
- 🐳 Docker (optional)

### 🏠 Local Development

```bash
# 🎯 Clone & Setup
git clone https://github.com/yourusername/EV-GPT.git
cd EV-GPT

# 🐍 Create Virtual Environment
python -m venv evgpt-venv
source evgpt-venv/bin/activate  # Linux/Mac
# evgpt-venv\Scripts\activate   # Windows

# 📦 Install Dependencies
pip install -r requirements.txt

# 🔑 Set API Key
export GOOGLE_API_KEY="your-api-key-here"

# 📁 Prepare Documents
mkdir -p data/manuals data/reviews
# Add your PDF and TXT files here! 📄

# 🗄️ Build Vector Database
python setup_vector_db.py

# 🚀 Launch Application
streamlit run app.py
```

**🎉 Open your browser at `http://localhost:8501`**

### 🐳 Docker Deployment

```bash
# 🏗️ Build Image
docker build -t ev-gpt .

# 🚀 Run Container
docker run -p 8501:8501 -e GOOGLE_API_KEY="your-api-key" ev-gpt
```

### ☁️ AWS Production

```bash
# 🔐 Store Secret
aws secretsmanager create-secret \
    --name "ev-gpt/google-api-key" \
    --secret-string '{"GOOGLE_API_KEY":"your-api-key"}' \
    --region us-east-2

# 🚀 Deploy with proper IAM roles
```

---

## 📁 Project Structure

```
EV-GPT/
├── 🗂️ data/                    # 📄 Document storage
│   ├── 📚 manuals/            # 🚗 EV manuals & specs
│   └── 📖 reviews/            # ⭐ EV reviews & comparisons
├── 🗄️ db/                     # 🧠 Vector database (ChromaDB)
│   ├── 📊 chroma.sqlite3     # 💾 Database file
│   └── 🔗 [uuid]/            # 🧩 Vector embeddings
├── ⚙️ .github/               # 🔧 GitHub workflows
├── 🎨 .streamlit/            # 🎯 Streamlit config
├── 🐍 evgpt-venv/           # 🏠 Virtual environment
├── 🚀 app.py                # ⚡ Main application
├── 🗄️ setup_vector_db.py    # 🏗️ Database setup
├── 📦 requirements.txt      # 📋 Dependencies
├── 🐳 dockerfile           # 🐳 Docker config
├── ☁️ task-definition.json # 🚀 AWS ECS config
├── 🚫 .gitignore          # 🚫 Git ignore
├── 🚫 .dockerignore       # 🚫 Docker ignore
└── 📖 README.md           # 📚 This file!
```

---

## ⚙️ Configuration

### 🔧 Environment Variables

| Variable | Description | Required | Default |
|:---------:|:------------|:--------:|:--------:|
| `🔑 GOOGLE_API_KEY` | Google AI API key | ✅ Yes | - |
| `🌍 AWS_REGION` | AWS region for secrets | ❌ No | `us-east-2` |

### 🎛️ Application Settings

- **📏 Chunk Size**: 1200 characters
- **🔄 Chunk Overlap**: 200 characters  
- **📚 Retrieval Count**: 7 documents per query
- **🌡️ Model Temperature**: 0.1 for consistency

---

## 🎯 Perfect For...

### 🚗 **EV Enthusiasts**
- 🔍 Compare different electric vehicle models
- 📊 Get detailed specifications and features  
- 🔋 Understand EV technology and capabilities
- ⚡ Research charging and range information

### 🏢 **Automotive Professionals**
- 📚 Access comprehensive EV documentation
- 📈 Generate detailed vehicle comparisons
- 🔬 Analyze technical specifications
- 📊 Research market trends and features

### 👨‍💻 **Developers**
- 🧠 Learn RAG implementation
- 🗄️ Study vector database integration
- 🤖 Understand AI document processing
- 🏗️ Explore modern web architecture

---

## 🔍 Try These Questions!

> 💡 **Ask EV-GPT anything about electric vehicles!**

- 🚗 *"How does the cargo space of the Ioniq 5 compare to the Model Y?"*
- 🔋 *"What are the charging capabilities of the latest Tesla models?"*
- 🛣️ *"Which EVs have the best range for long-distance travel?"*
- 🛡️ *"Compare the safety features of different electric SUVs"*
- 🔧 *"What are the maintenance requirements for electric vehicles?"*

---

## ⚡ Performance & Scalability

### 🚀 Current Capabilities
- **📄 Document Processing**: Handles thousands of pages efficiently
- **⚡ Response Time**: Sub-second retrieval with context-aware responses
- **👥 Concurrent Users**: Streamlit supports multiple simultaneous users
- **💾 Memory Usage**: Optimized for production deployment

### 📈 Scalability Features
- **🗄️ Vector Database**: ChromaDB scales with document volume
- **🐳 Docker Containerization**: Easy horizontal scaling
- **☁️ AWS Integration**: Cloud-native deployment options
- **🧩 Modular Architecture**: Easy to extend and customize

---

## 🤝 Contributing

> 🌟 **We love contributions! Join our community!**

### 🛠️ Development Setup
1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. ✅ Make your changes with proper testing
4. 💾 Commit with descriptive messages (`git commit -m 'Add AmazingFeature'`)
5. 🚀 Push to your branch (`git push origin feature/AmazingFeature`)
6. 🔄 Open a Pull Request

### 📋 Contribution Guidelines
- 🐍 Follow PEP 8 style guidelines
- 🧪 Add tests for new features
- 📚 Update documentation for API changes
- ✅ Ensure all tests pass before submitting

### 🎯 Areas for Contribution
- **🎨 UI/UX Improvements**: Enhance the Streamlit interface
- **📖 Documentation**: Expand guides and examples
- **⚡ Performance**: Optimize vector search and response generation
- **🚀 Features**: Add new AI capabilities or data sources

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🆘 Support & Community

### 🆘 Getting Help
- 📧 **GitHub Issues**: Report bugs and request features
- 💬 **Discussions**: Join community conversations
- 📚 **Documentation**: Check existing guides and examples
- 🔍 **Search**: Look through existing issues for solutions

### 🤝 Community Guidelines
- 🙏 Be respectful and inclusive
- 📝 Provide detailed information when reporting issues
- 🤗 Help others by answering questions
- 💡 Share your use cases and improvements

---

## 🏆 Acknowledgments

| 🏢 **Company** | 🎯 **Contribution** |
|:---------------:|:-------------------:|
| **🤖 Google AI** | Gemini models and embeddings |
| **🔗 LangChain** | Excellent RAG framework |
| **⚡ Streamlit** | Intuitive web framework |
| **🗄️ ChromaDB** | Vector database solution |
| **🌍 Open Source** | Supporting libraries |

---

## 📊 Project Status

| Feature | Status | Description |
|:--------:|:------:|:------------|
| 🚀 **Core Features** | ✅ Complete | Production-ready |
| 📄 **Document Processing** | ✅ Complete | Multi-format support |
| 🤖 **AI Integration** | ✅ Complete | Gemini 1.5 Flash |
| 🎨 **Web Interface** | ✅ Complete | Streamlit dashboard |
| 🗄️ **Vector Database** | ✅ Complete | ChromaDB persistence |
| ☁️ **AWS Integration** | ✅ Complete | Secrets management |
| 🐳 **Docker Support** | ✅ Complete | Containerization |
| 🔄 **Continuous Improvement** | 🔄 Ongoing | Enhancements |

---

## 🌟 Made with ❤️ by Nizar

[![GitHub Stars](https://img.shields.io/github/stars/yourusername/EV-GPT?style=social&label=Stars)](https://github.com/yourusername/EV-GPT/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/yourusername/EV-GPT?style=social&label=Forks)](https://github.com/yourusername/EV-GPT/forks)
[![GitHub Issues](https://img.shields.io/github/issues/yourusername/EV-GPT?style=flat&label=Issues)](https://github.com/yourusername/EV-GPT/issues)

---

> 🚀 **Ready to revolutionize your EV research? Start exploring with EV-GPT today!**
