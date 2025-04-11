from flask import Blueprint, render_template, request, redirect, url_for

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Exemplo de verificação (pode ser adaptado para autenticação real)
        if username == "admin" and password == "senha123":
            return redirect(url_for('admin.dashboard'))  # Altere conforme seu app
        else:
            return render_template('login.html', message="Credenciais inválidas")

    return render_template('login.html')
