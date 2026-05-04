from repositories.session_repository import SessionRepository


class InMemorySessionRepository(SessionRepository):

    def __init__(self):
        self._storage = {}

    def save(self, session):
        self._storage[session.session_id] = session

    def find_by_id(self, session_id):
        return self._storage.get(session_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, session_id):
        if session_id in self._storage:
            del self._storage[session_id]