from flask import Flask,render_template, request
from flask_cors import CORS
import config
import json
import urllib

app = Flask(__name__)
app._static_folder = "static"
CORS(app)
WEATHER_API_KEY = config.WEATHER_API_KEY

@app.route('/', methods=['GET'])
def root():
    return "Hello World"

# returns json of Cities from cities.json file
@app.route('/cities', methods=['GET'])
def getCities():
    f = open ('cities.json', "r")
    cities = json.loads(f.read())
    f.close()
    return cities

# returns json of weather data
# received from external API from weatherapi.com
# params: cityName (ei. "Venice") to be added to API url
@app.route('/weather/<cityName>', methods=['GET'])
def getWeather(cityName):
    url = 'http://api.weatherapi.com/v1/current.json?key='+WEATHER_API_KEY+'&q='+cityName+'&aqi=no'
    response = urllib.request.urlopen(url)
    weatherData = response.read()
    return weatherData

if __name__=="__main__":
    app.run()

