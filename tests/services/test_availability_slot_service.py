import pytest

from services.availability_slot_service import (
    AvailabilitySlotService
)

from src.availability_slot import AvailabilitySlot


def test_create_slot():

    service = AvailabilitySlotService()

    slot = AvailabilitySlot(
        "SL1",
        "09:00",
        "10:00"
    )

    created_slot = service.create_slot(slot)

    assert created_slot.slot_id == "SL1"


def test_invalid_slot_time():

    service = AvailabilitySlotService()

    slot = AvailabilitySlot(
        "SL2",
        "09:00",
        "09:00"
    )

    with pytest.raises(ValueError):
        service.create_slot(slot)