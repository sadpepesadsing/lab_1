from typing import List
from Movie import Movie

class MovieFormat:
    """Формат фильма"""
    def __init__(self, format_type: str):
        assert format_type in ["240p", "480p", "720p", "HD", "4K"], "Invalid format type"
        self.format_type = format_type
        self.movies: List[Movie] = []

    def add_movie(self, movie: Movie):
        """Добавить фильм в список формата"""
        if movie not in self.movies:
            self.movies.append(movie)
            print(f"Added '{movie.name}' to the format '{self.format_type}'.")
        else:
            print(f"Movie '{movie.name}' is already available in the format '{self.format_type}'.")

    def __str__(self):
        return f"MovieFormat(format_type={self.format_type}, movies={[movie.name for movie in self.movies]})"