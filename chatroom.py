class ChatRoom:
    def __init__(self):
        self.users = []
        self.messages = []

class User(ChatRoom):
    def __init__(self, username):
        self.username = username

class Message(ChatRoom):
    def __init__(self, content):
        self.content = content


user1 = User("Satoru Gojo")
user2 = User("Ryomen Sukuna")












