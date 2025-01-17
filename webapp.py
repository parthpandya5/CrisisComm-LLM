import streamlit as st
from app import *
import firebase_admin
from firebase_admin import credentials, auth, db

# Check if Firebase app is already initialized
if not firebase_admin._apps: cred = credentials.Certificate({ "type": st.secrets["firebase"]["type"], "project_id": st.secrets["firebase"]["project_id"], "private_key_id": st.secrets["firebase"]["private_key_id"], "private_key": st.secrets["firebase"]["private_key"], "client_email": st.secrets["firebase"]["client_email"], "client_id": st.secrets["firebase"]["client_id"], "auth_uri": st.secrets["firebase"]["auth_uri"], "token_uri": st.secrets["firebase"]["token_uri"], "auth_provider_x509_cert_url": st.secrets["firebase"]["auth_provider_x509_cert_url"], "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"], "universe_domain": st.secrets["firebase"]["universe_domain"] }) firebase_admin.initialize_app(cred, { 'databaseURL': 'https://crisiscomm-llm-default-rtdb.firebaseio.com/' })

# Function to register user
def register_user(email, password):
    user = auth.create_user(email=email, password=password)
    return user.uid

# Function to login user
def login_user(email, password):
    user = auth.get_user_by_email(email)
    return user.uid

# Function to save conversation
def save_conversation(user_id, conversation):
    ref = db.reference(f'conversations/{user_id}')
    ref.set({
        'conversation': conversation
    })

# Function to get conversation
def get_conversation(user_id):
    ref = db.reference(f'conversations/{user_id}')
    conversation = ref.get()
    return conversation.get('conversation', []) if conversation else []

# App title
st.title("Ask CrisisComm")

# Initial chatbot message
st.chat_message('chatbot').markdown("Hi! I'm CrisisComm. I'm here to help with you any questions related to FEMA.\n")

# User authentication (simple form for demo purposes)
email = st.text_input("Email")
password = st.text_input("Password", type="password")
if st.button("Register"):
    user_id = register_user(email, password)
    st.success("Registered successfully")
if st.button("Login"):
    user_id = login_user(email, password)
    st.session_state.user_id = user_id
    st.success("Logged in successfully")

if 'user_id' in st.session_state:
    # Initialize messages
    if 'messages' not in st.session_state:
        st.session_state.messages = get_conversation(st.session_state.user_id)

    # Display all the previous messages
    for message in st.session_state.messages:
        st.chat_message(message['role']).markdown(message['content'])

    # Build the prompt platform
    prompt = st.chat_input("Message")

    if prompt:
        # Display the prompt
        st.chat_message('user').markdown(prompt)
        # Store user prompt
        st.session_state.messages.append({'role': 'user', 'content': prompt})
        # Send the prompt to the llm
        response = app(prompt)
        # Show the response
        st.chat_message('chatbot').markdown(response)
        # Store the response
        st.session_state.messages.append(
            {'role': 'chatbot', 'content': response}
        )
        # Save conversation to Firebase
        save_conversation(st.session_state.user_id, st.session_state.messages)
