from repositories.inmemory.inmemory_payment_repository import InMemoryPaymentRepository
from src.payment import Payment


def test_save_payment():
    repo = InMemoryPaymentRepository()

    payment = Payment("P1", 500, "Completed")

    repo.save(payment)

    assert repo.find_by_id("P1") == payment


def test_find_all_payments():
    repo = InMemoryPaymentRepository()

    payment = Payment("P1", 500, "Completed")

    repo.save(payment)

    assert len(repo.find_all()) == 1


def test_delete_payment():
    repo = InMemoryPaymentRepository()

    payment = Payment("P1", 500, "Completed")

    repo.save(payment)
    repo.delete("P1")

    assert repo.find_by_id("P1") is None