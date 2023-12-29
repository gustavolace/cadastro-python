from flask import Flask
from routes import rotas_bp
import os

application = Flask(__name__, static_folder='./static', template_folder='templates')
application.secret_key = os.getenv('SECRET_KEY')
application.register_blueprint(rotas_bp)
