class User:
    def __init__(self):
        self._first_name = ""
        self._last_name = ""
        self._user_Id = 0
        self._email_address = ""
        self._password = ""
        self._date_of_birth = ""
        self._date_register = ""
        self._phone_number = ""

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, new_firstname: str):
        self._first_name = new_firstname

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, new_last_name: str):
        self._last_name = new_last_name

    @property
    def user_id(self):
        return self._user_Id

    @user_id.setter
    def user_id(self, new_user_id: str):
        self._user_Id = new_user_id

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, new_email_address: str):
        self._email_address = new_email_address

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password: str):
        self._password = new_password

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, new_date_of_birth: str):
        self._date_of_birth = new_date_of_birth

    @property
    def date_register(self):
        return self._date_register

    @date_register.setter
    def date_register(self, new_date_register: str):
        self.date_register = new_date_register

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, new_phone_number: str):
        self.phone_number = new_phone_number

    def __str__(self):
        return f"User(firstName='{self.first_name}'," \
               f" lastName='{self.last_name}'," \
               f" userId={self.user_id}, " \
               f"emailAddress='{self.email_address}'," \
               f" password='{self.password}', " \
               f"dateOfBirth='{self.date_of_birth}', " \
               f"phoneNumber={self.phone_number}'," \
               f"dateRegister='{self.date_register}')"


