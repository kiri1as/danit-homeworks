import os

import requests


class WeatherClient:
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

    def __init__(self, api_key=None, units='metric'):
        self._units = units

        if api_key is None:
            self._api_key = os.getenv("OPENWEATHER_API_KEY")
        else:
            self._api_key = api_key

    def get_weather_by_city(self, city_name):
        params = {
            'q': city_name,
            'appid': self._api_key,
            'units': self._units
        }
        return self._fetch_weather(params)

    def get_weather_by_coordinates(self, lat, lon):

        params = {
            'lat': lat,
            'lon': lon,
            'units': self._units,
            'appid': self._api_key,
        }
        return self._fetch_weather(params)

    def _fetch_weather(self, params):
        try:
            response = requests.get(url=self.BASE_URL, params=params)
            response.raise_for_status()
            payload_data = response.json()

            return {
                "city": payload_data["name"],
                "temperature": payload_data["main"]["temp"],
                "description": payload_data["weather"][0]["description"],
                "humidity": payload_data["main"]["humidity"],
                "wind_speed": payload_data["wind"]["speed"]
            }

        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
