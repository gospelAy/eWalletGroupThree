class User:
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.userId = 0
        self.emailAddress = ""
        self.password = ""
        self.dateOfBirth = ""
        self.dateRegister = ""
        self.phoneNumber = ""

        @property
        def firstName(self):
            return self._firstName

        @firstName.setter
        def first_name(self, first_name):
            self._firstName = firstName

        @property
        def lastName(self):
            return self._lastName

        @lastName.setter
        def lastName(self, lastName):
            self._lastName = lastName

        @property
        def userId(self):
            return self._userId

        @userId.setter
        def userId(self, userId):
            self._userId = userId

        @property
        def emailAddress(self):
            return self._emailAddress

        @emailAddress.setter
        def emailAddress(self, emailAddress):
            self._emailAddress = emailAddress

        @property
        def password(self):
            return self._password

        @password.setter
        def password(self, password):
            self._password = password

        @property
        def dateOfBirth(self):
            return self._dateOfBirth

        @dateOfBirth.setter
        def dateOfBirth(self, dateOfBirth):
            self._dateOfBirth = dateOfBirth

        @property
        def dateRegister(self):
            return self._dateRegister

        @dateRegister.setter
        def dateRegister(self, dateRegister):
            self.dateRegister = dateRegister

        @property
        def phoneNumber(self):
            return self._phoneNumber

        @phoneNumber.setter
        def phoneNumber(self, phoneNumber):
            self.phoneNumber = phoneNumber

        def __str__(self):
            return f"User(firstName='{self.firstName}'," \
                   f" lastName='{self.lastName}'," \
                   f" userId={self.userId}, " \
                   f"emailAddress='{self.emailAddress}'," \
                   f" password='{self.password}', " \
                   f"dateOfBirth='{self.dateOfBirth}', " \
                   f"phoneNumber={self.phoneNumber}'," \
                   f"dateRegister='{self.dateRegister}')"
