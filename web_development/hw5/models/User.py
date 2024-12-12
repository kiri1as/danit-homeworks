class User:
    def __init__(self, username: str, email: str, password: str, user_id=None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password

    @classmethod
    def from_dict(cls, data: dict):
        user = cls(data['username'], data['email'], data['password'], data['user_id'])
        return user

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'password': self.password
        }
