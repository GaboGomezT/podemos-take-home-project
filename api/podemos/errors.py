class ClientAlreadyExists(Exception):
    def __init__(self):
        super().__init__("Client with this ID already exists in DB")

class GroupAlreadyExists(Exception):
    def __init__(self):
        super().__init__("Group with this ID already exists in DB")

class AccountAlreadyExists(Exception):
    def __init__(self):
        super().__init__("Accounts with this ID already exists in DB")
class MissingGroup(Exception):
    def __init__(self):
        super().__init__("You are trying to create an account for a group that doesn't exist")
class PaymentExceedsDebt(Exception):
    def __init__(self):
        super().__init__("Payment recieved for account is greater than remaining debt.")