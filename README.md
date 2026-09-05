# JARVIS

> 🤖 Asistente virtual inteligente inspirado en J.A.R.V.I.S. de Iron Man.

JARVIS es un asistente virtual de escritorio desarrollado con **Python, FastAPI, React, TypeScript y Tauri**, diseñado para interactuar mediante voz y lenguaje natural.

El proyecto combina **inteligencia artificial, reconocimiento de voz, síntesis de voz, automatización del sistema, visión artificial y comunicación en tiempo real** para crear un asistente capaz de comprender instrucciones y ejecutar acciones en el equipo.

🚧 **Estado:** En desarrollo activo.

---

## ✨ Características

Actualmente JARVIS cuenta con:

* 🎙️ Reconocimiento de voz.
* 🧠 Interpretación de intenciones.
* 🤖 Conversación mediante modelos LLM.
* 👁️ Análisis visual de la pantalla mediante IA.
* 🔊 Síntesis de voz.
* 🌐 Búsquedas web.
* 🖥️ Apertura de aplicaciones y sitios web.
* 🔈 Control del volumen del sistema.
* 🎵 Control multimedia.
* 🔌 Comunicación en tiempo real mediante WebSocket.
* 🖥️ Interfaz gráfica desarrollada con React.
* 🪟 Aplicación de escritorio mediante Tauri.
* 🟢 Sistema de estados y disponibilidad de JARVIS.
* 🔑 Activación mediante Wake Word.

---

# 🛠️ Comandos disponibles

## 🔥 Control del sistema

### Volumen

JARVIS puede controlar el volumen del sistema mediante comandos de voz:

* `"sube el volumen"`
* `"baja el volumen"`
* `"pon el volumen al 50%"`
* `"silencia el sistema"`

### Multimedia

Actualmente están implementados:

* `"pausa la música"`
* `"reanuda la música"`

> 🚧 Próximamente: siguiente canción, canción anterior y otros controles multimedia.

---

## 🌐 Web

### Buscar en Google

JARVIS puede realizar búsquedas utilizando lenguaje natural:

* `"busca cómo instalar Docker"`
* `"googlea cuánto mide..."`

### Abrir sitios web

Puede abrir sitios previamente configurados mediante comandos de voz:

* `"abre YouTube"`
* `"abre GitHub"`
* `"abre Gmail"`
* `"abre ChatGPT"`

---

## 👁️ Visión artificial

JARVIS puede capturar la pantalla y enviarla a un modelo de visión para analizar su contenido.

Ejemplo:

> `"¿qué estoy mirando en pantalla?"`

El flujo es:

```text
Comando de voz
      ↓
Detección de intención
      ↓
Captura de pantalla
      ↓
Modelo de visión
      ↓
Análisis
      ↓
Respuesta de JARVIS
      ↓
Síntesis de voz
```

Las capturas utilizadas para el análisis se mantienen **en memoria durante el proceso y no se guardan como archivos en el disco**.

---

# 🧠 Inteligencia artificial

JARVIS utiliza modelos externos de IA para las tareas que requieren procesamiento de lenguaje y visión.

Actualmente el proyecto utiliza **Groq** como proveedor de modelos.

La arquitectura permite separar la lógica del asistente de los proveedores de IA, facilitando futuras modificaciones o incorporación de nuevos modelos.

---

# 🏗️ Arquitectura

La aplicación está dividida principalmente en un frontend de escritorio y un backend encargado de la lógica del asistente.

```text
┌─────────────────────────────┐
│        React + TypeScript   │
│          Interfaz UI        │
└──────────────┬──────────────┘
               │
               │ WebSocket
               │
┌──────────────▼──────────────┐
│           FastAPI           │
│        API + WebSocket      │
└──────────────┬──────────────┘
               │
┌──────────────▼──────────────┐
│        JARVIS CORE          │
│                             │
│  Assistant                  │
│  Intent                     │
│  Command Registry           │
│  Event Bus                  │
│  Memory                     │
└───────┬──────────┬──────────┘
        │          │
        │          │
┌───────▼─────┐ ┌──▼──────────┐
│  Commands   │ │     AI      │
│             │ │             │
│ Sistema     │ │ LLM         │
│ Multimedia  │ │ Vision      │
│ Web         │ │ Groq        │
│ Aplicaciones│ └─────────────┘
└─────────────┘
```

La aplicación de escritorio utiliza **Tauri** como capa nativa sobre el frontend.

---

# 📁 Estructura del proyecto

