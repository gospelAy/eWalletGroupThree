class users_controller:
    def __init__(self):
        self.user_service = user_service_implimentation()

    def register(self, request):
        try:
            return self.user_service.register(request)
        except ValueError as ex:
            return ex.args[0]

    def login(self, user_email, user_password):
        return self.user_service.findUser(user_email, user_password)

    def find_user_by_id(self, user_id):
        return self.user_service.findUser(user_id)

    def delete_user_by_id(self, user_id):
        return self.user_service.findUser(user_id)