from unittest.mock import patch, AsyncMock, Mock

import pytest
from aiohttp import ClientResponseError, ClientResponse, ClientError


@pytest.mark.asyncio
class TestWeatherClient:

    @patch('aiohttp.ClientSession.get')
    @pytest.mark.parametrize('test_lat, test_lon, expected_params', [
        (4.357, 5.878, {'lat': 4.357, 'lon': 5.878, 'units': 'metric', 'appid': 'correct_key'}),
        (12.879, 2.111, {'lat': 12.879, 'lon': 2.111, 'units': 'metric', 'appid': 'correct_key'})
    ])
    async def test_correct_coordinates_passing_reqeust(self, mock_get, weather_client_normal, test_lat, test_lon,
                                                       expected_params):
        await weather_client_normal.get_weather_by_coordinates(test_lat, test_lon)
        expected_url = 'https://api.openweathermap.org/data/2.5/weather'
        mock_get.assert_called_once_with(url=expected_url, params=expected_params)

    @patch('aiohttp.ClientSession.get')
    @pytest.mark.parametrize('test_city, expected_params', [
        ('New-York', {'q': 'New-York', 'units': 'metric', 'appid': 'correct_key'}),
        ('London', {'q': 'London', 'units': 'metric', 'appid': 'correct_key'}),
        ('Kyiv', {'q': 'Kyiv', 'units': 'metric', 'appid': 'correct_key'})
    ])
    async def test_correct_city_passing_reqeust(self, mock_get, weather_client_normal, test_city, expected_params):
        await weather_client_normal.get_weather_by_city(test_city)
        expected_url = 'https://api.openweathermap.org/data/2.5/weather'
        mock_get.assert_called_once_with(url=expected_url, params=expected_params)

    @patch('aiohttp.ClientSession.get')
    async def test_weather_by_city_success(self, mock_get, weather_client_normal, api_payload_success):
        mock_response = AsyncMock()
        mock_response.__aenter__.return_value = mock_response
        mock_response.status = 200
        mock_response.json.return_value = api_payload_success
        mock_get.return_value = mock_response
        weather_data = await weather_client_normal.get_weather_by_city('Province of Turin')

        assert weather_data == {
            'city': api_payload_success['name'],
            'temperature': api_payload_success['main']['temp'],
            'description': api_payload_success['weather'][0]['description'],
            'humidity': api_payload_success['main']['humidity'],
            'wind_speed': api_payload_success['wind']['speed']
        }

    @patch('aiohttp.ClientSession.get')
    async def test_weather_invalid_api_key(self, mock_get, weather_client_wrong_key):
        mock_response = AsyncMock()
        mock_response.__aenter__.return_value = mock_response
        mock_get.return_value = mock_response
        mock_response.json.side_effect = ClientResponseError(
            request_info=Mock(),
            history=Mock(spec=ClientResponse),
            status=401,
            message='Invalid API KEY'
        )
        with pytest.raises(Exception, match='Failed to fetch weather data; status: 401, message: Invalid API KEY'):
            await weather_client_wrong_key.get_weather_by_city('London')

    @patch('aiohttp.ClientSession.get')
    async def test_weather_invalid_city(self, mock_get, weather_client_normal):
        mock_response = AsyncMock()
        mock_response.__aenter__.return_value = mock_response
        mock_get.return_value = mock_response
        mock_response.json.side_effect = ClientResponseError(
            request_info=Mock(),
            history=Mock(spec=ClientResponse),
            status=404,
            message='City not found'
        )
        with pytest.raises(Exception, match='Failed to fetch weather data; status: 404, message: City not found'):
            await weather_client_normal.get_weather_by_city('ABD_No_Such_City_ZXY')

    @patch('aiohttp.ClientSession.get')
    async def test_fetch_weather_connection_error(self, mock_get, weather_client_normal):
        mock_get.side_effect = ClientError('Connection error')
        expected_exception_message = 'Failed to fetch weather data: Connection error'

        with pytest.raises(Exception, match=expected_exception_message):
            await weather_client_normal.get_weather_by_city('London')
