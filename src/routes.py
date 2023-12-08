from flask import Blueprint, render_template, jsonify, request, redirect, url_for
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


personagens = {
    1: {'id': 1, 'name': 'Personagem 1', 'str': 8, 'int': 5, 'user_id': 1, 'hair_color': 'green', 'skin_color': 'tan'},
    2: {'id': 2, 'name': 'Personagem 2', 'user_id': 1, 'hair_color': 'red', 'skin_color': 'bege'},
    3: {'id': 3, 'name': 'Personagem 3', 'str': 6, 'int': 7, 'user_id': 2, 'hair_color': 'blue', 'skin_color': 'brown'},
}
usuarios = {
    1: {'id': 1, 'nome': 'usuario1', 'senha': 'senha1'},
    2: {'id': 2, 'nome': 'usuario2', 'senha': 'senha2'},
}

@rotas_bp.route('/char/<int:char_id>', endpoint='character')
def character(char_id):
    personagem = personagens.get(char_id)
    if personagem:
        return render_template('char.html', personagem=personagem, colorLinks = colorLinks)
    return "Personagem não encontrado", 404

@rotas_bp.route('/charlist/<int:user_id>', endpoint='user')
def user(user_id):
    personagens_do_usuario = [personagem for personagem in personagens.values() if personagem.get('user_id') == user_id]
    usuario = usuarios.get(user_id)
    if usuario:
        return render_template('charlist.html', usuario=usuario, personagens=personagens_do_usuario, colorLinks = colorLinks)
    return "Usuário não encontrado", 404

@rotas_bp.route('/newchar/<int:id>')
def newchar(id):
    usuario = usuarios.get(id)
    if usuario:
        return render_template('newchar.html', usuario=usuario)
    return "Usuário não encontrado", 404


@rotas_bp.route('/login', methods=['POST'])
def validation():
    user_name = request.form['usuario']
    senha = request.form['senha']

    for usuario_id, usuario_info in usuarios.items():
        if usuario_info['nome'] == user_name and usuario_info['senha'] == senha:
            return redirect(url_for('rotas.user', id=usuario_id))
    return "Credenciais inválidas. Tente novamente."


@rotas_bp.route('/img', methods=['GET'])
def img():
    return jsonify(colorLinks)