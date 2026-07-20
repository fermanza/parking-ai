from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

from app.graph.workflow import graph
from app.memory import memory_store

router = APIRouter()


class ChatRequest(BaseModel):

    question: str
    session_id: Optional[str] = None


@router.post("/chat")
def chat(request: ChatRequest):

    session_id = request.session_id or memory_store.create_session_id()

    state = {

        "question": request.question,

        "session_id": session_id,

        "history": memory_store.get_history(session_id),

        "next_agent": None,

        "customer_id": None,

        "parking_lot_id": None,

        "reservation_id": None,

        "vehicle_plate": None,

        "intent": None,

        "confidence": 1,

        "api_result": {},

        "requires_human": False,

        "response": None

    }

    result = graph.invoke(state)

    return result
