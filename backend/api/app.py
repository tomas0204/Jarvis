from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MessageRequest(BaseModel):
    text: str
    
@app.post("/api/message")
def send_message(message: MessageRequest):
    return {
        "response": f"Recibí: {message.text}"
    }