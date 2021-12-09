from flask import Blueprint, render_template, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def homepage():
    return render_template("index.html")

@views.route("")
def page_one():
    return render_template("")

@views.route("")
def page_two():
    return render_template("")

@views.route("")
def page_three():
    return render_template("")

@views.route("")
def page_four():
    return render_template("")

@views.route("")
def page_five():
    return render_template("")

@views.route("/javascript")
def javascript_redirect():
    return redirect(url_for("views.homepage"))

@views.route("/js")
def js_redirect():
    return redirect(url_for("views.homepage"))

@views.route("/home")
def home_redirect():
    return redirect(url_for("views.homepage"))

@views.route("/admin")
def admin():
    return render_template("admin.html")
