from typing import List
from Movie import Movie

class Wishlist:
    def __init__(self, wishlist: List[Movie] = []):
        self.wishlist = wishlist

    def add_to_wishlist(self, movie: Movie):
        if movie not in self.wishlist:
            self.wishlist.append(movie)
            print(f"Added '{movie.name}' to wishlist")
        else:
            print(f"'{movie.name}' is already in the wishlist")

    def remove_from_wishlist(self, movie: Movie):
        if movie in self.wishlist:
            self.wishlist.remove(movie)
            print(f"Removed '{movie.name}' from wishlist")
        else:
            print(f"'{movie.name}' is not in the wishlist")

    def show_wishlist(self):
        movie_titles = [f"{movie.name}, {movie.genre}, {movie.director}, {movie.duration} mins" for movie in self.wishlist]
        return f"Wishlist: {movie_titles}"