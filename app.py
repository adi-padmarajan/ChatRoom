from flask import Flask, render_template, request, redirect
from chatroom import Chatroom, User  # import from chatroom.py

app = Flask(__name__)

# ---------- Create Chatroom and Users ----------

chatroom = Chatroom("HCI Research Project")

current_user = User("You")
jasmine = User("Jasmine")
brian = User("Brian")
madi = User("Madison")
fintan = User("Fintan")

chatroom.add_user(current_user)
chatroom.add_user(jasmine)
chatroom.add_user(brian)
chatroom.add_user(madi)
chatroom.add_user(fintan)

chatroom.broadcast_message(jasmine, "Are we all down to meet tomorrow for our presentation prep.")
chatroom.broadcast_message(madi, "Yes! I will have my script ready.")
chatroom.broadcast_message(brian, "What is our presentation time limit? ")
chatroom.broadcast_message(fintan, "No more than 7 minutes, so probably around 1.5 minutes of speaking time for each.")


# ---------- Routes ----------

# Root -> send people to the landing page
@app.route("/")
def root():
    return redirect("/welcome")


# Landing page
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


# Main chat page
@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        # Get the message from the form input
        message_text = request.form.get("message", "").strip()

        if message_text:
            chatroom.broadcast_message(current_user, message_text)
            print("New message from form:", message_text)

    # Pass messages to the template
    return render_template(
        "index.html",
        messages=chatroom.messages,
        room_name=chatroom.room_name,
        online_count=len(chatroom.users),
        current_user_name=current_user.user_name,
    )


@app.route("/create")
def create():
    return "Create chatroom page coming soon"


@app.route("/join")
def join():
    return redirect("/chat")



if __name__ == "__main__":
    app.run(debug=True, port=5050)
