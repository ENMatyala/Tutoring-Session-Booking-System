from src.student import Student
from src.tutor import Tutor

class UserFactory:
    @staticmethod
    def create_user(user_type, **kwargs):
        if user_type == "student":
            return Student(
                kwargs["user_id"],
                kwargs["email"],
                kwargs["password"],
                kwargs["student_id"],
                kwargs["name"]
            )
        elif user_type == "tutor":
            return Tutor(
                kwargs["user_id"],
                kwargs["email"],
                kwargs["password"],
                kwargs["tutor_id"],
                kwargs["name"],
                kwargs["subject"],
                kwargs["hourly_rate"]
            )
        else:
            raise ValueError("Invalid user type")