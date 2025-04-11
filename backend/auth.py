from flask import Blueprint, render_template, request, redirect, url_for, flash

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Aqui você pode adicionar a lógica de autenticação
        email = request.form.get('email')
        password = request.form.get('password')
        # Verifique o usuário no banco de dados, por exemplo
        flash('Login realizado com sucesso!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('login.html')

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Aqui você pode adicionar a lógica de registro
        email = request.form.get('email')
        password = request.form.get('password')
        # Salve o usuário no banco de dados
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

__all__ = ['auth_blueprint']
