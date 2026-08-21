function AISettings() {
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
          defaultValue="groq"
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
          defaultValue="llama"
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
            defaultValue="0.7"
          />

          <span>0.7</span>
        </div>
      </div>
    </section>
  )
}

export default AISettings