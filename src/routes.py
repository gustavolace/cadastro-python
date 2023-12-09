from flask import Blueprint, render_template, jsonify, request, redirect, url_for, session, flash
from src.helpers.imgLinks import colorLinks
from werkzeug.security import generate_password_hash, check_password_hash
from src.services.sql import start_server 


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
    1: {'id': 1, 'name': 'Personagem 1', 'strength': 8, 'intelligence': 5, 'user_id': 1, 'hair_color': 'green', 'skin_color': 'tan'},
    2: {'id': 2, 'name': 'Personagem 2', 'user_id': 1, 'hair_color': 'red', 'skin_color': 'bege'},
    3: {'id': 3, 'name': 'Personagem 3', 'strength': 6, 'intelligence': 7, 'user_id': 2, 'hair_color': 'blue', 'skin_color': 'brown'},
    21: {'id': 4, 'name': 'Personagem 3', 'strength': 6, 'intelligence': 7, 'user_id': 21, 'hair_color': 'blue', 'skin_color': 'brown'},
}
usuarios = {
    1: {'id': 1, 'nome': 'usuario1', 'username': "user2", 'password': 'senha1'},
    2: {'id': 2, 'nome': 'usuario2', 'username': "user2", 'password': 'senha2'},
    3: {'id': 3, 'nome': 'usuario3', 'username': "user2", 'password': 'senha3'},
    21:{'id': 21, 'nome': 'usuario3', 'username': "user2", 'password': 'senha3'},
}


@rotas_bp.route('/char/<int:char_id>', endpoint='character')
def character(char_id):
    if 'user_id' not in session:
        return "Usuário não autenticado", 401

    session_user_id = session.get('user_id')

    db = start_server()
    query = "SELECT * FROM characters WHERE id = %s"
    db.cursor.execute(query, (char_id,))
    character = db.cursor.fetchone()  
    
    if not character:
        return "Personagem não encontrado", 404

    usuario = {'id': character['user_id']}
    if session_user_id != usuario['id']:
        return "Acesso não autorizado: permissões insuficientes", 403

    return render_template('char.html', usuario=usuario, personagem=character, colorLinks=colorLinks)


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
    db = start_server()
    username = request.form['usuario']
    password = request.form['password']

    try:
        query = "SELECT id, name, username, password FROM user WHERE username = %s"
        db.cursor.execute(query, (username,))
        user = db.cursor.fetchone()  

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('rotas.user', user_id = user['id']))
        else:
            return "Credenciais inválidas. Faça login novamente ou registre-se."
    except Exception as e:
        db.connection.rollback()
        return f"Ocorreu um erro: {str(e)}"
    finally:
        db.cursor.close()
        db.connection.close()

@rotas_bp.route('/register', methods=['POST'])
def register():

    try:
        db = start_server()
        name = request.form['name']
        user_name = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        add_user_query = "INSERT INTO user (name, username, password) VALUES (%s, %s, %s)"
        user_data = (name, user_name, hashed_password)
        db.cursor.execute(add_user_query, user_data)
        db.connection.commit()

        flash('Usuario registrado com sucesso!', 'success')
        return redirect(url_for('rotas.route_')) 
    except Exception as e:
        db.connection.rollback()
        flash('Ocorreu um erro ao registrar o usuario. Por favor, tente novamente.', 'error')
        print(f"Ocorreu um erro: {str(e)}")
        return redirect(url_for('rotas.route_')) 
    finally:
        db.cursor.close()
        db.connection.close()

@rotas_bp.route('/img', methods=['GET'])
def img():
    return jsonify(colorLinks)

@rotas_bp.route('/sql')
def sql_():  
    db = start_server()

    query =  "SELECT * FROM characters"
    db.cursor.execute(query)
    results = db.cursor.fetchall()
    db.cursor.close()
    db.connection.close()
    return jsonify({'valores': results})


@rotas_bp.route('/pagina_protegida')
def pagina_protegida():
    if 'user_id' in session:
        return "Você está logado e acessou uma página protegida."
    else:
        return redirect(url_for('nome_da_rota_de_login'))
    
@rotas_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('rotas.route_')) 