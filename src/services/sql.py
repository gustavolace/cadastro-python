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
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise  # Lança a exceção para sinalizar que a conexão falhou

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print('Conexão ao banco de dados encerrada')

    def is_connected(self):
        return self.connection.is_connected() if self.connection else False

try:
    db = DB(host=os.getenv("DB_HOST"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASS"), database=os.getenv("DB_DATABASE"))
    db.connect()

    if db.is_connected():
        print("Conexão estabelecida")

except mysql.connector.Error as e: 
    print(f"Erro ao conectar ao banco de dados: {e}")