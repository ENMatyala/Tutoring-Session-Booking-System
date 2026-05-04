from repositories.inmemory.inmemory_tutor_repository import InMemoryTutorRepository
from src.tutor import Tutor


def test_save_tutor():
    repo = InMemoryTutorRepository()

    tutor = Tutor(
        "U2",
        "tutor@mail.com",
        "456",
        "T1",
        "John Doe",
        "Math",
        250.0
    )

    repo.save(tutor)

    assert repo.find_by_id("T1") == tutor


def test_find_all_tutors():
    repo = InMemoryTutorRepository()

    tutor = Tutor(
        "U2",
        "tutor@mail.com",
        "456",
        "T1",
        "John Doe",
        "Math",
        250.0
    )

    repo.save(tutor)

    assert len(repo.find_all()) == 1


def test_delete_tutor():
    repo = InMemoryTutorRepository()

    tutor = Tutor(
        "U2",
        "tutor@mail.com",
        "456",
        "T1",
        "John Doe",
        "Math",
        250.0
    )

    repo.save(tutor)
    repo.delete("T1")

    assert repo.find_by_id("T1") is None