export interface SystemInfo {
  cpu: number
  memory: number
  uptime: string
}

class SystemService {
  async getSystemInfo(): Promise<SystemInfo> {
    const response = await fetch(
      'http://127.0.0.1:8000/api/system'
    )

    if (!response.ok) {
      throw new Error('Error obteniendo información del sistema')
    }

    return await response.json()
  }
}

export const systemService = new SystemService()