import "./styles/JarvisCore.css"
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

        <div className="core-radial">
          <span />
          <span />
          <span />
          <span />
          <span />
          <span />
          <span />
          <span />
        </div>

        <div className="core-orbit">
          <span className="orbit-point"></span>
          <span className="orbit-segment"></span>
          <span className="orbit-point"></span>
          <span className="orbit-segment"></span>
          <span className="orbit-point"></span>
          <span className="orbit-segment"></span>
          <span className="orbit-point"></span>
          <span className="orbit-segment"></span>
          <span className="orbit-point"></span>
          <span className="orbit-segment"></span>
          <span className="orbit-point"></span>
          <span className="orbit-segment"></span>
        </div>
        <div className="core-hud">

          <div className="hud-line hud-line-top" />
          <div className="hud-line hud-line-bottom" />

          <div className="hud-mark hud-mark-top" />
          <div className="hud-mark hud-mark-right" />
          <div className="hud-mark hud-mark-bottom" />
          <div className="hud-mark hud-mark-left" />
        </div>

        <div className="core-ring core-ring-outer" />
        <div className="core-ring core-ring-middle" />
        <div className="core-ring core-ring-inner" />

        <div className="core-center">
          
        </div>
      </div>
    </section>
  )
}

export default JarvisCore