import abc


class wallet_service(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def send(self, send_money_request):
        pass

    @abc.abstractmethod
    def receive(self, receive_money_response):
        pass

    @abc.abstractmethod
    def check_balance(self, check_balance_response):
        pass
