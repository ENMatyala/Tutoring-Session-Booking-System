from pydantic import BaseModel


class PaymentModel(BaseModel):
    payment_id: str
    amount: float
    status: str