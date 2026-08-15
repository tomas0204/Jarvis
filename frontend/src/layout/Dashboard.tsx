import Header from '../components/Header'
import SystemPanel from '../components/SystemPanel'
import JarvisCore from '../components/JarvisCore'
import ConversationPanel from '../components/ConversationPanel'
import ControlBar from '../components/ControlBar'

function Dashboard() {
  return (
    <main className="dashboard">
      <Header />

      <section className="dashboard-content">
        <SystemPanel />
        <JarvisCore />
        <ConversationPanel />
      </section>

      <ControlBar />
    </main>
  )
}

export default Dashboard