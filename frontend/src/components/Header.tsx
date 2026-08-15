import { FiSettings, FiWifi } from 'react-icons/fi'

function Header() {
  return (
    <header className="topbar">
      <div className="brand">
        J.A.R.V.I.S
      </div>

      <div className="system-status">
        <FiWifi className="status-icon" />
        <span className="status-dot" />
        ONLINE
      </div>

      <div className="topbar-right">
        <span>20:12</span>

        <button className="icon-button" aria-label="Configuración">
          <FiSettings />
        </button>
      </div>
    </header>
  )
}

export default Header