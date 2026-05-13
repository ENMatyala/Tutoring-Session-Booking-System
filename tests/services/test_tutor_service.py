import pytest

from services.tutor_service import TutorService
from src.tutor import Tutor


def test_create_tutor():

    service = TutorService()

    tutor = Tutor(
        "U1",
        "tutor@mail.com",
        "123",
        "T1",
        "John",
        "Math",
        250
    )

    created_tutor = service.create_tutor(tutor)

    assert created_tutor.tutor_id == "T1"


def test_invalid_hourly_rate():

    service = TutorService()

    tutor = Tutor(
        "U1",
        "tutor@mail.com",
        "123",
        "T2",
        "John",
        "Math",
        -100
    )

    with pytest.raises(ValueError):
        service.create_tutor(tutor)