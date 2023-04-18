import unittest
from my_module import User, UserDatabase


class TestUserDatabase(unittest.TestCase):
    def setUp(self):
        self.user_db = UserDatabase()
        self.user = User(name="John", email="john@example.com")

    def test_create_user(self):
        # Test that a user is created and added to the database
        created_user = self.user_db.create_user(self.user)
        self.assertEqual(created_user, self.user)
        self.assertIn(created_user, self.user_db.users)

        # Test that a user with an existing ID is not created
        existing_user = User(name="Jane", email="jane@example.com", id=1)
        created_existing_user = self.user_db.create_user(existing_user)
        self.assertNotEqual(created_existing_user, existing_user)
        self.assertNotIn(created_existing_user, self.user_db.users)

    def test_find_by_id(self):
        # Test that find_by_id returns the correct user
        self.user_db.create_user(self.user)
        found_user = self.user_db.find_by_id(1)
        self.assertEqual(found_user, self.user)

        # Test that find_by_id returns None when user is not found
        not_found_user = self.user_db.find_by_id(2)
        self.assertIsNone(not_found_user)

    def test_delete(self):
        # Test that a user is deleted from the database
        self.user_db.create_user(self.user)
        self.user_db.delete(1)
        self.assertNotIn(self.user, self.user_db.users)
        self.assertEqual(self.user_db.count, 0)

        # Test that deleting a non-existent user doesn't change the database
        self.user_db.delete(2)
        self.assertNotIn(self.user, self.user_db.users)
        self.assertEqual(self.user_db.count, 0)


if __name__ == '__main__':
    unittest.main()

#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()
