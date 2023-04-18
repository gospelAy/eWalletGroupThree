from typing import Dict, Any


class WalletServiceImpl(WalletService):
    def __init__(self):
        self.wallets = {}

    def send(self, send_money_request: SendMoneyRequest) -> Dict[str, str]:
        sender_wallet = self.wallets.get(send_money_request.sender_id)
        receiver_wallet = self.wallets.get(send_money_request.receiver_id)
        if sender_wallet is None or receiver_wallet is None:
            return {"Status": "Error", "Message": "You inputted an invalid sender or receiver ID."}
        if sender_wallet['balance'] < send_money_request.amount:
            return {"Status": "Error", "Message": "Insufficient balance."}
        sender_wallet['balance'] -= send_money_request.amount
        receiver_wallet['balance'] += send_money_request.amount
        return {"Status": "Success", "Message": "Cash sent successfully."}

    def receive(self, receive_money_response: ReceiveMoneyResponse) -> Dict[str, str]:
        receiver_wallet = self.wallets.get(receive_money_response.receiver_id)
        if receiver_wallet is None:
            return {"Status": "Error", "Message": "You inputted an invalid receiver ID."}
        receiver_wallet['balance'] += receive_money_response.amount
        return {"Status": "Success", "Message": "Cash received successfully."}

    def check_balance(self, user_id: str) -> dict[str, str] | dict[str, str | Any]:
        wallet = self.wallets.get(user_id)
        if wallet is None:
            return {"Status": "Error", "Message": "Invalid user ID."}
        return {"Status": "Success", "Balance": wallet['balance']}
