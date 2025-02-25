import requests


def get_weather(city):
    api_key = "1fc9cc264077666d0486b4131f72c12e"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&lang=es&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        wind = data["wind"]
        weather_description = data["weather"][0]["description"]
        
        return {
            "temperature": main["temp"],
            "pressure": main["pressure"],
            "humidity": main["humidity"],
            "wind_speed": wind["speed"],
            "description": weather_description
        }
    else:
        return None
    
print(get_weather("Bogota"))    
    
