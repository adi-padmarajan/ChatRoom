from flask import Flask, render_template, request
# request is imported to read data sent from the browser
app = Flask(__name__) #App Instance

#Route Decorator
@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method ==  "POST":
        # Get the message from the form input
        message = request.form.get("message")
        print("New message from form:", message)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
