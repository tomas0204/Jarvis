import { FiActivity } from 'react-icons/fi'

function JarvisCore() {
  return (
    <section className="core-panel">
      <div className="jarvis-core">
        <div className="core-ring core-ring-outer" />
        <div className="core-ring core-ring-middle" />
        <div className="core-ring core-ring-inner" />

        <div className="core-center">
          <FiActivity />
          <h6>J . A . R . V . I . S</h6>
          <small>STANDBY</small>
        </div>
      </div>

      <div className="core-status">
        <span className="status-dot" />
        SYSTEM STANDBY
      </div>
    </section>
  )
}

export default JarvisCore