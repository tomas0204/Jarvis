import Header from '../components/Header'
import SystemPanel from '../components/SystemPanel'
import ConversationPanel from '../components/ConversationPanel'

function Dashboard() {
  return (
    <main className="dashboard">
      <Header />

      <section className="dashboard-content">
        <SystemPanel />

        <section className="core-panel">
          <div className="core-placeholder">
            <span>J.A.R.V.I.S</span>
          </div>
        </section>

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