from Director import Director
from typing import Optional, List

class Movie:
    def __init__(self, name: str, genre: str, duration: int, director: Optional[Director]):
        assert isinstance(name, str) and name, "The name must be a non-empty string"
        assert isinstance(genre, str) and genre, "The genre must be a non-empty string"
        assert isinstance(duration, int) and duration, "The duration must be a non-empty integer"

        self.name = name
        self.genre = genre
        self.duration = duration
        self.director = director

    def display_movie_info(self):
        print(f"Movie: {self.name}, Director: {self.director}, Genre: {self.genre}, Duration: {self.duration} mins")

    def change_info(self, name: str, genre: str, duration: int, director: Optional[Director]):
        assert isinstance(name, str) and name, "The name must be a non-empty string"
        assert isinstance(genre, str) and genre, "The genre must be a non-empty string"
        assert isinstance(duration, int) and duration, "The duration must be a non-empty integer"

        self.name = name
        self.genre = genre
        self.duration = duration
        self.director = director


class Review:
    def __init__(self, movie: Movie, user: str, rating: int, comment: str = ""):
        assert isinstance(rating, int) and 1 <= rating <= 5, "Rating must be between 1 and 5"
        assert isinstance(comment, str), "Comment must be a string"

        self.movie = movie
        self.user = user
        self.rating = rating
        self.comment = comment

    def display_review(self):
        print(f"Review for '{self.movie.name}' by {self.user}:")
        print(f"Rating: {self.rating} stars")
        if self.comment:
            print(f"Comment: {self.comment}")
        else:
            print("No comments provided.")

    def __str__(self):
        return f"Review(movie={self.movie.name}, user={self.user}, rating={self.rating}, comment={self.comment})"


class MovieFormat:
    def __init__(self, format_type: str):
        assert format_type in ["240p", "480p", "720p", "HD", "4K"], "Invalid format type"
        self.format_type = format_type
        self.movies: List[Movie] = []

    def add_movie(self, movie: Movie):
        if movie not in self.movies:
            self.movies.append(movie)
            print(f"Added '{movie.name}' to the format '{self.format_type}'.")
        else:
            print(f"Movie '{movie.name}' is already available in the format '{self.format_type}'.")

    def __str__(self):
        return f"MovieFormat(format_type={self.format_type}, movies={[movie.name for movie in self.movies]})"