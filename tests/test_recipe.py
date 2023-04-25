import unittest
from app.recipe import Recipe
from app.database import Database

class TestRecipe(unittest.TestCase):

    def setUp(self):
        db = Database()
        self.all_recipes = db.recipes

        self.recipe1 = Recipe(
            id="1",
            title="Test Recipe",
            ingredients=[
                {"name": "ingredient1", "quantity": "1 cup"},
                {"name": "ingredient2", "quantity": "2 tbsp"},
            ],
            instructions="Mix ingredient1 and ingredient2.",
            tags={"easy", "quick"},
        )

    def test_add_tag(self):
        self.recipe1.add_tag("vegetarian")
        self.assertIn("vegetarian", self.recipe1.tags)

    def test_remove_tag(self):
        self.recipe1.remove_tag("easy")
        self.assertNotIn("easy", self.recipe1.tags)

    def test_load_from_json(self):
        recipe_json = {
            "id": "1",
            "title": "Test Recipe",
            "ingredients": [
                {"name": "ingredient1", "quantity": "1 cup"},
                {"name": "ingredient2", "quantity": "2 tbsp"},
            ],
            "instructions": "Mix ingredient1 and ingredient2.",
            "tags": ["easy", "quick"],
        }
        recipe = Recipe.load_from_json(recipe_json)
        self.assertEqual(recipe.id, self.recipe1.id)
        self.assertEqual(recipe.title, self.recipe1.title)
        self.assertEqual(recipe.ingredients, self.recipe1.ingredients)
        self.assertEqual(recipe.instructions, self.recipe1.instructions)
        self.assertEqual(recipe.tags, self.recipe1.tags)

if __name__ == '__main__':
    unittest.main()