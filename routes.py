from flask import Flask, render_template

def configure_routes(app):
    # Rota para a página de login
    @app.route('/')
    def login():
        return render_template('login.html')

    # Rota para a página de pontos
    @app.route('/tela_pontos')
    def pontos():
        return render_template('tela_pontos.html')

    # Rota para a página "Sobre Nós"
    @app.route('/sobre')
    def sobre():
        return render_template('sobre.html')

    # Rota para servir arquivos estáticos (CSS, JS, imagens)
    @app.route('/static/<path:filename>')
    def static_files(filename):
        return app.send_static_file(filename)
    