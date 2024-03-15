from flask import Blueprint, render_template, redirect

helloworld_bp = Blueprint("helloworld",__name__, template_folder= "templates")


@helloworld_bp.route("/")
def index():
    return render_template("helloworld/bootcamp.html")


@helloworld_bp.route("/hello")
def hello():
    return "Hello World!"


@helloworld_bp.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}"

