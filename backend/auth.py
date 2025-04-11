from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_blueprint = Blueprint('auth', __name__)

# Simulação de um "banco de dados"
usuarios = {'admin': 'senha123'}

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        senha = request.form['password']
        if usuario in usuarios and usuarios[usuario] == senha:
            session['usuario'] = usuario
            return redirect(url_for('dashboard'))
        else:
            flash('Usuário ou senha inválido')
    return render_template('login.html')

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        usuario = request.form['username']
        senha = request.form['password']
        usuarios[usuario] = senha
        flash('Cadastro realizado com sucesso!')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_blueprint.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('auth.login'))

@auth_blueprint.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))
    return render_template('dashboard.html', usuario=session['usuario'])

__all__ = ['auth_blueprint']
  
