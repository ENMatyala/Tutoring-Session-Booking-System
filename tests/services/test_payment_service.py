import pytest

from services.payment_service import PaymentService
from src.payment import Payment


def test_create_payment():

    service = PaymentService()

    payment = Payment(
        "P1",
        500,
        "Paid"
    )

    created_payment = service.create_payment(
        payment
    )

    assert created_payment.payment_id == "P1"


def test_invalid_payment_amount():

    service = PaymentService()

    payment = Payment(
        "P2",
        -10,
        "Paid"
    )

    with pytest.raises(ValueError):
        service.create_payment(payment)