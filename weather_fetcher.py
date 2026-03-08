```python
import requests
import json

class WeatherFetcher:
    def __init__(self, api_key, base_url='http://api.openweathermap.org/data/2.5/'):
        """
        Initializes the WeatherFetcher instance.

        Args:
            api_key (str): The API key for the OpenWeatherMap API.
            base_url (str): The base URL for the OpenWeatherMap API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def get_weather_data(self, city):
        """
        Fetches the weather data for a given city.

        Args:
            city (str): The name of the city.

        Returns:
            dict: The weather data for the given city.
        """
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.base_url + 'weather', params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_forecast_data(self, city):
        """
        Fetches the forecast data for a given city.

        Args:
            city (str): The name of the city.

        Returns:
            dict: The forecast data for the given city.
        """
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.base_url + 'forecast', params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

def get_weather_data(city, api_key):
    """
    Fetches the weather data for a given city.

    Args:
        city (str): The name of the city.
        api_key (str): The API key for the OpenWeatherMap API.

    Returns:
        dict: The weather data for the given city.
    """
    weather_fetcher = WeatherFetcher(api_key)
    return weather_fetcher.get_weather_data(city)

def get_forecast_data(city, api_key):
    """
    Fetches the forecast data for a given city.

    Args:
        city (str): The name of the city.
        api_key (str): The API key for the OpenWeatherMap API.

    Returns:
        dict: The forecast data for the given city.
    """
    weather_fetcher = WeatherFetcher(api_key)
    return weather_fetcher.get_forecast_data(city)
```