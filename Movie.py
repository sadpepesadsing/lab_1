from Director import Director
from typing import Optional

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
