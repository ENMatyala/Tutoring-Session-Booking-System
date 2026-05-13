from repositories.inmemory.inmemory_booking_repository import (
    InMemoryBookingRepository
)


class BookingService:

    VALID_STATUSES = [
        "Pending",
        "Confirmed",
        "Cancelled"
    ]

    def __init__(self):
        self.repo = InMemoryBookingRepository()

    def create_booking(self, booking):

        if booking.status not in self.VALID_STATUSES:
            raise ValueError("Invalid booking status")

        self.repo.save(booking)

        return booking

    def confirm_booking(self, booking_id):

        booking = self.repo.find_by_id(booking_id)

        if not booking:
            raise ValueError("Booking not found")

        if booking.status == "Cancelled":
            raise ValueError(
                "Cancelled booking cannot be confirmed"
            )

        booking.status = "Confirmed"

        self.repo.save(booking)

        return booking

    def get_booking(self, booking_id):

        booking = self.repo.find_by_id(booking_id)

        if not booking:
            raise ValueError("Booking not found")

        return booking

    def get_all_bookings(self):
        return self.repo.find_all()

    def delete_booking(self, booking_id):

        self.repo.delete(booking_id)