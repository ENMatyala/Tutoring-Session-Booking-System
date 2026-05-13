from repositories.inmemory.inmemory_session_repository import (
    InMemorySessionRepository
)


class SessionService:

    def __init__(self):
        self.repo = InMemorySessionRepository()

    def create_session(self, session):

        if not session.topic:
            raise ValueError("Session topic required")

        self.repo.save(session)

        return session

    def get_session(self, session_id):

        session = self.repo.find_by_id(session_id)

        if not session:
            raise ValueError("Session not found")

        return session

    def get_all_sessions(self):
        return self.repo.find_all()

    def delete_session(self, session_id):
        self.repo.delete(session_id)