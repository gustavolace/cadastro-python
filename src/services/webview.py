import webview

def  run_webview():
    webview.create_window('Minha Janela', "http://localhost:5000", width=800, height=600)
    webview.start(debug=True)