# LLM4 PersonalChatbot

## Project
The objective of this project is to interact with the Hugging Face model llama-2-7b-chat.Q2_K.gguf using Langchain within a Colab notebook. A web application user interface was developed for the chatbot using Streamlit. Local tunnel was used to expose the Streamlit app to the internet.

## Reference
Create a Chatbot using Hugging Face and Streamlit, Kavit (zenwraight)

- Modifications were made for deprecated modules:
  - llama_index
  - llama_index.llms.llama_utils
 
## Tools
- Colab
- Python
- langchain
- wget
- llama-index=embeddings-huggingface
- llama-index-llms-llama-cpp
- cohere
- jedi
- Hugging Face model: llama-2-7b-chat.Q2_K.gguf
- streamlit
- localtunnel (exposes Streamlit app to the internet)

## Model
- Model is downloaded to a file using wget in the /content directory on colab

## Tasks
- Installed modules
- Downloaded Hugging Face model
- Code for Streamlit App
    - import streamlit
    - UI Page Configuration
    - Create Conversation Button
    - Define Response
    - Prompt for question
    - Display messages
- Install local tunnel
- Run Streamlit & localtunnel
- Copy External URL IP provided by localtunnel
- Click on URL provided for the app
- Enter ther URL IP and click enter
- Streamlit App is displayed (will take a little time)
- Enter a question and press enter
    - It will take some time to reply


## Streamlit App

<img src="https://github.com/Sarah269/psychic-eureka-AI/blob/main/LLM4_PersonalChatbot/LLM4_0.png" height=300>

## Chatbot Questions

### What is acne?

<img src="https://github.com/Sarah269/psychic-eureka-AI/blob/main/LLM4_PersonalChatbot/LLM4_1.png" height=300>

### How many oceans are there in the world?

<img src="https://github.com/Sarah269/psychic-eureka-AI/blob/main/LLM4_PersonalChatbot/LLM4_2.png" height=300>

### How many countries are there in Europe?

<img src="https://github.com/Sarah269/psychic-eureka-AI/blob/main/LLM4_PersonalChatbot/LLM4_3.png" height=300>



