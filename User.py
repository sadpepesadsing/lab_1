from typing import List
from Movie import Movie

class UserNotification:
    def __init__(self, message: str, notification_type: str):
        assert notification_type in ["System", "Info", "Warning", "Promotion"], "Invalid notification type"
        self.message = message
        self.notification_type = notification_type

    def set_notification(self, message: str, notification_type: str):
        assert notification_type in ["Info", "Warning", "Promotion"], "Invalid notification type"
        self.message = message
        self.notification_type = notification_type

    def send_notification(self):
        print(f"Notification: {self.message} ({self.notification_type})")

    def __str__(self):
        return f"UserNotification(message={self.message}, notification_type={self.notification_type})"

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
        movie_titles = [movie.name for movie in self.wishlist]
        print(f"Wishlist: {movie_titles}")

class Subscription:
    def __init__(self, subscription_type: str):
        self.subscription_type = subscription_type

    def upgrade_subscription(self, new_type: str):
        assert isinstance(new_type, str) and new_type, "new type must be a non-empty string"
        self.subscription_type = new_type
        print(f"Subscription upgraded to {new_type}")


class User:
    def __init__(self, name: str, email: str, subscription = Subscription("None"),
                 wishlist = Wishlist(), notification = UserNotification("Empty", "System")):
        assert isinstance(name, str) and name, "User name must be a non-empty string"
        assert isinstance(email, str) and email, "Email must be a non-empty string"

        self.name = name
        self.email = email
        self.subscription = subscription
        self.wishlist = wishlist
        self.notification = notification

    def change_subscription(self, new_type: str):
        self.subscription.upgrade_subscription(new_type)

    def add_to_wishlist(self, movie: Movie):
        self.wishlist.add_to_wishlist(movie)

    def remove_from_wishlist(self, movie: Movie):
        self.wishlist.remove_from_wishlist(movie)

    def show_wishlist(self):
        self.wishlist.show_wishlist()

    def set_notification(self, message: str, notification_type: str):
        self.notification.set_notification(message, notification_type)

    def send_notification(self):
        self.notification.send_notification()

    def __str__(self):
        return (f"name={self.name}, email={self.email}, sub={self.subscription.subscription_type},"
                f" wishlist: {[movie for movie in self.wishlist.wishlist]}")
