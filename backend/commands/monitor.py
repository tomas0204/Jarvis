import time

import psutil


class SystemMonitor:

    def get_cpu_usage(self) -> float:
        return psutil.cpu_percent(interval=0.5)

    def get_memory_usage(self) -> float:
        return psutil.virtual_memory().percent

    def get_uptime(self) -> str:
        seconds = int(time.time() - psutil.boot_time())

        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return f"{hours:02}:{minutes:02}:{seconds:02}"