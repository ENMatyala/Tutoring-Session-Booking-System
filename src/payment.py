class Payment:
    def __init__(self, payment_id, amount, status="pending"):
        self.payment_id = payment_id
        self.amount = amount
        self.status = status

    def process_payment(self):
        self.status = "completed"
        return "Payment processed."

    def validate_payment(self):
        return self.amount > 0