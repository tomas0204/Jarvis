from fastapi import FastAPI
from pydantic import BaseModel

from backend.core.assistant import Assistant


app = FastAPI()

assistant = Assistant()


class MessageRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {"message": "Jarvis API funcionando"}


@app.post("/api/message")
def send_message(message: MessageRequest):
    return assistant.process(message.text)