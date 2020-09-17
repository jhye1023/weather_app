import requests
from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=5a1e92988643e6c2a4036afd5872619f'

        weather_data = requests.get(url).json()
    
        temp = weather_data['main']['temp']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']

  
        return render_template('results.html', temp=temp, description=description, wind_speed=wind_speed, city=city)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
