import os
import streamlit as st
import boto3
import json
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# --- We will add a print statement here to ensure the script starts ---
print("--- SCRIPT TOP: app.py has started executing. ---")

# --- SECURE SECRET HANDLING FOR RUNTIME ---
def get_google_api_key_from_aws():
    """Fetches the Google API key securely from AWS Secrets Manager."""
    print("--- DEBUG: Entering get_google_api_key_from_aws() ---")
    secret_name = "ev-gpt/google-api-key"
    region_name = os.environ.get("AWS_REGION", "us-east-2")
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        secret = json.loads(get_secret_value_response['SecretString'])
        print("--- DEBUG: Successfully retrieved secret from AWS. ---")
        return secret['GOOGLE_API_KEY']
    except Exception as e:
        print(f"--- ERROR: Failed to retrieve secret: {e} ---")
        st.error(f"Failed to retrieve secret from AWS Secrets Manager: {e}")
        return None

# Fetch the key and set it in the environment for LangChain
api_key = get_google_api_key_from_aws()
if api_key:
    os.environ['GOOGLE_API_KEY'] = api_key
    print("--- DEBUG: GOOGLE_API_KEY environment variable has been set. ---")
else:
    st.error("FATAL: Could not set Google API Key from AWS. App cannot start.")
    st.stop()
# --- END OF SECRET HANDLING ---

prompt_template = """
You are an expert automotive analyst. Your task is to provide a detailed, helpful answer to the user's question based ONLY on the provided context documents.

First, understand the user's question and identify the key criteria needed for a good answer. For example, if they ask about mountain driving, the criteria are long range, good handling, and drivetrain (AWD).

Next, carefully review the following context and extract information related to these criteria for all relevant vehicles.

Finally, synthesize this information into a clear, comparative answer. Do not add any information that is not from the provided context. If the context is insufficient, politely state what information is missing.

CONTEXT:
{context}

QUESTION:
{question}

YOUR EXPERT ANALYSIS:
"""
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

@st.cache_resource
def load_llm_and_retriever():
    """Load the vector database and create the RAG chain."""
    print("--- DEBUG: Entering load_llm_and_retriever() ---")
    db_path = 'db'

    print("--- DEBUG: Step 1 - Initializing embedding function... ---")
    embedding_function = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    print("--- DEBUG: Step 2 - Embedding function initialized. ---")

    print("--- DEBUG: Step 3 - Loading ChromaDB from disk... THIS IS THE LIKELY HANG POINT ---")
    vectordb = Chroma(persist_directory=db_path, embedding_function=embedding_function)
    print("--- DEBUG: Step 4 - ChromaDB loaded successfully. ---")
    
    print("--- DEBUG: Step 5 - Setting up retriever... ---")
    retriever = vectordb.as_retriever(search_kwargs={"k": 7})
    print("--- DEBUG: Step 6 - Setting up LLM... ---")
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.1)
    
    print("--- DEBUG: Step 7 - Creating RAG chain... ---")
    chain_type_kwargs = {"prompt": PROMPT}
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=retriever,
        chain_type_kwargs=chain_type_kwargs, return_source_documents=True
    )
    print("--- DEBUG: Step 8 - RAG chain created. Function complete. ---")
    return qa_chain

# --- UI CODE ---
st.set_page_config(page_title="EV-GPT", page_icon="⚡")
st.header("⚡ EV-GPT: Your EV Features Chatbot")
st.write("Powered by Google Gemini 1.5 Flash")
st.write("Ask me anything about the EV models in my knowledge base!")

print("--- DEBUG: UI elements are about to be drawn. Calling load_llm_and_retriever... ---")
qa_chain = load_llm_and_retriever()
print("--- DEBUG: Caching function finished. Drawing final UI elements. ---")

user_question = st.text_input(
    "Your Question:",
    placeholder="e.g., How does the cargo space of the Ioniq 5 compare to the Model Y?"
)
if user_question:
    with st.spinner("Analyzing with Gemini..."):
        response = qa_chain.invoke({"query": user_question})
        st.success(response['result'])
        with st.expander("View Sources Used"):
            for doc in response['source_documents']:
                st.info(f"**Source Document:** {os.path.basename(doc.metadata.get('source', 'Unknown'))}")
                st.text(f"Content: \"{doc.page_content[:250]}...\"")