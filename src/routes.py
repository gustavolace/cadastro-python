from flask import Blueprint, render_template



rotas_bp = Blueprint('rotas', __name__, template_folder='views/pages')


@rotas_bp.route('/')
def index():
    return render_template('login/index.html')
