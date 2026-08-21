import * as Dialog from "@radix-ui/react-dialog"
import { FiSettings, FiX } from "react-icons/fi"
import "../styles/SettingsModal.css"
import VoiceSettings from "./sections/VoiceSettings"
import AISettings from "./sections/AISettings"
function SettingsModal() {
  return (
    <Dialog.Root>
      <Dialog.Trigger asChild>
        <button
          className="icon-button"
          aria-label="Configuración"
        >
          <FiSettings />
        </button>
      </Dialog.Trigger>

      <Dialog.Portal>
        <Dialog.Overlay className="settings-overlay" />

        <Dialog.Content className="settings-modal">
          <div className="settings-header">
            <Dialog.Title>
              JARVIS SETTINGS
            </Dialog.Title>

            <Dialog.Close asChild>
              <button
                className="settings-close"
                aria-label="Cerrar configuración"
              >
                <FiX />
              </button>
            </Dialog.Close>
          </div>

            <Dialog.Description className="settings-description">
                Configuración del asistente
            </Dialog.Description>

          <div className="settings-content">
            <VoiceSettings></VoiceSettings>
            <AISettings></AISettings>
          </div>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  )
}

export default SettingsModal