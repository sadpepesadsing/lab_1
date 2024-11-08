from Director import Director
from User import *

user = User("Denis", "qwerty@example.com")

print(f"user info: {user}")

user.change_subscription("Pro")
user.add_to_wishlist(Movie("Pulp Fiction", "Crime", 154, Director("Quentin Tarantino", "27.03.1963")))

print(f"user info: {user}")

user.set_notification("Thrillers and comedies are the best sponsor of your evening...", "Promotion")
user.send_notification()