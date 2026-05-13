from fastapi import APIRouter, HTTPException

from models.session_model import SessionModel
from services.session_service import SessionService
from src.session import Session

router = APIRouter()

service = SessionService()


@router.post("/sessions")
def create_session(session: SessionModel):

    try:

        new_session = Session(
            session.session_id,
            session.topic,
            session.date
        )

        created_session = service.create_session(
            new_session
        )

        return {
            "message": "Session created",
            "session": created_session.__dict__
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.get("/sessions")
def get_all_sessions():

    return [
        session.__dict__
        for session in service.get_all_sessions()
    ]


@router.get("/sessions/{session_id}")
def get_session(session_id: str):

    try:

        session = service.get_session(session_id)

        return session.__dict__

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.delete("/sessions/{session_id}")
def delete_session(session_id: str):

    service.delete_session(session_id)

    return {"message": "Session deleted"}