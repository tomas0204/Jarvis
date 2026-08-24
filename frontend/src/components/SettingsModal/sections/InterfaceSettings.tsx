import { useSettings } from "../SettingsContext"

function InterfaceSettings() {
  const {settings, updateSetting} = useSettings()

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
              settings.animations ? "active" : ""
          }`}
          onClick={() =>
              updateSetting(
                "animations",
              !settings.animations
              )
          } 
          >
          {settings.animations ? "ON" : "OFF"}
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
              settings.soundEffects? "active" : ""
          }`}
          onClick={() =>
              updateSetting(
                "soundEffects",
              !settings.soundEffects
              )
          } 
          >
          {settings.soundEffects ? "ON" : "OFF"}
        </button>
      </div>
    </section>
  )
}

export default InterfaceSettings