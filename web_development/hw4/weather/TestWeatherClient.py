from unittest.mock import patch

import pytest

from WeatherClient import WeatherClient


class TestWeatherClient:
    @pytest.fixture(autouse=True)
    def setup_client(self):
        self.api_key = "test_api_key"
        self.client = WeatherClient(self.api_key)

    @pytest.fixture
    def api_payload_success(self):
        return {
            "coord": {
                "lon": 7.367,
                "lat": 45.133
            },
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 284.2,
                "feels_like": 282.93,
                "temp_min": 283.06,
                "temp_max": 286.82,
                "pressure": 1021,
                "humidity": 60,
                "sea_level": 1021,
                "grnd_level": 910
            },
            "visibility": 10000,
            "wind": {
                "speed": 4.09,
                "deg": 121,
                "gust": 3.47
            },
            "rain": {
                "1h": 2.73
            },
            "clouds": {
                "all": 83
            },
            "dt": 1726660758,
            "sys": {
                "type": 1,
                "id": 6736,
                "country": "IT",
                "sunrise": 1726636384,
                "sunset": 1726680975
            },
            "timezone": 7200,
            "id": 3165523,
            "name": "Province of Turin",
            "cod": 200
        }

    @patch('requests.get')
    @pytest.mark.parametrize('test_lat, test_lon, expected_params', [
        (4.357, 5.878, {'lat': 4.357, 'lon': 5.878, 'units': 'metric', 'appid': 'test_api_key'}),
        (12.879, 2.111, {'lat': 12.879, 'lon': 2.111, 'units': 'metric', 'appid': 'test_api_key'})
    ])
    def test_correct_coordinates_passing_reqeust(self, mock_req_get, test_lat, test_lon, expected_params):
        self.client.get_weather_by_coordinates(test_lat, test_lon)
        expected_url = 'https://api.openweathermap.org/data/2.5/weather'
        mock_req_get.assert_called_once_with(url=expected_url, params=expected_params)

    @patch('requests.get')
    @pytest.mark.parametrize('test_city, expected_params', [
        ('New-York', {'q': 'New-York', 'units': 'metric', 'appid': 'test_api_key'}),
        ('London', {'q': 'London', 'units': 'metric', 'appid': 'test_api_key'}),
        ('Kyiv', {'q': 'Kyiv', 'units': 'metric', 'appid': 'test_api_key'})
    ])
    def test_correct_city_passing_reqeust(self, mock_req_get, test_city, expected_params):
        self.client.get_weather_by_city(test_city)
        expected_url = 'https://api.openweathermap.org/data/2.5/weather'
        mock_req_get.assert_called_once_with(url=expected_url, params=expected_params)

    @patch('requests.get')
    def test_weather_by_city_success(self, mock_req_get, api_payload_success):
        mock_req_get.return_value.status_code = 200
        mock_req_get.return_value.json.return_value = api_payload_success
        weather_data = self.client.get_weather_by_city('Province of Turin')

        assert weather_data == {
            "city": api_payload_success.get("name"),
            "temperature": api_payload_success["main"]["temp"],
            "description": api_payload_success["weather"][0]["description"],
            "humidity": api_payload_success["main"]["humidity"],
            "wind_speed": api_payload_success["wind"]["speed"]
        }

    @patch("requests.get")
    def test_get_weather_by_city_failure(self, mock_get):
        mock_get.return_value.status_code = 404
        weather = self.client.get_weather_by_city("InvalidCity")
        assert weather is None
