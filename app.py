from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Function to get weather data from OpenWeatherMap
def get_weather(city):
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
    else:
        return None

@app.route('/')
def home():
    return "Welcome to the Weather App! Use /weather?city= to get the weather."

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'Please provide a city name.'}), 400
    
    weather_data = get_weather(city)
    if weather_data:
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'City not found or API limit reached.'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
