
import * as Dialog from "@radix-ui/react-dialog"
import { FiSettings } from "react-icons/fi"
const SettingsModal = () => {
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
            <Dialog.Title className="settings-title">
                JARVIS SETTINGS
            </Dialog.Title>

            <Dialog.Description className="settings-description">
                Configuración del asistente
            </Dialog.Description>

            {/* Acá vamos a construir las opciones */}

            <Dialog.Close asChild>
                <button className="settings-close">
                Cerrar
                </button>
            </Dialog.Close>
            </Dialog.Content>
        </Dialog.Portal>
    </Dialog.Root>
  )
}

export default SettingsModal