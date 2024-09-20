from flask import Blueprint, render_template

app_bp = Blueprint('login', __name__, template_folder='templates')


@app_bp.route('/')
def login():
    return render_template('login.html')

@app_bp.route('/autos')
def autos():
    return render_template('autos.html')

