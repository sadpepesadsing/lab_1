import xml.etree.ElementTree as ET
from typing import Optional
from User import User

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

        user_element = ET.SubElement(root, "user")
        ET.SubElement(user_element, "name").text = user.name
        ET.SubElement(user_element, "email").text = user.email
        ET.SubElement(user_element, "watchlist").text = user.watchlist
        ET.SubElement(user_element, "subscription").text = user.subscription.subscription_type
        ET.SubElement(user_element, "wishlist").text = [movie.name for movie in user.wishlist.wishlist]
        ET.SubElement(user_element, "wishlist").text = ([user.notification.message]
                                                        + [user.notification.notification_type])

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
                    notification = user_element.find("notificaion").text
                    return User(name, email, subscription, )
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