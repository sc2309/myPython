from flask import Blueprint, render_template

views = Blueprint('views', __name__)

#my_variable = "Hello from Python!"

@views.route('/')
def index():
    lst = []
    for i in range(1,11):
        lst.append(i)
    return render_template('index.html', my_variable=lst)