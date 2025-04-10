from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Gustinni está funcionando!"

if __name__ == '__main__':
    print("Iniciando Gustinni...")
    app.run(debug=True)
from backend.auth import db

with app.app_context():
    db.create_all()
    print("Banco de dados criado!")
  
