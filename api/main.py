from fastapi import FastAPI
from faker import Faker
from api.langchain_mock import create_llm
from api.chats import Chats, ChatRequest, ChatResponse

fake = Faker()
llm = create_llm(fake)
app = FastAPI()
chats = Chats("qwen3:4b")


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/api/chat")
def chat(request: ChatRequest) -> ChatResponse:
    return chats.chat(request)
