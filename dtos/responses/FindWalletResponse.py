class FindWalletResponse:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.wallet_balance = ""

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_wallet_balance(self, wallet_balance):
        self.wallet_balance = wallet_balance

    def get_wallet_balance(self):
        return self.wallet_balance

    def __str__(self):
        return f"First name: {self.first_name}, Last Name: {self.last_name}, Wallet Balance: {self.wallet_balance}"
