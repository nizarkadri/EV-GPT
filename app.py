# app.py
import os
import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# --- API KEY SETUP ---
# The key will be securely injected into the container's environment by AWS ECS
# We'll add a check to ensure it's present.
if "GOOGLE_API_KEY" not in os.environ:
    st.error("Google API Key not found. Please set the GOOGLE_API_KEY environment variable.")
    st.stop()
# os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"] 



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


PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)



# --- RAG SETUP ---
@st.cache_resource
def load_llm_and_retriever():
    """Load the vector database and create the RAG chain."""
    print("Loading vector database and setting up RAG chain with Gemini 1.5 Flash...")
    db_path = 'db'

    embedding_function = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

    vectordb = Chroma(
        persist_directory=db_path,
        embedding_function=embedding_function
    )

    
    retriever = vectordb.as_retriever(search_kwargs={"k": 7})

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.1
    )

    
    
    chain_type_kwargs = {"prompt": PROMPT}
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs=chain_type_kwargs, 
        return_source_documents=True
    )
    

    print("Setup complete.")
    return qa_chain



st.set_page_config(page_title="EV-GPT", page_icon="⚡")
st.header("⚡ EV-GPT: Your EV Features Chatbot")
st.write("Powered by Google Gemini 1.5 Flash")
st.write("Ask me anything about the EV models in my knowledge base!")

try:
    qa_chain = load_llm_and_retriever()

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

except Exception as e:
    st.error(f"An error occurred: {e}")
    st.error("Please ensure your Google API key is set correctly in the script and the 'db' folder exists.")