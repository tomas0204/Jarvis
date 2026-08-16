export type JarvisState =
  | 'IDLE'
  | 'LISTENING'
  | 'PROCESSING'
  | 'SPEAKING'

export interface Message {
    id: number,
    sender: "JARVIS" | "USER"
    text: string
    timestamp: Date 
}