import streamlit as st
from openai import OpenAI

st.set_page_config(layout='wide',
                initial_sidebar_state='expanded',
                page_title='2lf تيك (beta)',
                page_icon='icons/alftech.jpg'
                   )

with st.sidebar:
    st.sidebar.title("2lf تيك")
    with st.expander("Languages / اللغة"):
        st.session_state.language = st.radio('Choose Language / اختر لغة', options=['English', 'عربي'])
        if st.session_state.language == 'English':
            del_button = "New Question"
        else:
            del_button = "سؤال جديد"
    if st.button(del_button):
        st.session_state.franco_msgs = []

if st.session_state.language == 'English':
    how = "How to use Alf Tech"
    tips = "Tech Tips & Tricks"
    franco = "2lf تك (Beta) "
    setting_new = "Setting Up New Devices"
    log = "Login / Register"
    main = "Ask!"
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
st.sidebar.page_link("pages/06 History.py", label=hist)

prompt = ("You are a Langage System you only goal is to translate the user's phrase from franco arabic to arabic"
          "you are only supposed to translate and help making the user understand franco arabic"
          "you are still in beta phase")

if st.session_state.language == "English":
    placeholder = "What you want to translate?"
    welcome_message = "Welcome to 2lf تيك!"
else:
    placeholder = "تحب اترجم اية؟"
    welcome_message = "!اهلا بك في 2lf تيك"

st.title(welcome_message)
open_api_key = st.secrets["my_cool_secrets"]["OPENAI_API_KEY"]

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=open_api_key[0])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4-turbo"

# Initialize chat history
if "franco_msgs" not in st.session_state:
    st.session_state.franco_msgs = []

# Display chat messages from history on app rerun
for message in st.session_state.franco_msgs:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if query := st.chat_input(placeholder):
    # Add user message to chat history
    st.session_state.franco_msgs.append({"role": "user", "content": query})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(query)

    # Add context and prompt to the messages list
    full_messages = [
                        {"role": "system", "content": prompt},
                    ] + [
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.franco_msgs
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
    st.session_state.franco_msgs.append({"role": "assistant", "content": response})
