from abc import ABC, abstractmethod

from Data.model.User import User


class user_repository_interface(ABC):

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    def find_user_by_id(self, user_id: int) -> User:
        pass

    def delete_user_by_id(self, user_id: int) -> None:
        pass

    def count_users(self):
        pass
