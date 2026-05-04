from repositories.student_repository import StudentRepository


class InMemoryStudentRepository(StudentRepository):

    def __init__(self):
        self._storage = {}

    def save(self, student):
        self._storage[student.student_id] = student

    def find_by_id(self, student_id):
        return self._storage.get(student_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, student_id):
        if student_id in self._storage:
            del self._storage[student_id]