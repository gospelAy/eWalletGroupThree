class FindWalletBalanceResponse:
    def __init__(self):
        self._wallet_balance = ""

    def get_wallet_balance(self):
        return self._wallet_balance

    def set_wallet_balance(self, wallet_balance):
        self._wallet_balance = wallet_balance

    def __str__(self):
        return f"Wallet Balance: {self._wallet_balance}"
