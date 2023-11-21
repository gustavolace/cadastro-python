from flask import Flask
from src.routes import rotas_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(rotas_bp)
    app.run()




