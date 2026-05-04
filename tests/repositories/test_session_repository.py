from repositories.inmemory.inmemory_session_repository import InMemorySessionRepository
from src.session import Session


def test_save_session():
    repo = InMemorySessionRepository()

    session = Session("SE1", "Python Tutoring", "2026-05-10")

    repo.save(session)

    assert repo.find_by_id("SE1") == session


def test_find_all_sessions():
    repo = InMemorySessionRepository()

    session = Session("SE1", "Python Tutoring", "2026-05-10")

    repo.save(session)

    assert len(repo.find_all()) == 1


def test_delete_session():
    repo = InMemorySessionRepository()

    session = Session("SE1", "Python Tutoring", "2026-05-10")

    repo.save(session)
    repo.delete("SE1")

    assert repo.find_by_id("SE1") is None