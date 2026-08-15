from core.intent import Intent

intent = Intent()

print(intent.detect("Jarvis busca Python"))
print(intent.detect("Jarvis busca gatos en YouTube"))
print(intent.detect("Jarvis abre YouTube"))
print(intent.detect("Jarvis abre GitHub"))