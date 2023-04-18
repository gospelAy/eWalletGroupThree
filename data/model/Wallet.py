
    def __init__(self):
        self.userId = 0
        self.emailAddress = ""
        self.password = ""
        self.securityQuestion = ""
        self.bankAccount = ""

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
        def securityQuestion(self):
            return self._securityQuestion

        @securityQuestion.setter
        def securityQuestion(self, securityQuestion):
            self._securityQuestion = securityQuestion

        @property
        def bankAccount(self):
            return self._bankAccount

        @bankAccount.setter
        def password(self, password):
            self._bankAccount = bankAccount


            def __str__(self):
                return f"User(userId={self.userId}," \
                       f" emailAddress={self.emailAddress}, " \
                       f"password={self.password}, " \
                       f"securityQuestion={self.securityQuestion}," \
                       f" bankAccount={self.bankAccount})"
