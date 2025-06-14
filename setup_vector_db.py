# setup_vector_db.py
import os
from langchain_community.vectorstores import Chroma

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader

os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]# PASTE YOUR GOOGLE API KEY HERE

# Define the path to the data folder and the persistent database directory
DATA_PATH = 'data/'
DB_PATH = 'db'

print("Starting the setup process...")

# 1. Define Loaders for Different File Types
print("Defining document loaders...")
loader_pdf = DirectoryLoader(DATA_PATH, glob="**/*.pdf", loader_cls=PyPDFLoader, use_multithreading=True)
loader_txt = DirectoryLoader(DATA_PATH, glob="**/*.txt", loader_cls=TextLoader)

# 2. Load Documents
print("Loading documents from the data folder...")
documents_pdf = loader_pdf.load()
documents_txt = loader_txt.load()
all_documents = documents_pdf + documents_txt

if not all_documents:
    print("\n--- No documents found in the 'data' folder! ---")
    print("Please add PDF or TXT files to the 'data' directory and run the script again.")
    exit()

print(f"Successfully loaded {len(all_documents)} documents.")

# 3. Split Documents into Manageable Chunks
print("Splitting documents into chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=200)
texts = text_splitter.split_documents(all_documents)
print(f"Split the documents into {len(texts)} chunks.")

# 4. Create Embeddings and Store in ChromaDB
print("Creating embeddings with 'text-embedding-004' and storing them in ChromaDB...")
print("(This may take a minute or two depending on the number of documents...)")

# Use the Google Generative AI embedding model

embedding_function = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

# Create and persist the vector database
vectordb = Chroma.from_documents(
    documents=texts,
    embedding=embedding_function,
    persist_directory=DB_PATH
)

print("\n--- Setup Complete! ---")
print(f"Vector database has been created and saved in the '{DB_PATH}' directory.")
print("You can now run the main application script: app.py")