from flask import Blueprint, request, render_template

auth = Blueprint('auth', __name__)

@auth.route('/result', methods=['GET', 'POST'])
def login():
    M = int(request.form.get('math_marks'))
    S = int(request.form.get('science_marks'))
    EH = int(request.form.get('EngHin_marks'))
    C = int(request.form.get('Comp_marks'))
    S = int(request.form.get('SSC_marks'))
    T = int(request.form.get('total_marks'))
    sum = M + S + EH + C + S
    head = sum/T * 100
    return render_template('result.html', headtype=head)