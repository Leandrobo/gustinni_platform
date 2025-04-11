from flask import Flask, render_template
from auth import auth_blueprint
from ml import ml_blueprint

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Registro dos Blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(ml_blueprint)

@app.route('/')
def home():
    return 'Plataforma Gustinni online!'

if __name__ == '__main__':
    app.run(debug=True)
  
