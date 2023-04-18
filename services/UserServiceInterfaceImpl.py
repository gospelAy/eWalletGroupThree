from typing import Dict, Any


def generate_account_number(phone_number: str) -> str:
    numeric_phone_number = ''.join(filter(str.isdigit, phone_number))
    account_number = 'AC' + numeric_phone_number
    return account_number


class UserServiceImpl(UserService):
    def __init__(self):
        self.users = {}

    def register(self, register_user_request: RegisterUserRequest) -> Dict[str, str]:
        if register_user_request.email in self.users:
            return {"Status": "Error", "Message": "User with the inputted email already exists."}
        if not register_user_request.phone_number.startswith("+234") or len(register_user_request.phone_number) != 13:
            return {"Status": "Error", "Message": "Phone number must begin with '+234' and have 13 characters."}
        if not register_user_request.phone_number[4:].isdigit():
            return {"Status": "Error", "Message": "Phone number must contain only numbers."}
        account_number = self.generate_account_number(register_user_request.phone_number)
        self.users[register_user_request.username] = {
            "First name": register_user_request.first_name,
            "Last name": register_user_request.last_name,
            "Email address": register_user_request.email,
            "Password": register_user_request.password,
            "Date of birth": register_user_request.date_of_birth,
            "Phone number": register_user_request.phone_number,
            "Security question": register_user_request.security_question,
        }
        success_message = f"You have registered successfully. Your generated account number is {account_number}."
        return {"Status": "Success", "Message": success_message}

    def login(self, login_user_request: LoginUserRequest) -> Dict[str, str]:
        if login_user_request.username not in self.users:
            return {"Status": "Error", "Message": "User with the inputted username not found."}
        if self.users[login_user_request.username]['password'] != login_user_request.password:
            return {"Status": "Error", "Message": "You inputted an incorrect password."}
        return {"Status": "Success", "Message": "You have logged in successfully."}



from UserServiceInterface import UserServiceInterface
from dtos.requests.RegisterUserRequest import RegisterUserRequest
from dtos.requests.LoginUserRequest import LoginUserRequest

class UserServiceInterfaceImpl(UserServiceInterface):

    def register(self, register_user_request: RegisterUserRequest):
        # Implement the logic for registering a user here
        user_id = register_user_request.get_user_id()
        first_name = register_user_request.get_first_name()
        last_name = register_user_request.get_last_name()
        email_address = register_user_request.get_email_address()
        password = register_user_request.get_password()
        date_of_birth = register_user_request.get_date_of_birth()
        phone_number = register_user_request.get_phone_number()
        bank_account = register_user_request.get_bank_account()
        security_question = register_user_request.get_security_question()

        # Register the user in the database or user management system
        # and return the user ID if successful
        return user_id

    def login(self, login_user_request: LoginUserRequest):
        # Implement the logic for logging in a user here
        email_address = login_user_request.get_email_address()
        password = login_user_request.get_password()

        # Check if the email address and password match with a registered user
        # in the database or user management system
        # and return True if the credentials are valid
        return True
