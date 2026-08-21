import { useState } from "react"

function VoiceSettings() {
  const [voiceResponses, setVoiceResponses] = useState(true)

  return (
    <section className="settings-section">
      <div className="settings-section-title">
        VOICE
      </div>

      <div className="settings-option">
        <div>
          <span className="settings-option-name">
            Voice responses
          </span>

          <span className="settings-option-description">
            Jarvis responds using text-to-speech
          </span>
        </div>

        <button
          className={`settings-switch ${
            voiceResponses ? "active" : ""
          }`}
          onClick={() => setVoiceResponses(prev => !prev)}
        >
          {voiceResponses ? "ON" : "OFF"}
        </button>
      </div>

      <div className="settings-option">
        <div>
          <span className="settings-option-name">
            Language
          </span>

          <span className="settings-option-description">
            Language used for voice interaction
          </span>
        </div>

        <select
          className="settings-select"
          defaultValue="en-US"
        >
          <option value="en-US">ENGLISH</option>
          <option value="es-AR">ESPAÑOL</option>
        </select>
      </div>

      <div className="settings-option">
        <div>
          <span className="settings-option-name">
            Speech rate
          </span>

          <span className="settings-option-description">
            Adjust Jarvis speaking speed
          </span>
        </div>

        <div className="settings-range">
          <input
            type="range"
            min="0.5"
            max="2"
            step="0.1"
            defaultValue="1"
          />

          <span>1.0x</span>
        </div>
      </div>
    </section>
  )
}

export default VoiceSettings