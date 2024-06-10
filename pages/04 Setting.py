import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    initial_sidebar_state='expanded',
    page_title='Tips & Tricks',
    page_icon='icons/alftech.jpg'
)

if 'language' not in st.session_state:
    st.session_state.language = 'English'

with st.sidebar:
    st.sidebar.title('Tips & Tricks')
    with st.expander("Languages / اللغة"):
        st.session_state.language = st.radio('Choose Language / اختر لغة', options=['English', 'عربي'])


if st.session_state.language == 'English':
    main = "Ask!"
    how = "How to use Alf Tech"
    tips = "Tech Tips & Tricks"
    franco = "2lf تك (Beta)"
    setting_new = "Setting Up New Devices"
    log = "Login / Register"
    page_title = 'Setting Up New Devices'
    hist = "Chat History"
else:
    main = "أسأل"
    how = "ازاي تستخدم الف تيك؟"
    tips = "نصائح وحيل"
    franco = "2lf تك (Beta)"
    setting_new = "إعداد أجهزة جديدة"
    log = "تسجيل الدخول / اشتراك"
    page_title = "إعداد أجهزة جديدة"
    hist = "سجل المحادثات"

if st.session_state.language == 'English':
    options = ['Windows', 'IOS', 'Android']
else:
    options = ["ويندوز", "آي أو إس", "أندرويد"]

st.sidebar.page_link("main.py", label=main)
st.sidebar.page_link("pages/01 How.py", label=how)
st.sidebar.page_link("pages/02 Tips.py", label=tips)
st.sidebar.page_link("pages/03 2lf.py", label=franco)
st.sidebar.page_link("pages/04 Setting.py", label=setting_new)
st.sidebar.page_link("pages/05 Login.py", label=log)
st.sidebar.page_link("pages/06 History.py", label= hist)

st.title(page_title)

selected = option_menu(
    menu_title=None,
    options=['Windows', 'IOS', 'Android'],
    icons=['windows', 'apple', 'android'],
    orientation='horizontal'
)

