import pytest

from services.booking_service import BookingService
from src.booking import Booking


def test_create_booking():

    service = BookingService()

    booking = Booking(
        "B1",
        "2026-05-13",
        "Pending"
    )

    created_booking = service.create_booking(
        booking
    )

    assert created_booking.booking_id == "B1"


def test_invalid_booking_status():

    service = BookingService()

    booking = Booking(
        "B2",
        "2026-05-13",
        "Invalid"
    )

    with pytest.raises(ValueError):
        service.create_booking(booking)