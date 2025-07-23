# Ollama RAG Chatbot2

# Project Objective
# Create a retrieval-augmented generation (RAG) chatbot with a functional 
# Streamlit user interface

# Use the 2025 Capital One Beneftis document as a knowledge base for the LLM

# Reference
# https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/streaming/
# Build a chatbot with customer data sources, powered by Llamaindex, Caroline Frasca, Krista Muir, and Yi Ding

# load Ollama
from llama_index.llms.ollama import Ollama

# Load Libraries
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.ollama import OllamaEmbedding
import streamlit as st
from ollama import Client

# Fix for Ollama API Error [WinError 10049]
client = Client(
    host='http://localhost:11434',
    headers={'x-some-header':'some-value'}
)

# Identify LLM
llm = Ollama(
    model="llama3.2:3b",
    request_timeout=300.0,
    # Manually set the context window to limit memory usage
    context_window=8000,
)

# Identify embedding model
embed_model = OllamaEmbedding(model_name="nomic-embed-text")

# Set global settings
Settings.embed_model = embed_model
Settings.llm = llm

# Page configuration
st.set_page_config(
    page_title="2025 Benefits",
    page_icon="💬",
    layout="wide"
    )

# Page Header
st.header("Ask Me About Capital One 2025 Benefits 💬 ")

# Cache for loading data. 
@st.cache_resource(show_spinner=False)
def get_data():
    # Load the Benefits document
    reader = SimpleDirectoryReader(input_files = ["2025_Benefits_Guide_capitalone.pdf"])
    text = reader.load_data()
    print(f"Length of docs: {len(text)}")

    # Split the document into chunks
    text_splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.get_nodes_from_documents(text)

    # Create the Index.
    # The embedding step is automatic when using Llamaindex
    # Llamaindex has a built-in vector store
    index = VectorStoreIndex(docs)

    return index

# Load data, divide into chunks, and index data
index = get_data()

# chat engine
chat_engine = index.as_chat_engine(chat_mode="condense_question",streaming=True)

# Initialize the messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# for all the messages in session_state 
# display message content
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def generate_response(prompt):
    response = chat_engine.stream_chat(prompt)

    # response will come in chunks. display chunks as received
    # token receives the chunk then add to full_message
    for chunk in response.response_gen:
        print(chunk,end= " ")
        token  = chunk["message"]["content"]
        st.session_state["full_message"] += token
        # display token
        yield token


if prompt := st.chat_input("ready for your request"): # placeholder text in input bar
    # if user types a prompt, append to session_state.messages
    st.session_state.messages.append({"role": "user", "content" : prompt})
    # display prompt
    with st.chat_message("user"):
        st.markdown(prompt)
    # define a session_state for the full message. initialize as empty
    st.session_state['full_message'] = ""
    # get assistant response
    with st.chat_message("assistant"):
        stream = chat_engine.stream_chat(prompt)
        response = ""
        # write the streamed response
        
        for token in stream.response_gen:
            response += token
        
        #update the display
        st.text(response)
        
        # append the assistant response to session_state.messages
        st.session_state["messages"].append({"role": "assistant", "content" : response})