from flask import Flask, render_template, request
from scripts.PostScriptWebVariant import hack_plc

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/hacks")
def show_hacks():
    return render_template('hacks.html')

@app.route("/hack1", methods=["GET", "POST"])
def hack1():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        fill_time = request.form["fill_time"]
        empty_time = request.form["empty_time"]

        message = hack_plc(username, password, fill_time, empty_time)

    return render_template("hack1.html", message=message)

@app.route("/AutomatedAlwaysOffScript", methods=["GET", "POST"])
def AutomatedAlwaysOffScript():
    if request.method == "POST":
        from scripts.AutomatedAlwaysOffScriptWebVariant import start
        shouldRun = request.form["shouldRun"]
        start(shouldRun)
    return render_template("AutomatedAlwaysOffScript.html")