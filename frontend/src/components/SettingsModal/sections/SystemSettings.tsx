import { useState } from "react"
import { useSettings } from "../SettingsContext"

function SystemSettings() {
  const [startWithWindows, setStartWithWindows] = useState(false)
  const [confirmActions, setConfirmActions] = useState(true)
  const [voiceActivation, setVoiceActivation] = useState(true)
  const { settings, updateSetting } = useSettings()

  return (
    <section className="settings-section">
      <div className="settings-section-title">
        SYSTEM
      </div>

      <div className="settings-option">
        <div>
          <span className="settings-option-name">
            Start with Windows
          </span>

          <span className="settings-option-description">
            Launch Jarvis automatically when Windows starts
          </span>
        </div>

        <button
        className={`settings-switch ${
            settings.startWithWindows ? "active" : ""
        }`}
        onClick={() =>
            updateSetting(
              "startWithWindows",
            !settings.startWithWindows
            )
        } 
        >
        {settings.startWithWindows ? "ON" : "OFF"}
        </button>
      </div>

      <div className="settings-option">
        <div>
          <span className="settings-option-name">
            Confirm actions
          </span>

          <span className="settings-option-description">
            Ask for confirmation before executing sensitive commands
          </span>
        </div>

        <button
        className={`settings-switch ${
            settings.confirmActions ? "active" : ""
        }`}
        onClick={() =>
            updateSetting(
              "confirmActions",
            !settings.confirmActions
            )
        } 
        >
        {settings.confirmActions ? "ON" : "OFF"}
        </button>
      </div>

      <div className="settings-option">
        <div>
          <span className="settings-option-name">
            Voice activation
          </span>

          <span className="settings-option-description">
            Allow Jarvis to receive commands through the microphone
          </span>
        </div>

        <button
        className={`settings-switch ${
            settings.voiceActivation ? "active" : ""
        }`}
        onClick={() =>
            updateSetting(
              "voiceActivation",
            !settings.voiceActivation
            )
        } 
        >
        {settings.voiceActivation ? "ON" : "OFF"}
        </button>
      </div>
    </section>
  )
}

export default SystemSettings