class AvailabilitySlot:
    def __init__(self, slot_id, start_time, end_time, status="available"):
        self.slot_id = slot_id
        self.start_time = start_time
        self.end_time = end_time
        self.status = status

    def add_slot(self):
        return "Slot added."

    def remove_slot(self):
        self.status = "unavailable"
        return "Slot removed."