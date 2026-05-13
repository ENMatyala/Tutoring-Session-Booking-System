from pydantic import BaseModel


class StudentModel(BaseModel):
    user_id: str
    email: str
    password: str
    student_id: str
    name: str