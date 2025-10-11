class User:
    def __init__(self, id: int, username: str, email: str):
        self.id = id
        self.username = username
        self.email = email

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"