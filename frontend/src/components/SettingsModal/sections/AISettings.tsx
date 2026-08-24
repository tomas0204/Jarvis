import { useSettings } from "../SettingsContext"

function AISettings() {
  const {settings, updateSetting} = useSettings()
  return (
    <section className="settings-section">
      <div className="settings-section-title">
        ARTIFICIAL INTELLIGENCE
      </div>

      <div className="settings-option">
        <div>
          <span className="settings-option-name">
            Provider
          </span>

          <span className="settings-option-description">
            AI service used by Jarvis
          </span>
        </div>

        <select
          className="settings-select"
          value={settings.provider}
          onChange={(event) =>
            updateSetting(
              "provider",
              event.target.value
            )
          }
        >
          <option value="groq">GROQ</option>
        </select>
      </div>

      <div className="settings-option">
        <div>
          <span className="settings-option-name">
            Model
          </span>

          <span className="settings-option-description">
            Language model used for conversations
          </span>
        </div>

        <select
          className="settings-select"
          value={settings.model}
          onChange={(event) =>{
            updateSetting(
              "model",
              event.target.value
            )
          }}
        >
          <option value="llama">
            LLAMA
          </option>
        </select>
      </div>

      <div className="settings-option">
        <div>
          <span className="settings-option-name">
            Temperature
          </span>

          <span className="settings-option-description">
            Controls response creativity
          </span>
        </div>

        <div className="settings-range">
          <input
            type="range"
            min="0"
            max="2"
            step="0.1"
            value={settings.temperature}
            onChange={(event) =>
              updateSetting(
                "temperature",
                Number(event.target.value)
              )
            }
          />

          <span>{settings.temperature.toFixed(1)}</span>
        </div>
      </div>
    </section>
  )
}

export default AISettings