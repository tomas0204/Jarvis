import { FiSettings, FiWifi } from 'react-icons/fi'
import useCurrentTime from '../hooks/useCurrentTime'
import './styles/Header.css'
import type { JarvisStatus } from '../types/jarvis'

interface HeaderProps {
  status: JarvisStatus
}

function Header({ status }: HeaderProps) {
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

      <div
        className={`system-status ${status.toLowerCase()}`}
        title={ 
          status === 'ONLINE'
            ? 'Voice activo. Jarvis está escuchando.'
            : 'Voice inactivo. Di "Jarvis" para activarlo.'
        }
      >
        <span className="status-dot" />
        {status}
      </div>

      <div className="topbar-right">
        <span>{formatedTime}</span>

        <button
          className="icon-button"
          aria-label="Configuración"
        >
          <FiSettings />
        </button>
      </div>
    </header>
  )
}

export default Header
