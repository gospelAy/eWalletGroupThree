class wallet_controller:
    def __init__(self):
        self.wallet_service = wallet_service_implimentation()

    def send_money(self, card_number, amount):
        try:
            return self.wallet_service.send_money(card_number, amount)
        except ValueError as ex:
            return ex.args[0]

    def receive_money(self, card_number, amount):
        return self.wallet_service.receive_money(card_number, amount)

    def check_balance(self, user_id):
        return self.wallet_service.check_balance(user_id)
