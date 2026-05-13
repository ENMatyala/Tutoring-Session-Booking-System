import pytest

from services.session_service import SessionService
from src.session import Session


def test_create_session():

    service = SessionService()

    session = Session(
        "SE1",
        "Python",
        "2026-05-13"
    )

    created_session = service.create_session(
        session
    )

    assert created_session.session_id == "SE1"


def test_empty_topic():

    service = SessionService()

    session = Session(
        "SE2",
        "",
        "2026-05-13"
    )

    with pytest.raises(ValueError):
        service.create_session(session)