from Director import Director
from User import *
from UserJSONHandler import *
from UserXMLHandler import *

user = User("Denis", "qwerty@example.com")

print(f"user info: {user}")

user.change_subscription("Pro")
user.add_to_wishlist(Movie("Pulp Fiction", "Crime", 154, Director("Quentin Tarantino", "27.03.1963")))

print(f"user info: {user}")

user.set_notification("Thrillers and comedies are the best sponsor of your evening...", "Promotion")
user.send_notification()

userJSON = UserJSONHandler("C:\\Users\Денис\PycharmProjects\lab_1\\userJSON")

userJSON.create(user)

example_user = userJSON.read("Denis")

print(f"\n\n\n{example_user}")

userJSON.update("Denis", "pi")

example_user = userJSON.read("Denis")

print(f"\n{example_user}\n")

userXML = UserXMLHandler("C:\\Users\Денис\PycharmProjects\lab_1\\userXML")

userXML.create(user)
example_user = userJSON.read("Denis")

print(example_user)
