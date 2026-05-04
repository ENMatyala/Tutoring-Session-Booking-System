from repositories.tutor_repository import TutorRepository


class InMemoryTutorRepository(TutorRepository):

    def __init__(self):
        self._storage = {}

    def save(self, tutor):
        self._storage[tutor.tutor_id] = tutor

    def find_by_id(self, tutor_id):
        return self._storage.get(tutor_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, tutor_id):
        if tutor_id in self._storage:
            del self._storage[tutor_id]