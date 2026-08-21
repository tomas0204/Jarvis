function InterfaceSettings() {
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

        <button className="settings-switch active">
          ON
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

        <button className="settings-switch active">
          ON
        </button>
      </div>

      <div className="settings-option">
        <div>
          <span className="settings-option-name">
            Chat panel
          </span>

          <span className="settings-option-description">
            Show the conversation panel on the dashboard
          </span>
        </div>

        <button className="settings-switch active">
          ON
        </button>
      </div>

      <div className="settings-option">
        <div>
          <span className="settings-option-name">
            System panel
          </span>

          <span className="settings-option-description">
            Show system information on the dashboard
          </span>
        </div>

        <button className="settings-switch active">
          ON
        </button>
      </div>
    </section>
  )
}

export default InterfaceSettings