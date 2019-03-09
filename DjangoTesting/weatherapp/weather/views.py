from django.shortcuts import render
import requests
from .models import City

# Create your views here.

OPEN_WEATHER_API_KEY = "f52e3e58521361afd959186d487fb974"

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    #city = 'chennai'
    #city_weather = requests.get(url.format(city,OPEN_WEATHER_API_KEY)).json()

    cities = City.objects.all()
    weather_data=[]

    for city in cities:
        city_weather = requests.get(url.format(city,OPEN_WEATHER_API_KEY)).json()
        weather = {
            'city' : city_weather['name'],
            'temp' : city_weather['main']['temp'],
            'desc' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)
    render_var = {'weather_data' : weather_data}
    return render(request,'weather/index.html', render_var)
