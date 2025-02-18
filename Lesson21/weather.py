import requests
import os
from pprint import pprint

def get_current_weather():
    print("\n*** Get Current Weather conditions***\n")
    city = input("\nPlease enter a city name")

    request_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&models=jma_seamless"
    # print(request_url)

    weather_data = requests.get(request_url).json()

    # print(weather_data)
    # pprint(weather_data)
    print(f"Current Weather for {weather_data['hourly_units']}")

get_current_weather()
