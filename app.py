import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=5a1e92988643e6c2a4036afd5872619f'
    city = 'Las Vegas'
    r = requests.get(url.format(city)).json()
    print(r)

    weather = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon']
    }
    print(weather)
    return render_template('weather.html', weather=weather)

if __name__ == "__main__":
    app.run(debug=True)