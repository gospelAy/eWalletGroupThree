import abc
from dtos.requests.TransferRequest import TransferRequest


class WalletServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def transfer_money(self, transfer_request: TransferRequest):
        raise NotImplementedError
