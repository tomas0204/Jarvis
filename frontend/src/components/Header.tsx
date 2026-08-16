import { FiSettings, FiWifi } from 'react-icons/fi'
import useCurrentTime from '../hooks/useCurrentTime'

function Header() {
  const time = useCurrentTime()

  const formatedTime = time.toLocaleTimeString([], {
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
  })
  

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
        <span>{formatedTime}</span>

        <button className="icon-button" aria-label="Configuración">
          <FiSettings />
        </button>
      </div>
    </header>
  )
}

export default Header