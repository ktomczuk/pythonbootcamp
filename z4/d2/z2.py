#the_temp
#sys ,json, url.lib
import sys
import json
import urllib.request

#miasto = input
miasto = "warsaw"
f = urllib.request.urlopen(f"https://www.metaweather.com/api/location/search/?query={miasto}")
data = f.read()
data = json.loads(data)
#print(data)
for kurs in data:
    numer = kurs['woeid']
    #print(numer)
pogoda = urllib.request.urlopen(f"https://www.metaweather.com/api/location/{numer}/")
weather = pogoda.read()
weather = json.loads(weather)
print(weather)

pog = weather[0]['consolidated_weather']
print(data[0]['rates'])
#for kurs in kursy:



#Pogoda w Warsaw:

###  with urllib.request.urlopen(f"https://www.metaweather.com/api/location/search/?query={miasto}")
