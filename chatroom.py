class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

class ChatRoom: 
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

class Message: 
    message_count = 0
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_count
        message_count += 1