La estructura principal del backend está organizada por responsabilidades:

```text
backend/
│
├── ai/
│   ├── llm.py
│   ├── vision.py
│   └── providers/
│       └── groq.py
│
├── api/
│
├── commands/
│   ├── applications/
│   ├── automation/
│   ├── files/
│   ├── media/
│   ├── system/
│   ├── system_info/
│   ├── web/
│   ├── configuration/
│   ├── registry.py
│   └── setup.py
│
├── core/
│   ├── assistant.py
│   ├── intent.py
│   ├── memory.py
│   └── events/
│
├── integrations/
│
├── utils/
│   └── logger.py
│
└── voice/
    ├── speech_to_text.py
    └── text_to_speech.py
```

El frontend contiene los componentes de la interfaz y la comunicación con el backend:

```text
frontend/
│
├── components/
│   ├── Header
│   ├── SystemPanel
│   ├── JarvisCore
│   ├── ConversationPanel
│   └── ControlBar
│
└── services/
    └── jarvisService
```

---

# ⚙️ Tecnologías

### Backend

* **Python**
* **FastAPI**
* **WebSocket**
* **Speech Recognition**
* **Google Speech-to-Text**
* **Groq API**

### Frontend

* **React**
* **TypeScript**
* **CSS**

### Desktop

* **Tauri**
* **Rust**

### Inteligencia artificial

* LLM mediante Groq
* Modelos de visión mediante Groq
* Procesamiento de lenguaje natural
* Análisis de imágenes

---

# 🚀 Instalación

## Requisitos

Antes de comenzar necesitas tener instalado:

* Python 3.13+
* Node.js
* npm
* Rust
* Cargo
* Tauri CLI

Puedes comprobar las instalaciones con:

```bash
python --version
node --version
npm --version
rustc --version
cargo --version
```

---

## 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/Jarvis.git
cd Jarvis
```

> Reemplaza `TU_USUARIO` por tu usuario de GitHub.

---

## 2. Crear el entorno virtual

Desde la carpeta del proyecto:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows:

```powershell
.venv\Scripts\activate
```

---

## 3. Instalar dependencias del backend

```bash
pip install -r requirements.txt
```

### Instalar dependencias del frontend

Desde la carpeta `frontend`:

```bash
cd frontend
npm install
```


---

## 4. Configurar las variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
GROQ_API_KEY=tu_api_key
```

La API Key es necesaria para las funciones de inteligencia artificial.

⚠️ **Nunca subas tu archivo `.env` a GitHub.**

Asegúrate de incluirlo en `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
```

---

# ▶️ Ejecutar JARVIS

## Backend

Con el entorno virtual activado:

```bash
uvicorn backend.main:app --reload
```

El backend quedará disponible localmente.

---

## Frontend

En otra terminal:

```bash
npm install
npm run dev
```

La interfaz estará disponible en:

```text
http://localhost:5173
```

---

# 🖥️ Ejecutar como aplicación de escritorio

Una vez configurado Tauri:

```bash
npm run tauri dev
```

Esto inicia JARVIS como una aplicación de escritorio durante el desarrollo.

---

# 🔐 Seguridad

JARVIS utiliza servicios externos para determinadas funciones de inteligencia artificial.

Las credenciales y API Keys deben almacenarse mediante variables de entorno.

Nunca deben incluirse directamente en el código fuente ni subirse al repositorio.

---

# 🗺️ Roadmap

JARVIS continúa en desarrollo. Las siguientes funcionalidades forman parte del roadmap del proyecto.

## 🔥 Prioridad alta

### Control multimedia

* [ ] Siguiente canción
* [ ] Canción anterior

### Control de ventanas

* [ ] Minimizar todo
* [ ] Maximizar ventana
* [ ] Cerrar ventana

### Capturas de pantalla

* [ ] `"haz una captura"`
* [x] `"analiza lo que hay en pantalla"`

### Portapapeles

* [ ] Copiar contenido
* [ ] Limpiar portapapeles
* [ ] Leer portapapeles

### Energía del sistema

* [ ] Bloquear PC
* [ ] Reiniciar equipo
* [ ] Apagar equipo

---

# 🧠 Prioridad media

## Archivos

* [ ] Abrir documentos
* [ ] Buscar archivos
* [ ] Crear carpetas
* [ ] Abrir Descargas

## Procesos

* [ ] Mostrar programas ejecutándose
* [ ] Cerrar procesos/aplicaciones
* [ ] Consultar uso de RAM

