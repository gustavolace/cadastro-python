from flask import Flask
from waitress import serve
from src.routes import rotas_bp
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    port = os.getenv('APP_PORT')
    host = os.getenv('APP_HOST')
 
    app = Flask(__name__, static_folder='../static', template_folder='templates')
    app.register_blueprint(rotas_bp)

    print(f"Servidor rodando em http://localhost:{port}/")
    serve(app, host=host, port=port)




