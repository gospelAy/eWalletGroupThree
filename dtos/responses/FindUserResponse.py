class FindUserResponse:
    def __init__(self):
        self.email_address = ""
        self.first_name = ""
        self.last_name = ""

    def set_email_address(self, email_address):
        self.email_address = email_address

    def get_email_address(self):
        return self.email_address

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def __str__(self):
        return f"First name: {self.first_name}, Last Name: {self.last_name},"\
            f"Email Address: {self.email_address}"
