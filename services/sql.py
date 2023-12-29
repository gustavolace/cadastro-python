import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

class DB:
    def __init__(self, host, user, password, database) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print('Conexão ao banco de dados estabelecida')
                self.cursor = self.connection.cursor(dictionary=True)  # Atribua o cursor aqui
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise

def start_server(): 
    db = DB(host=os.getenv("DB_HOST"), 
                user=os.getenv("DB_USER"), 
                password=os.getenv("DB_PASS"), 
                database=os.getenv("DB_DATABASE"))
    db.connect()
    return db

