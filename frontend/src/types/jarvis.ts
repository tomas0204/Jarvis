export type JarvisState =
  | 'IDLE'
  | 'LISTENING'
  | 'PROCESSING'
  | 'SPEAKING'


export type JarvisStatus =
  | 'ONLINE'
  | 'OFFLINE'


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
      type: 'JARVIS_STATUS'
      status: JarvisStatus
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