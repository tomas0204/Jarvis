import requests

from config import (
    WEATHER_LATITUDE,
    WEATHER_LONGITUDE,
)


class WeatherService:

    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def get_current_weather(self):
        params = {
            "latitude": WEATHER_LATITUDE,
            "longitude": WEATHER_LONGITUDE,
            "current": "temperature_2m,weather_code",
            "temperature_unit": "celsius",
            "timezone": "auto",
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        return {
            "temperature": data["current"]["temperature_2m"],
            "weather_code": data["current"]["weather_code"],
        }