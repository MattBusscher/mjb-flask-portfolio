from flask import Blueprint, render_template

views = Blueprint(__name__, "views")
@views.route("/")
def index():
    return render_template("home_index.html")

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/resume")
def resume():
    return render_template("resume.html")

@views.route("/projects")
def projects():
    return render_template("projects.html")