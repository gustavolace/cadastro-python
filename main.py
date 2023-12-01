import multiprocessing
from src.app import create_app
from src.services.webview import run_webview
from src.services.sql import start_server

if __name__ == '__main__':

    flask_process = multiprocessing.Process(target=create_app)
    webview_process = multiprocessing.Process(target=run_webview)
    server_process = multiprocessing.Process(target=start_server)

    flask_process.start()
    webview_process.start()
    server_process.start()

    flask_process.join()
    webview_process.join()
    server_process.join()
