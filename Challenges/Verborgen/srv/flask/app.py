#!/usr/bin/env python

from flask import Flask, render_template, request  # , url_for, redirect

# import subprocess

# from flask.helpers import make_response

app = Flask(__name__)

DEBUG = True


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/robots.txt")
def robots_txt():
    return render_template("robots_txt.html")


@app.route("/calc_6432647836", methods=["POST", "GET"])
def webshell():
    PS1 = "Calculate: "

    if request.method == "POST":
        cmd = request.form["calc"]
        if cmd:
            stdout = str(eval(cmd))
            return render_template("calc.html", stdout=stdout, PS1=PS1)

    return render_template("calc.html", PS1=PS1)


if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0", port=8888)
