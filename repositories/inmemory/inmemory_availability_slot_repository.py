from repositories.availability_slot_repository import AvailabilitySlotRepository


class InMemoryAvailabilitySlotRepository(AvailabilitySlotRepository):

    def __init__(self):
        self._storage = {}

    def save(self, slot):
        self._storage[slot.slot_id] = slot

    def find_by_id(self, slot_id):
        return self._storage.get(slot_id)

    def find_all(self):
        return list(self._storage.values())

    def delete(self, slot_id):
        if slot_id in self._storage:
            del self._storage[slot_id]