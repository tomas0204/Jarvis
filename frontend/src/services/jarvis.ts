import type { JarvisEvent } from '../types/jarvis'

class JarvisService {
  private listeners: Array<(event: JarvisEvent) => void> = []

  subscribe(listener: (event: JarvisEvent) => void) {
    this.listeners.push(listener)

    return () => {
      this.listeners = this.listeners.filter(
        currentListener => currentListener !== listener
      )
    }
  }

  private emit(event: JarvisEvent) {
    this.listeners.forEach(listener => {
      listener(event)
    })
  }

  async sendMessage(text: string) {
    const response = await fetch(
      'http://127.0.0.1:8000/api/message',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text,
        }),
      }
    )

    if (!response.ok) {
      throw new Error('Error comunicándose con Jarvis')
    }

    return await response.json()
  }
}

export const jarvisService = new JarvisService()