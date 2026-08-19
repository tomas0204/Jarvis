import asyncio

from contextlib import asynccontextmanager
from threading import Thread

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from backend.core.assistant import Assistant
from backend.core.event_bus import event_queue


assistant = Assistant()
connected_clients: list[WebSocket] = []


async def broadcast_event(event: dict):
    disconnected = []

    for websocket in connected_clients:
        try:
            await websocket.send_json(event)

        except Exception:
            disconnected.append(websocket)

    for websocket in disconnected:
        if websocket in connected_clients:
            connected_clients.remove(websocket)


async def event_listener():
    while True:
        event = await asyncio.to_thread(event_queue.get)
        
        print(f"[EVENT] {event}")

        await broadcast_event(event)


@asynccontextmanager
async def lifespan(app: FastAPI):

    voice_thread = Thread(
        target=assistant.run,
        daemon=True
    )

    voice_thread.start()

    asyncio.create_task(event_listener())

    yield


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MessageRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {"message": "Jarvis API funcionando"}


@app.post("/api/message")
def send_message(message: MessageRequest):
    return assistant.process(
        message.text,
        source="web"
    )
@app.websocket("/ws/jarvis")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    connected_clients.append(websocket)

    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:

        if websocket in connected_clients:
            connected_clients.remove(websocket)