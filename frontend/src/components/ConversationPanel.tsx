import "./styles/ConversationPanel.css"
import { FiMessageSquare, FiSend } from 'react-icons/fi'
import type { Message } from "../types/jarvis"
import { useState, useRef, useEffect } from "react"
import { jarvisService } from "../services/jarvis"

interface ConversationPanelProps {
  messages: Message[]
  onSendMessage: (message: Message) => void
}

function ConversationPanel({
  messages,
  onSendMessage,
}: ConversationPanelProps) {

  const messagesEndRef = useRef<HTMLDivElement>(null)
  const [input, setInput] = useState('')

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: 'smooth',
    })
  }, [messages])

  const handleSend = async () => {
    const text = input.trim()

    if (!text) return

    setInput('')

    const userMessage: Message = {
      id: Date.now(),
      sender: 'USER',
      text,
      timestamp: new Date(),
    }

    // Mostrar mensaje del usuario
    onSendMessage(userMessage)

    try {
      const data = await jarvisService.sendMessage(text)

      const jarvisMessage: Message = {
        id: Date.now() + 1,
        sender: 'JARVIS',
        text: data.response,
        timestamp: new Date(),
      }

      // Mostrar respuesta de Jarvis
      onSendMessage(jarvisMessage)

    } catch (error) {
      console.error('Error enviando mensaje:', error)
    }
  }

  const sender = (send: Message['sender']) => {
    if (send === 'JARVIS') {
      return 'message assistant-message message-author'
    }

    return 'message user-message message-author'
  }

  return (
    <aside className="conversation-panel">

      <div className="panel-header">
        <div className="panel-title">
          <FiMessageSquare />
          <span>JARVIS CHAT</span>
        </div>

        <div className="chat-status">
          <span className="status-dot" />
          AVAILABLE
        </div>
      </div>
      <div className="conversation-messages">

        {messages.map((message) => (
          <div
            key={message.id}
            className={`message ${message.sender.toLowerCase()}-message`}
          >

            <span className={sender(message.sender)}>
              {message.sender}
            </span>

            <p>{message.text}</p>

            <span className="message-time">
              {message.timestamp.toLocaleTimeString([], {
                hour: '2-digit',
                minute: '2-digit',
              })}
            </span>

          </div>
        ))}

        <div ref={messagesEndRef} />

      </div>

      <div className="conversation-input">

        <FiMessageSquare />

        <input
          type="text"
          placeholder="Enter command..."
          value={input}
          onChange={(event) => setInput(event.target.value)}
          onKeyDown={(event) => {
            if (event.key === 'Enter') {
              handleSend()
            }
          }}
        />

        <button
          onClick={handleSend}
          aria-label="Send command"
        >
          <FiSend />
        </button>

      </div>

    </aside>
  )
}

export default ConversationPanel