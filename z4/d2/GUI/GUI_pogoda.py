import sys
import requests
from collections import namedtuple
import tkinter

root = tkinter.Tk()
root.title("Pogodynka")

location_name_label = tkinter.Label(master=root, text="Podaj miasto")
location_name_label.grid(row=0, column=0)
location_name_entry = tkinter.Entry(master=root)
location_name_entry.grid(row=0, column=1)

def wyrzuc_pogode():
    location_name = location_name_entry.get()
    """to jest docstring"""
    with requests.get(f"https://www.metaweather.com/api/location/search/?query={location_name}") as f:
        data = f.json()
    return data[0]["woeid"]


Weather = namedtuple("Weather", ["location", 'the_temp', 'air_pressure', 'humidity'])

def get_location_weather():
    with requests.get(f"https://www.metaweather.com/api/location/{location_id}/") as f:
        data = f.json()

    weather = Weather(
        location=data['title'],
        the_temp=data['consolidated_weather'][0]['the_temp'],
        air_pressure=data['consolidated_weather'][0]['air_pressure'],
        humidity=data['consolidated_weather'][0]['humidity'],
    )
    return weather


def present_results(weather):
    temp_label.configure(text=f"{weather.the_temp}")
    air_pressure.configure(text=f"{weather.air_pressure}")
    humadity_label.configure(text=f"{weather.humidity}")
    print(output)



temp_label = tkinter.Label(master=root, text="Temperatura")
temp_label.grid(row=1, column=0)
air_pressure_label = tkinter.Label(master=root, text="Cisnienie")
air_pressure_label.grid(row=2, column=0)
humadity_label = tkinter.Label(master=root, text="Cisnienie")
humadity_label.grid(row=3, column=0)

oblicz_button = tkinter.Button(master=root, text="Podaj pogode", command=get_location_weather )
oblicz_button.grid(row=4, column=0)

id_ = get_location_id(sys.argv[1])
weather = get_location_weather(id_)
present_results(weather)