import { useState } from 'react'
import Header from '../components/Header'
import SystemPanel from '../components/SystemPanel'
import JarvisCore from '../components/JarvisCore'
import ConversationPanel from '../components/ConversationPanel'
import ControlBar from '../components/ControlBar'
import './Dashboard.css'

import type { JarvisState, Message } from '../types/jarvis'

function Dashboard() {
  const [jarvisState, setJarvisState] = useState<JarvisState>('IDLE')

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

  const handleSendMessage = (text: string) => {
    const newMessage: Message = {
      id: Date.now(),
      sender: 'USER',
      text,
      timestamp: new Date()
    }

    setMessages((currentMessages) => [
      ...currentMessages,
      newMessage,
    ])
  }

  return (
    <main className="dashboard">
      <Header />

      <section className="dashboard-content">
        <SystemPanel />

        <JarvisCore state={jarvisState} />

        <ConversationPanel
          messages={messages}
          onSendMessage={handleSendMessage}
        />
      </section>

      <ControlBar
        state={jarvisState}
        onStateChange={setJarvisState}
      />
    </main>
  )
}

export default Dashboard