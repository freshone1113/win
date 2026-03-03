from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.language_models import BaseChatModel
from pydantic import BaseModel


class ChatMessage(BaseModel):
    type: str
    timestamp: str
    content: str


class ChatRequest(BaseModel):
    messages: list[ChatMessage]


class ChatResponse(BaseModel):
    content: str


class Chats:
    def __init__(self, llm: BaseChatModel) -> None:
        self.llm = llm

    def parseMessages(self, msgs: list[ChatMessage]):
        lc_msgs = []

        for msg in msgs:
            lc_msg = None
            if msg.type == 'SystemMessage':
                lc_msg = SystemMessage(msg.content)
            elif msg.type == 'HumanMessage':
                lc_msg = HumanMessage(msg.content)
            elif msg.type == 'AIMessage':
                lc_msg = AIMessage(msg.content)
            else:
                raise ValueError(f'unknown message type {msg.type}')

            lc_msgs.append(lc_msg)

        return lc_msgs

    def chat(self, request: ChatRequest):
        msgs = self.parseMessages(request.messages)
        lc_response = self.llm.invoke(msgs)
        response = None

        if type(lc_response.content) is str:
            response = ChatResponse(content=lc_response.content)
        else:
            raise ValueError(f'undefined message content type')

        return response
