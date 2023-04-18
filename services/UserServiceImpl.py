class UserServiceImpl(UserService):
    def __init__(self):
        self.users = {}

    def register(self, register_user_request: RegisterUserRequest) -> Dict[str, str]:
        if register_user_request.username in self.users:
            return {"Status": "Error", "Message": "User with the inputted username already exists."}
        self.users[register_user_request.username] = {
            "Username": register_user_request.username,
            "Password": register_user_request.password,
            "Email": register_user_request.email
        }
        return {"Status": "Success", "Message": "User registered successfully."}

    def login(self, login_user_request: LoginUserRequest) -> Dict[str, str]:
        if login_user_request.username not in self.users:
            return {"Status": "Error", "Message": "User with the inputted username not found."}
        if self.users[login_user_request.username]['password'] != login_user_request.password:
            return {"Status": "Error", "Message": "You inputted an incorrect password."}
        return {"Status": "Success", "Message": "You have logged in successfully."}
