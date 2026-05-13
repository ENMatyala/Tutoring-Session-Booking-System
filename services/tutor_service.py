from repositories.inmemory.inmemory_tutor_repository import (
    InMemoryTutorRepository
)


class TutorService:

    def __init__(self):
        self.repo = InMemoryTutorRepository()

    def create_tutor(self, tutor):

        if tutor.hourly_rate <= 0:
            raise ValueError(
                "Hourly rate must be greater than zero"
            )

        if not tutor.subject:
            raise ValueError("Subject is required")

        existing_tutor = self.repo.find_by_id(
            tutor.tutor_id
        )

        if existing_tutor:
            raise ValueError("Tutor ID already exists")

        self.repo.save(tutor)

        return tutor

    def get_tutor(self, tutor_id):

        tutor = self.repo.find_by_id(tutor_id)

        if not tutor:
            raise ValueError("Tutor not found")

        return tutor

    def get_all_tutors(self):
        return self.repo.find_all()

    def delete_tutor(self, tutor_id):

        tutor = self.repo.find_by_id(tutor_id)

        if not tutor:
            raise ValueError("Tutor not found")

        self.repo.delete(tutor_id)
    