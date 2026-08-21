import { useState } from "react"

function InterfaceSettings() {
  const [animations, setAnimations] = useState(true)
  const [soundEffects, setSoundEffects] = useState(true)

  return (
    <section className="settings-section">
      <div className="settings-section-title">
        INTERFACE
      </div>

      <div className="settings-option">
        <div>
          <span className="settings-option-name">
            Animations
          </span>

          <span className="settings-option-description">
            Enable interface transitions and visual effects
          </span>
        </div>

        <button
          className={`settings-switch ${
            animations ? "active" : ""
          }`}
          onClick={() => setAnimations(prev => !prev)}
        >
          {animations ? "ON" : "OFF"}
        </button>
      </div>

      <div className="settings-option">
        <div>
          <span className="settings-option-name">
            Sound effects
          </span>

          <span className="settings-option-description">
            Play interface sounds and system notifications
          </span>
        </div>

        <button
          className={`settings-switch ${
            soundEffects ? "active" : ""
          }`}
          onClick={() => setSoundEffects(prev => !prev)}
        >
          {soundEffects ? "ON" : "OFF"}
        </button>
      </div>
    </section>
  )
}

export default InterfaceSettings