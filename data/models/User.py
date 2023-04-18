class User:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.user_id = 0
        self.email_address = ""
        self.password = ""
        self.date_of_birth = ""
        self.date_registered = ""
        self.phone_number = ""

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        self._email_address = email_address

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    @property
    def date_registered(self):
        return self._date_registered

    @date_registered.setter
    def date_registered(self, date_registered):
        self._date_registered = date_registered

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number

    def __str__(self):
        return f"User(First Name = '{self.first_name}'," \
               f" Last Name = '{self.last_name}'," \
               f" User Id = {self.user_id}, " \
               f"Email Address = '{self.email_address}'," \
               f"Password = '{self.password}', " \
               f"Date Of Birth = '{self.date_of_birth}', " \
               f"Phone Number = {self.phone_number}," \
               f"Date Register = '{self.date_registered}')"
