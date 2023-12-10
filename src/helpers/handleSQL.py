from src.services.sql import start_server 
import mysql.connector

def get_from_database(table, condition, fetch_all, *params):
    db = start_server()
    query = f"SELECT * FROM {table} WHERE {condition}"
    db.cursor.execute(query, params)
    
    if fetch_all:
        return db.cursor.fetchall()
    else:
        return db.cursor.fetchone()
    

def insert_on_database(table, columns, values):
    try:
        db = start_server()
        query = f"INSERT INTO {table} ({columns}) VALUES ({', '.join(['%s'] * len(values))})"
        db.cursor.execute(query, values)
        db.connection.commit()
        return "Insercao realizada com sucesso"
    except mysql.connector.Error as error:
        if error.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
            return "Chave duplicada: Ja existe um registro com esses valores"
        else:
            return f"Erro MySQL: {str(error)}"
    except Exception as e:
        return f"Ocorreu um erro durante a insercao: {str(e)}"
    finally:
        db.cursor.close()
        db.connection.close()
