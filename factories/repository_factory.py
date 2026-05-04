from repositories.inmemory.inmemory_student_repository import InMemoryStudentRepository
from repositories.inmemory.inmemory_tutor_repository import InMemoryTutorRepository
from repositories.inmemory.inmemory_booking_repository import InMemoryBookingRepository
from repositories.inmemory.inmemory_session_repository import InMemorySessionRepository
from repositories.inmemory.inmemory_payment_repository import InMemoryPaymentRepository
from repositories.inmemory.inmemory_review_repository import InMemoryReviewRepository
from repositories.inmemory.inmemory_availability_slot_repository import InMemoryAvailabilitySlotRepository


class RepositoryFactory:

    @staticmethod
    def get_student_repository(storage_type="MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryStudentRepository()
        raise ValueError("Invalid storage type")

    @staticmethod
    def get_tutor_repository(storage_type="MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryTutorRepository()
        raise ValueError("Invalid storage type")

    @staticmethod
    def get_booking_repository(storage_type="MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryBookingRepository()
        raise ValueError("Invalid storage type")

    @staticmethod
    def get_session_repository(storage_type="MEMORY"):
        if storage_type == "MEMORY":
            return InMemorySessionRepository()
        raise ValueError("Invalid storage type")

    @staticmethod
    def get_payment_repository(storage_type="MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryPaymentRepository()
        raise ValueError("Invalid storage type")

    @staticmethod
    def get_review_repository(storage_type="MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryReviewRepository()
        raise ValueError("Invalid storage type")

    @staticmethod
    def get_availability_slot_repository(storage_type="MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryAvailabilitySlotRepository()
        raise ValueError("Invalid storage type")