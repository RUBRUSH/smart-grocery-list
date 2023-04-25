import unittest
from app.user import User
from app.database import Database

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user1 = User("test_user1", "test1@example.com", "password1234", preferences={"vegan"})
        self.user2 = User("test_user2", "test2@example.com", "password5678", preferences={"gluten-free"})

    def test_add_preference(self):
        self.user1.add_preference("vegetarian")
        self.assertIn("vegetarian", self.user1.preferences)

    def test_remove_preference(self):
        self.user1.remove_preference("vegan")
        self.assertNotIn("vegan", self.user1.preferences)

    def test_save_and_load(self):
        db = Database()
        
        # Save the user into the db
        self.user1.save(db)

        # Try to load the saved user
        loaded_user = User.load("test_user1", "password1234", db)
        self.assertIsNotNone(loaded_user)
        self.assertEqual(self.user1.username, loaded_user.username)
        self.assertEqual(self.user1.email, loaded_user.email)
        self.assertEqual(self.user1.preferences, loaded_user.preferences)

    def test_load_wrong_password(self):
        db = Database()

        # Save the user into the db
        self.user1.save(db)

        # Try to load the saved user with wrong password
        loaded_user = User.load("test_user1", "wrong_password", db)
        self.assertIsNone(loaded_user)

    def test_save_existing_user(self):
        db = Database()

        # Try to save the same user twice
        self.user1.save(db)
        self.assertRaises(ValueError, self.user1.save, db)

if __name__ == '__main__':
    unittest.main()