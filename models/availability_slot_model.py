from pydantic import BaseModel


class AvailabilitySlotModel(BaseModel):
    slot_id: str
    start_time: str
    end_time: str