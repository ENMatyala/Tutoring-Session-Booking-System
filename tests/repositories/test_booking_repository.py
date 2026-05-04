from repositories.inmemory.inmemory_booking_repository import InMemoryBookingRepository
from src.booking import Booking


def test_save_booking():
    repo = InMemoryBookingRepository()

    booking = Booking("B1", "2026-05-01", "Confirmed")

    repo.save(booking)

    assert repo.find_by_id("B1") == booking


def test_find_all_bookings():
    repo = InMemoryBookingRepository()

    booking = Booking("B1", "2026-05-01", "Confirmed")

    repo.save(booking)

    assert len(repo.find_all()) == 1


def test_delete_booking():
    repo = InMemoryBookingRepository()

    booking = Booking("B1", "2026-05-01", "Confirmed")

    repo.save(booking)
    repo.delete("B1")

    assert repo.find_by_id("B1") is None