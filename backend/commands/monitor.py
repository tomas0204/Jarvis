import psutil


class SystemMonitor:

    def get_cpu_usage(self) -> float:
        return psutil.cpu_percent(interval=0.5)