from pydantic import BaseModel


class TutorModel(BaseModel):
    user_id: str
    email: str
    password: str
    tutor_id: str
    name: str
    subject: str
    hourly_rate: float