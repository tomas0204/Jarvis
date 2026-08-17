from fastapi                    import FastAPI
from pydantic                   import BaseModel

from backend.core.assistant     import Assistant
from fastapi.middleware.cors    import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

assistant = Assistant()


class MessageRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {"message": "Jarvis API funcionando"}


@app.post("/api/message")
def send_message(message: MessageRequest):
    return assistant.process(message.text)