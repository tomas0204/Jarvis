import "./styles/SystemPanel.css"
import {
  FiCpu,
  FiHardDrive,
  FiClock,
  FiCloud,
  FiCamera,
} from 'react-icons/fi'
import { useEffect, useState } from 'react'
import {
          systemService,
          type SystemInfo,
        } from '../services/systemService'

function SystemPanel() {
  const [systemInfo, setSystemInfo] = useState<SystemInfo | null>(null)
  useEffect(() => {

    const updateSystemInfo = async () => {
      try {
        const data = await systemService.getSystemInfo()
        setSystemInfo(data)
      } catch (error) {
        console.error('Error obteniendo información del sistema:', error)
      }
    }

    updateSystemInfo()

    const interval = setInterval(updateSystemInfo, 5000)

    return () => {
      clearInterval(interval)
    }

  }, [])
  return (
    <aside className="system-panel">
      <div className="panel-header">
        <span>SYSTEM</span>
        <span className="panel-line" />
      </div>

      <div className="system-stats">
        <div className="stat-card">
          <FiCpu />
          <div>
            <span className="stat-label">CPU</span>
            {systemInfo ? `${systemInfo.cpu}%` : '--'}
          </div>
        </div>

        <div className="stat-card">
          <FiHardDrive />
          <div>
            <span className="stat-label">MEMORY</span>
            {systemInfo ? `${systemInfo.memory}%` : '--'}
          </div>
        </div>

        <div className="stat-card">
          <FiClock />
          <div>
            <span className="stat-label">UPTIME</span>
            {systemInfo ? `${systemInfo.uptime}` : '--:--:--'}
          </div>
        </div>
      </div>

      <div className="system-section">
        <div className="section-title">
          <FiCloud />
          WEATHER
        </div>

        <div className="weather">
          <strong>24°C</strong>
          <span>Clear Sky</span>
        </div>
      </div>

      <div className="system-section">
        <div className="section-title">
          <FiCamera />
          CAMERA
        </div>

        <div className="camera-status">
          <span className="status-dot" />
          READY
        </div>
      </div>
    </aside>
  )
}

export default SystemPanel