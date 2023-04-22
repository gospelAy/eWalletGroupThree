import unittest

from Data.Repo.user_repo import user_repository_interface
from Data.Repo.user_repo_implimentation import user_repository_impl
from Data.model import User
from Data.Repo import user_repo_implimentation


class TestUserRepo(unittest.TestCase):

    user_repo: user_repository_interface
    user: User

    def setUp(self):
        self.user_repo = user_repository_impl()
        user = User()
        user("mike", "Josh", 0, "mike@gmail.com", "1234", "0806", "01/04/2005", "0706")

    def test_create_user(self):
        # Test that a user is created and added to the database
        self.user_repo.create_user(self.user)
        self.assertEqual(1, self.user_repo.count_users())


if __name__ == '__main__':
    unittest.main()
