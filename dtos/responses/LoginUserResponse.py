class LoginUserResponse:
    def __init__(self):
        self._email_address = ""

    def set_email_address(self, email_address):
        self._email_address = email_address

    def get_email_address(self):
        return self._email_address

    def _str_(self):
        return f"Email address: {self._email_address}"
