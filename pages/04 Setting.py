import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    initial_sidebar_state='expanded',
    page_title='Setting Up New Devices',
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

android_setting_en = ("""# Setting Up a New Android Device

## 1. Power On and Initial Setup
1. **Power On**: Press and hold the power button to turn on the device.
2. **Select Language**: Choose your preferred language.
3. **Connect to Wi-Fi**: Select a Wi-Fi network and enter the password to connect.

## 2. Account Setup
1. **Google Account**: Sign in with your Google account. If you don't have one, you can create a new account.
2. **Backup and Restore**: Choose to restore your apps and data from a previous backup if available.

## 3. Set Up Security Options
1. **Screen Lock**: Set up a screen lock method (PIN, pattern, or password).
2. **Biometric Authentication**: If supported, set up fingerprint or face recognition.

## 4. Google Services
1. **Google Assistant**: Follow the prompts to set up Google Assistant.
2. **Location Services**: Enable or disable location services according to your preference.

## 5. Install Essential Apps
1. **Google Play Store**: Open the Play Store and sign in if required.
2. **Download Apps**: Download and install essential apps such as browsers, social media, communication, and productivity tools.

## 6. Customize Your Device
1. **Home Screen**: Arrange your home screen, add widgets, and set a wallpaper.
2. **Notification Settings**: Customize notification settings for apps.

## 7. Set Up Backup
1. **Google Backup**: Ensure that Google Backup is enabled to back up your data regularly.
2. **External Backup**: Consider using additional backup options like cloud storage or external drives.

## 8. Explore Features and Settings
1. **System Updates**: Check for and install any available system updates.
2. **Device Settings**: Explore other settings such as display, sound, and accessibility options.

## Conclusion
By following these steps, your new Android device should be set up, secure, and personalized to your needs. If you encounter any issues, refer to the device’s manual or search online for solutions. Enjoy your new device!
""")
android_setting_ar = ("""# إعداد جهاز أندرويد جديد

## 1. التشغيل والإعداد الأولي
1. **تشغيل الجهاز**: اضغط مع الاستمرار على زر الطاقة لتشغيل الجهاز.
2. **اختيار اللغة**: اختر اللغة المفضلة.
3. **الاتصال بشبكة Wi-Fi**: اختر شبكة Wi-Fi وأدخل كلمة المرور للاتصال.

## 2. إعداد الحساب
1. **حساب جوجل**: سجل الدخول باستخدام حساب جوجل الخاص بك. إذا لم يكن لديك حساب، يمكنك إنشاء حساب جديد.
2. **النسخ الاحتياطي والاستعادة**: اختر استعادة التطبيقات والبيانات من نسخة احتياطية سابقة إذا كانت متوفرة.

## 3. إعداد خيارات الأمان
1. **قفل الشاشة**: قم بإعداد طريقة قفل الشاشة (رقم سري، نمط، أو كلمة مرور).
2. **المصادقة البيومترية**: إذا كان مدعومًا، قم بإعداد بصمة الإصبع أو التعرف على الوجه.

## 4. خدمات جوجل
1. **مساعد جوجل**: اتبع الإرشادات لإعداد مساعد جوجل.
2. **خدمات الموقع**: قم بتمكين أو تعطيل خدمات الموقع وفقًا لتفضيلاتك.

## 5. تثبيت التطبيقات الأساسية
1. **متجر جوجل بلاي**: افتح متجر بلاي وسجل الدخول إذا لزم الأمر.
2. **تحميل التطبيقات**: قم بتحميل وتثبيت التطبيقات الأساسية مثل المتصفحات، وسائل التواصل الاجتماعي، تطبيقات الاتصال، وأدوات الإنتاجية.

## 6. تخصيص جهازك
1. **الشاشة الرئيسية**: قم بترتيب الشاشة الرئيسية، إضافة الأدوات، وتعيين خلفية.
2. **إعدادات الإشعارات**: تخصيص إعدادات الإشعارات للتطبيقات.

## 7. إعداد النسخ الاحتياطي
1. **نسخ جوجل الاحتياطي**: تأكد من تفعيل نسخ جوجل الاحتياطي لنسخ بياناتك بانتظام.
2. **النسخ الاحتياطي الخارجي**: استخدم خيارات النسخ الاحتياطي الإضافية مثل التخزين السحابي أو الأقراص الخارجية.

## 8. استكشاف الميزات والإعدادات
1. **تحديثات النظام**: تحقق من وجود تحديثات للنظام وقم بتثبيتها إذا كانت متوفرة.
2. **إعدادات الجهاز**: استكشاف إعدادات أخرى مثل العرض، الصوت، وخيارات الوصول.

## الخاتمة
باتباع هذه الخطوات، يجب أن يكون جهاز الأندرويد الجديد مجهزًا، آمنًا، ومخصصًا لاحتياجاتك. إذا واجهت أي مشكلات، يمكنك الرجوع إلى دليل الجهاز أو البحث عبر الإنترنت عن الحلول. استمتع بجهازك الجديد!
""")
windows_setting_en = ("""# Setting Up a New Windows Device

## 1. Initial Setup and Configuration
1. **Power On**: Turn on the device and follow the on-screen instructions.
2. **Select Region and Language**: Choose the appropriate region and language settings.
3. **Network Connection**: Connect to Wi-Fi or a wired network to ensure internet access for updates and account setup.
4. **Account Setup**:
    - **Microsoft Account**: Sign in with a Microsoft account for access to cloud services, apps, and more.
    - **Local Account**: Alternatively, set up a local account if preferred.

## 2. Update Windows
1. **Check for Updates**: Go to **Settings > Update & Security > Windows Update** and click on **Check for updates**. Install all available updates to ensure the system is secure and up-to-date.

## 3. Install Essential Software
1. **Web Browser**: Install preferred browsers like Google Chrome, Firefox, or Microsoft Edge.
2. **Security Software**: Ensure Windows Defender is active or install another antivirus program if preferred.
3. **Productivity Tools**: Install necessary productivity tools such as Microsoft Office, Adobe Reader, etc.
4. **Communication Apps**: Install apps like Zoom, Skype, or Teams for video calls and communication.

## 4. Personalization
1. **Background and Theme**: Customize the desktop background, theme, and colors. This can be done via **Settings > Personalization**.
2. **Taskbar and Start Menu**: Pin frequently used apps to the taskbar and organize the Start menu.

## 5. Set Up Backup
1. **OneDrive**: Set up OneDrive to automatically back up important files to the cloud.
2. **External Backup**: Use an external hard drive for additional backups via **Settings > Update & Security > Backup**.

## 6. Configure Privacy Settings
1. **Privacy Options**: Go to **Settings > Privacy** and adjust privacy settings according to preference, including location services, microphone, camera access, etc.

## 7. Device Security
1. **Password or PIN**: Set up a strong password or PIN for logging in.
2. **Windows Hello**: If supported, configure Windows Hello for fingerprint or facial recognition login.
3. **BitLocker**: Enable BitLocker for additional security if the device supports it.

## 8. Install Additional Drivers
1. **Device Manager**: Check the Device Manager for any missing drivers or hardware that requires additional drivers.

## 9. Familiarization
1. **Explore Windows Features**: Spend some time exploring features like Cortana, Task View, virtual desktops, and the Microsoft Store.
2. **Learn Keyboard Shortcuts**: Learning basic keyboard shortcuts can improve efficiency.

## 10. Set Up Email and Apps
1. **Email Client**: Set up email accounts in the preferred email client (Outlook, Mail app, etc.).
2. **Download Apps**: Download any additional apps or software your grandpa might need from the Microsoft Store or other trusted sources.

## 11. Parental Controls (if needed)
1. **Family Safety**: If there are younger users, set up family safety and parental controls through **Settings > Accounts > Family & other users**.

## 12. Maintenance Tips
1. **Regular Updates**: Ensure that the device checks for and installs updates regularly.
2. **Disk Cleanup**: Use built-in tools like Disk Cleanup to free up space.
3. **Performance Monitoring**: Keep an eye on performance via Task Manager and take steps to manage startup programs and services.

## Conclusion
By following these steps, your grandpa's new Windows device should be well set up, secure, and personalized to his needs. If he encounters any issues, many solutions can be found through the built-in Windows Help or by searching online. Enjoy the new device!
""")
windows_setting_ar = ("""# إعداد جهاز ويندوز جديد

## 1. الإعداد والتكوين الأولي
1. **تشغيل الجهاز**: قم بتشغيل الجهاز واتبع التعليمات التي تظهر على الشاشة.
2. **اختيار المنطقة واللغة**: اختر إعدادات المنطقة واللغة المناسبة.
3. **الاتصال بالشبكة**: اتصل بشبكة Wi-Fi أو شبكة سلكية لضمان الوصول إلى الإنترنت لتحديثات الحساب والإعدادات.
4. **إعداد الحساب**:
    - **حساب مايكروسوفت**: سجل الدخول باستخدام حساب مايكروسوفت للوصول إلى الخدمات السحابية والتطبيقات والمزيد.
    - **حساب محلي**: بدلاً من ذلك، قم بإعداد حساب محلي إذا كان مفضلاً.

## 2. تحديث ويندوز
1. **التحقق من التحديثات**: اذهب إلى **الإعدادات > التحديث والأمان > تحديث ويندوز** وانقر على **التحقق من وجود تحديثات**. قم بتثبيت جميع التحديثات المتاحة لضمان أن النظام آمن ومحدث.

## 3. تثبيت البرامج الأساسية
1. **متصفح الإنترنت**: قم بتثبيت المتصفحات المفضلة مثل Google Chrome أو Firefox أو Microsoft Edge.
2. **برنامج الأمان**: تأكد من تفعيل Windows Defender أو قم بتثبيت برنامج مضاد للفيروسات إذا كان مفضلاً.
3. **أدوات الإنتاجية**: قم بتثبيت أدوات الإنتاجية الضرورية مثل Microsoft Office و Adobe Reader، إلخ.
4. **تطبيقات الاتصال**: قم بتثبيت تطبيقات مثل Zoom أو Skype أو Teams للمكالمات الفيديو والتواصل.

## 4. التخصيص
1. **خلفية وثيم**: قم بتخصيص خلفية سطح المكتب والثيم والألوان. يمكن القيام بذلك عبر **الإعدادات > التخصيص**.
2. **شريط المهام وقائمة ابدأ**: قم بتثبيت التطبيقات المستخدمة بشكل متكرر على شريط المهام وتنظيم قائمة ابدأ.

## 5. إعداد النسخ الاحتياطي
1. **OneDrive**: قم بإعداد OneDrive للنسخ الاحتياطي التلقائي للملفات الهامة إلى السحابة.
2. **النسخ الاحتياطي الخارجي**: استخدم قرص صلب خارجي للنسخ الاحتياطي الإضافي عبر **الإعدادات > التحديث والأمان > النسخ الاحتياطي**.

## 6. تكوين إعدادات الخصوصية
1. **خيارات الخصوصية**: اذهب إلى **الإعدادات > الخصوصية** واضبط إعدادات الخصوصية وفقًا للتفضيلات، بما في ذلك خدمات الموقع والوصول إلى الميكروفون والكاميرا، إلخ.

## 7. أمان الجهاز
1. **كلمة المرور أو الرقم السري**: قم بإعداد كلمة مرور قوية أو رقم سري لتسجيل الدخول.
2. **Windows Hello**: إذا كان مدعومًا، قم بتكوين Windows Hello لتسجيل الدخول باستخدام بصمة الإصبع أو التعرف على الوجه.
3. **BitLocker**: قم بتمكين BitLocker لأمان إضافي إذا كان الجهاز يدعمه.

## 8. تثبيت التعريفات الإضافية
1. **مدير الجهاز**: تحقق من مدير الجهاز لأي تعريفات مفقودة أو أجهزة تتطلب تعريفات إضافية.

## 9. التعرف على النظام
1. **استكشاف ميزات ويندوز**: اقض بعض الوقت في استكشاف ميزات مثل Cortana و Task View وسطح المكتب الافتراضي ومتجر مايكروسوفت.
2. **تعلم اختصارات لوحة المفاتيح**: تعلم اختصارات لوحة المفاتيح الأساسية يمكن أن يحسن الكفاءة.

## 10. إعداد البريد الإلكتروني والتطبيقات
1. **عميل البريد الإلكتروني**: قم بإعداد حسابات البريد الإلكتروني في عميل البريد المفضل (Outlook أو تطبيق البريد، إلخ).
2. **تحميل التطبيقات**: قم بتحميل أي تطبيقات أو برامج إضافية قد يحتاجها جدك من متجر مايكروسوفت أو مصادر موثوقة أخرى.

## 11. التحكم الأبوي (إذا لزم الأمر)
1. **سلامة العائلة**: إذا كان هناك مستخدمون صغار، قم بإعداد سلامة العائلة والتحكم الأبوي عبر **الإعدادات > الحسابات > العائلة والمستخدمون الآخرون**.

## 12. نصائح الصيانة
1. **التحديثات المنتظمة**: تأكد من أن الجهاز يتحقق من ويثبت التحديثات بانتظام.
2. **تنظيف القرص**: استخدم الأدوات المدمجة مثل تنظيف القرص لتحرير المساحة.
3. **مراقبة الأداء**: راقب الأداء عبر مدير المهام واتخذ الخطوات لإدارة البرامج والخدمات التي تبدأ مع التشغيل.

## الخاتمة
باتباع هذه الخطوات، يجب أن يكون جهاز ويندوز الجديد لجدك مجهزًا بشكل جيد وآمن ومخصص لاحتياجاته. إذا واجه أي مشكلات، يمكن العثور على العديد من الحلول من خلال مساعدة ويندوز المدمجة أو البحث عبر الإنترنت. استمتع بالجهاز الجديد!
""")
ios_setting_en = ("""# Setting Up a New iOS Device

## 1. Power On and Initial Setup
1. **Power On**: Press and hold the power button to turn on the device.
2. **Language and Region**: Select your preferred language and region.
3. **Quick Start**: If you have another iOS device running iOS 11 or later, use Quick Start to transfer settings automatically. Place the devices close to each other and follow the instructions.
4. **Manual Setup**: If you don't have another device, tap on "Set Up Manually" and follow the on-screen instructions.

## 2. Network Connection
1. **Wi-Fi**: Choose a Wi-Fi network and enter the password to connect.
2. **Cellular Network**: If the device has a SIM card, you can set up the cellular network.

## 3. Security Settings
1. **Touch ID or Face ID**: Follow the instructions to set up Touch ID (fingerprint) or Face ID (facial recognition) for added security.
2. **Passcode**: Create a passcode to secure your device.

## 4. Restore Data and Apps
1. **Restore from Backup**: Choose to restore from an iCloud backup or an iTunes backup if available.
2. **Move Data from Android**: Use the "Move to iOS" app to transfer data from an Android device.
3. **Set Up as New**: Select "Set Up as New iPhone/iPad" if you want to start fresh without restoring any data.

## 5. Sign in to Apple ID
1. **Apple ID**: Enter your Apple ID and password. If you don't have an Apple ID, you can create a new one.
2. **iCloud**: Choose which iCloud services you want to use, such as Mail, Contacts, and Calendars.

## 6. Set Up Siri and Other Services
1. **Siri**: Set up Siri, the voice assistant, by following the instructions.
2. **Other Services**: Choose to enable or disable services such as Location Services, Analytics, Automatic Updates, etc.

## 7. Customize Your Device
1. **Wallpaper**: Choose your preferred wallpaper.
2. **Apps**: Download and install necessary apps from the App Store.
3. **Other Settings**: Explore and adjust other settings such as Notifications, Do Not Disturb, Display & Brightness.

## 8. Set Up Email and Accounts
1. **Email**: Set up email accounts by going to **Settings > Mail > Accounts > Add Account**.
2. **Other Accounts**: Add other accounts like Google, Facebook, or Microsoft.

## 9. Backup and Sync
1. **iCloud Backup**: Ensure iCloud Backup is enabled by going to **Settings > [Your Name] > iCloud > iCloud Backup**.
2. **iTunes Backup**: You can also create backups using iTunes if preferred.

## 10. Explore Features and Get Familiar
1. **New Features**: Explore the new features in iOS.
2. **User Guide**: Visit Apple's website or use the "Tips" app for additional guidance.

## Conclusion
By following these steps, your grandpa's new iOS device should be well set up, secure, and personalized to his needs. If he encounters any issues, many solutions can be found through Apple's built-in Help or by searching online. Enjoy the new device!
""")
ios_setting_ar = ("""# إعداد جهاز iOS جديد

## 1. التشغيل والإعداد الأولي
1. **التشغيل**: اضغط مع الاستمرار على زر الطاقة لتشغيل الجهاز.
2. **الاختيار**: اختر اللغة والمنطقة المفضلتين.
3. **البدء السريع**: إذا كان لديك جهاز iOS آخر يعمل بنظام iOS 11 أو أحدث، يمكنك استخدام ميزة البدء السريع لنقل الإعدادات تلقائيًا. ضع الأجهزة بالقرب من بعضها واتبع التعليمات.
4. **التهيئة اليدوية**: إذا لم يكن لديك جهاز آخر، اضغط على "إعداد يدوي" واتبع التعليمات التي تظهر على الشاشة.

## 2. الاتصال بالشبكة
1. **Wi-Fi**: اختر شبكة Wi-Fi وأدخل كلمة المرور للاتصال.
2. **شبكة خلوية**: إذا كان الجهاز يحتوي على بطاقة SIM، يمكنك إعداد الشبكة الخلوية.

## 3. إعدادات الأمان
1. **Touch ID أو Face ID**: اتبع التعليمات لإعداد بصمة الإصبع (Touch ID) أو التعرف على الوجه (Face ID) لتحسين الأمان.
2. **رمز المرور**: قم بإنشاء رمز مرور للوصول إلى الجهاز.

## 4. استعادة البيانات والتطبيقات
1. **استعادة من نسخة احتياطية**: اختر الاستعادة من نسخة iCloud الاحتياطية أو نسخة iTunes الاحتياطية إذا كانت متوفرة.
2. **النقل من Android**: استخدم تطبيق "Move to iOS" لنقل البيانات من جهاز Android.
3. **إعداد جديد**: اختر "إعداد كجهاز جديد" إذا كنت تريد بدء استخدام الجهاز بدون استعادة أي بيانات.

## 5. تسجيل الدخول إلى Apple ID
1. **Apple ID**: أدخل معرف Apple وكلمة المرور. إذا لم يكن لديك معرف Apple، يمكنك إنشاء واحد جديد.
2. **iCloud**: اختر الخدمات التي تريد استخدامها مع iCloud مثل البريد، وجهات الاتصال، والتقويمات.

## 6. إعداد Siri والخدمات الأخرى
1. **Siri**: قم بإعداد Siri للمساعد الصوتي باتباع التعليمات.
2. **الخدمات الأخرى**: اختر تفعيل أو تعطيل الخدمات مثل الموقع، التحليل، تحديثات iOS التلقائية، وغيرها.

## 7. تخصيص الجهاز
1. **خلفية الشاشة**: اختر خلفية الشاشة المفضلة.
2. **التطبيقات**: قم بتنزيل وتثبيت التطبيقات المطلوبة من App Store.
3. **الإعدادات الأخرى**: استكشاف إعدادات أخرى مثل الإشعارات، عدم الإزعاج، والشاشة والسطوع.

## 8. إعداد البريد الإلكتروني والحسابات
1. **البريد الإلكتروني**: قم بإعداد حسابات البريد الإلكتروني عبر الذهاب إلى **الإعدادات > البريد > الحسابات > إضافة حساب**.
2. **الحسابات الأخرى**: أضف حسابات أخرى مثل Google، Facebook، أو Microsoft.

## 9. النسخ الاحتياطي والمزامنة
1. **iCloud Backup**: تأكد من تفعيل النسخ الاحتياطي على iCloud عبر الذهاب إلى **الإعدادات > [اسمك] > iCloud > النسخ الاحتياطي على iCloud**.
2. **iTunes Backup**: يمكنك أيضًا إنشاء نسخ احتياطية عبر iTunes إذا كنت تفضل ذلك.

## 10. استكشاف الميزات والتعرف عليها
1. **الميزات الجديدة**: استكشاف الميزات الجديدة لنظام iOS.
2. **دليل المستخدم**: يمكنك زيارة موقع Apple على الويب أو استخدام تطبيق "Tips" للحصول على إرشادات إضافية.

## الخاتمة
باتباع هذه الخطوات، يجب أن يكون جهاز iOS الجديد لجدك مجهزًا بشكل جيد وآمن ومخصص لاحتياجاته. إذا واجه أي مشكلات، يمكن العثور على العديد من الحلول من خلال مساعدة Apple المدمجة أو البحث عبر الإنترنت. استمتع بالجهاز الجديد!
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
