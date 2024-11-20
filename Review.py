from Movie import Movie

class Review:
    """Класс рецензии"""
    def __init__(self, movie: Movie, user: str, rating: int, comment: str = ""):
        assert isinstance(rating, int) and 1 <= rating <= 5, "Rating must be between 1 and 5"
        assert isinstance(comment, str), "Comment must be a string"

        self.movie = movie
        self.user = user
        self.rating = rating
        self.comment = comment

    def display_review(self):
        """Вывести рецензии"""
        print(f"Review for '{self.movie.name}' by {self.user}:")
        print(f"Rating: {self.rating} stars")
        if self.comment:
            print(f"Comment: {self.comment}")
        else:
            print("No comments provided.")

    def __str__(self):
        return f"Review(movie={self.movie.name}, user={self.user}, rating={self.rating}, comment={self.comment})"