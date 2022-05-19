from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = [
    "Volleyboll", "Footboll", "Ultimate Frisbee", "Capture the Flag",
    "Dance Battle"
]


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/register", method=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("sport"):
      return render_template("failure.html")
    return render_template("success.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
