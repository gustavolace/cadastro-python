from flask import Flask
from src.routes import rotas_bp

def create_app():
    app = Flask(__name__, static_folder='../static', template_folder='templates')
    app.register_blueprint(rotas_bp)
    app.run()




