import requests
from plyer import notification 

API_KEY = "e082a3d727c2a5a7ce93d40400841523"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather" 
APP_NAME = "AI Weather Assistant" 

def get_weather_data():
   
    city = input("🤖 AI Weather: Please enter the city you want the forecast for: ").strip()
   
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        print(f"❌ Network Error: Could not connect to weather service. {e}")
        return None

    if response.status_code == 200:
        data = response.json()
        
        try:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            
            recommendation = ""
            if 'rain' in desc.lower() or 'drizzle' in desc.lower():
                recommendation = "☔️ Recommendation: Take an umbrella! (Rain likely)"
            elif temp > 30.0:
                recommendation = "☀️ Recommendation: High heat! Stay hydrated."
            else:
                recommendation = "✅ Recommendation: You're good to go." 
            
            print("----------------------------------------")
            print(f"🌍 Weather Report for {city.title()}:") 
            print(f"   Temperature: {temp}°C")
            print(f"   Conditions: {desc.capitalize()}")
            print(f"   {recommendation}")
            print("----------------------------------------")
            
            notification.notify(
                title=f"Forecast for {city.title()}",
                message=f"{desc.capitalize()} at {temp}°C. {recommendation}",
                app_name=APP_NAME,
                timeout=5
            )

        except (KeyError, IndexError) as e:
            print(f"⚠️ Error: Could not parse weather data structure. {e}")
            
    else:
        print(f"❌ API Error: Could not retrieve data for {city}. Check city name.")

if __name__ == "__main__":
    get_weather_data()