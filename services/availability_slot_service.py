from repositories.inmemory.inmemory_availability_slot_repository import (
    InMemoryAvailabilitySlotRepository
)


class AvailabilitySlotService:

    def __init__(self):
        self.repo = InMemoryAvailabilitySlotRepository()

    def create_slot(self, slot):

        if slot.start_time == slot.end_time:
            raise ValueError(
                "Start and end time cannot match"
            )

        self.repo.save(slot)

        return slot

    def get_slot(self, slot_id):

        slot = self.repo.find_by_id(slot_id)

        if not slot:
            raise ValueError("Slot not found")

        return slot

    def get_all_slots(self):
        return self.repo.find_all()

    def delete_slot(self, slot_id):
        self.repo.delete(slot_id)