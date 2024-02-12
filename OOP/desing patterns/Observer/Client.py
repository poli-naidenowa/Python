from Observer import Observer


class Client(Observer):
    def __init__(self, username):
        self.username = username
        self._email = {}


