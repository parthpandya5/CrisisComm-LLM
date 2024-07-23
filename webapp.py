import streamlit as st
from app import*

#app title
st.title("Ask CrisisComm")

st.chat_message('chatbot').markdown("Hi! I'm CrisisComm. I'm here to help with you any questions related to FEMA.\n")

#setup a message variable to hold the old messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

#displays all the previous messages
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

#build the prompt platform
prompt = st.chat_input("Message")

if prompt:
    #display the prompt
    st.chat_message('user').markdown(prompt)
    #stores user prompt
    st.session_state.messages.append({'role':'user', 'content':prompt})
    #send the prompt to the llm
    response = app(prompt)
    #show the response
    st.chat_message('chatbot').markdown(response)
    #store the response
    st.session_state.messages.append(
        {'role':'chatbot', 'content':response})
