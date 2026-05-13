import pytest

from services.student_service import StudentService
from src.student import Student


def test_create_student():

    service = StudentService()

    student = Student(
        "U1",
        "student@mail.com",
        "123",
        "S1",
        "Clark"
    )

    created_student = service.create_student(student)

    assert created_student.student_id == "S1"


def test_empty_email():

    service = StudentService()

    student = Student(
        "U2",
        "",
        "123",
        "S2",
        "Bruce"
    )

    with pytest.raises(ValueError):
        service.create_student(student)