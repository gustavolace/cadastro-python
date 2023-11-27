from flask import Blueprint, render_template

rotas_bp = Blueprint('rotas', __name__, template_folder='../static/templates')


@rotas_bp.route('/')
def index():
    return render_template('start.html')

@rotas_bp.route('/login')
def login():
    return render_template('login.html')


