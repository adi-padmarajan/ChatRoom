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
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if(self.chatroom):
            print(f"{self.user_name} is already in Chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.user_name} has joined {chatroom.room_name}")

    def leave_chatroom(self, chatroom):
        if not self.chatroom:
            print(f"{self.user_name} is not in any Chatroom")
        
        


room = Chatroom("Jujutsu High Group Chat")

user1 = User("Satoru Gojo")
user2 = User("Ryomen Sukuna")

user1.join_chatroom(room)
user2.join_chatroom(room)











