from creational_patterns.prototype.session_prototype import (
    SessionPrototype, SessionCache
)

def test_prototype_clone():
    session = SessionPrototype("S1", "10:00", "11:00")
    clone = session.clone()

    assert session.session_id == clone.session_id
    assert session is not clone  # different objects


def test_session_cache():
    cache = SessionCache()

    original = SessionPrototype("S2", "12:00", "13:00")
    cache.add_session("session1", original)

    cloned = cache.get_session("session1")

    assert cloned.session_id == "S2"
    assert cloned is not original