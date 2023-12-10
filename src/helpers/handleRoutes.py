from src.helpers.handleSQL import get_from_database, insert_on_database
from werkzeug.security import check_password_hash, generate_password_hash

def get_user_characters(user_id):
    characters = get_from_database('characters', 'user_id = %s', True, user_id)
    user = get_from_database('user', 'id = %s', False, user_id)
    return user, characters

def get_user(user_id):
    return get_from_database('user', 'id = %s', False, user_id)

def login_user(username, password):
        user = get_from_database('user', "username = %s", False, username)
        if user and check_password_hash(user['password'], password):
            return user
        else:
            return None

def register_user(name, username, password):
    hashed_password = generate_password_hash(password)
    user_data = (name, username, hashed_password)
    result_message = insert_on_database("user", "name, username, password", user_data)
    return result_message

def char_route(char_id):
    character = get_from_database("characters", "id = %s", False, char_id)
    user = get_from_database("user", "id = %s", False, character['user_id'])

    return user, character
