from Data.Repo.user_repo import user_repository_interface


class user_repository_impl(user_repository_interface):
    def __init__(self):
        self.balance = 0
        self.count = 0
        self.users = []

    def create_user(self, user):
        user_has_not_been_saved = user.user_id == 0
        if user_has_not_been_saved:
            user.user_id(self.generate_id(), self.generate_balance())
            self.users.append(user)
            self.count += 1
        return user

    def generate_id(self):
        return self.count + 1

    def find_by_id(self, user_id):
        for user in self.users:
            if user.get_id() == user_id:
                return user
        return None

    def generate_balance(self):
        return self.balance

    def generate_account_number(self, user):
        return user.get_id + 8765

    def delete(self, user_id):
        for user in self.users:
            if user.getId() == user_id:
                self.users.remove(user)
                self.count -= 1
                break

    def count(self):
        return self.count

