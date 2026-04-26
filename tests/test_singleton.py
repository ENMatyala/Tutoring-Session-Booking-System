from creational_patterns.singleton.database_connection import DatabaseConnection

def test_singleton_instance():
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    assert db1 is db2


def test_connection_state():
    db = DatabaseConnection()
    db.connect()

    assert db.connected is True