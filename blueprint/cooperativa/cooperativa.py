from flask import Blueprint, render_template, redirect

cooperativa_bp = Blueprint("cooperativa",__name__, template_folder= "templates")


@cooperativa_bp.route("/")
def index():
    return render_template("cooperativa/cooperativa.html")


""" @helloworld_bp.route("/hello")
def hello():
    return "Hello World!"


@helloworld_bp.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}"

"""
