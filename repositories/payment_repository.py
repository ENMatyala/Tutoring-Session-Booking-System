from repositories.repository import Repository
from src.payment import Payment


class PaymentRepository(Repository[Payment, str]):
    pass