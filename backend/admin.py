# backend/admin.py

from flask import Blueprint, render_template, request, redirect, url_for, flash

admin_blueprint = Blueprint('admin', __name__, url_prefix='/admin')

# Rota do painel de administração
@admin_blueprint.route('/')
def dashboard():
    return render_template('admin/dashboard.html')

# Rota para adicionar uma nova loja
@admin_blueprint.route('/add-store', methods=['GET', 'POST'])
def add_store():
    if request.method == 'POST':
        store_name = request.form['store_name']
        # Aqui, você pode salvar a loja em um banco de dados ou em algum lugar
        flash(f'Loja {store_name} cadastrada com sucesso!', 'success')
        return redirect(url_for('admin.dashboard'))  # Redireciona de volta ao painel
    return render_template('admin/add_store.html')  # Exibe o formulário de cadastro de loja
