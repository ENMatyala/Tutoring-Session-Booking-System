class Review:
    def __init__(self, review_id, rating, comment):
        self.review_id = review_id
        self.rating = rating
        self.comment = comment

    def create_review(self):
        return "Review created."

    def update_review(self, new_rating, new_comment):
        self.rating = new_rating
        self.comment = new_comment
        return "Review updated."