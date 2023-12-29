from dotenv import load_dotenv
import os
import webbrowser
load_dotenv()

host = os.getenv("APP_HOST")
port = os.getenv("APP_PORT")

def open_browser():
    url = f'http://{host}:{port}'  # URL que deseja abrir
    webbrowser.open(url)

