import Header from '../components/Header'
import SystemPanel from '../components/SystemPanel'
import JarvisCore from '../components/JarvisCore'
import ConversationPanel from '../components/ConversationPanel'

function Dashboard() {
  return (
    <main className="dashboard">
      <Header />

      <section className="dashboard-content">
        <SystemPanel />

        <JarvisCore />

        <ConversationPanel />
      </section>

      <footer className="control-bar">
        <button>MIC</button>
        <button>KEYBOARD</button>
        <button>CAMERA</button>
      </footer>
    </main>
  )
}

export default Dashboard