## Información del sistema

* [ ] Consultar RAM instalada
* [ ] Consultar procesador
* [ ] Consultar tarjeta gráfica
* [ ] Consultar almacenamiento disponible

## Temporizadores

* [ ] Temporizadores
* [ ] Avisos programados

## Recordatorios

* [ ] Recordatorios por hora
* [ ] Recordatorios por fecha

## Notas rápidas

* [ ] Crear notas
* [ ] Guardar notas
* [ ] Consultar notas

Estas funcionalidades permitirán aprovechar progresivamente el sistema de memoria de JARVIS.

---

# 🚀 Futuras funcionalidades

## Rutinas

La idea es permitir comandos como:

```text
"modo programación"
"modo trabajo"
"modo gaming"
```

Por ejemplo:

```text
Modo programación
      ↓
Abrir VS Code
      ↓
Abrir Chrome
      ↓
Abrir Spotify
      ↓
Abrir proyecto
      ↓
Abrir terminal
      ↓
Consultar información del sistema
```

---

## 📊 Información avanzada del sistema

JARVIS podrá responder preguntas como:

```text
"¿qué está consumiendo CPU?"
"¿qué proceso consume más memoria?"
"¿cuánto tiempo lleva encendido?"
```

---

## 🧠 Historial y memoria

Se busca permitir conversaciones más contextuales:

```text
"¿qué te pregunté antes?"
"¿qué comandos ejecuté hoy?"
```

Esto permitirá aprovechar el sistema de memoria de JARVIS para conservar contexto relevante.

---

## ⚠️ Confirmaciones

Para acciones potencialmente destructivas:

```text
Usuario:
"apaga el PC"

JARVIS:
"¿Confirmas que quieres apagar el equipo?"

Usuario:
"sí"

JARVIS:
"De acuerdo."
```

---

## 🔗 Comandos encadenados

Una de las funcionalidades más importantes del roadmap será permitir múltiples acciones dentro de una misma instrucción:

```text
"abre Chrome y busca GitHub"
```

JARVIS deberá interpretar la intención compuesta y ejecutar las acciones correspondientes en orden.

---

## 🗣️ Alias naturales

El objetivo es que diferentes expresiones produzcan la misma intención.

Por ejemplo:

```text
"abre Chrome"
"ejecuta Chrome"
"inicia Chrome"
"pon Chrome"
```

Todas deberían terminar ejecutando:

```text
open_application("Chrome")
```

Esto permitirá que la interacción sea más natural y menos dependiente de comandos rígidos.

---

# 🎯 Objetivo del proyecto

El objetivo de JARVIS no es simplemente crear un chatbot con voz.

La meta es construir un **asistente de escritorio capaz de comprender lenguaje natural, interactuar con el sistema operativo, utilizar herramientas, analizar información visual y ejecutar acciones de manera autónoma y contextual**.

El proyecto está siendo desarrollado progresivamente, priorizando una arquitectura modular que permita agregar nuevas capacidades sin tener que modificar el núcleo del asistente.

---

# 🚧 Estado actual

JARVIS se encuentra actualmente en **desarrollo activo**.

Las funcionalidades pueden cambiar, reorganizarse o ser reemplazadas a medida que evoluciona la arquitectura.

Por este motivo, actualmente no existe una versión estable de producción.

Las instrucciones de instalación están orientadas principalmente a desarrolladores que quieran ejecutar el proyecto durante su etapa de desarrollo.

---

# 📸 Demo

> Próximamente se agregará una demostración del funcionamiento de JARVIS mediante capturas de pantalla, GIFs o vídeo.

---

# 📌 Próximos objetivos

El desarrollo continuará principalmente en estas áreas:

1. Expandir el sistema de comandos.
2. Mejorar la interpretación de lenguaje natural.
3. Ampliar el sistema de memoria.
4. Incorporar automatizaciones y rutinas.
5. Mejorar la interacción mediante voz.
6. Implementar confirmaciones para acciones sensibles.
7. Incorporar comandos encadenados.
8. Mejorar la aplicación de escritorio.
9. Preparar una versión distribuible.
10. Llegar eventualmente a una primera versión estable.

---

## 📄 Licencia

Este proyecto se encuentra actualmente en desarrollo.

La licencia definitiva será definida antes de la primera versión estable.

---

## 👨‍💻 Autor

Desarrollado como proyecto personal de aprendizaje y portfolio.

**JARVIS — Intelligent Desktop Assistant**

> *"Your personal AI assistant."*
