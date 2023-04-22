class RegisterRequest:
    def __init__(self):
        self._phone_number = None
        self._bank_account = None
        self._security_question = None
        self._date_of_birth = None
        self._password = None
        self._email_address = None
        self._last_name = None
        self._first_name = None
        self._user_id = None

    def set_userid(self, user_id):
        self._user_id = user_id

    def get_userid(self):
        return self._user_id

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_last_name(self):
        return self._last_name

    def set_email_address(self, email_address):
        self._email_address = email_address

    def get_email_address(self):
        return self._email_address

    def set_password(self, password):
        self._password = password

    def get_password(self):
        return self._password

    def set_date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    def get_date_of_birth(self):
        return self._date_of_birth

    def set_security_question(self, security_question):
        self._security_question = security_question

    def get_security_question(self):
        return self._security_question

    def set_bank_account(self, value):
        self._bank_account = value

    def get_bank_account(self):
        return self._bank_account

    def set_phone_number(self, value):
        self._phone_number = value

    def get_phone_number(self):
        return self._phone_number

