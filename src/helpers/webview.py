import webview

def exibir_interface():
    with open('src/views/pages/index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    webview.create_window('Minha Janela', html=html_content, width=800, height=600)
    webview.start(debug=True, gui='edge')

exibir_interface()
