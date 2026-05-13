from pydantic import BaseModel


class BookingModel(BaseModel):
    booking_id: str
    date: str
    status: str