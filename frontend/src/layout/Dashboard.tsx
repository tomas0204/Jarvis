import { useEffect, useState } from 'react'

import Header from '../components/Header'
import SystemPanel from '../components/SystemPanel'
import JarvisCore from '../components/JarvisCore'
import ConversationPanel from '../components/ConversationPanel'
import ControlBar from '../components/ControlBar'

import { jarvisService } from '../services/jarvis'

import type { JarvisState, Message } from '../types/jarvis'

import './Dashboard.css'


function Dashboard() {

  const [jarvisState, setJarvisState] =
    useState<JarvisState>('IDLE')

  const [messages, setMessages] =
    useState<Message[]>([])


  useEffect(() => {

    jarvisService.connect()

    const unsubscribe =
      jarvisService.subscribe((event) => {

        // Estos eventos solamente vienen
        // del backend por WebSocket.
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
    <main className="dashboard">

      <Header />

      <section className="dashboard-content">

        <SystemPanel />

        <JarvisCore
          state={jarvisState}
        />

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