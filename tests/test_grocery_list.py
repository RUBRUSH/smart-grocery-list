import unittest
from app.recipe import Recipe
from app.grocery_list import GroceryList

class TestGroceryList(unittest.TestCase):

    def setUp(self):
        self.recipe1 = Recipe(
            id="1",
            title="Test Recipe 1",
            ingredients=[
                {"name": "ingredient1", "quantity": "1 cup"},
                {"name": "ingredient2", "quantity": "2 tbsp"},
            ],
            instructions="Mix ingredient1 and ingredient2.",
        )

        self.recipe2 = Recipe(
            id="2",
            title="Test Recipe 2",
            ingredients=[
                {"name": "ingredient1", "quantity": "1 cup"},
                {"name": "ingredient3", "quantity": "3 cups"},
            ],
            instructions="Mix ingredient1 and ingredient3.",
        )

        self.g_list = GroceryList()
    
    def test_add_recipe(self):
        self.g_list.add_recipe(self.recipe1)
        self.assertIn("ingredient1", self.g_list.items)
        self.assertIn("ingredient2", self.g_list.items)
        self.assertEqual(self.g_list.items["ingredient1"], "1 cup")
        self.assertEqual(self.g_list.items["ingredient2"], "2 tbsp")

    def test_remove_recipe(self):
        self.g_list.add_recipe(self.recipe1)
        self.g_list.add_recipe(self.recipe2)
        self.assertEqual(self.g_list.items["ingredient1"], "1 cup1 cup")  # Допустим, наши две единицы измерения объединяются вместе для строк с одинаковыми именами
        self.g_list.remove_recipe(self.recipe1)
        self.assertNotIn("ingredient2", self.g_list.items)
        self.assertEqual(self.g_list.items["ingredient1"], "1 cup")

    def test_filter_by_preferences(self):
        self.g_list.add_recipe(self.recipe1)
        self.g_list.add_recipe(self.recipe2)
        
        user_preferences = {"ingredient2"}
        self.g_list.filter_by_preferences(user_preferences)

        self.assertNotIn("ingredient2", self.g_list.items)
        self.assertIn("ingredient1", self.g_list.items)
        self.assertIn("ingredient3", self.g_list.items)

if __name__ == '__main__':
    unittest.main()