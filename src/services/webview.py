import webview

def  run_webview():
    with open('src/views/pages/login/index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    webview.create_window('Minha Janela', "https://pywebview.flowrl.com", width=800, height=600)
    webview.start(debug=True, gui='edge')

