import os

import aiohttp


class WeatherClient:
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

    def __init__(self, api_key=None, units='metric'):
        self._units = units

        if api_key is None:
            self._api_key = os.getenv("OPENWEATHER_API_KEY")
        else:
            self._api_key = api_key

    async def get_weather_by_city(self, city_name):
        params = {
            'q': city_name,
            'appid': self._api_key,
            'units': self._units
        }
        return await self._fetch_weather(params)

    async def get_weather_by_coordinates(self, lat, lon):
        params = {
            'lat': lat,
            'lon': lon,
            'units': self._units,
            'appid': self._api_key
        }
        return await self._fetch_weather(params)

    async def _fetch_weather(self, params):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url=self.BASE_URL, params=params) as response:
                    response.raise_for_status()
                    payload_data = await response.json()

                    return {
                        "city": payload_data["name"],
                        "temperature": payload_data["main"]["temp"],
                        "description": payload_data["weather"][0]["description"],
                        "humidity": payload_data["main"]["humidity"],
                        "wind_speed": payload_data["wind"]["speed"]
                    }

            except aiohttp.ClientResponseError as error:
                raise Exception(f"Failed to fetch weather data; status: {error.status}, message: {error.message}")
            except aiohttp.ClientError as e:
                raise Exception(f"Failed to fetch weather data: {e}")
