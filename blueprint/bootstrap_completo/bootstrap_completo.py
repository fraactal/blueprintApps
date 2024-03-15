from flask import Blueprint, render_template, redirect

bootstrap_completo_bp = Blueprint("bootstrap_completo",__name__, template_folder= "templates")


@bootstrap_completo_bp.route("/")
def index():
    return render_template("bootstrap_completo/bootstrap_completo.html")


@bootstrap_completo_bp.route("/hello")
def hello():
    return "Hello World!"


