class Chatroom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []
    
    def display_chatroom_name(self):
        print(f"{self.room_name}\n")
    
    def add_user(self, user):
        self.users.append(user)
    
    def remove_user(self, user):
        self.users.remove(user)
    
    def broadcast_message(self, sender, message_contents):
        message = Message(sender, message_contents)
        self.messages.append(message_contents)
        print(message)

class Message:
    count = 0
    def __init__(self, sender, message_contents):
        self.sender = sender
        self.message_contents = message_contents
        self.message_id = Message.count
        Message.count += 1
    
    def __str__(self):
        return f"{self.message_id}  {self.sender.user_name}:  {self.message_contents}"

class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if(self.chatroom):
            print(f"{self.user_name} is already in the Chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.user_name} has joined {chatroom.room_name}")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.user_name} is not the Chatroom")
        else:
            chatroom.remove_user(self)
            print(f"{self.user_name} has left the {chatroom.room_name}.")
            chatroom = None 

    def send_message(self, message_content):
        if not self.chatroom:
            print(f"{self.user_name} is not in the Chatroom")
        else: 
            self.chatroom.broadcast_message(self, message_content)


        
room = Chatroom("Jujutsu High Group Chat")
room.display_chatroom_name()

user1 = User("Ryomen Sukuna")
user2= User("Satoru Gojo")

user1.join_chatroom(room)
user2.join_chatroom(room)

user1.send_message("I feel bad taking on a handicap.")
user2.send_message("Sukuna, I am not Satoru Gojo because I am the strongest. I am the strongest because I am Satoru Gojo.")













