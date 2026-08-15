import Header from '../components/Header'

function Dashboard() {
  return (
    <main className="dashboard">
      <Header />

      <section className="dashboard-content">
        <aside className="left-panel">
          <div className="panel-placeholder">
            SYSTEM
          </div>
        </aside>

        <section className="core-panel">
          <div className="core-placeholder">
            <span>J.A.R.V.I.S</span>
          </div>
        </section>

        <aside className="right-panel">
          <div className="panel-placeholder">
            CONVERSATION
          </div>
        </aside>
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