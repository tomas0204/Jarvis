import "./styles/SystemPanel.css"
import {
  FiCpu,
  FiHardDrive,
  FiClock,
  FiCloud,
  FiCamera,
  FiChevronLeft,
  FiChevronRight,
} from 'react-icons/fi'
import { useEffect, useState } from 'react'
import {
  systemService,
  type SystemInfo,
} from '../services/systemService'
import {
  weatherService,
  type WeatherStats
} from "../services/weatherService"
interface SystemPanelProps {
  isOpen: boolean
  onToggle: () => void
}
function SystemPanel({
  isOpen,
  onToggle,
}: SystemPanelProps) {

  const [systemInfo, setSystemInfo] =
    useState<SystemInfo | null>(null)

  const [weatherStats, setWeatherStats] =
    useState<WeatherStats | null>(null)


  useEffect(() => {

    const updateSystemInfo = async () => {

      try {
        const data =
          await systemService.getSystemInfo()

        setSystemInfo(current => ({
          cpu: data.cpu,
          memory: data.memory,
          uptime: current?.uptime ?? data.uptime,
        }))
      } catch (error) {

        console.error(
          'Error obteniendo información del sistema:',
          error
        )
      }
    }

    updateSystemInfo()

    const interval =
      setInterval(updateSystemInfo, 5000)

    return () => {
      clearInterval(interval)
    }

  }, [])

  useEffect(() => {

    if (!systemInfo) return
    const interval = setInterval(() => {
      setSystemInfo(current => {
        if (!current) return current
        const [hours, minutes, seconds] =
          current.uptime
            .split(':')
            .map(Number)

        let totalSeconds =
          hours * 3600 +
          minutes * 60 +
          seconds +
          1

        const newHours =
          Math.floor(totalSeconds / 3600)

        totalSeconds %= 3600

        const newMinutes =
          Math.floor(totalSeconds / 60)

        const newSeconds =
          totalSeconds % 60

        return {
          ...current,

          uptime: `${String(newHours).padStart(2, '0')}:${String(
            newMinutes
          ).padStart(2, '0')}:${String(
            newSeconds
          ).padStart(2, '0')}`,
        }

      })

    }, 1000)

    return () => {
      clearInterval(interval)
    }

  }, [systemInfo])


  useEffect(() => {
    const updateWeather = async () => {
      try {
        const data =
          await weatherService.getWeatherinfo()

        setWeatherStats(data)

      } catch (error) {

        console.error(
          'Error obteniendo información del clima:',
          error
        )
      }
    }
    updateWeather()
    const interval =
      setInterval(updateWeather, 600000)
    return () => {
      clearInterval(interval)
    }
  }, [])
  return (
    <aside
      className={`system-panel ${
        isOpen ? '' : 'collapsed'
      }`}
    >
      <div className="panel-header">
        <span>SYSTEM</span>
        <span className="panel-line" />
        <button
          className="panel-toggle"
          onClick={onToggle}
          aria-label={
            isOpen
              ? 'Collapse system panel'
              : 'Open system panel'
          }
        >
          {isOpen
            ? <FiChevronLeft />
            : <FiChevronRight />
          }
        </button>
      </div>
      <div className="system-stats">
        <div className="stat-card">
          <FiCpu />
          <div>
            <span className="stat-label">
              CPU
            </span>
            {systemInfo
              ? `${systemInfo.cpu}%`
              : '--'}
          </div>
        </div>
        <div className="stat-card">
          <FiHardDrive />
          <div>
            <span className="stat-label">
              MEMORY
            </span>
            {systemInfo
              ? `${systemInfo.memory}%`
              : '--'}
          </div>
        </div>
        <div className="stat-card">
          <FiClock />
          <div>
            <span className="stat-label">
              UPTIME
            </span>
            {systemInfo
              ? systemInfo.uptime
              : '--:--:--'}
          </div>
        </div>
      </div>
      <div className="system-section">
        <div className="section-title">
          <FiCloud />
          WEATHER
        </div>
        <div className="weather">
          <strong>
            {weatherStats
              ? `${weatherStats.temperature}°C`
              : '--°C'}
          </strong>
          <span>
            {weatherStats
              ? weatherStats.description
              : '--'}
          </span>
        </div>
      </div>
      <div className="system-section">
        <div className="section-title">
          <FiCamera />
          CAMERA
        </div>
        <div className="camera-status">
          <span className="status-dot" />
          OFF
        </div>
      </div>
    </aside>
  )
}

export default SystemPanel