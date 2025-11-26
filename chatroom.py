class Chatroom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []
    
    def add_user(self, user):
        self.users.append(user)
    
    def remove_user(self, user):
        self.users.remove(user)

class User:
    def __init__(self, user_name):
        self.user_name = user_name
    

room = Chatroom("Jujutsu High Group Chat")
user1 = User("Satoru Gojo")











