from src.services.sql import start_server 

def get_from_database(table, condition, fetch_all, *params):
    db = start_server()
    query = f"SELECT * FROM {table} WHERE {condition}"
    db.cursor.execute(query, params)
    
    if fetch_all:
        return db.cursor.fetchall()
    else:
        return db.cursor.fetchone()


def get_user_characters(user_id):
    return get_from_database('characters', 'user_id = %s', True, user_id)

def get_user(user_id):
    return get_from_database('user', 'id = %s', False, user_id)