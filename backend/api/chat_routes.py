from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.rag.dependencies import agent

from backend.services.chat_service import (
    save_message,
    get_history,
    create_session
)

from backend.services.rag.agent import building_react_agent

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    user_id: str
    session_id: str | None = None


@router.post("/")
def chat_route(req: ChatRequest):

    # create or reuse session
    session_id = req.session_id or create_session(req.user_id)

    # run agent
    result = agent.invoke(
        {"input": req.message},
        config={"configurable": {"session_id": session_id}}
    )

    # safe extraction
    response = result.get("output", "")

    # save messages
    save_message(session_id, "user", req.message)
    save_message(session_id, "assistant", response)

    return {
        "response": response,
        "session_id": session_id
    }


@router.get("/history/{session_id}")
def history_route(session_id: str):
    return get_history(session_id)