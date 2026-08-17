export type JarvisState =
  | 'IDLE'
  | 'LISTENING'
  | 'PROCESSING'
  | 'SPEAKING'

export interface Message {
  id: number
  sender: 'JARVIS' | 'USER'
  text: string
  timestamp: Date
}

export type JarvisEvent =
  | {
      type: 'STATE_CHANGED'
      state: JarvisState
    }
  | {
      type: 'USER_MESSAGE'
      message: Message
    }
  | {
      type: 'JARVIS_MESSAGE'
      message: Message
    }
  | {
      type: 'COMMAND_EXECUTED'
      command: string
    }