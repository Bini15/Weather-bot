# 🌦️ AI Weather Assistant

A Python-based intelligent weather assistant that fetches real-time weather data and provides smart recommendations along with desktop notifications.

---

## 🚀 Features

- 🌍 Real-time weather data using OpenWeatherMap API  
- 🧠 Smart recommendations (rain alerts, heat warnings, normal conditions)  
- 🔔 Desktop notifications for instant updates  
- 💬 Simple CLI-based user interaction  
- ⚡ Fast and lightweight script  

---

## 🛠️ Tech Stack

- Python  
- Requests (API handling)  
- Plyer (Desktop notifications)  
- OpenWeatherMap API  

---

## ⚙️ How It Works

1. User enters a city name  
2. System fetches real-time weather data via API  
3. Extracts temperature and weather condition  
4. Applies logic to generate recommendations:
   - Rain → Take umbrella ☔  
   - High temperature → Stay hydrated ☀️  
   - Normal → Good to go ✅  
5. Displays output + sends desktop notification  

---

## ▶️ Run Locally

```bash
pip install requests plyer
python weather_bot.py
