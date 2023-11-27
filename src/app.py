from flask import Flask
from src.routes import rotas_bp
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
 
    app = Flask(__name__, static_folder='../static', template_folder='templates')

    app.config['SERVER_NAME'] = os.getenv('SERVER_NAME')

    app.register_blueprint(rotas_bp)
    app.run()




