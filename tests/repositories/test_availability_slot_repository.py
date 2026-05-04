from repositories.inmemory.inmemory_availability_slot_repository import (
    InMemoryAvailabilitySlotRepository
)
from src.availability_slot import AvailabilitySlot


def test_save_slot():
    repo = InMemoryAvailabilitySlotRepository()

    slot = AvailabilitySlot("SL1", "09:00", "10:00")

    repo.save(slot)

    assert repo.find_by_id("SL1") == slot


def test_find_all_slots():
    repo = InMemoryAvailabilitySlotRepository()

    slot = AvailabilitySlot("SL1", "09:00", "10:00")

    repo.save(slot)

    assert len(repo.find_all()) == 1


def test_delete_slot():
    repo = InMemoryAvailabilitySlotRepository()

    slot = AvailabilitySlot("SL1", "09:00", "10:00")

    repo.save(slot)
    repo.delete("SL1")

    assert repo.find_by_id("SL1") is None