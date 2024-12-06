class User:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    def login(self, username: str, password: str) -> bool:
        pass

    def register(self):
        pass