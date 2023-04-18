class ReceiveMoneyResponse:
    def __init__(self):
        self.receiver_id = ""
        self.amount = 0.0

    @property
    def receiver_id(self):
        return self._receiver_id

    @receiver_id.setter
    def receiver_id(self, value):
        self._receiver_id = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    def __str__(self):
        return f"Receive Money (Receiver ID = {self.receiver_id}, Amount = {self.amount})"
