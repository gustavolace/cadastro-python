from flask import Blueprint, render_template, jsonify
from src.helpers.imgLinks import colorLinks

rotas_bp = Blueprint('rotas', __name__, template_folder='../static/templates')

def create_route(route, template):
    @rotas_bp.route(route)
    def route_function():
        return render_template(template)
    route_function.__name__ = f"route_{route.replace('/', '_').strip('_')}"
    
create_route('/', 'start.html')
create_route('/signin', 'sign-in.html')
create_route('/signup', 'sign-up.html')
create_route('/header', 'header.html')
create_route('/char', 'char.html')
create_route('/charlist', 'charlist.html')


@rotas_bp.route('/img', methods=['GET'])
def img():
    return jsonify(colorLinks)