from flask import Blueprint, render_template

views = Blueprint(__name__, "views")
def calculate_lines_of_code():
    python_code = """
    def say_hello():
        print("Hello, World!")

    for i in range(15000):
        print(i)
    """
    return len(python_code.strip().split('\n'))
@views.route("/")
def index():
    lines_of_code = calculate_lines_of_code()
    return render_template("home_index.html", lines_of_code=lines_of_code)

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/resume")
def resume():
    return render_template("resume.html")

@views.route("/projects")
def projects():
    return render_template("projects.html")

@views.route("/download-resume")
def downloadresume():
    return render_template("word_resume.html")