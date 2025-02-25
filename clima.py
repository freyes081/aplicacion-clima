import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

def get_weather(city):
    # Obtener API key desde variables de entorno
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    if not api_key:
        raise ValueError("La API key no está configurada. Configura la variable de entorno OPENWEATHER_API_KEY.")
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&lang=es&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        wind = data["wind"]
        weather_description = data["weather"][0]["description"]
        
        # Agregamos la ciudad al diccionario de retorno
        return {
            "city": city.capitalize(),  # Capitalizar el nombre de la ciudad
            "temperature": main["temp"],
            "pressure": main["pressure"],
            "humidity": main["humidity"],
            "wind_speed": wind["speed"],
            "description": weather_description
        }
    else:
        return None

# Código para probar en modo desarrollo (no se ejecutará cuando se importe)
if __name__ == "__main__":
    print(get_weather("Bogota"))    
    
