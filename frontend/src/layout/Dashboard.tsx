import { useState } from 'react'

import Header from '../components/Header'
import SystemPanel from '../components/SystemPanel'
import JarvisCore from '../components/JarvisCore'
import ConversationPanel from '../components/ConversationPanel'
import ControlBar from '../components/ControlBar'

import type { JarvisState } from '../types/jarvis'

function Dashboard() {
  const [jarvisState, setJarvisState] = useState<JarvisState>('IDLE')

  return (
    <main className="dashboard">
      <Header />

      <section className="dashboard-content">
        <SystemPanel />

        <JarvisCore state={jarvisState} />

        <ConversationPanel />
      </section>

      <ControlBar
        state={jarvisState}
        onStateChange={setJarvisState}
      />
    </main>
  )
}

export default Dashboard