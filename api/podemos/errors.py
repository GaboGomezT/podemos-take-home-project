class ClientAlreadyExists(Exception):
    def __init__(self):
        super().__init__("Client with this ID already exists in DB")