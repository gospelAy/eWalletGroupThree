class TransferResponse:
    def __init__(self, success: bool, message: str):
        self.success = success
        self.message = message

    def __str__(self):
        return f"Transfer Response(success={self.success}, message='{self.message}')"
