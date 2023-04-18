from typing import Dict, Any


class UserServiceImpl(UserService):
    def __init__(self):
        self.users = {}

    def register(self, register_user_request: RegisterUserRequest) -> Dict[str, str]:
        if register_user_request.email in self.users:
            return {"Status": "Error", "Message": "User with the inputted email already exists."}
        if not register_user_request.phone_number.startswith("+234") or len(register_user_request.phone_number) != 13:
            return {"Status": "Error", "Message": "Phone number must begin with '+234' and have 13 characters."}
        if not register_user_request.phone_number[4:].isDigit():
            return {"Status": "Error", "Message": "Phone number must contain only numbers."}
        self.users[register_user_request.username] = {
            "First name": register_user_request.first_name,
            "Last name": register_user_request.last_name,
            "Email address": register_user_request.email,
            "Password": register_user_request.password,
            "Date of birth": register_user_request.date_of_birth,
            "Phone number": register_user_request.phone_number,
            "Security question": register_user_request.security_question,
        }
        return {"Status": "Success", "Message": "You have registered successfully."}

    def login(self, login_user_request: LoginUserRequest) -> Dict[str, str]:
        if login_user_request.username not in self.users:
            return {"Status": "Error", "Message": "User with the inputted username not found."}
        if self.users[login_user_request.username]['password'] != login_user_request.password:
            return {"Status": "Error", "Message": "You inputted an incorrect password."}
        return {"Status": "Success", "Message": "You have logged in successfully."}
