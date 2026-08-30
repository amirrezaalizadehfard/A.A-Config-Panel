<!-- Language Switcher -->
<p align="center">
  <a href="#-فارسی"><b>فارسی</b></a> | <a href="#-english"><b>English</b></a>
</p>

---

# 🇮🇷 فارسی

# 🚀 AA Config Panel (A.A-C-P)

یک پنل حرفه‌ای، کامل و کاملاً رایگان برای مدیریت و ساخت کانفیگ بدون نیاز به خرید سرور اختصاصی (VPS) یا پرداخت هزینه.

---

## 📝 تغییرات اخیر در ورژن 2.1 (Changelog)

### 🆕 نسخه جدید
* 🛡️ **فیلتر محتوای بزرگسال (Adult Content Filter):** قابلیت انسداد و فیلترسازی هوشمند وب‌سایت‌ها و محتوای بزرگسال برای افزایش امنیت و سلامت شبکه.

---

## ✨ ویژگی‌های کلیدی

* 🪙 **کاملاً رایگان:** بدون نیاز به پرداختی یا خرید سرور اختصاصی (VPS) - اجرا روی Railway.
* 🎛️ **پنل مدیریتی جامع:** دسترسی به تمام امکانات مدیریتی در یک محیط ساده و مدرن.
* 🛡️ **فیلتر محتوای بزرگسال:** امکان فعال‌سازی و کنترل فیلتر محتوای نامناسب و بزرگسال.
* 👤 **مدیریت پیشرفته کانفیگ‌ها:** قابلیت کنترل و تنظیم دقیق تک‌تک کانفیگ‌های ساخته‌شده.
* 📊 **اعمال محدودیت‌های هوشمند:**
  - 📦 محدودیت حجم مصرفی (GB/MB/KB)
  - 🚀 محدودیت سرعت (Mbps)
  - 👥 محدودیت تعداد کاربران هم‌زمان (IP Limit)
  - 📅 تاریخ انقضا (تعداد روزهای اعتبار)
* 🌐 **پروتکل‌های متنوع:** پشتیبانی از VLESS + WebSocket و XHTTP (packet-up, stream-up, stream-one)
* 🔒 **تنظیمات امنیتی:** قابلیت تنظیم Fingerprint (uTLS) و ALPN برای هر کانفیگ
* 🤖 **ربات تلگرام:** امکان اتصال به ربات تلگرام جهت ساخت و مدیریت سریع‌تر کانفیگ‌ها
* 🗂 **گروه‌های ساب:** قابلیت ایجاد لینک اشتراک حرفه‌ای برای گروهی از کانفیگ‌ها

---

## 🛠️ راهنمای نصب و راه‌اندازی (Step-by-Step)

برای راه‌اندازی رایگان پروژه، مراحل زیر را به ترتیب انجام دهید:

