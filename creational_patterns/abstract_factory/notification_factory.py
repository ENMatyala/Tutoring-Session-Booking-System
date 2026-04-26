from abc import ABC, abstractmethod

# Abstract Products
class EmailNotification(ABC):
    @abstractmethod
    def send_email(self):
        pass

class SMSNotification(ABC):
    @abstractmethod
    def send_sms(self):
        pass

# Concrete Products (Student)
class StudentEmail(EmailNotification):
    def send_email(self):
        return "Email sent to student"

class StudentSMS(SMSNotification):
    def send_sms(self):
        return "SMS sent to student"

# Concrete Products (Tutor)
class TutorEmail(EmailNotification):
    def send_email(self):
        return "Email sent to tutor"

class TutorSMS(SMSNotification):
    def send_sms(self):
        return "SMS sent to tutor"

# Abstract Factory
class NotificationFactory(ABC):
    @abstractmethod
    def create_email(self):
        pass

    @abstractmethod
    def create_sms(self):
        pass

# Concrete Factories
class StudentNotificationFactory(NotificationFactory):
    def create_email(self):
        return StudentEmail()

    def create_sms(self):
        return StudentSMS()

class TutorNotificationFactory(NotificationFactory):
    def create_email(self):
        return TutorEmail()

    def create_sms(self):
        return TutorSMS()