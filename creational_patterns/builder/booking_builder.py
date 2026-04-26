from src.booking import Booking

class BookingBuilder:
    def __init__(self):
        self.booking = Booking(None, None)

    def set_id(self, booking_id):
        self.booking.booking_id = booking_id
        return self

    def set_date(self, date):
        self.booking.date = date
        return self

    def set_status(self, status):
        self.booking.status = status
        return self

    def build(self):
        return self.booking