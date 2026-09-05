import { useEffect, useState } from 'react'

import Header from '../components/Header'
import SystemPanel from '../components/SystemPanel'
import JarvisCore from '../components/JarvisCore'
import ConversationPanel from '../components/ConversationPanel'
import ControlBar from '../components/ControlBar'
import { SettingsProvider } from "../components/SettingsModal/SettingsContext"
import { jarvisService } from '../services/jarvis'

import type { JarvisState, Message, JarvisStatus } from '../types/jarvis'

import './Dashboard.css'


function Dashboard() {

  const [chatOpen, setChatOpen] = useState(true)
  const [systemOpen, setSystemOpen] = useState(true)

  const [jarvisState, setJarvisState] =
    useState<JarvisState>('IDLE')

  const [messages, setMessages] =
    useState<Message[]>([])

  
  const [status, setStatus] = useState<JarvisStatus>('OFFLINE')


  useEffect(() => {

    jarvisService.connect()

    const unsubscribe =
      jarvisService.subscribe((event) => {

        if (event.type === 'STATE_CHANGED') {
          
          console.log('Estado de Jarvis:', event.state)
          setJarvisState(event.state)

        }
        
        if (event.type === "JARVIS_STATUS"){
              setStatus(event.status)
        }

        if (event.type === 'USER_MESSAGE') {

          setMessages((currentMessages) => [
            ...currentMessages,
            event.message,
          ])

        }

        if (event.type === 'JARVIS_MESSAGE') {

          setMessages((currentMessages) => [
            ...currentMessages,
            event.message,
          ])

        }

        if (event.type === 'COMMAND_EXECUTED') {

          console.log(
            'Comando ejecutado:',
            event.command
          )

        }

      })


    return () => {

      unsubscribe()
      jarvisService.disconnect()

    }

  }, [])


  const handleSendMessage = (message: Message) => {

    setMessages((currentMessages) => [
      ...currentMessages,
      message,
    ])

  }


  return (
    <SettingsProvider>
      <main className="dashboard">

        <Header status={status}/>

        <section className={`dashboard-content
          ${!chatOpen ? 'chat-collapsed' : ''}
          ${!systemOpen ? 'system-collapsed' : ''}
        `}>

          <SystemPanel 
            isOpen={systemOpen}
            onToggle={() => setSystemOpen(current => !current)}
          />

          <JarvisCore
            state={jarvisState}
          />

          <ConversationPanel
            messages={messages}
            onSendMessage={handleSendMessage}
            isOpen={chatOpen}
            onToggle={() => setChatOpen(current => !current)}
          />

        </section>

        <ControlBar
          state={jarvisState}
          onStateChange={setJarvisState}
        />

      </main>
    </SettingsProvider>
  )
}

export default Dashboard