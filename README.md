# EV-GPT

A question-answering system for electric vehicle (EV) information using Google's Generative AI and document retrieval.

## Overview

This project creates a vector database from PDF and TXT documents containing EV information, enabling semantic search and Q&A capabilities through Google's Generative AI.

## Features

- Document processing for PDF and TXT files
- Vector embedding using Google's text-embedding-004 model 
- Document chunking and semantic search
- Persistent vector storage using ChromaDB
- Multi-threaded PDF processing

## Prerequisites

- Python 3.8+
- Google API key for Generative AI services

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/EV-GPT.git
cd EV-GPT
```

2. Create and activate virtual environment
```bash
python -m venv evgpt-venv
source evgpt-venv/bin/activate  # Linux/Mac
evgpt-venv\Scripts\activate     # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Add your Google API key to setup_vector_db.py

Usage
1. Add your EV-related documents (PDF/TXT) to the data directory
2. Run the setup script to create the vector database:

```bash
python setup_vector_db.py
```

3. Start the application:

```bash

python app.py

```
Project Structure:

EV-GPT/
├── data/               # Store your PDF/TXT documents here
│   ├── manuals/       # EV manuals
│   └── reviews/       # EV reviews
├── db/                # Vector database storage
├── evgpt-venv/       # Virtual environment
├── setup_vector_db.py # Database setup script
├── app.py            # Main application
├── requirements.txt   # Project dependencies
└── README.md         # Project documentation

License
MIT License

Contributing
Fork the repository
Create feature branch (git checkout -b feature/AmazingFeature)
Commit changes (git commit -m 'Add AmazingFeature')
Push to branch (git push origin feature/AmazingFeature)
Open a Pull Request
