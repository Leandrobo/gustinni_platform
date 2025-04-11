from flask import Flask
from auth import auth_blueprint
from ml import ml_blueprint

app = Flask(__name__)

# Configurações básicas
app.secret_key = 'sua_chave_secreta_aqui'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Registro dos blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(ml_blueprint)

# Página inicial
@app.route('/')
def home():
    return 'Plataforma Gustinni Online!'

# Início da aplicação
if __name__ == '__main__':
    app.run(debug=True)
    # Arquivo principal do Flask
