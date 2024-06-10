import streamlit as st
import firebase_admin
from firebase_admin import firestore, credentials, auth
import hashlib
import json
# Page configuration
st.set_page_config(
    initial_sidebar_state='expanded',
    page_title='Login / Register',
page_icon='icons/alftech.jpg'
)


# Initialize Firebase app (if not already initialized)
if not firebase_admin._apps:
    cred = credentials.Certificate('alftech-dada2-a42e24ca6b05.json')
    firebase_admin.initialize_app(cred)
db = firestore.client()


# Sidebar configuration
with st.sidebar:
    st.sidebar.title('Login / Register')
    with st.expander("Languages / اللغة"):
        st.session_state.language = st.radio('Choose Language / اختر لغة', options=['English', 'عربي'])

# Language handling
if st.session_state.language == 'English':
    main = "Ask!"
    how = "How to use Alf Tech"
    tips = "Tech Tips & Tricks"
    franco = "2lf تك "
    setting_new = "Setting Up New Devices"
    log = "Login / Register"
    hist = "Chat History"
    page_title = "إعداد أجهزة جديدة"
    login_title = "Login"
    signup_title_ = "Sign Up"
    email_title = "Email"
    password_title = "Password"
    error_valid_email = "Please enter a valid email."
    email_exist = "Email already exists. Please choose a different email."
    signup_success = "Sign up successful! You can now log in."
    error_occ = "An error occurred. Please try again."
    have_acc = "Have an account?"
    back_login = "Back to Login"
    login_done = "Login successful!"
    wrong_creds = "Invalid email or password"
    u_not_found = "User not found"
    no_acc = "Don't have an account?"
    welcome = "Welcome to Alf Tech!"
    out = "Logout"
else:
    main = "أسأل"
    tips = "نصائح وحيل تقنية"
    how = "ازاي تستخدم الف تك؟"
    franco = "2lf تك (Beta)"
    setting_new = "إعداد أجهزة جديدة"
    log = "تسجيل الدخول / اشتراك"
    hist = "سجل المحادثات"
    page_title = "إعداد أجهزة جديدة"
    login_title = "تسجيل الدخول"
    signup_title_ = "اشتراك"
    email_title = 'بريد إلكتروني'
    password_title = 'كلمة المرور'
    error_valid_email = "يرجى إدخال البريد الإلكتروني الصحيح."
    email_exist = "البريد الالكتروني موجود بالفعل. الرجاء اختيار بريد إلكتروني مختلف."
    signup_success = "البريد الالكتروني موجود بالفعل. الرجاء اختيار بريد إلكتروني مختلف."
    error_occ = "حدث خطأ. حاول مرة اخرى."
    have_acc = "هل لديك حساب؟"
    back_login = "العودة إلى تسجيل الدخول"
    login_done = "تم تسجيل الدخول بنجاح!"
    wrong_creds = "البريد الإلكتروني أو كلمة السر خاطئة"
    u_not_found = "لم يتم العثور على المستخدم"
    no_acc = "ليس لديك حساب؟"
    welcome = "مرحبا بكم في ألف تك!"
    out = "تسجيل خروج"

# Sidebar navigation
st.sidebar.page_link("main.py", label=main)
st.sidebar.page_link("pages/01 How.py", label=how)
st.sidebar.page_link("pages/02 Tips.py", label=tips)
st.sidebar.page_link("pages/03 2lf.py", label=franco)
st.sidebar.page_link("pages/04 Setting.py", label=setting_new)
st.sidebar.page_link("pages/05 Login.py", label=log)
st.sidebar.page_link("pages/06 History.py", label= hist)


# Hashing function for passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Functions for signup and login
def signup():

    st.title(signup_title_)
    email = st.text_input(email_title)
    password = st.text_input(password_title, type="password")

    if st.button(signup_title_):

        # Check if email is empty
        if not email:
            st.error(error_valid_email)
            return

        try:
            # Check if email already exists
            user_ref = db.collection('users').document(email)
            user_doc = user_ref.get()
            if user_doc.exists:
                st.error(email_exist)
                return
            # Email does not exist, proceed with signup
            hashed_password = hash_password(password)
            user_ref.set({
                'email': email,
                'password': hashed_password
            })
            st.success(signup_success)
            st.session_state.page = 'login'
            st.experimental_rerun()
        except Exception as e:
            st.error(error_occ)
    st.info(have_acc)
    # Button to go back to login page
    if st.button(back_login):
        st.session_state.page = 'login'
        st.experimental_rerun()


def login():
    st.title(login_title)
    email = st.text_input(email_title)
    password = st.text_input(password_title, type="password")

    if st.button(login_title):
        try:
            user_ref = db.collection('users').document(email)
            user_doc = user_ref.get()
            if user_doc.exists:
                user_data = user_doc.to_dict()
                hashed_password = user_data.get('password')
                if hashed_password == hash_password(password):
                    st.success(login_done)
                    # st.write(f"Welcome {email}!")
                    st.session_state.user_info = {
                        "email": email,
                        # You can remove the line below if you don't need to store the name
                        # "name": f"{user_data['first_name']} {user_data['last_name']}"
                    }
                    # Redirect to main page after successful login
                    st.session_state.page = 'main.py'

                else:
                    st.error(wrong_creds)
            else:
                st.error(u_not_found)
        except Exception as e:
            st.error(f"Error: {e}")

    st.info(no_acc)
    if st.button(signup_title_):
        st.session_state.page = 'signup'



def check_login():
    if "user_info" in st.session_state:
        user_info = st.session_state.user_info
        # st.success(f"Welcome back, {user_info['name']}!")
        return True
    return False

# Initialize the page state
if 'page' not in st.session_state:
    st.session_state.page = 'login'

# Check if the user is already logged in
if check_login():
    st.session_state.page = 'Welcome!'

# Render the appropriate page
if st.session_state.page == 'login':
    login()
elif st.session_state.page == 'signup':
    signup()
else:
    st.title(welcome)
    if st.button(out):
        st.session_state.clear()
        st.session_state.page = 'login'
        st.experimental_rerun()
