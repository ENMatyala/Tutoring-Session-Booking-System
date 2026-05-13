from fastapi import APIRouter, HTTPException
from models.student_model import StudentModel
from services.student_service import StudentService
from src.student import Student

router = APIRouter()

service = StudentService()


@router.post("/students")
def create_student(student: StudentModel):

    try:

        new_student = Student(
            student.user_id,
            student.email,
            student.password,
            student.student_id,
            student.name
        )

        created_student = service.create_student(
            new_student
        )

        return {
            "message": "Student created",
            "student": created_student.__dict__
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.get("/students")
def get_all_students():

    return [
        student.__dict__
        for student in service.get_all_students()
    ]


@router.get("/students/{student_id}")
def get_student(student_id: str):

    try:

        student = service.get_student(student_id)

        return student.__dict__

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.delete("/students/{student_id}")
def delete_student(student_id: str):

    service.delete_student(student_id)

    return {"message": "Student deleted"}