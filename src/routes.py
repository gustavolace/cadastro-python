from flask import Blueprint, render_template, jsonify, request, redirect, url_for, session, flash
from src.helpers.imgLinks import colorLinks
from werkzeug.security import generate_password_hash, check_password_hash
from src.services.sql import start_server 
from src.middlewares.auth import authentication_required


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
def character(char_id, character=None, usuario_id=None):
    if not character:
        return "Personagem não encontrado", 404

    return render_template('char.html', usuario_id=usuario_id, personagem=character, colorLinks=colorLinks)



@rotas_bp.route('/charlist/<int:user_id>', endpoint='user')
@authentication_required
def user(user_id):
    db = start_server()
    query = "SELECT * FROM characters WHERE user_id = %s"
    db.cursor.execute(query, (user_id,))
    results = db.cursor.fetchall()

    if not results:
        return "Personagem não encontrado", 404    

    return render_template('charlist.html', usuario_id=user_id, personagens=results, colorLinks = colorLinks)

@rotas_bp.route('/newchar/<int:user_id>')
@authentication_required
def newchar(user_id):
    db = start_server()
    query = "SELECT * FROM user WHERE id = %s"
    db.cursor.execute(query, (user_id,))
    results = db.cursor.fetchone()

    if not results:
        return "Usuario nao encontrado", 404
    
    usuario_id = results['id']
    return render_template('newchar.html', usuario_id=usuario_id)


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

    
@rotas_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('rotas.route_')) 