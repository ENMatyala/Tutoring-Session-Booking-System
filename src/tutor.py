from src.user import User

class Tutor(User):
    def __init__(self, user_id, email, password, tutor_id, name, subject, hourly_rate, rating=0.0):
        super().__init__(user_id, email, password, role="tutor")
        self.tutor_id = tutor_id
        self.name = name
        self.subject = subject
        self.hourly_rate = hourly_rate
        self.rating = rating

    def manage_availability(self):
        return "Availability updated."

    def update_profile(self):
        return "Profile updated."