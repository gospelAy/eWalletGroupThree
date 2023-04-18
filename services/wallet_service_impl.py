class wallet_service_impl(wallet_service):

    def __init__(self, user_service, repository):
        self.user_service = user_service
        self.repository = repository

    def send(self, send_money_request):
        sender = self.user_service.get_user_by_id(send_money_request.sender_id)
        receiver = self.user_service.get_user_by_id(send_money_request.receiver_id)
        if not sender or not receiver:
            raise ValueError("You inputted an invalid sender or receiver details.")
        if sender.balance < send_money_request.amount:
            raise ValueError("Insufficient funds.")
        sender.balance -= send_money_request.amount
        receiver.balance += send_money_request.amount
        self.repository.save_user(sender)
        self.repository.save_user(receiver)
        return send_money_response(True)

    def receive(self, receive_money_response):
        receiver = self.user_service.get_user_by_id(receive_money_response.receiver_id)
        if not receiver:
            raise ValueError("Invalid receiver ID. Try again.")
        receiver.balance += receive_money_response.amount
        self.repository.save_user(receiver)
        return receive_money_response(True)

    def check_balance(self, check_balance_request):
        # Get the user from the user service by ID
        user = self.user_service.get_user_by_id(check_balance_request.user_id)
        if not user:
            raise ValueError("Invalid user ID")

        # Return the user's current balance
        return CheckBalanceResponse(user.balance)
