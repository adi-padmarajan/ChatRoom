from flask import Flask, render_template, request
# request is imported to read data sent from the browser

from chatroom import Chatroom, User #import from chatroom.py
app = Flask(__name__) #App Instance

chatroom = Chatroom("Jujutsu High School")
current_user = User("You")
chatroom.add_user(current_user)


#Route Decorator
@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method ==  "POST":
        # Get the message from the form input
        message_text = request.form.get("message", "").strip()

        if message_text: 
            # Use existing OOP
            chatroom.broadcast_message(current_user, message_text)
            print("New message from form:", message_text)

    # Pass messages to the template
    return render_template(
        "index.html", 
        messages = chatroom.messages,
        room_name = chatroom.room_name,
        online_count=len(chatroom.users)
    )

if __name__ == "__main__":
    app.run(debug = True, port = 5050)
