from repositories.repository import Repository
from src.review import Review


class ReviewRepository(Repository[Review, str]):
    pass