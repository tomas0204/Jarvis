function Dashboard() {
    return (
        <main className="dashboard">
            <header className="topbar">
                <div className="brand">J.A.R.V.I.S</div>

                <div className="system-status">
                <span className="status-dot" />
                ONLINE
                </div>

                <div className="topbar-right">
                <span>20:12</span>
                <span>⚙</span>
                </div>
            </header>

            <section className="dashboard-content">
                <aside className="left-panel">
                <div className="panel-placeholder">SYSTEM</div>
                </aside>

                <section className="core-panel">
                <div className="core-placeholder">
                    <span>J.A.R.V.I.S</span>
                </div>
                </section>

                <aside className="right-panel">
                <div className="panel-placeholder">CONVERSATION</div>
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