from repositories.inmemory.inmemory_payment_repository import (
    InMemoryPaymentRepository
)


class PaymentService:

    def __init__(self):
        self.repo = InMemoryPaymentRepository()

    def create_payment(self, payment):

        if payment.amount <= 0:
            raise ValueError(
                "Amount must be greater than zero"
            )

        self.repo.save(payment)

        return payment

    def get_payment(self, payment_id):

        payment = self.repo.find_by_id(payment_id)

        if not payment:
            raise ValueError("Payment not found")

        return payment

    def get_all_payments(self):
        return self.repo.find_all()

    def delete_payment(self, payment_id):
        self.repo.delete(payment_id)