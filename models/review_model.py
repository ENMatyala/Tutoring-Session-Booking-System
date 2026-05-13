from pydantic import BaseModel


class ReviewModel(BaseModel):
    review_id: str
    rating: int
    comment: str