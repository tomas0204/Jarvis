import { FiMessageSquare, FiSend } from 'react-icons/fi'
import type { Message } from "../types/jarvis"
import { useState, useRef, useEffect } from "react"

function ConversationPanel() {

  const messagesEndRef = useRef<HTMLDivElement>(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({
      behavior: 'smooth',
    })
  }
  const [messages, setMessages] = useState<Message[]>([
    {
      id: 1,
      sender: 'JARVIS',
      text: 'Good evening, sir. How can I assist you?',
      timestamp: new Date()
    },
    {
      id: 2,
      sender: 'USER',
      text: 'What is the current system status?',
      timestamp: new Date()
    },
  ])

  const [input, setInput] = useState('')

  const handleSend = () => {
    if (!input.trim()) return

    const newMessage: Message = {
      id: Date.now(),
      sender: 'USER',
      text: input,
      timestamp: new Date()
    }

    setMessages((currentMessages) => [
      ...currentMessages,
      newMessage,
    ])

    setInput('')

    scrollToBottom()
  }

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: 'smooth',
    })
  }, [messages])

  const sender = (send: string) => {
    if (send == "JARVIS") {
      return "message assistant-message message-author"
    } else {
      return "message user-message message-author"
    }
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

        <button onClick={handleSend} aria-label="Send command">
          <FiSend />
        </button>
      </div>
    </aside>
  )
}

export default ConversationPanel