from flask import Flask, render_template, request
# request is imported to read data sent from the browser
app = Flask(__name__) #App Instance

messages = []

#Route Decorator
@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method ==  "POST":
        # Get the message from the form input
        message = request.form.get("message", "").strip()

        if message: 
            messages.append(message)
            print("New message from form:", message)

    # Pass messages to the template
    return render_template("index.html", messages = messages)

if __name__ == "__main__":
    app.run(debug = True, port = 5050)
