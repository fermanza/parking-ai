from fastapi import APIRouter
from pydantic import BaseModel

from app.graph.workflow import graph

router = APIRouter()


class ChatRequest(BaseModel):

    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    state = {

        "question": request.question,

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
