# LLM6 Chatbot with Streamlit
# Project Objective
# The purpose of this project is to create a chatbot with a functioning Streamlit
# user interface.

# Reference
# How to Use Ollama with Streamlit, Prerak Patel
# Github Ollama API Error:[WinError 10049] #33: https://github.com/chrishayuk/mcp-cli/issues/33

# Create python virtual environment
# python -m venv myenv

# Activate virtual environment
# myenv\Scripts\activate

# Install modules
# python -m pip install ollama streamlit

# To run Streamlit app.
# streamlit run chatbot.py

# A browser window will open
# Enter your prompt

# When done, close browser. Deactivate virtual environment
# myenv\Scripts\deactivate

# Tools
# Visual Studio Code

# Load Libraries
import streamlit as st
import ollama
from ollama import Client

# Fix for Ollama API Error [WinError 10049]
client = Client(
    host='http://localhost:11434',
    headers={'x-some-header':'some-value'}
)

# Identify model
MODEL = "llama3.2:3b"

# App Title
st.title(MODEL)

# Initialize the messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# for all the messages in session_state 
# display message content
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# response generation from ollama
# client.chat resolves the WinError 10049

def generate_response():
    #response = ollama.chat(model=MODEL, stream=True, messages=st.session_state.messages)
    response = client.chat(model=MODEL, stream=True, messages=st.session_state.messages)
    
    # response will come in chunks. display chunks as received
    # token receives the chunk then add to full_message
    for chunk in response:
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
        stream = generate_response()
        # write the streamed response
        response = st.write_stream(stream)
        # append the assistant response to session_state.messages
        st.session_state["messages"].append({"role": "assistant", "content" : response})