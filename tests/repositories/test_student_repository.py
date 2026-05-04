from repositories.inmemory.inmemory_student_repository import InMemoryStudentRepository
from src.student import Student


def test_save_student():
    repo = InMemoryStudentRepository()

    student = Student("U1", "student@mail.com", "123", "S1", "Clark")

    repo.save(student)

    assert repo.find_by_id("S1") == student


def test_find_all_students():
    repo = InMemoryStudentRepository()

    student = Student("U1", "student@mail.com", "123", "S1", "Clark")

    repo.save(student)

    assert len(repo.find_all()) == 1


def test_delete_student():
    repo = InMemoryStudentRepository()

    student = Student("U1", "student@mail.com", "123", "S1", "Clark")

    repo.save(student)
    repo.delete("S1")

    assert repo.find_by_id("S1") is None