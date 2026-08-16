import "./styles/SystemPanel.css"
import {
  FiCpu,
  FiHardDrive,
  FiClock,
  FiCloud,
  FiCamera,
} from 'react-icons/fi'

function SystemPanel() {
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
            <strong>24%</strong>
          </div>
        </div>

        <div className="stat-card">
          <FiHardDrive />
          <div>
            <span className="stat-label">MEMORY</span>
            <strong>41%</strong>
          </div>
        </div>

        <div className="stat-card">
          <FiClock />
          <div>
            <span className="stat-label">UPTIME</span>
            <strong>02:41:18</strong>
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