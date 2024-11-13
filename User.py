from Movie import Movie
from UserNotification import UserNotification
from Wishlist import Wishlist
from Subscription import Subscription

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
