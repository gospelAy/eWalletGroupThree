class BankAccount:
    def __init__(self):
        self._balance = ""
        self._security_question = ""
        self._bank_account = ""

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def security_question(self):
        return self._security_question

    @security_question.setter
    def security_question(self, security_question):
        self._security_question = security_question

    @property
    def bank_account(self):
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        self._bank_account = bank_account

    def __str__(self):
        return f"Balance = {self.balance}, " \
               f"Security Question = {self.securityQuestion}, " \
               f"Bank Account = {self.bankAccount}"
