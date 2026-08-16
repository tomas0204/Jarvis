import { FiActivity, FiMic, FiCpu, FiVolume2 } from 'react-icons/fi'
import type { JarvisState } from '../types/jarvis'

interface JarvisCoreProps {
  state: JarvisState
}

function JarvisCore({ state }: JarvisCoreProps) {
  const getStateIcon = () => {
    switch (state) {
      case 'LISTENING':
        return <FiMic />

      case 'PROCESSING':
        return <FiCpu />

      case 'SPEAKING':
        return <FiVolume2 />

      default:
        return <FiActivity />
    }
  }

  return (
    <section className={`core-panel state-${state.toLowerCase()}`}>
      <div className="jarvis-core">
        <div className="core-ring core-ring-outer" />
        <div className="core-ring core-ring-middle" />
        <div className="core-ring core-ring-inner" />

        <div className="core-center">
          {getStateIcon()}

          <span>J.A.R.V.I.S</span>

          <small>{state}</small>
        </div>
      </div>

      <div className="core-status">
        <span className="status-dot" />
        SYSTEM {state}
      </div>
    </section>
  )
}

export default JarvisCore