#!/usr/bin/env python

from flask import Flask


app = Flask(__name__)

DEBUG = True

codes = {
    "400": "Bad Request",
    "401": "Unauthorized",
    "402": "Payment Required",
    "403": "Forbidden",
    "404": "Not Found",
    "405": "Method Not Allowed",
    "406": "Not Acceptable",
    "407": "Proxy Authentication Required",
    "408": "Request Timeout",
    "409": "Conflict",
    "410": "Gone",
    "411": "Length Required",
    "412": "Precondition Failed",
    "413": "Request Entity Too Large",
    "414": "Request-URI Too Long",
    "415": "Unsupported Media Type",
    "416": "Requested Range Not Satisfiable",
    "417": "Expectation Failed",
    "418": "I'm a teapot",
    "419": "Page Expired",
    "420": "Method Failure",
    "421": "Misdirected Request",
    "422": "Unprocessable Entity",
    "423": "Locked",
    "424": "Failed Dependency",
    "426": "Upgrade Required",
    "508": "Loop Detected",
}


message = "ivegotclienterrors"

alphabet = "abcdefghijklmnopqrstuvwxyz"

numbers = [alphabet.index(n)+1 for n in message]

numbers.append(508)

counter = 0


@app.route("/")
def home():
    global counter
    code = numbers[counter]

    if code < 100:
        code += 400

    counter += 1

    if counter+1 > len(numbers):
        counter = 0
    return f"{code} {codes[str(code)]}", code


if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0", port=8888)
