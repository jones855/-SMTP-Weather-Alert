# 🌧️ SMTP Weather Alert

A Python application that checks the weather forecast using the OpenWeatherMap API and automatically sends an email notification if rain is expected within the next 12 hours.

Instead of using Twilio SMS, this project uses **SMTP** to send weather alerts directly to your email inbox.

---

## 📸 Preview

(Add a screenshot here)

---

## ✨ Features

- Checks the weather forecast using the OpenWeatherMap API
- Detects if rain is expected within the next 12 hours
- Sends an email alert automatically using SMTP
- Uses environment variables to protect sensitive information
- Easy to customize for any location

---

## 🛠️ Built With

- Python 3
- SMTP (smtplib)
- OpenWeatherMap API
- Requests
- python-dotenv (optional)

---

## 📂 Project Structure

```
SMTP-Weather-Alert/
│
├── main.py
├── .env.example
├── requirements.txt
├── README.md
└── screenshots/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/SMTP-Weather-Alert.git
```

### 2. Navigate into the project

```bash
cd SMTP-Weather-Alert
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
API_KEY=your_openweathermap_api_key

EMAIL=your_email@gmail.com
PASSWORD=your_app_password

TO_EMAIL=recipient@email.com
```

> **Note:** If you're using Gmail, create an App Password instead of using your normal password.

---

## ▶️ Run the Project

```bash
python main.py
```

If rain is expected within the next 12 hours, an email notification will be sent automatically.

---

## 📧 Example Email

**Subject**

```
Rain Alert 🌧️
```

**Body**

```
Rain is expected within the next 12 hours.

Don't forget to take an umbrella! ☔
```

---

## 📚 What I Learned

This project helped me learn:

- Working with REST APIs
- API Authentication
- Parsing JSON data
- Using SMTP for email automation
- Working with environment variables
- Protecting API keys and passwords
- Python automation

---

## 🚀 Future Improvements

- Support multiple cities
- Add weather icons
- HTML email formatting
- Schedule automatic daily checks with GitHub Actions
- Desktop notifications
- SMS and WhatsApp support

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

---

## 📄 License

This project is licensed under the MIT License.
