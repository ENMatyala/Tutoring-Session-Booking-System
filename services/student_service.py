from repositories.inmemory.inmemory_student_repository import (
    InMemoryStudentRepository
)


class StudentService:

    def __init__(self):
        self.repo = InMemoryStudentRepository()

    def create_student(self, student):

        if not student.email:
            raise ValueError("Email cannot be empty")

        existing_student = self.repo.find_by_id(
            student.student_id
        )

        if existing_student:
            raise ValueError("Student ID already exists")

        self.repo.save(student)

        return student

    def get_student(self, student_id):

        student = self.repo.find_by_id(student_id)

        if not student:
            raise ValueError("Student not found")

        return student

    def get_all_students(self):
        return self.repo.find_all()

    def delete_student(self, student_id):

        student = self.repo.find_by_id(student_id)

        if not student:
            raise ValueError("Student not found")

        self.repo.delete(student_id)