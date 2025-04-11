from flask import Flask, render_template
from auth import auth_blueprint
from ml import ml_blueprint

app = Flask(__name__, template_folder="../templates")

app.register_blueprint(auth_blueprint)
app.register_blueprint(ml_blueprint)

@app.route("/")
def home():
    return "<h1>Plataforma Gustinni Online</h1><a href='/login'>Ir para Login</a>"

if __name__ == "__main__":
    app.run()
    
