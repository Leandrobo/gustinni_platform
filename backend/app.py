# backend/app.py

from flask import Flask
from backend.admin import admin_blueprint
from backend.auth import auth_blueprint

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Defina sua chave secreta para sessões

# Registre os blueprints
app.register_blueprint(admin_blueprint)
app.register_blueprint(auth_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
  
