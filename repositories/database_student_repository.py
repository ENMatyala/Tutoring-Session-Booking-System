from repositories.student_repository import StudentRepository


class DatabaseStudentRepository(StudentRepository):

    def save(self, entity):
        pass

    def find_by_id(self, entity_id):
        pass

    def find_all(self):
        pass

    def delete(self, entity_id):
        pass