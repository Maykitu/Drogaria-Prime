from flask import Flask
from routes import configure_routes  # Importa a função de configuração de rotas

app = Flask(__name__)  # Cria a aplicação Flask

# Configura as rotas
configure_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Roda o servidor na porta 5000
    