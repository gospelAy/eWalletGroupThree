class Wallet:
    def __init__(self):
        self.balance = ""
        self.security_question = ""
        self.bank_account = ""

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def security_question(self):
        return self._securityQuestion

    @security_question.setter
    def security_question(self, security_question):
        self._securityQuestion = security_question

    @property
    def bank_account(self):
        return self._bankAccount

    @bank_account.setter
    def bank_account(self, bank_account):
        self._bankAccount = bank_account

    def __str__(self):
        return f"password={self.balance}, " \
               f"securityQuestion={self.security_question}," \
               f" bankAccount={self.bank_account})"
