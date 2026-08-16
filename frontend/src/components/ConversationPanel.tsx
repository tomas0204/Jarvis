import { FiMessageSquare, FiSend } from 'react-icons/fi'
import type { Message } from "../types/jarvis"
import { useState } from "react"

function ConversationPanel() {

  const [messages, setMessages] = useState<Message[]>([
    {
      id: 1,
      sender: 'JARVIS',
      text: 'Good evening, sir. How can I assist you?',
    },
    {
      id: 2,
      sender: 'USER',
      text: 'What is the current system status?',
    },
    {
      id: 3,
      sender: 'JARVIS',
      text: 'All systems are operating normally.',
    },
  ])

  const [input, setInput] = useState('')

  const handleSend = () => {
    if (!input.trim()) return

    const newMessage: Message = {
      id: Date.now(),
      sender: 'USER',
      text: input,
    }

    setMessages((currentMessages) => [
      ...currentMessages,
      newMessage,
    ])

    setInput('')
  }

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
          </div>
        ))}
      </div>

      <div className="conversation-input">
        <FiMessageSquare />

        <input
          type="text"
          placeholder="Enter command..."
          value={input}
          onChange={(event) => setInput(event.target.value)}
        />

        <button onClick={handleSend} aria-label="Send command">
          <FiSend />
        </button>
      </div>
    </aside>
  )
}

export default ConversationPanel