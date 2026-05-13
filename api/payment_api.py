from fastapi import APIRouter, HTTPException

from models.payment_model import PaymentModel
from services.payment_service import PaymentService
from src.payment import Payment

router = APIRouter()

service = PaymentService()


@router.post("/payments")
def create_payment(payment: PaymentModel):

    try:

        new_payment = Payment(
            payment.payment_id,
            payment.amount,
            payment.status
        )

        created_payment = service.create_payment(
            new_payment
        )

        return {
            "message": "Payment created",
            "payment": created_payment.__dict__
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.get("/payments")
def get_all_payments():

    return [
        payment.__dict__
        for payment in service.get_all_payments()
    ]


@router.get("/payments/{payment_id}")
def get_payment(payment_id: str):

    try:

        payment = service.get_payment(payment_id)

        return payment.__dict__

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.delete("/payments/{payment_id}")
def delete_payment(payment_id: str):

    service.delete_payment(payment_id)

    return {"message": "Payment deleted"}