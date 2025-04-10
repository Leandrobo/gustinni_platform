from flask import Flask, render_template, request, redirect, url_for, session
import json, os

app = Flask(__name__)
app.secret_key = 'gustinni_secret_key'

# Carregar usuários
def load_users():
    if not os.path.exists('users.json'):
        return {}
    with open('users.json', 'r') as f:
        return json.load(f)

def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        users = load_users()
        if email in users and users[email]['senha'] == senha:
            session['user'] = email
            if users[email].get('admin'):
                return redirect('/admin')
            return redirect('/dashboard')
        return 'Login inválido'
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        users = load_users()
        if email in users:
            return 'Usuário já existe'
        users[email] = {'senha': senha, 'admin': False}
        save_users(users)
        return redirect('/login')
    return render_template('cadastro.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    return render_template('dashboard.html', user=session['user'])

@app.route('/admin')
def admin():
    if 'user' not in session:
        return redirect('/login')
    users = load_users()
    if not users[session['user']].get('admin'):
        return 'Acesso negado'
    return render_template('admin.html', user=session['user'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
  
