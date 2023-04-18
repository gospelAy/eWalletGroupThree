from data.models.User import User
from abc import ABC, abstractmethod
from typing import List


class UserRepositoryInterface(ABC):
    @abstractmethod
    def add_user(self, user: User) -> None:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_users_by_email_address(self, email_address: str) -> List[User]:
        pass