### ۱. ساخت ایمیل موقت و اکانت گیت‌هاب
1. ابتدا به سایت [atomicmail.io](https://atomicmail.io) مراجعه کرده و یک ایمیل موقت (فیک) بسازید.
2. با استفاده از ایمیل ساخته‌شده، یک حساب کاربری جدید در [GitHub](https://github.com) ایجاد کنید.

### ۲. فورک کردن پروژه (Fork)
1. وارد صفحه همین پروژه در گیت‌هاب شوید.
2. از بالای صفحه سمت راست، روی دکمه **Fork** کلیک کنید.
3. یک نام دلخواه برای پروژه خود انتخاب کرده و دکمه **Create Fork** را بزنید تا پروژه به اکانت شما اضافه شود.

### ۳. دپلاوی روی سرویس Railway
1. وارد سایت [Railway.com](https://railway.com) شوید و از بالای صفحه روی **Sign In** کلیک کنید.
2. گزینه **Continue with GitHub** را انتخاب کرده و با اکانتی که در مرحله قبل ساختید وارد شوید.
3. در داشبورد اصلی، روی دکمه **New** کلیک کرده و گزینه **GitHub Repository** را انتخاب کنید.
4. پروژه‌ای که فورک کرده بودید را انتخاب کنید و منتظر بمانید تا فرایند ساخت اولیه تمام شود.

### ۴. تنظیمات دامنه و لوکیشن
1. روی پروژه ساخته‌شده کلیک کرده و وارد زبانه **Settings** شوید.
2. از بخش **Networking**، روی دکمه **Generate Domain** کلیک کنید تا یک لینک اختصاصی برای شما ساخته شود.
3. به پایین صفحه اسکرول کرده و از بخش **Scale**، لوکیشن (سرور) مورد نظر خود را انتخاب کنید.
4. در نهایت روی دکمه **Deploy** کلیک کنید تا پروژه اجرا شود.

---

## 🌐 ورود به پنل

آدرس دامنه‌ای که در بخش **Networking** ساخته شد را کپی کرده، در مرورگر خود وارد کنید و عبارتی مانند زیر را به انتهای آن اضافه کنید:

```text
https://your-domain.up.railway.app/login
```

🎉 **تبریک!** پنل مدیریت شما با موفقیت و بدون پرداخت هیچ هزینه‌ای راه‌اندازی شد.

---

## 📋 پروتکل‌های پشتیبانی‌شده

| پروتکل | توضیحات |
|--------|---------|
| `vless-ws` | VLESS over WebSocket (کلاسیک) |
| `xhttp-packet-up` | XHTTP با حالت packet-up |
| `xhttp-stream-up` | XHTTP با حالت stream-up (بهینه‌شده با موتور تطبیقی) |
| `xhttp-stream-one` | XHTTP با حالت stream-one |

---

## 🔧 Fingerprintهای قابل انتخاب

`chrome`, `firefox`, `safari`, `ios`, `android`, `edge`, `360`, `qq`, `random`, `randomized`

---

## 🤝 مشارکت

اگر نظری دارید یا مشکلی دیدید، خوشحال می‌شم از بخش Issues یا Pull Requests با من در میان بگذارید!

<br/><hr/><br/>

# 🇬🇧 English

# 🚀 AA Config Panel (A.A-C-P)

A professional, feature-rich, and completely free management panel to create and control proxy configurations without purchasing a VPS or paying server costs.

---

## 📝 Recent Updates in v2.1 (Changelog)

### 🆕 Latest Release
* 🛡️ **Adult Content Filtering:** Added built-in feature to block adult content and inappropriate websites for safer browsing.

---

## ✨ Key Features

* 🪙 **100% Free:** No VPS or payment required — hosted directly on Railway.
* 🎛️ **Comprehensive Admin Panel:** Manage all settings within a modern and user-friendly dashboard.
* 🛡️ **Adult Content Filter:** Toggle and manage content filtering for adult websites.
* 👤 **Advanced Config Management:** Fine-tune individual configuration parameters easily.
* 📊 **Smart Restrictions:**
  - 📦 Data Usage Limits (GB/MB/KB)
  - 🚀 Speed Limits (Mbps)
  - 👥 Concurrent Connection Limits (IP Limit)
  - 📅 Expiration Dates (Days active)
* 🌐 **Protocol Support:** VLESS + WebSocket and XHTTP (packet-up, stream-up, stream-one)
* 🔒 **Security Settings:** Customizable Fingerprint (uTLS) and ALPN options.
* 🤖 **Telegram Bot:** Integrated Telegram Bot support for creating and managing configs on the fly.
* 🗂 **Subscription Groups:** Create professional subscription links for grouped configurations.

---

## 🛠️ Installation Guide (Step-by-Step)

Follow these steps to deploy your panel for free:

### 1. Create a Temporary Email & GitHub Account
1. Visit [atomicmail.io](https://atomicmail.io) to generate a temporary email address.
2. Sign up for a new account on [GitHub](https://github.com) using the temporary email.

### 2. Fork the Repository
1. Navigate to this repository page on GitHub.
2. Click the **Fork** button in the top right corner.
3. Choose a name for your repository and click **Create Fork**.

### 3. Deploy to Railway
1. Go to [Railway.com](https://railway.com) and click **Sign In**.
2. Select **Continue with GitHub** and log in using your newly created GitHub account.
3. In the dashboard, click **New** and select **GitHub Repository**.
4. Choose your forked repository and wait for the initial setup to complete.

### 4. Domain & Location Setup
1. Open your deployed project and navigate to the **Settings** tab.
2. Under **Networking**, click **Generate Domain** to create your public URL.
3. Scroll down to **Scale** and select your preferred server location.
4. Click **Deploy** to publish the panel.

---

## 🌐 Accessing the Panel

Copy the domain generated in the **Networking** section, paste it into your browser, and add `/login` to the end:

```text
https://your-domain.up.railway.app/login
```

🎉 **Congratulations!** Your management panel is live and fully functional without spending a dime.

---

## 📋 Supported Protocols

| Protocol | Description |
|--------|---------|
| `vless-ws` | VLESS over WebSocket (Classic) |
| `xhttp-packet-up` | XHTTP with packet-up mode |
| `xhttp-stream-up` | XHTTP with stream-up mode (Optimized with adaptive engine) |
| `xhttp-stream-one` | XHTTP with stream-one mode |

---

## 🔧 Available Fingerprints

`chrome`, `firefox`, `safari`, `ios`, `android`, `edge`, `360`, `qq`, `random`, `randomized`

---

## 🤝 Contributing

Feel free to submit issues or open pull requests if you have suggestions or bug reports!
