from backend.integrations.weather import WeatherService

weather = WeatherService()

print(weather.get_current_weather())