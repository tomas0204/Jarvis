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
            "description": self._get_description(
                data["current"]["weather_code"]
                ),
        }
    
    def _get_description(self, weather_code):
        descriptions = {
            0: "Clear Sky",
            1: "Mainly Clear",
            2: "Partly Cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Rime Fog",
            51: "Light Drizzle",
            53: "Moderate Drizzle",
            55: "Dense Drizzle",
            61: "Light Rain",
            63: "Moderate Rain",
            65: "Heavy Rain",
            71: "Light Snow",
            73: "Moderate Snow",
            75: "Heavy Snow",
            80: "Light Showers",
            81: "Moderate Showers",
            82: "Heavy Showers",
            95: "Thunderstorm",
            96: "Thunderstorm with Hail",
            99: "Thunderstorm with Heavy Hail",
        }

        return descriptions.get(weather_code, "Unknown")