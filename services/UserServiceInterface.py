import abc
from dtos.requests.RegisterUserRequest import RegisterUserRequest
from dtos.requests.LoginUserRequest import LoginUserRequest


class UserServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def register(self, register_user_request: RegisterUserRequest):
        raise NotImplementedError

    @abc.abstractmethod
    def login(self, login_user_request: LoginUserRequest):
        raise NotImplementedError
