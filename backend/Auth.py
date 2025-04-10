from flask import Blueprint, render_template, request, redirect, session, url_for
import sqlite3
import hashlib

auth_bp = Blueprint('auth', __name__)

# Conexão com banco
def get_db():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Rota de registro
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()

        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT * FROM users WHERE email = ?", (email,))
        if cur.fetchone():
            return "Usuário já existe"

        cur.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        db.commit()
        db.close()
        return redirect('/login')
    return render_template('register.html')

# Rota de login
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()

        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cur.fetchone()
        db.close()

        if user:
            session['user_id'] = user['id']
            session['user_email'] = user['email']
            return redirect('/dashboard')
        else:
            return "Login inválido"
    return render_template('login.html')

# Rota de logout
@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
  
