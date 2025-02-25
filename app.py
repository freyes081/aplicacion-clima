from flask import Flask, render_template, request, redirect, url_for
import clima

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    if not city:
        return render_template('index.html', error="Por favor, ingresa el nombre de una ciudad.")
    
    weather_data = clima.get_weather(city)
    
    if weather_data is None:
        return render_template('index.html', error="No se encontraron datos para esa ciudad.")
    
    return render_template('weather.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
    
    
