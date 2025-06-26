import os
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader

# This path is where Docker will mount the secret file from the --secret flag
SECRET_PATH = "/run/secrets/google_api_key"

# Securely read the secret from the file and set it as an environment variable
# for the langchain library to use automatically.

# Ensure there are NO streamlit imports or st.secrets calls in this file.
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set.")
os.environ['GOOGLE_API_KEY'] = api_key

# try:
#     with open(SECRET_PATH, 'r') as f:
#         os.environ['GOOGLE_API_KEY'] = f.read().strip()
# except FileNotFoundError:
#     print("Build secret not found. Make sure you're using 'docker build --secret...'")
#     # Check if the key is in the environment for local testing
#     if 'GOOGLE_API_KEY' not in os.environ:
#         print("GOOGLE_API_KEY environment variable not set. Exiting.")
#         exit(1)

# Define paths
DATA_PATH = 'data/'
DB_PATH = 'db'

print("Starting DB build process...")

# Load documents
loader_pdf = DirectoryLoader(DATA_PATH, glob="**/*.pdf", loader_cls=PyPDFLoader, use_multithreading=True)
loader_kwargs = {'encoding': 'utf-8'}
loader_txt = DirectoryLoader(DATA_PATH, glob="**/*.txt", loader_cls=TextLoader, loader_kwargs=loader_kwargs)
all_documents = loader_pdf.load() + loader_txt.load()

print(f"Successfully loaded {len(all_documents)} documents.")

# Split documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=200)
texts = text_splitter.split_documents(all_documents)
print(f"Split the documents into {len(texts)} chunks.")

# Create embeddings and store in ChromaDB
print("Creating embeddings with 'text-embedding-004'...")
embedding_function = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
vectordb = Chroma.from_documents(documents=texts, embedding=embedding_function, persist_directory=DB_PATH)

print("\n--- Setup Complete! Database built successfully. ---")