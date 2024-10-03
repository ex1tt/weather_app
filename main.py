# WEATHER APP
# Made by ex1tt https://github.com/ex1tt
# Get your own Weather API https://api.openweathermap.org/
# Weather Forecast may not be 100% accurate

import tkinter as tk
import requests
import json

root = tk.Tk()
root.geometry("400x200")
root.title("Weather App")
root.resizable(0, 0)

#  All Locations
locations = ['Cork', 'Berlin', 'London', 'Paris', 'Tokyo', 'Sydney']

#  Creating variables before defined in functions
api_key = ''
temperature = ''
weather = ''
timezone = ''

#  ALL API KEYS
api_key_cork = ''

api_key_berlin = ''

api_key_london = ''

api_key_paris = ''

api_key_tokyo = ''

api_key_sydney = ''


#  Running all functions together
def run_all_functions():
    get_api_key()
    get_temp_and_location()
    show_information()


#  Create Function To Choose API KEY/Location
def get_api_key():

    global api_key

    location_chosen_get = location_chosen.get()

    if str(location_chosen_get) == 'Cork':
        api_key = api_key_cork
    elif str(location_chosen_get) == 'Berlin':
        api_key = api_key_berlin
    elif str(location_chosen_get) == 'London':
        api_key = api_key_london
    elif str(location_chosen_get) == 'Paris':
        api_key = api_key_paris
    elif str(location_chosen_get) == 'Tokyo':
        api_key = api_key_tokyo
    elif str(location_chosen_get) == 'Sydney':
        api_key = api_key_sydney


#  Create Function To Show Temp Of Chosen Location
def get_temp_and_location():

    global temperature
    global weather

    api_request = requests.get(api_key)

    api = json.loads(api_request.content)

    base_temperature = float(api['main']['temp']) - 273.15

    converted_temperature = round(base_temperature, 1)

    temperature = "Temperature: " + str(converted_temperature) + "°C"

    #  Get the weather
    base_weather = api['weather'][0]['main']
    weather = "Weather: " + base_weather


#  put all the information on the screen
def show_information():

    temp_lbl = tk.Label(root, text=temperature, font=('calibri', 15), width=30,  anchor='w', bg='white')
    temp_lbl.place(x=100, y=150)

    location_lbl = tk.Label(root, text=weather, font=('calibri', 15), width=30, anchor='w', bg='white')
    location_lbl.place(x=100, y=100)


#  Create Button/OptionMenu To Choose Location
location_chosen = tk.StringVar(root)
location_chosen.set(locations[0])

location_option_menu = tk.OptionMenu(root, location_chosen, *locations)
location_option_menu.configure(font=('calibri', 15), width=6)
location_option_menu.place(x=120, y=20)

location_btn = tk.Button(root, command=run_all_functions)
location_btn.configure(font=('calibri', 13), width=2)
location_btn.place(x=230, y=21)


root.mainloop()
