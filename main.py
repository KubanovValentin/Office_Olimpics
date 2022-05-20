from flask import Flask, render_template, request, redirect

app = Flask(__name__)

SPORTS = [
    "Volleyboll", "Footboll", "Ultimate Frisbee", "Capture the Flag",
    "Dance Battle"
]
REGISTRANTS = {}


@app.route("/")
def index():

    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():

    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name!")

    sport = request.form.getlist("sport")
    if not sport:
        return render_template("error.html", message="Missing sport!")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport!")
    REGISTRANTS[name] = sport
    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