android_setting_en = ("""# Tips & Tricks for Android Device Optimization

## 1. Use Google Assistant
Activate Google Assistant by saying "Hey Google" or holding the home button. It can help with setting reminders, sending texts, or searching the web.

## 2. Customizable Home Screen
Long-press on your home screen to access widgets and wallpaper settings. Arrange your most-used apps for easy access.

## 3. Quick Settings Menu
Swipe down from the top of the screen to access the Quick Settings menu. You can quickly toggle Wi-Fi, Bluetooth, flashlight, and more.

## 4. Battery Saver Mode
Activate Battery Saver mode from the Quick Settings menu or in Settings > Battery to extend battery life.

## 5. Screen Brightness
Adjust screen brightness manually from the Quick Settings menu to save battery or reduce eye strain.

## 6. Do Not Disturb Mode
Turn on Do Not Disturb mode from the Quick Settings menu or Settings > Sound to silence notifications during meetings or sleep.

## 7. Manage Notifications
Customize app notifications in Settings > Apps & notifications. You can choose which apps can send notifications and how they appear.

## 8. App Drawer
Swipe up from the bottom of the screen to access the App Drawer, where all your apps are listed.

## 9. Use Search Bar
Use the search bar at the top of the App Drawer to quickly find apps or contacts.

## 10. Split Screen Mode
Open two apps simultaneously by using split-screen mode. Open an app, then long-press the recent apps button and select another app.

## 11. Clear App Cache
Speed up your phone by clearing app cache in Settings > Storage > Cached data.

## 12. Secure Your Phone
Set up a PIN, password, or fingerprint for security in Settings > Security.

## 13. Find My Device
Enable Find My Device in Settings > Security to locate your phone if it's lost or stolen.

## 14. Backup Your Data
Use Google Backup in Settings > System > Backup to regularly back up your contacts, photos, and app data.

## 15. Install a Launcher
Customize your phone’s appearance and functionality with a third-party launcher like Nova Launcher from the Google Play Store.

## 16. Use a File Manager
Access your files easily with a file manager app like Google Files, which also helps clean up unnecessary files.

## 17. Voice Typing
Use Google Voice Typing by tapping the microphone icon on the keyboard to dictate text instead of typing.

## 18. Magnification Gestures
Enable magnification gestures in Settings > Accessibility to zoom in on any part of the screen.

## 19. Reduce Data Usage
Enable Data Saver in Settings > Network & Internet to reduce background data usage.

## 20. Google Photos
Use Google Photos for automatic photo backup and easy photo organization.
follow the same sizing as this""")
android_setting_ar = ("""# نصائح وحيل لتحسين أجهزة الأندرويد

## 1. استخدم مساعد Google
قم بتنشيط مساعد Google عبر القول "مرحبًا جوجل" أو الضغط على زر الصفحة الرئيسية. يمكن أن يساعدك في ضبط تذكيراتك، وإرسال الرسائل النصية، أو البحث على الويب.

## 2. الشاشة الرئيسية قابلة للتخصيص
اضغط باستمرار على شاشة الصفحة الرئيسية للوصول إلى الودجت وإعدادات الخلفية. قم بترتيب التطبيقات التي تستخدمها بشكل متكرر لسهولة الوصول.

## 3. قائمة الإعدادات السريعة
اسحب للأسفل من أعلى الشاشة للوصول إلى قائمة الإعدادات السريعة. يمكنك التبديل بسرعة لشبكة الواي فاي، البلوتوث، الفلاش، وغيرها.

## 4. وضع توفير الطاقة
قم بتنشيط وضع توفير الطاقة من قائمة الإعدادات السريعة أو في الإعدادات > البطارية لتمديد عمر البطارية.

## 5. سطوع الشاشة
قم بضبط سطوع الشاشة يدويًا من قائمة الإعدادات السريعة لتوفير البطارية أو للحد من إجهاد العين.

## 6. وضع عدم الإزعاج
قم بتشغيل وضع عدم الإزعاج من قائمة الإعدادات السريعة أو الإعدادات > الصوت لكتم الإشعارات أثناء الاجتماعات أو النوم.

## 7. إدارة الإشعارات
قم بتخصيص إشعارات التطبيقات في الإعدادات > التطبيقات والإشعارات. يمكنك اختيار التطبيقات التي يمكنها إرسال الإشعارات وكيفية ظهورها.

## 8. درج التطبيقات
اسحب لأعلى من أسفل الشاشة للوصول إلى درج التطبيقات، حيث تُدرج جميع تطبيقاتك.

## 9. استخدم شريط البحث
استخدم شريط البحث في أعلى درج التطبيقات للعثور بسرعة على التطبيقات أو جهات الاتصال.

## 10. وضع الشاشة المقسمة
افتح تطبيقين بشكل متزامن باستخدام وضع الشاشة المقسمة. افتح تطبيقًا، ثم اضغط باستمرار على زر التطبيقات الأخيرة وحدد تطبيقًا آخر.

## 11. مسح ذاكرة التخزين المؤقت للتطبيقات
قم بتسريع هاتفك عن طريق مسح ذاكرة التخزين المؤقت للتطبيقات في الإعدادات > التخزين > البيانات المؤقتة.

## 12. أمن هاتفك
قم بتعيين رقم سري، كلمة مرور، أو بصمة للأمان في الإعدادات > الأمان.

## 13. العثور على هاتفك
قم بتمكين العثور على جهازك في الإعدادات > الأمان للعثور على هاتفك إذا كان مفقودًا أو مسروقًا.

## 14. احتياطي البيانات الخاصة بك
استخدم نسخ احتياطي Google في الإعدادات > النظام > النسخ الاحتياطي للنسخ الاحتياطي الدوري لجهات الاتصال، الصور، وبيانات التطبيقات.

## 15. تثبيت مشغل
قم بتخصيص مظهر ووظائف هاتفك باستخدام مشغل طرف ثالث مثل Nova Launcher من متجر Google Play.

## 16. استخدم مدير الملفات
قم بالوصول إلى ملفاتك بسهولة باستخدام تطبيق مدير الملفات مثل Google Files، الذي يساعد أيضًا في تنظيف الملفات غير الضرورية.

## 17. الكتابة الصوتية
استخدم الكتابة الصوتية من Google عن طريق الضغط على أيقونة الميكروفون على لوحة المفاتيح لنطق النص بدلاً من كتابته.

## 18. الإيماءات للتكبير
قم بتمكين إيماءات التكبير في الإعدادات > الإمكانيات > التكبير للتكبير في أي جزء من الشاشة.

## 19. تقليل استخدام البيانات
قم بتمكين وضع توفير البيانات في الإعدادات > الشبكة والإنترنت لتقليل استخدام البيانات الخلفية.

## 20. صور جوجل
استخدم صور جوجل للنسخ الاحتياطي التلقائي للصور وتنظيمها بسهولة.

""")
windows_setting_en = ("""# Tips & Tricks for Windows Optimization

## 1. Keyboard Shortcuts
Learn common keyboard shortcuts like Ctrl+C (copy), Ctrl+V (paste), and Win+D (show desktop).

## 2. Taskbar Customization
Right-click on the taskbar to customize it, including hiding or showing icons, resizing, and more.

## 3. File Explorer Tricks
Use Ctrl + Scroll to zoom in or out in File Explorer for better readability.

## 4. Snap Windows
Drag windows to the edge of the screen to automatically resize and snap them to that side.

## 5. Virtual Desktops
Organize your work by using virtual desktops. Press Win+Tab to access Task View and create multiple desktops.

## 6. Night Light
Reduce eye strain by enabling Night Light in Settings > System > Display.

## 7. Search Everywhere
Use Win+S to quickly search for apps, files, and settings.

## 8. Task Manager
Press Ctrl+Shift+Esc to open Task Manager. It's your go-to tool for monitoring and managing processes.

## 9. Windows Terminal
Upgrade your command-line experience with Windows Terminal, available in the Microsoft Store.

## 10. PowerToys
Install PowerToys to enhance productivity with features like FancyZones for window management.

## 11. Customize Start Menu
Right-click on the Start menu to customize it, including adding or removing tiles and folders.

## 12. Game Mode
Improve gaming performance by enabling Game Mode in Settings > Gaming.

## 13. Dictation
Use Win+H to open the built-in dictation tool for hands-free typing.

## 14. Remote Desktop
Access your PC remotely by enabling Remote Desktop in Settings > System > Remote Desktop.

## 15. Clipboard History
Press Win+V to access Clipboard History and easily paste previously copied items.

## 16. Storage Sense
Free up disk space by enabling Storage Sense in Settings > System > Storage.

## 17. Privacy Settings
Review and customize your privacy settings in Settings > Privacy for better control over your data.

## 18. Focus Assist
Minimize distractions by enabling Focus Assist in Settings > System > Focus Assist.

## 19. Backup and Restore
Set up regular backups using Windows Backup or a third-party solution to protect your data.

## 20. Windows Updates
Stay up-to-date with the latest features and security patches by regularly checking for Windows Updates.
""")
windows_setting_ar = ("""# نصائح وحيل لتحسين نظام ويندوز

## 1. اختصارات لوحة المفاتيح
تعلم اختصارات لوحة المفاتيح الشائعة مثل Ctrl+C (نسخ)، Ctrl+V (لصق)، وWin+D (عرض سطح المكتب).

## 2. تخصيص شريط المهام
انقر بزر الماوس الأيمن على شريط المهام لتخصيصه، بما في ذلك إخفاء أو إظهار الأيقونات، تغيير الحجم، والمزيد.

## 3. حيل مستكشف الملفات
استخدم Ctrl + Scroll للتكبير أو التصغير في مستكشف الملفات لتحسين القراءة.

## 4. تثبيت النوافذ
اسحب النوافذ إلى حافة الشاشة لتغيير حجمها وتثبيتها تلقائيًا إلى ذلك الجانب.

## 5. سطح المكتب الافتراضي
نظم عملك باستخدام أسطح المكتب الافتراضية. اضغط Win+Tab للوصول إلى عرض المهام وإنشاء عدة أسطح مكتب.

## 6. إضاءة الليل
قلل من إجهاد العين عن طريق تمكين إضاءة الليل في الإعدادات > النظام > العرض.

## 7. البحث في كل مكان
استخدم Win+S للبحث بسرعة عن التطبيقات والملفات والإعدادات.

## 8. مدير المهام
اضغط Ctrl+Shift+Esc لفتح مدير المهام. إنه أداتك الأساسية لمراقبة وإدارة العمليات.

## 9. محطة ويندوز
حسن تجربة سطر الأوامر مع محطة ويندوز، المتاحة في متجر مايكروسوفت.

## 10. أدوات PowerToys
قم بتثبيت أدوات PowerToys لتعزيز الإنتاجية مع ميزات مثل FancyZones لإدارة النوافذ.

## 11. تخصيص قائمة البدء
انقر بزر الماوس الأيمن على قائمة البدء لتخصيصها، بما في ذلك إضافة أو إزالة المربعات والمجلدات.

## 12. وضع الألعاب
حسن أداء الألعاب عن طريق تمكين وضع الألعاب في الإعدادات > الألعاب.

## 13. الإملاء
استخدم Win+H لفتح أداة الإملاء المدمجة للكتابة بدون استخدام اليدين.

## 14. سطح المكتب البعيد
الوصول إلى جهاز الكمبيوتر الخاص بك عن بُعد عن طريق تمكين سطح المكتب البعيد في الإعدادات > النظام > سطح المكتب البعيد.

## 15. سجل الحافظة
اضغط Win+V للوصول إلى سجل الحافظة ولصق العناصر المنسوخة سابقًا بسهولة.

## 16. استشعار التخزين
حرر مساحة على القرص عن طريق تمكين استشعار التخزين في الإعدادات > النظام > التخزين.

## 17. إعدادات الخصوصية
راجع وخصص إعدادات الخصوصية الخاصة بك في الإعدادات > الخصوصية للحصول على تحكم أفضل في بياناتك.

## 18. مساعد التركيز
قلل من التشتت عن طريق تمكين مساعد التركيز في الإعدادات > النظام > مساعد التركيز.

## 19. النسخ الاحتياطي والاستعادة
قم بإعداد نسخ احتياطية منتظمة باستخدام النسخ الاحتياطي لنظام ويندوز أو حل تابع لجهة خارجية لحماية بياناتك.

## 20. تحديثات ويندوز
ابقَ على اطلاع بأحدث الميزات والتحديثات الأمنية عن طريق التحقق بانتظام من تحديثات ويندوز.
""")
ios_setting_en = ("""# Tips & Tricks for iOS Optimization

## 1. Siri Shortcuts
Use Siri Shortcuts to automate tasks and streamline your workflow. You can create custom voice commands to perform specific actions.

## 2. Customize Home Screen
Long-press on the home screen to enter jiggle mode. From there, you can rearrange apps, create folders, and add widgets for quick access to information.

## 3. Control Center
Swipe down from the top-right corner of the screen to access Control Center. From here, you can toggle various settings like Wi-Fi, Bluetooth, and screen brightness.

## 4. Low Power Mode
Activate Low Power Mode to conserve battery life when your device's battery is running low. You can enable it from Control Center or in Settings > Battery.

## 5. Display & Brightness
Adjust screen brightness and enable Night Shift mode to reduce eye strain, especially at night. You can customize these settings in Settings > Display & Brightness.

## 6. Do Not Disturb
Turn on Do Not Disturb mode to silence calls, notifications, and alerts. You can schedule it to activate during specific times or manually enable it from Control Center.

## 7. Notifications
Manage app notifications in Settings > Notifications. You can customize how notifications appear, including banners, alerts, or none at all.

## 8. App Library
Swipe right on the home screen to access the App Library, where all your installed apps are automatically organized into categories for easier navigation.

## 9. Spotlight Search
Swipe down from the middle of the home screen to access Spotlight Search. You can quickly search for apps, contacts, messages, and more.

## 10. Split View & Slide Over
On iPad, use Split View to multitask by running two apps side by side, or use Slide Over to quickly access a second app without leaving the first one.

## 11. Clear App Cache
Speed up your device by clearing app cache in Settings > General > iPhone/iPad Storage. You can offload unused apps and delete app data to free up space.

## 12. Face ID/Touch ID
Secure your device with Face ID or Touch ID. You can set up these biometric authentication methods in Settings > Face ID & Passcode or Touch ID & Passcode.

## 13. Find My iPhone/iPad
Enable Find My iPhone/iPad in Settings > [Your Name] > Find My to locate your device if it's lost or stolen. You can also remotely lock or erase your device for added security.

## 14. iCloud Backup
Automatically back up your device to iCloud to ensure your data is safe and easily recoverable. You can enable iCloud Backup in Settings > [Your Name] > iCloud > iCloud Backup.

## 15. Install a Launcher
Customize your device's appearance and functionality with third-party launchers from the App Store. These launchers offer additional customization options beyond the default iOS experience.

## 16. Use Files App
Access and manage your files with the Files app. You can organize documents, photos, and videos stored on your device or in iCloud Drive.

## 17. Siri Dictation
Use Siri Dictation to transcribe your voice into text. You can enable it by tapping the microphone icon on the keyboard and speaking your message.

## 18. Magnifier
Turn your device into a magnifying glass with the Magnifier feature. You can enable it in Settings > Accessibility > Magnifier and triple-click the side button to activate it.

## 19. Reduce Data Usage
Limit background data usage and conserve cellular data by enabling Low Data Mode in Settings > Cellular or by restricting app access to cellular data.

## 20. Apple Photos
Organize and edit your photos with the built-in Apple Photos app. You can create albums, apply filters, and share your memories with friends and family.
""")
ios_setting_ar = ("""# نصائح وحيل لتحسين نظام iOS

## 1. اختصارات Siri
استخدم اختصارات Siri لتتمكن من أتمتة المهام وتسهيل سير عملك. يمكنك إنشاء أوامر صوتية مخصصة لأداء أفعال محددة.

## 2. تخصيص شاشة البداية
اضغط بشكل طويل على شاشة البداية للدخول إلى وضع الاهتزاز. من هناك، يمكنك إعادة ترتيب التطبيقات، وإنشاء مجلدات، وإضافة ويدجتات للوصول السريع إلى المعلومات.

## 3. مركز التحكم
اسحب للأسفل من الزاوية العلوية اليمنى للشاشة للوصول إلى مركز التحكم. من هنا، يمكنك تبديل إعدادات مختلفة مثل الواي فاي، والبلوتوث، وسطوع الشاشة.

## 4. وضع الطاقة المنخفضة
قم بتنشيط وضع الطاقة المنخفضة لتوفير عمر البطارية عندما تكون بطارية جهازك منخفضة. يمكنك تمكينه من مركز التحكم أو في الإعدادات > البطارية.

## 5. العرض والسطوع
ضبط سطوع الشاشة وتمكين وضع التحول الليلي للحد من تعب العين، خاصة في الليل. يمكنك تخصيص هذه الإعدادات في الإعدادات > العرض والسطوع.

## 6. وضع عدم الإزعاج
قم بتشغيل وضع عدم الإزعاج لكتم المكالمات والإشعارات والتنبيهات. يمكنك جدولته للتنشيط خلال أوقات محددة أو تمكينه يدويًا من مركز التحكم.

## 7. الإشعارات
إدارة إشعارات التطبيقات في الإعدادات > الإشعارات. يمكنك تخصيص كيفية ظهور الإشعارات، بما في ذلك الشعارات والتنبيهات، أو عدم ظهورها على الإطلاق.

## 8. مكتبة التطبيقات
اسحب لليمين على شاشة البداية للوصول إلى مكتبة التطبيقات، حيث يتم تنظيم جميع التطبيقات المثبتة تلقائيًا في فئات لسهولة التصفح.

## 9. بحث Spotlight
اسحب للأسفل من منتصف شاشة البداية للوصول إلى بحث Spotlight. يمكنك البحث بسرعة عن التطبيقات وجهات الاتصال والرسائل وأكثر من ذلك.

## 10. شاشة مقسمة وشريحة فوق
على الآيباد، استخدم شاشة مقسمة للقيام بأكثر من مهمة من خلال تشغيل تطبيقين جنبًا إلى جنب، أو استخدم شريحة فوق للوصول السريع إلى تطبيق ثانٍ دون مغادرة التطبيق الأول.

## 11. مسح ذاكرة التخزين المؤقت للتطبيقات
قم بتسريع جهازك عن طريق مسح ذاكرة التخزين المؤقت للتطبيقات في الإعدادات > عام > التخزين على iPhone/iPad. يمكنك تفريغ التطبيقات غير المستخدمة وحذف بيانات التطبيق لتحرير مساحة.

## 12. Face ID/Touch ID
حمي جهازك بـ Face ID أو Touch ID. يمكنك تعيين هذه الطرق للمصادقة البيومترية في الإعدادات > Face ID والرقم السري أو Touch ID والرقم السري.

## 13. البحث عن iPhone/iPad الخاص بي
قم بتمكين البحث عن iPhone/iPad الخاص بي في الإعدادات > [اسمك] > البحث عني للعثور على جهازك في حالة فقده أو سرقته. يمكنك أيضًا قفل الجهاز أو مسحه عن بُعد لزيادة الأمان.

## 14. النسخ الاحتياطي في iCloud
قم بعمل نسخ احتياطي لجهازك تلقائيًا في iCloud لضمان سلامة بياناتك وسهولة استرجاعها. يمكنك تمكين النسخ الاحتياطي في iCloud في الإعدادات > [اسمك] > iCloud > النسخ الاحتياطي في iCloud.

## 15. تثبيت لانشر
قم بتخصيص مظهر ووظائف جهازك باستخدام لانشرات من متجر التطبيقات. تقدم هذه اللانشرات خيارات تخصيص إضافية تتجاوز تجربة iOS الافتراضية.

## 16. استخدام تطبيق الملفات
استخدم تطبيق الملفات للوصول إلى وإدارة ملفاتك. يمكنك تنظيم المستندات والصور ومقاطع الفيديو المخزنة على جهازك أو في iCloud Drive.

## 17. تحرير النصوص بواسطة Siri
استخدم خاصية تحرير النصوص بواسطة Siri لتحويل صوتك إلى نص. يمكنك تمكينها بالضغط على أيقونة الميكروفون على لوحة المفاتيح والتحدث برسالتك.

## 18. المكبر
حوّل جهازك إلى عدسة مكبرة باستخدام ميزة المكبر. يمكنك تمكينها في الإعدادات > التيسير > المكبر والنقر على الزر الجانبي ثلاث مرات لتنشيطها.

## 19. تقليل استخدام البيانات
حدد استخدام البيانات الخلفية وتوفير البيانات الخلوية عن طريق تمكين وضع البيانات المنخفضة في الإعدادات > الخلوي أو عن طريق تقييد وصول التطبيقات إلى البيانات الخلوية.

## 20. تطبيق Apple Photos
نظم وحرّر صورك باستخدام تطبيق Apple Photos المدمج. يمكنك إنشاء البومات وتطبيق الفلاتر ومشاركة ذكرياتك مع الأصدقاء والعائلة.

""")

if selected == 'Android' and st.session_state.language == 'English':
    st.markdown(android_setting_en)
if selected == 'Android' and st.session_state.language == 'عربي':
    st.markdown(android_setting_ar)

if selected == 'IOS' and st.session_state.language == 'English':
    st.markdown(ios_setting_en)
if selected == 'IOS' and st.session_state.language == 'عربي':
    st.markdown(ios_setting_ar)

if selected == 'Windows' and st.session_state.language == 'English':
    st.markdown(windows_setting_en)
if selected == 'Windows' and st.session_state.language == 'عربي':
    st.markdown(windows_setting_ar)
