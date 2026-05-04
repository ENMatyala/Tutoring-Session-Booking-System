from repositories.inmemory.inmemory_review_repository import InMemoryReviewRepository
from src.review import Review


def test_save_review():
    repo = InMemoryReviewRepository()

    review = Review("R1", 5, "Excellent tutor")

    repo.save(review)

    assert repo.find_by_id("R1") == review


def test_find_all_reviews():
    repo = InMemoryReviewRepository()

    review = Review("R1", 5, "Excellent tutor")

    repo.save(review)

    assert len(repo.find_all()) == 1


def test_delete_review():
    repo = InMemoryReviewRepository()

    review = Review("R1", 5, "Excellent tutor")

    repo.save(review)
    repo.delete("R1")

    assert repo.find_by_id("R1") is None