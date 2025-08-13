from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Homepage</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"
@app.route("/")
def home():
    return render_template("home.html", title="Homepage", name="Asif")
@app.route("/profile")
def profile():
    return render_template("profile.html", name="Asif", age=25)


if __name__ == "__main__":
    app.run(debug=True)
