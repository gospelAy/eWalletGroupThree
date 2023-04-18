class LoginUserRequest:
    def __init__(self):
        self._email_address = ""
        self._password = ""

    def set_email_address(self, email_address):
        self._email_address = email_address

    def get_email_address(self):
        return self._email_address

    def set_password(self, password):
        self._password = password

    def get_password(self):
        return self._password


def _str_(self):
    return f"Email address: {self._email_address}, Password: {self._password}"
