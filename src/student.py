from src.user import User

class Student(User):
    def __init__(self, user_id, email, password, student_id, name):
        super().__init__(user_id, email, password, role="student")
        self.student_id = student_id
        self.name = name

    def search_tutor(self):
        return "Searching for tutors..."

    def book_session(self):
        return "Session booked."

    def write_review(self):
        return "Review submitted."