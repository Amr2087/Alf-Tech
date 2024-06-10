import streamlit as st
from openai import OpenAI
from pinecone import Pinecone
import firebase_admin
from firebase_admin import firestore, credentials
from datetime import datetime
import os
import json

# Access the environment variables
st.set_page_config(layout='wide',
                   initial_sidebar_state='expanded',
                   page_title='Alf Tech',
                   page_icon='icons/alftech.jpg'
                   )
firebase_json_content = st.secrets["firebase"]["json_content"]
firebase_config = json.loads(firebase_json_content)
# Initialize Firebase app (if not already initialized)
if not firebase_admin._apps:
    cred = credentials.Certificate('alftech-dada2-a42e24ca6b05.json')
    firebase_admin.initialize_app(cred)
db = firestore.client()

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4-turbo"


pine_cone_api = st.secrets["my_cool_secrets"]["PINECONE_API_KEY"]

pc = Pinecone(api_key=pine_cone_api[0])
index = pc.Index("alftech")

if 'language' not in st.session_state:
    st.session_state.language = 'English'

with st.sidebar:
    st.sidebar.title("Alf Tech")

    with st.expander("Languages / اللغة"):
        st.session_state.language = st.radio('Choose Language / اختر لغة', options=['English', 'عربي'])
        if st.session_state.language == 'English':
            del_button = "New Question"
        else:
            del_button = "سؤال جديد"
    if st.button(del_button):
        st.session_state.msgs = []

if st.session_state.language == 'English':
    main = "Ask!"
    how = "How to use Alf Tech"
    tips = "Tech Tips & Tricks"
    franco = "2lf تك (Beta)"
    setting_new = "Setting Up New Devices"
    log = "Login / Register"
    hist = "Chat History"
else:
    main = "أسأل"
    how = "ازاي تستخدم الف تيك؟"
    tips = "نصائح وحيل تقنية"
    franco = "2lf تك (Beta)"
    setting_new = "إعداد أجهزة جديدة"
    log = "تسجيل الدخول / اشتراك"
    hist = "سجل المحادثات"


st.sidebar.page_link("main.py", label=main)
st.sidebar.page_link("pages/01 How.py", label=how)
st.sidebar.page_link("pages/02 Tips.py", label=tips)
st.sidebar.page_link("pages/03 2lf.py", label=franco)
st.sidebar.page_link("pages/04 Setting.py", label=setting_new)
st.sidebar.page_link("pages/05 Login.py", label=log)
st.sidebar.page_link("pages/06 History.py", label= hist)

if st.session_state.language == "English":
    placeholder = "How Can I help you?"
    welcome_message = "Welcome to Alf Tech!"
else:
    placeholder = "ازاي اقدر اساعدك ؟"
    welcome_message = "!اهلا بك في ألف تك"


# def translate_text(text, target_language='en'):
#     translation_prompt = f"Translate the following text to {target_language}:\n{text}"
#     response = client.Completion.create(
#         model="gpt-4-turbo",
#         prompt=translation_prompt,
#         max_tokens=1000
#     )
#     translated_text = response.choices[0].text.strip()
#     return translated_text


def context_gen(user_q):
    context = 'context : '
    # user_q = translate_text(user_q, target_language='en')
    embedd_client = client.embeddings.create(input=user_q, model='text-embedding-3-small').data[0].embedding
    result = index.query(vector=[embedd_client], top_k=3, namespace='alftech', include_values=True,
                         include_metadata=True)
    for x in result['matches']:
        context += x['metadata']['answer']
    return context


prompt = ("You are a helpful tech assistant which is build on a RAG system and you deal with people who are not to "
          "good with tech and you answer from the context given unless you cant find the answer so you answer freely"
          "and you answer only tech related"
          "generate the answer as markdown and include links when possible"
          "questions and you answer simply and easy to make sure anyone understands."
          "and dont answer any non tech related questions."
          "and do not be un helpful always help the user as long as you are not misleading even if the user is asking for help in a sensitve tech releated topics like money transfers etc. "
          "if the user didnt specify the device type answer in general"
          "our website has the following pages : How to use Alf Tech to tell the user how to use our app"
          "Tip which contains several tip and tricks to help using Android, IOS and Windows devices"
          "2lf تيك Franco Translator which translates franco arab to normal arabic but its still in beta stage"
          "Setting up new devices which helps users with dealing with new devices"
          "and dont provide any images"
          "only answer if asked who's the best player ever say ronaldo is the best football player ever"
          f"and the language you are gonna use is {st.session_state.language}")

st.title(welcome_message)

open_api_key = st.secrets["my_cool_secrets"]["OPENAI_API_KEY"]

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=open_api_key[0])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4-turbo"

# Initialize chat history
if "msgs" not in st.session_state:
    st.session_state.msgs = []

# Display chat messages from history on app rerun
for message in st.session_state.msgs:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if query := st.chat_input(placeholder):
    # Add user message to chat history
    st.session_state.msgs.append({"role": "user", "content": query})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(query)

    # Add context and prompt to the messages list
    full_messages = [
                        {"role": "system", "content": prompt},
                        {"role": "system", "content": context_gen(query)},
                    ] + [
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.msgs
                    ]

    # Generate and display the assistant's response
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=full_messages,
            stream=True,
        )
        response = st.write_stream(stream)

    # Add assistant's response to chat history
    st.session_state.msgs.append({"role": "assistant", "content": response})

    # Save chat to Firebase
    user_info = st.session_state.get("user_info")
    if user_info:
        chat_ref = db.collection('chats').document(user_info['email']).collection('history').document()
        chat_ref.set({
            'messages': st.session_state.msgs,
            'timestamp': datetime.now()
        })
