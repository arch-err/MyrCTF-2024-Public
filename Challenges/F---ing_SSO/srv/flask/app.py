#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, make_response
import random
import os
import threading
import time as t

app = Flask(__name__)

with open("/flag.txt", "r") as f:
    flag = f.read()
print(flag)

DEBUG = True
DEBUG = False
REQUIRE_AUTH = True
# REQUIRE_AUTH = False
DOMAIN = "rcerebri.se"
SITE_SUBDOMAIN = "rcia"
# COOKIE = os.environ["COOKIE"]
COOKIE = "af800b536d5de83768c0a9986ed73847"


valid_cookies = []


@app.route("/")
def home():
    if REQUIRE_AUTH and request.cookies.get("_rcia_session_id") != COOKIE:
        response = make_response(
            redirect(f"https://idpi.{DOMAIN}/internal/authenticate/SSLFedAD/", code=302)
        )
        response.set_cookie(
            f"BIGipServer~rc-com-prod~{SITE_SUBDOMAIN}.{DOMAIN}-443",
            str(random.getrandbits(128)),
        )
        response.set_cookie("PhxAuthN", str(random.getrandbits(128)))
        return response

    # response = make_response(render_template("index.html"))
    response = make_response(render_template("auth.html"))
    return flag


def runHttp():
    app.run(
        debug=DEBUG,
        host="0.0.0.0",
        port=8088,
    )


def runHttps():
    app.run(
        debug=DEBUG,
        host="0.0.0.0",
        port=443,
        ssl_context=("cert.pem", "privkey.pem"),
    )


if __name__ == "__main__":
    # if not DEBUG:
    #     y = threading.Thread(target=runHttp)
    #     x = threading.Thread(target=runHttps)
    #     y.start()
    #     t.sleep(0.5)
    #     x.start()
    # else:
    #     runHttp()
    runHttp()
