import "./styles/ControlBar.css"
import {
  FiMic,
  FiCommand,
  FiCamera,
  FiVolume2,
} from 'react-icons/fi'

import type { JarvisState } from '../types/jarvis'

interface ControlBarProps {
  state: JarvisState
  onStateChange: (state: JarvisState) => void
}

function ControlBar({ state, onStateChange }: ControlBarProps) {
  return (
    <footer className="control-bar">
      <button
        className={`control-button ${state === 'LISTENING' ? 'active' : ''}`}
        onClick={() => onStateChange('LISTENING')}
      >
        <FiMic />
        <span>MICROPHONE</span>
      </button>

      <button
        className={`control-button ${state === 'PROCESSING' ? 'active' : ''}`}
        onClick={() => onStateChange('PROCESSING')}
      >
        <FiCommand />
        <span>PROCESSING</span>
      </button>

      <button
        className={`control-button ${state === 'SPEAKING' ? 'active' : ''}`}
        onClick={() => onStateChange('SPEAKING')}
      >
        <FiVolume2 />
        <span>SPEAKING</span>
      </button>

      <button
        className={`control-button ${state === 'IDLE' ? 'active' : ''}`}
        onClick={() => onStateChange('IDLE')}
      >
        <FiCamera />
        <span>IDLE</span>
      </button>
    </footer>
  )
}

export default ControlBar