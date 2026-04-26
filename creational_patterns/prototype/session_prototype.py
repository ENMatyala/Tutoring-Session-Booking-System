import copy
from src.session import Session

class SessionPrototype(Session):
    def clone(self):
        return copy.deepcopy(self)


class SessionCache:
    def __init__(self):
        self._cache = {}

    def add_session(self, key, session):
        self._cache[key] = session

    def get_session(self, key):
        session = self._cache.get(key)
        return session.clone() if session else None