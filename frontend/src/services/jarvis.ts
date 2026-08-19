import type { JarvisEvent } from '../types/jarvis'

class JarvisService {
  private listeners: Array<(event: JarvisEvent) => void> = []
  private socket: WebSocket | null = null

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

  connect() {
    if (this.socket) return

    this.socket = new WebSocket(
      'ws://127.0.0.1:8000/ws/jarvis'
    )

    this.socket.onopen = () => {
      console.log('WebSocket conectado con Jarvis')
    }

    this.socket.onmessage = (event) => {
        const data = JSON.parse(event.data)

        if (
            data.type === 'USER_MESSAGE' ||
            data.type === 'JARVIS_MESSAGE'
        ) {
            data.message.timestamp = new Date(
            data.message.timestamp
            )
        }

        this.emit(data)
    }

    this.socket.onclose = () => {
      console.log('WebSocket desconectado')
      this.socket = null
    }

    this.socket.onerror = (error) => {
      console.error('WebSocket error:', error)
    }
  }

  disconnect() {
    this.socket?.close()
    this.socket = null
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