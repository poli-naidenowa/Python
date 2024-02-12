class Event:
    def __init__(self, content):
        self.clients = []
        self.content = content

    def notify(self):
        for client in self.clients:
            client.update(self.content)

    def subscribe(self, client):
        self.clients.append(client)

    def unsubscribe(self, client):
        self.clients.remove(client)
