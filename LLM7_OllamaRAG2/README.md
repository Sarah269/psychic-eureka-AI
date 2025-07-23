# LLM7 Ollama RAG chatbot 2

## Project Objective

The objective of this project is to develop a Retrieval-Augmented Generation (RAG) chatbot using LlamaIndex to assist employees in accessing accurate and timely information about Capital One’s 2025 benefits offerings. The chatbot will leverage a Large Language Model (LLM) enhanced by an external knowledge base, the 2025 Capital One Benefits PDF document, to retrieve and generate relevant answers to employee inquiries.  This version of the chatbot will have a user-friendly interface built using Streamlit.

## Reference
- https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/streaming/
- Build a chatbot with customer data sources, powered by Llamaindex, Caroline Frasca, Krista Muir, and Yi Ding

## Models
- llama3.2:3b
- nomic-embed-text

## Tools
- Visual Studio Code
- Python
- llama-index-llms-ollama
- llama-index
- llama-index-embeddings-ollama
- Streamlit

## Setup Ollama 
- Download Ollama
- Install Ollama
- Powershell
  - Start Ollama 
      - Ollama serve
  - Pull Ollama models
      - ollama pull llama3.2:3b
      - ollama pull nomic-embed-text
  - List Ollama models
      - Ollama list
  - Check to see if model is running
      - Ollama run llam3.2:3b

## Python Virtual Environment
- Visual Studio Code Terminal window
  - Create python virtual environment
      - python -m venv myenv
  - Activate virtual environment
      - myenv\Scripts\activate

## Install required Python modules
- Install modules
   -  python -m pip install -r requirements.txt

 ## Run Chatbot         
- To run Streamlit app
    - streamlit run OllamaRAG2.py

## RAG Chatbot with Streamlit User Interface

<img src="https://github.com/Sarah269/psychic-eureka-AI/blob/main/LLM7_OllamaRAG2/OllamaRAG2_1.png" height=400>

<img src="https://github.com/Sarah269/psychic-eureka-AI/blob/main/LLM7_OllamaRAG2/OllamaRAG2_2.png" height=400>

<img src="https://github.com/Sarah269/psychic-eureka-AI/blob/main/LLM7_OllamaRAG2/OllamaRAG2_3.png" height=400>

<img src="https://github.com/Sarah269/psychic-eureka-AI/blob/main/LLM7_OllamaRAG2/OllamaRAG2_4.png" height=400>

