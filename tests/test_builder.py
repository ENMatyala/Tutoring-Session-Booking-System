from creational_patterns.builder.booking_builder import BookingBuilder

def test_booking_builder():
    booking = (
        BookingBuilder()
        .set_id("B1")
        .set_date("2026-01-01")
        .set_status("confirmed")
        .build()
    )

    assert booking.booking_id == "B1"
    assert booking.status == "confirmed"
    
def test_builder_missing_fields():
    builder = BookingBuilder()
    booking = builder.build()

    assert booking.booking_id is None
    assert booking.date is None