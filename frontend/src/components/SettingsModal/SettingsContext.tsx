import {
  createContext,
  useContext,
  useState,
  type ReactNode,
} from "react"

interface JarvisSettings {
  voiceResponses: boolean
  language: string
  speechRate: number

  provider: string
  model: string
  temperature: number

  startWithWindows: boolean
  confirmActions: boolean
  voiceActivation: boolean

  animations: boolean
  soundEffects: boolean
}

interface SettingsContextType {
  settings: JarvisSettings
  updateSetting: <K extends keyof JarvisSettings>(
    key: K,
    value: JarvisSettings[K]
  ) => void
}

const defaultSettings: JarvisSettings = {
  voiceResponses: true,
  language: "es-AR",
  speechRate: 1,

  provider: "groq",
  model: "llama",
  temperature: 0.7,

  startWithWindows: false,
  confirmActions: true,
  voiceActivation: true,

  animations: true,
  soundEffects: true,
}

const SettingsContext = createContext<
  SettingsContextType | undefined
>(undefined)

interface SettingsProviderProps {
  children: ReactNode
}

export function SettingsProvider({
  children,
}: SettingsProviderProps) {
  const [settings, setSettings] =
    useState<JarvisSettings>(defaultSettings)

  const updateSetting = <
    K extends keyof JarvisSettings
  >(
    key: K,
    value: JarvisSettings[K]
  ) => {
    setSettings((current) => ({
      ...current,
      [key]: value,
    }))
  }

  return (
    <SettingsContext.Provider
      value={{
        settings,
        updateSetting,
      }}
    >
      {children}
    </SettingsContext.Provider>
  )
}

export function useSettings() {
  const context = useContext(SettingsContext)

  if (!context) {
    throw new Error(
      "useSettings must be used inside SettingsProvider"
    )
  }

  return context
}