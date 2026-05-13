import pytest

from services.review_service import ReviewService
from src.review import Review


def test_create_review():

    service = ReviewService()

    review = Review(
        "R1",
        5,
        "Excellent"
    )

    created_review = service.create_review(
        review
    )

    assert created_review.review_id == "R1"


def test_invalid_review_rating():

    service = ReviewService()

    review = Review(
        "R2",
        10,
        "Bad"
    )

    with pytest.raises(ValueError):
        service.create_review(review)