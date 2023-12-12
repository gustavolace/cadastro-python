import multiprocessing
from src.app import create_app
from src.services.webview import open_browser

if __name__ == '__main__':
    multiprocessing.freeze_support()

    flask_process = multiprocessing.Process(target=create_app)
    webview_process = multiprocessing.Process(target=open_browser)

    flask_process.start()
    webview_process.start()

    flask_process.join()
    webview_process.join()
