from unicodedata import name
from .models import WeatherData
from .locations import locationsData
import requests
import time

def update():
    print("Update db is Running")
    for cityData in locationsData:
        obj = WeatherData.objects.get_or_create(city=cityData['name'])
        resp=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityData['name']}&appid=1bd2c0b98f742f4ade03813ce9413d51&units=metric")
        resp=resp.json()
        obj[0].data = resp
        obj[0].save()
    
    time.sleep(30)