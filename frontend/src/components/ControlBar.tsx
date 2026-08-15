import {
  FiMic,
  FiCommand,
  FiCamera,
  FiVolume2,
} from 'react-icons/fi'

function ControlBar() {
  return (
    <footer className="control-bar">
      <button className="control-button active">
        <FiMic />
        <span>MICROPHONE</span>
      </button>

      <button className="control-button">
        <FiCommand />
        <span>KEYBOARD</span>
      </button>

      <button className="control-button">
        <FiCamera />
        <span>CAMERA</span>
      </button>

      <button className="control-button">
        <FiVolume2 />
        <span>VOICE</span>
      </button>
    </footer>
  )
}

export default ControlBar