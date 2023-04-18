class TransferRequest:
    def __init__(self):
        self.receiver_account_number = ""
        self.transfer_amount = ""
        self.transfer_pin = ""

    @property
    def receiver_account_number(self):
        return self._receiver_account_number

    @receiver_account_number.setter
    def receiver_account_number(self, value):
        self._receiver_account_number = value

    @property
    def transfer_amount(self):
        return self._transfer_amount

    @transfer_amount.setter
    def transfer_amount(self, value):
        self._transfer_amount = value

    @property
    def transfer_pin(self):
        return self._transfer_pin

    @transfer_pin.setter
    def transfer_pin(self, value):
        self._transfer_pin = value

    def _str_(self):
        return f"Transaction(Receiver account number = {self._receiver_account_number}, " \
               f"Transfer amount = {self._transfer_amount}, Transfer pin = {self._transfer_pin})"
