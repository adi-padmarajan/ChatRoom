from flask import Flask, render_template, request, redirect
# request is imported to read data sent from the browser

from chatroom import Chatroom, User #import from chatroom.py
app = Flask(__name__) #App Instance

#Create Chatroom
chatroom = Chatroom("Jujutsu High School")

current_user = User("You")
gojo = User("Satoru Gojo")
sukuna = User("Ryomen Sukuna")

chatroom.add_user(current_user)
chatroom.add_user(gojo)
chatroom.add_user(sukuna)

chatroom.broadcast_message(sukuna, "I feel bad taking on a handicap.")
chatroom.broadcast_message(gojo, "I am still standing")


#Root -> send people to the landing page
@app.route("/")
def root():
    return redirect("/welcome")


# Landing page
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


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
        online_count=len(chatroom.users),
        current_user_name = current_user.user_name
    )

@app.route("/create")
def create():
    return "Create chatroom page coming soon"


@app.route("/join")
def join():
    return "Join chatroom page coming soon"

if __name__ == "__main__":
    app.run(debug = True, port = 5050)
