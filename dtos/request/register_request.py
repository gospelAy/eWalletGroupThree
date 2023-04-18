class RegisterRequest:
    def _init_(self):
        self._user_id = ""
        self._first_name = ""
        self._last_name = ""
        self._email_address = ""
        self._password = ""
        self._date_of_birth = ""
        self._phone_number = ""
        self._bank_account = ""
        self._security_question = ""

    def set_userId(self, user_id):
        self._user_id = user_id

    def get_userId(self):
        return self._user_id

    def set_firstName(self, first_name):
        self._first_name = first_name

    def get_firstName(self):
        return self._first_name

    def set_lastName(self, last_name):
        self._last_name = last_name

    def get_lastName(self):
        return self._last_name

    def set_emailAddress(self, email_address):
        self._email_address = email_address

    def get_emailAddress(self):
        return self._email_address

    def set_password(self, password):
        self._password = password

    def get_password(self):
        return self._password

    def set_dateOfBirth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    def get_dateOfBirth(self):
        return self._date_of_birth

    def set_security_question(self, security_question):
        self._security_question = security_question

    def get_security_question(self):
        return self._security_question