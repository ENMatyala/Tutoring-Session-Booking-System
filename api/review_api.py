from fastapi import APIRouter, HTTPException

from models.review_model import ReviewModel
from services.review_service import ReviewService
from src.review import Review

router = APIRouter()

service = ReviewService()


@router.post("/reviews")
def create_review(review: ReviewModel):

    try:

        new_review = Review(
            review.review_id,
            review.rating,
            review.comment
        )

        created_review = service.create_review(
            new_review
        )

        return {
            "message": "Review created",
            "review": created_review.__dict__
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.get("/reviews")
def get_all_reviews():

    return [
        review.__dict__
        for review in service.get_all_reviews()
    ]


@router.get("/reviews/{review_id}")
def get_review(review_id: str):

    try:

        review = service.get_review(review_id)

        return review.__dict__

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.delete("/reviews/{review_id}")
def delete_review(review_id: str):

    service.delete_review(review_id)

    return {"message": "Review deleted"}