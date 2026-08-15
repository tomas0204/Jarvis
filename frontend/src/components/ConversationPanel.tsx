import { FiMessageSquare, FiSend } from 'react-icons/fi'

function ConversationPanel() {
  return (
    <aside className="conversation-panel">
      <div className="panel-header">
        <span>CONVERSATION</span>
        <span className="panel-line" />
      </div>

      <div className="conversation-messages">
        <div className="message assistant-message">
          <span className="message-author">J.A.R.V.I.S</span>
          <p>Good evening. How may I assist you?</p>
        </div>

        <div className="message user-message">
          <span className="message-author">YOU</span>
          <p>Show me the system status.</p>
        </div>

        <div className="message assistant-message">
          <span className="message-author">J.A.R.V.I.S</span>
          <p>All systems are operating normally.</p>
        </div>
      </div>

      <div className="conversation-input">
        <FiMessageSquare />

        <input
          type="text"
          placeholder="Enter command..."
        />

        <button aria-label="Send command">
          <FiSend />
        </button>
      </div>
    </aside>
  )
}

export default ConversationPanel