from flask import Flask, render_template
from auth import auth_blueprint
from admin import admin_blueprint
from ml import ml_blueprint

app = Flask(__name__)

# Configura o local dos templates e arquivos estáticos
app.template_folder = "../templates"
app.static_folder = "../static"

# Registro dos Blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
app.register_blueprint(ml_blueprint)

# Rota principal
@app.route("/")
def home():
    return render_template("index.html")  # Exibe "Plataforma Gustinni Online" ou página inicial

if __name__ == "__main__":
    app.run(debug=True)
