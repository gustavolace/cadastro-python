from flask import Blueprint, render_template, jsonify, request, redirect, url_for, session, flash
from src.helpers.imgLinks import colorLinks
from src.services.sql import start_server 
from src.middlewares.auth import authentication_required
from src.helpers.handleRoutes import get_user_characters, get_user, login_user, register_user, check_username

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

@rotas_bp.route('/char/<int:char_id>', endpoint='character')
@authentication_required
def character(char_id, character= None, user = None):
    
    if not character:
        return "Personagem não encontrado", 404
    return render_template('char.html', user = user, personagem=character, colorLinks=colorLinks)

@rotas_bp.route('/charlist/<int:user_id>', endpoint='user')
@authentication_required
def user(user_id):
    user, characters = get_user_characters(user_id)  
    return render_template('charlist.html', user=user, personagens=characters, colorLinks = colorLinks)

@rotas_bp.route('/newchar/<int:user_id>')
@authentication_required
def newchar(user_id):
    user = get_user(user_id)
    if not user:
        return "Usuario nao encontrado", 404
    return render_template('newchar.html', user=user)

@rotas_bp.route('/login', methods=['POST'])
def validation():
    username = request.form['usuario']
    password = request.form['password']
    user = login_user(username, password)

    if user:
        session['user_id'] = user['id']
        session['username'] = user['username']
        return redirect(url_for('rotas.user', user_id = user['id']))
    else:
        return "Credenciais inválidas. Faça login novamente ou registre-se."

@rotas_bp.route('/register', methods=['POST'])
def register():
    try:
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']

        result_message = register_user(name, username, password)
        flash(result_message, 'success')
    except Exception as e:
        flash('Ocorreu um erro ao registrar o usuario. Por favor, tente novamente.', 'error')
        print(f"Ocorreu um erro: {str(e)}")
    return redirect(url_for('rotas.route_'))

@rotas_bp.route('/img', methods=['GET'])
def img():
    return jsonify(colorLinks)

@rotas_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('rotas.route_')) 

@rotas_bp.route('/username/<username>') 
def route_check_username(username):
    db_username = check_username(username)
    if db_username:
        return jsonify({'available': False})
    else:
        return jsonify({'available': True})
        