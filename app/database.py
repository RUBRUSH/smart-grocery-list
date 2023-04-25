import json
from pathlib import Path
from .user import User
from .recipe import Recipe

class Database:
    def __init__(self, users_file="data/users.json", recipes_file="data/recipes.json"):
        self.users_file = users_file
        self.recipes_file = recipes_file

        self._users = None
        self._recipes = None

    @property
    def users(self):
        if self._users is None:
            self._users = self.load_users()
        return self._users

    @property
    def recipes(self):
        if self._recipes is None:
            self._recipes = self.load_recipes()
        return self._recipes

    def load_users(self):
        try:
            with open(self.users_file, "r") as f:
                users_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            users_data = {}

        return users_data

    def save_users(self):
        with open(self.users_file, "w") as f:
            json.dump(self._users, f, indent=4, sort_keys=True)

    def load_recipes(self):
        try:
            with open(self.recipes_file, "r") as f:
                recipes_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            return []

        return [Recipe.load_from_json(recipe_json) for recipe_json in recipes_data]

    def save_recipes(self):
        with open(self.recipes_file, "w") as f:
            recipes_data = [recipe.__dict__ for recipe in self._recipes]
            json.dump(recipes_data, f, indent=4, sort_keys=True)