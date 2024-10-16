#!/usr/bin/env python

from flask import Flask, render_template, request, url_for, redirect
import subprocess

app = Flask(__name__)

DEBUG=False

DEFAULT_FORMAT = "%2b%25R%0a"


@app.route("/")
@app.route("/index.html")
def index():
    cmd = request.args.get("format")

    if not cmd:
        return redirect(url_for('index')+f"?format={DEFAULT_FORMAT}")

    cmd = ["/bin/bash", "-c", f"date {cmd}"]
    try:
        stdout = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()
        return render_template("index.html", stdout=stdout)
    except subprocess.CalledProcessError as err:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0", port=8080)
