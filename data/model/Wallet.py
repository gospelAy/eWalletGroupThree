
    def __init__(self):

        self.balance = ""
        self.securityQuestion = ""
        self.bankAccount = ""



        @property
        def balance(self):
            return self._balance

        @balance.setter
        def password(self, balance):
            self._balance = balance

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
                return f"password={self.balance}, " \
                       f"securityQuestion={self.securityQuestion}," \
                       f" bankAccount={self.bankAccount})"
