from repositories.repository import Repository
from src.booking import Booking


class BookingRepository(Repository[Booking, str]):
    pass