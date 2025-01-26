from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded credentials for login
valid_username = "Student"
valid_password = "Box5 4life"

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == valid_username and password == valid_password:
            return redirect(url_for("home"))
        else:
            error = "Invalid username or password. Please try again."
    return render_template("login.html", error=error)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/resources.html")
def resources():
    return render_template("resources.html")

@app.route("/about us.html")
def about_us():
    return render_template("about us.html")

if __name__ == "__main__":
    app.run(debug=True)