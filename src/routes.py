from flask import Blueprint, render_template

rotas_bp = Blueprint('rotas', __name__, template_folder='../static/templates')


@rotas_bp.route('/')
def index():
    return render_template('start.html')

@rotas_bp.route('/signin')
def signin():
    return render_template('login.html')

@rotas_bp.route('/signup')
def signup():
    return render_template('g.html')

@rotas_bp.route('/char')
def char():
    return render_template('char.html')

