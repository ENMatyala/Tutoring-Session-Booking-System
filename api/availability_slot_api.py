from fastapi import APIRouter, HTTPException

from models.availability_slot_model import (
    AvailabilitySlotModel
)

from services.availability_slot_service import (
    AvailabilitySlotService
)

from src.availability_slot import AvailabilitySlot

router = APIRouter()

service = AvailabilitySlotService()


@router.post("/slots")
def create_slot(slot: AvailabilitySlotModel):

    try:

        new_slot = AvailabilitySlot(
            slot.slot_id,
            slot.start_time,
            slot.end_time
        )

        created_slot = service.create_slot(
            new_slot
        )

        return {
            "message": "Availability slot created",
            "slot": created_slot.__dict__
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.get("/slots")
def get_all_slots():

    return [
        slot.__dict__
        for slot in service.get_all_slots()
    ]


@router.get("/slots/{slot_id}")
def get_slot(slot_id: str):

    try:

        slot = service.get_slot(slot_id)

        return slot.__dict__

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.delete("/slots/{slot_id}")
def delete_slot(slot_id: str):

    service.delete_slot(slot_id)

    return {"message": "Slot deleted"}