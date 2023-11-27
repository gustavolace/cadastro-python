import multiprocessing
from src.app import create_app
from src.services.webview import run_webview

if __name__ == '__main__':

    flask_process = multiprocessing.Process(target=create_app)
    webview_process = multiprocessing.Process(target=run_webview)

    flask_process.start()
    webview_process.start()

    flask_process.join()
    webview_process.join()
