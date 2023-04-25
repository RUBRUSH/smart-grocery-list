# импортируем классы и функции из модулей
from .main import run_app
from .user import User
from .recipe import Recipe
from .grocery_list import GroceryList
from .database import Database  # предполагая, что там есть класс Database

# делаем их доступными для импорта из основного пакета
__all__ = ['run_app', 'User', 'Recipe', 'GroceryList', 'Database']