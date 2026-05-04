from repositories.booking_repository import BookingRepository


class InMemoryBookingRepository(BookingRepository):

    def __init__(self):
        self._storage = {}

    def save(self, booking):
        self._storage[booking.booking_id] = booking

    def find_by_id(self, booking_id):
        return self._storage.get(booking_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, booking_id):
        if booking_id in self._storage:
            del self._storage[booking_id]