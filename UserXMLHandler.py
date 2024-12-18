import xml.etree.ElementTree as ET
from typing import Optional

from Subscription import Subscription
from User import User
from Movie import Movie
from Director import Director
from UserNotification import UserNotification
from Wishlist import Wishlist


class UserExistsError(Exception):
    pass

class UserNotFoundError(Exception):
    pass

class UserXMLHandler:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def create(self, user: User):
        try:
            tree = ET.parse(self.filepath)
            root = tree.getroot()
        except (FileNotFoundError, ET.ParseError):
            root = ET.Element("users")

        for user_element in root.findall("user"):
            if user_element.find("name").text == user.name:
                raise UserExistsError(f"User '{user.name}' already exists.")
        wishlist = ''
        for movie in user.wishlist.wishlist:
            wishlist += "\t\t"
            wishlist += (f"{movie.name}\t{movie.genre}\t{movie.duration}\t"
                         f"{movie.director.name}\t{movie.director.birthdate}")

        user_element = ET.SubElement(root, "user")
        ET.SubElement(user_element, "name").text = user.name
        ET.SubElement(user_element, "email").text = user.email
        ET.SubElement(user_element, "subscription").text = user.subscription.subscription_type
        ET.SubElement(user_element, "wishlist").text = wishlist[2:]
        ET.SubElement(user_element, "notification").text = (f"{user.notification.message}\t"
                                                        f"{user.notification.notification_type}")
        tree = ET.ElementTree(root)
        tree.write(self.filepath)

    def read(self, name: str) -> Optional[User]:
        try:
            tree = ET.parse(self.filepath)
            root = tree.getroot()

            for user_element in root.findall("user"):
                if user_element.find("name").text == name:
                    email = user_element.find("email").text
                    subscription = user_element.find("subscription").text
                    notification = user_element.find("notification").text.split('\t')
                    wishlist = [] # список фильмов Movie()
                    for wish in user_element.find("wishlist").text.split('\t\t'):
                        wish = wish.split('\t')
                        movie_name = wish[0]
                        genre = wish[1]
                        duration = int(wish[2])
                        director = wish[3]
                        birthday = wish[4]
                        wishlist.append(Movie(movie_name, genre, duration, Director(director, birthday)))

                    return User(name, email, Subscription(subscription), Wishlist(wishlist),
                                UserNotification(notification[0],notification[1]))
        except (FileNotFoundError, ET.ParseError):
            return None
        return None

    def update(self, name: str, new_email: str) -> bool:
        try:
            tree = ET.parse(self.filepath)
            root = tree.getroot()
            for user_element in root.findall("user"):
                if user_element.find("name").text == name:
                    user_element.find("email").text = new_email
                    tree.write(self.filepath)
                    return True

            raise UserNotFoundError(f"User '{name}' not found for update.")
        except (FileNotFoundError, ET.ParseError):
            return False
        except UserNotFoundError as e:
            print(e)
            return False

    def delete(self, name: str) -> bool:
        try:
            tree = ET.parse(self.filepath)
            root = tree.getroot()
            for user_element in root.findall("user"):
                if user_element.find("name").text == name:
                    root.remove(user_element)
                    tree.write(self.filepath)
                    return True

            raise UserNotFoundError(f"User '{name}' not found for deletion.")
        except (FileNotFoundError, ET.ParseError):
            return False
        except UserNotFoundError as e:
            print(e)
            return False