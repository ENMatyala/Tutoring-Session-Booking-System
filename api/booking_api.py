from fastapi import APIRouter, HTTPException
from models.booking_model import BookingModel
from services.booking_service import BookingService
from src.booking import Booking

router = APIRouter()

service = BookingService()


@router.post("/bookings")
def create_booking(booking: BookingModel):

    try:

        new_booking = Booking(
            booking.booking_id,
            booking.date,
            booking.status
        )

        created_booking = service.create_booking(
            new_booking
        )

        return {
            "message": "Booking created",
            "booking": created_booking.__dict__
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.put("/bookings/{booking_id}/confirm")
def confirm_booking(booking_id: str):

    try:

        booking = service.confirm_booking(
            booking_id
        )

        return {
            "message": "Booking confirmed",
            "booking": booking.__dict__
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.get("/bookings")
def get_all_bookings():

    return [
        booking.__dict__
        for booking in service.get_all_bookings()
    ]


@router.get("/bookings/{booking_id}")
def get_booking(booking_id: str):

    try:

        booking = service.get_booking(booking_id)

        return booking.__dict__

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.delete("/bookings/{booking_id}")
def delete_booking(booking_id: str):

    service.delete_booking(booking_id)

    return {"message": "Booking deleted"}