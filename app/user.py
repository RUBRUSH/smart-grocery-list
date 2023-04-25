import json

class User:
    def __init__(self, username, email, password, preferences=None):
        self.username = username
        self.email = email
        self.password = password  # В реальном приложении следует использовать безопасное хранение пароля
        self.preferences = preferences if preferences is not None else set()

    def add_preference(self, preference):
        self.preferences.add(preference)

    def remove_preference(self, preference):
        self.preferences.discard(preference)

    def save(self, database):
        if self.username not in database.users:
            user_data = {
                "email": self.email,
                "password": self.password,
                "preferences": list(self.preferences),
            }
            
            database.users[self.username] = user_data
            database.save_users()
        else:
            raise ValueError(f"User {self.username} already exists.")

    @classmethod
    def load(cls, username, password, database):
        user_data = database.users.get(username, None)

        if user_data is not None and user_data["password"] == password:
            user = cls(
                username=username,
                email=user_data["email"],
                password=user_data["password"],
                preferences=set(user_data["preferences"])
            )
            return user
        else:
            return None

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}, Preferences: {', '.join(self.preferences)}"

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"