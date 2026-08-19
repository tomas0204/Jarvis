from backend.commands.monitor import SystemMonitor

monitor = SystemMonitor()

print(monitor.get_cpu_usage())
print(monitor.get_memory_usage())
