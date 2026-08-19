import psutil


class SystemMonitor:

    def get_cpu_usage(self) -> float:
        return psutil.cpu_percent(interval=0.5)

    def get_memory_usage(self) -> float:
        return psutil.virtual_memory().percent