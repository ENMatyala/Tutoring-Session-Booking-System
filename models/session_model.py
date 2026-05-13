from pydantic import BaseModel


class SessionModel(BaseModel):
    session_id: str
    topic: str
    date: str