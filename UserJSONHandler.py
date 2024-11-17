import json
from typing import Optional

from Director import Director
from Movie import Movie
from User import User, Subscription, Wishlist, UserNotification


class UserExistsError(Exception):
    pass
class UserNotFoundError(Exception):
    pass

class UserJSONHandler:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def create(self, user: User):
        author_data = {
            "name": user.name,
            "email": user.email,
            "subscription": user.subscription.subscription_type,
            "wishlist": [f"{movie.name}\t{movie.genre}\t{movie.duration}\t{movie.director.name}\t{movie.director.birthdate}"
                         for movie in user.wishlist.wishlist],
            "notification": [user.notification.message] + [user.notification.notification_type]
        }

        try:
            with open(self.filepath, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"users": []}

        for existing_users in data.get("users", []):
            if existing_users["name"] == user.name:
                raise UserExistsError(f"User '{user.name}' already exists.")

        data["users"].append(author_data)
        with open(self.filepath, "w") as file:
            json.dump(data, file, indent=4)

    def read(self, name: str) -> Optional[User]:
        try:
            with open(self.filepath, "r") as file:
                data = json.load(file)
            for user_data in data.get("users", []):
                if user_data["name"] == name:
                    wishlist = [] #Список фильмов Movie()
                    for wish in user_data["wishlist"]:
                        wish = wish.split('\t')
                        movie_name = wish[0]
                        genre = wish[1]
                        duration = int(wish[2])
                        director = wish[3]
                        birthday = wish[4]
                        wishlist.append(Movie(movie_name, genre, duration, Director(director, birthday)))
                    return User(user_data["name"], user_data["email"],
                        Subscription(user_data["subscription"]), Wishlist(wishlist),
                        UserNotification(user_data["notification"][0], user_data["notification"][1]))
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def update(self, name: str, new_email: str):
        try:
            with open(self.filepath, "r") as file:
                data = json.load(file)
            for user_data in data.get("users", []):
                if user_data["name"] == name:
                    user_data["email"] = new_email
                    with open(self.filepath, "w") as file:
                        json.dump(data, file, indent=4)
                    return True
            raise UserNotFoundError(f"Author '{name}' not found for update.")
        except (FileNotFoundError, json.JSONDecodeError):
            return False
        except UserNotFoundError as e:
            print(e)
            return False

    def delete(self, name: str):
        try:
            with open(self.filepath, "r") as file:
                data = json.load(file)
            original_length = len(data.get("users", []))
            data["users"] = [users for users in data.get("users", []) if users["name"] != name]

            if len(data["users"]) == original_length:
                raise UserNotFoundError(f"User '{name}' not found for deletion.")

            with open(self.filepath, "w") as file:
                json.dump(data, file, indent=4)
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            return False
        except UserNotFoundError as e:
            print(e)
            return False