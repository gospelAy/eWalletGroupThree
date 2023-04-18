
class user_repository_interface:

    def _init_(self):
        self.users = {}

    def create_user(self, user):
        self.users[user.id] = user

    def find_user_by_id(self, user_id):
        return self.users.get(user_id)

    def delete_user_by_id(self, user_id):
        if user_id in self.users:
            del self.users[user_id]

    def count_users(self):
        self.users.__len__()

