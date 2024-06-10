import streamlit as st
import firebase_admin
from firebase_admin import firestore
from datetime import datetime
import json
st.set_page_config(layout='wide',
                   initial_sidebar_state='expanded',
                   page_title='Chat History',
                   page_icon='icons/alftech.jpg'
                   )



firebase_json_content = st.secrets["firebase"]["json_content"]
firebase_config = json.loads(firebase_json_content)
# Initialize Firebase app (if not already initialized)
if not firebase_admin._apps:
    cred = credentials.Certificate('alftech-dada2-a42e24ca6b05.json')
    firebase_admin.initialize_app(cred)
db = firestore.client()


with st.sidebar:
    st.sidebar.title('How to use Alf Tech')
    with st.expander("Languages / اللغة"):
        st.session_state.language = st.radio('Choose Language / اختر لغة', options=['English', 'عربي'])


if st.session_state.language == 'English':
    main = "Ask!"
    how = "How to use Alf Tech"
    tips = "Tech Tips & Tricks"
    franco = "2lf تيك "
    setting_new = "Setting Up New Devices"
    log = "Login / Register"
    hist = 'Chat History'
    err_msg = "Please Login to view your chat history."

else:
    main = "أسأل"
    how = "ازاي تستخدم الف تك؟"
    tips = "نصائح وحيل تقنية"
    franco = "2lf تك (Beta)"
    setting_new = "إعداد أجهزة جديدة"
    log = "تسجيل الدخول / اشتراك"
    hist = "سجل المحادثات"
    err_msg = "الرجاء تسجيل الدخول لعرض سجل المحادثات الخاصة بك."

st.sidebar.page_link("main.py", label=main)
st.sidebar.page_link("pages/01 How.py", label=how)
st.sidebar.page_link("pages/02 Tips.py", label=tips)
st.sidebar.page_link("pages/03 2lf.py", label=franco)
st.sidebar.page_link("pages/04 Setting.py", label=setting_new)
st.sidebar.page_link("pages/05 Login.py", label=log)
st.sidebar.page_link("pages/06 History.py", label=hist)


if 'user_info' not in st.session_state:
    st.error(err_msg)
    st.stop()

user_info = st.session_state["user_info"]
user_email = user_info['email']

st.title(hist)

# Fetch chat history from Firebase
history_ref = db.collection('chats').document(user_email).collection('history')
history_docs = history_ref.order_by('timestamp', direction=firestore.Query.DESCENDING).stream()

for doc in history_docs:
    chat_data = doc.to_dict()
    chat_time = chat_data['timestamp'].strftime("%Y-%m-%d %H:%M:%S")

    if st.button(chat_time):
        for message in chat_data['messages']:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
