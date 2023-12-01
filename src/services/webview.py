import webview
from dotenv import load_dotenv
import os
load_dotenv()

def  run_webview():
    webview.create_window('Minha Janela', "http://localhost:3333", width=1600, height=900)
    webview.start(debug=True)