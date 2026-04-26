class Booking:
    def __init__(self, booking_id, date, status="pending"):
        self.booking_id = booking_id
        self.date = date
        self.status = status

    def create_booking(self):
        self.status = "confirmed"
        return "Booking created."

    def cancel_booking(self):
        self.status = "cancelled"
        return "Booking cancelled."