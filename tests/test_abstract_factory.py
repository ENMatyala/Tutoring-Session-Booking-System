from creational_patterns.abstract_factory.notification_factory import (
    StudentNotificationFactory, TutorNotificationFactory
)
def test_student_notifications():
    factory = StudentNotificationFactory()

    email = factory.create_email()
    sms = factory.create_sms()

    assert email.send_email() == "Email sent to student"
    assert sms.send_sms() == "SMS sent to student"


def test_tutor_notifications():
    factory = TutorNotificationFactory()

    email = factory.create_email()
    sms = factory.create_sms()

    assert email.send_email() == "Email sent to tutor"
    assert sms.send_sms() == "SMS sent to tutor"