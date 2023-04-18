from abc import ABC
from typing import Any
from data.repositories.UserRepositoryInterface import UserRepositoryInterface
from data.models.User import User


class UserRepositoryInterfaceImpl(UserRepositoryInterface, ABC):
    def __init__(self):
        self.users = []

    def add_user(self, user: User) -> None:
        self.users.append(user)

    def get_user_by_id(self, user_id: int) -> Any | None:
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def get_users_by_email_address(self, email_address: str) -> List[User]:
        result = []
        for user in self.users:
            if user.email_address == email_address:
                result.append(user)
        return result
