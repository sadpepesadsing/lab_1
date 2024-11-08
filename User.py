from typing import List, Optional
from Movie import Movie

class Wishlist:
    def __init__(self):
        self.wishlist: List[Movie] = []

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
        movie_titles = [movie.name for movie in self.wishlist]
        print(f"Wishlist for {self.name}: {movie_titles}")

class Subscription:
    def __init__(self, subscription_type: str):
        self.subscription_type = subscription_type

    def upgrade_subscription(self, new_type: str):
        assert isinstance(new_type, str) and new_type, "new type must be a non-empty string"
        self.subscription_type = new_type
        print(f"Subscription upgraded to {new_type}")


class User:
    def __init__(self, name: str, email: str, subscription: Optional[Subscription]):
        assert isinstance(name, str) and name, "User name must be a non-empty string"
        assert isinstance(email, str) and email, "Email must be a non-empty string"

        self.name = name
        self.email = email
        self.watchlist: List[Movie] = []
        self.subscription = subscription

    def add_to_watchlist(self, movie: Movie):
        if movie not in self.watchlist:
            self.watchlist.append(movie)
            print(f"Added '{movie.name}' to watchlist")
        else:
            print(f"'{movie.name}' is already in the watchlist")
    def change_subscription(self, new_type: str):
        self.subscription.upgrade_subscription(new_type)

    def __str__(self):
        return f"name={self.name}, email={self.email}, sub={self.subscription.subscription_type}"


class UserNotification:
    def __init__(self, user: User, message: str, notification_type: str):
        assert notification_type in ["Info", "Warning", "Promotion"], "Invalid notification type"
        self.user = user
        self.message = message
        self.notification_type = notification_type

    def send_notification(self):
        print(f"Notification sent to {self.user.name}: {self.message} ({self.notification_type})")

    def __str__(self):
        return f"UserNotification(user={self.user.name}, message={self.message}, notification_type={self.notification_type})"
