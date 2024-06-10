import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    initial_sidebar_state='expanded',
    layout="wide",
    page_title='How to',
    page_icon='icons/alftech.jpg'
)
with st.sidebar:
    st.sidebar.title('How to use Alf Tech')
    with st.expander("Languages / اللغة"):
        st.session_state.language = st.radio('Choose Language / اختر لغة', options=['English', 'عربي'])



if st.session_state.language == 'English':
    main = "Ask!"
    how = "How to use Alf Tech"
    franco = "2lf تك (Beta) "
    tips = "Tech Tips & Tricks"
    setting_new = "Setting Up New Devices"
    log = "Login / Register"
    hist = "Chat History"

else:
    main = "أسأل"
    how = "ازاي تستخدم الف تك؟"
    franco = "2lf تك (Beta)"
    tips = "نصائح وحيل تقنية"
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

video_url_win = 'videos/desk tes.mp4'
video_url_mob = 'videos/test video2.mp4'
st.title(how)

if st.session_state.language == "English":
    st.markdown("""## How to Use Alf Tech

### If You Want to Ask a Question
1. Open the side bar.
2. Go to the task tab.
3. Click/tap on it.
4. Click on the text box "how can I help".
5. Write the question and press enter.
6. Wait for the response.

### To Use Tech Tips & Tricks
1. Open the side bar.
2. Choose (Tech Tips & Tricks).
3. Click/tap on it.
4. Choose your preferred device:
    - Windows
    - iOS
    - Android
5. Scroll in the Tips (that gets updated weekly).

### How to Use 2lf تك (Beta) "Franco Translator"
1. Open the side bar.
2. Choose (2lf تك (Beta)).
3. Click/tap on it.
4. Click on the text box "What you want to translate".
5. Enter the Franco text that you want to translate.
6. Wait for the translation.

### To Set Up a New Device
1. Open the side bar.
2. Choose (Setting up new devices).
3. Click/tap on it.
4. Choose your preferred device.
5. Follow the shown instructions to set up your new device.

## To Log In / Register

### If You Have an Account
1. Open the side bar.
2. Choose (Log in / Register).
3. Click/tap on it.
4. Enter your email.
5. Enter your password.
6. Click/tap on log in.

### If You Don't Have an Account
1. Open the side bar.
2. Choose (Log in / Register).
3. Click/tap on it.
4. Click/tap on sign up.
5. Enter your email.
6. Set up a password (that you don't forget).
7. Click/tap on sign up.
8. The website will take you back to the log in page.
9. Enter the email and password.
10. Click/tap on log in.

### To Check Chat History (For Logged-In Users Only)
1. Open the side bar.
2. Choose (Chat History).
3. Click/tap on it.
4. If you have saved chats, you will find the date and time of the chat.

### To Change the Website Language
1. Open the side bar.
2. Click/tap on Menu named languages اللغة.
3. Choose your preferred language.
""")
if st.session_state.language == "عربي":
    st.markdown("""### كيفية استخدام تقنية Alf لطرح سؤال

1. افتح الشريط الجانبي
2. انتقل إلى علامة تبويب المهام
3. اضغط/انقر عليها
4. اضغط على مربع النص "كيف يمكنني مساعدتك"
5. اكتب السؤال واضغط على Enter
6. انتظر الرد

### لاستخدام Tech Tips & Tricks

1. افتح الشريط الجانبي
2. اختر (Tech Tips & Tricks)
3. اضغط/انقر عليها
4. اختر جهازك المفضل
   - ويندوز
   - iOS
   - أندرويد
5. تصفح النصائح (التي يتم تحديثها أسبوعياً)

### كيفية استخدام 2lf تك (Beta) "Franco translator"

1. افتح الشريط الجانبي
2. اختر (2lf تك (Beta))
3. اضغط/انقر عليها
4. اضغط على مربع النص "ما الذي تريد ترجمته"
5. أدخل النص الفرنكو الذي تريد ترجمته
6. انتظر الترجمة

### لإعداد جهاز جديد

1. افتح الشريط الجانبي
2. اختر (Setting up new devices)
3. اضغط/انقر عليها
4. اختر جهازك المفضل
5. اتبع التعليمات المعروضة لإعداد جهازك الجديد

### لتسجيل الدخول / التسجيل

1. افتح الشريط الجانبي
2. اختر (Log in / Register)
3. اضغط/انقر عليها
4. إذا كان لديك حساب:
   - أدخل بريدك الإلكتروني
   - أدخل كلمة المرور
   - اضغط/انقر على تسجيل الدخول
5. إذا لم يكن لديك حساب:
   - اضغط/انقر على التسجيل
   - أدخل بريدك الإلكتروني
   - أنشئ كلمة مرور (التي لا تنساها)
   - اضغط/انقر على التسجيل
   - ستعيدك الصفحة إلى صفحة تسجيل الدخول
6. أدخل البريد الإلكتروني وكلمة المرور
7. اضغط/انقر على تسجيل الدخول

### للتحقق من سجل الدردشة (للمستخدمين المسجلين فقط)

1. افتح الشريط الجانبي
2. اختر (Chat History)
3. اضغط/انقر عليها
4. إذا كان لديك دردشة محفوظة، ستجد تاريخ ووقت الدردشة

### لتغيير لغة الموقع

1. افتح الشريط الجانبي
2. اضغط/انقر على القائمة المسماة اللغات
3. اختر لغتك المفضلة""")
