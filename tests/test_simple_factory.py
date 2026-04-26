from creational_patterns.simple_factory.user_factory import UserFactory

def test_create_student():
    student = UserFactory.create_user(
        "student",
        user_id="1",
        email="test@mail.com",
        password="123",
        student_id="S1",
        name="Clark"
    )
    assert student.role == "student"
    assert student.name == "Clark"


def test_create_tutor():
    tutor = UserFactory.create_user(
        "tutor",
        user_id="2",
        email="tutor@mail.com",
        password="456",
        tutor_id="T1",
        name="John",
        subject="Math",
        hourly_rate=200
    )
    assert tutor.role == "tutor"
    assert tutor.subject == "Math"


def test_invalid_user():
    import pytest
    with pytest.raises(ValueError):
        UserFactory.create_user("invalid")