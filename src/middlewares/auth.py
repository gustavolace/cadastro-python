from functools import wraps
from flask import session
from src.services.sql import start_server

def authentication_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return "Usuário não autenticado", 401

        session_user_id = session.get('user_id')

        if 'char_id' in kwargs:
            char_id = kwargs['char_id']
            character = fetch_character(char_id)

            if not character:
                return "Personagem não encontrado", 404

            usuario_id = character['user_id']
            if session_user_id != usuario_id:
                return "Acesso não autorizado: permissões insuficientes", 403

            kwargs['character'] = character  
            kwargs['usuario_id'] = usuario_id  

        if 'user_id' in kwargs:
            route_user_id = kwargs.get('user_id')
            if session_user_id != route_user_id:
                return "Acesso não autorizado: permissões insuficientes", 403

        return func(*args, **kwargs)

    return decorated_function

def fetch_character(char_id):
    db = start_server()
    query = "SELECT * FROM characters WHERE id = %s"
    db.cursor.execute(query, (char_id,))
    return db.cursor.fetchone()
