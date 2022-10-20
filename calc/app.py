# Put your app in here.
from flask import Flask, request
from operations import *


app = Flask(__name__)
print('hi')


@app.route("/<operation>")
def do_math(operation):
    """perform the operation that matches the route name."""

    a = request.args.get("a")
    b = request.args.get("b")
    val = eval(operation+f"({a},{b})")

    return f"<h1>{val}</h1>"

# Looks like I already did the shortcut in my original!
# I will do it again, adding the "/math"


@app.route("/math/<operation>")
def do__more_math(operation):
    """perform the operation that matches the route name."""

    a = request.args.get("a")
    b = request.args.get("b")
    val = eval(operation+f"({a},{b})")

    return f"<h1>{val}</h1>"
