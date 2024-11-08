from typing import List, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from Movie import Movie

class Director:
    def __init__(self, name: str, birthdate: str):
        assert isinstance(name, str) and name, "Director name must be a non-empty string"
        assert isinstance(birthdate, str) and birthdate, "Birthdate must be a non-empty string"

        self.name = name
        self.birthdate = birthdate
        self.movies: List[Movie] = []

    def add_book(self, movie: Optional["Movie"]):
        if movie not in self.movies:
            self.movies.append(movie)
            print(f"Added '{movie.name}' to the director's movies.")
        else:
            print(f"Movie '{movie.name}' already added to the director.")

    def __str__(self):
        movie_titles = [movie.name for movie in self.movies]
        return f"Director(name={self.name}, birthdate={self.birthdate}, movies={movie_titles})"