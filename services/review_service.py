from repositories.inmemory.inmemory_review_repository import (
    InMemoryReviewRepository
)


class ReviewService:

    def __init__(self):
        self.repo = InMemoryReviewRepository()

    def create_review(self, review):

        if review.rating < 1 or review.rating > 5:
            raise ValueError(
                "Rating must be between 1 and 5"
            )

        self.repo.save(review)

        return review

    def get_review(self, review_id):

        review = self.repo.find_by_id(review_id)

        if not review:
            raise ValueError("Review not found")

        return review

    def get_all_reviews(self):
        return self.repo.find_all()

    def delete_review(self, review_id):
        self.repo.delete(review_id)