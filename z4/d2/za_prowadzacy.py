#zainstalować  pip install requests
import sys # do wywoalania warsaw zeby wywolac w konsoli python i miasto
import json
import urllib.request
import requests


def get_location(location_name):
    with requests.get(f"https://www.metaweather.com/api/location/search/?query={location_name}") as f:
        data = f.json()
    return data[0]['woeid']

def get_location_weather(location_id):
    with requests.get(f"https://www.metaweather.com/api/location/{location_id}") as f:
        data = f.json()
        the_temp = data['consolidated_weather'][0]['the_temp']
        air_pressure = data['consolidated_weather'][0]['air_pressure']

#Weather = sametuple

def present_results(dane):
   pass
#print(data)
#for kurs in data:
#    numer = kurs['woeid']
#    #print(numer)
##pogoda = urllib.request.urlopen(f"https://www.metaweather.com/api/location/{numer}/")
#weather = pogoda.read()
#weather = json.loads(weather)
#print(weather)

#pog = weather[0]['consolidated_weather']
#print(data[0]['rates'])
#for kurs in kursy: