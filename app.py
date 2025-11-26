from flask import Flask

app = Flask(__name__) #App Instance

#Route Decorator
@app.route("/")
def home():
    return "Chatroom is running"

if __name__ == "__main__":
    app.run(debug = True)
