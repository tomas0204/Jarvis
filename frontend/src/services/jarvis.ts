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

  sendMessage(text: string) {
    console.log('JARVIS SERVICE →', text)
  }
}

export const jarvisService = new JarvisService()