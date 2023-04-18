import abc


class UserService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def register(self, RegisterUserRequest):
        pass

    @abc.abstractmethod
    def login(self, LoginUserRequest):
        pass
