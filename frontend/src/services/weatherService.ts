export interface WeatherStats {
  temperature: number,
  weather_code: number,
  description: string
}

class WeatherService {

  async getWeatherinfo(): Promise<WeatherStats> {
    const response = await fetch(
      'http://127.0.0.1:8000/api/weather'
    )

    if (!response.ok) {
      throw new Error(
        'Error obteniendo información del sistema'
      )
    }

    return await response.json()
  }
}

export const weatherService = new WeatherService()