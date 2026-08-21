function SystemSettings() {
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

        <button className="settings-switch">
          OFF
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

        <button className="settings-switch active">
          ON
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

        <button className="settings-switch active">
          ON
        </button>
      </div>
    </section>
  )
}

export default SystemSettings