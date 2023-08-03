from flask import Blueprint, request, render_template

auth = Blueprint('auth', __name__)

@auth.route('/result', methods=['GET', 'POST'])
def login():
    x = int(request.form.get('name'))
    if x >= 65 and x <= 80:
        head = 'A'
    elif x <= 64 and x >= 50:
        head = 'B'
    elif x <= 49 and x >= 35:
        head = 'C'
    elif x <= 34 and x >= 18:
        head = 'D'
    elif x <= 17 and x >= 0:
        head = 'F'
    else:
        head = 'Invalid Marks'
    return render_template('result.html', headtype=head)