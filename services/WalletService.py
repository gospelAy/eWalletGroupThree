import abc


class WalletService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def send(self, SendMoneyRequest):
        pass

    @abc.abstractmethod
    def receive(self, ReceiveMoneyResponse):
        pass

    @abc.abstractmethod
    def check_balance(self, CheckBalanceResponse):
        pass
