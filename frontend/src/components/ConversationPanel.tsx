import "./styles/ConversationPanel.css"
import { FiMessageSquare, FiSend } from 'react-icons/fi'
import type { Message } from "../types/jarvis"
import { useState, useRef, useEffect } from "react"

interface ConversationPanelProps {
  messages: Message[]
  onSendMessage: (text: string) => void
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

  const handleSend = () => {
    if (!input.trim()) return

    onSendMessage(input.trim())

    setInput('')
  }

  const sender = (send: Message['sender']) => {
    if (send === "JARVIS") {
      return "message assistant-message message-author"
    }

    return "message user-message message-author"
  }

  return (
    <aside className="conversation-panel">
      <div className="panel-header">
        <span>CONVERSATION</span>
        <span className="panel-line" />
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
            if (event.key === "Enter") {
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