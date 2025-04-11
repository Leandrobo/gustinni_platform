from flask import Blueprint, render_template

admin_blueprint = Blueprint("admin", __name__, url_prefix="/admin")

@admin_blueprint.route("/")
def dashboard():
    return render_template("admin/dashboard.html")

@admin_blueprint.route("/users")
def users():
    sample_users = [
        {"id": 1, "name": "João"},
        {"id": 2, "name": "Maria"},
        {"id": 3, "name": "Carlos"},
    ]
    return render_template("admin/users.html", users=sample_users)

@admin_blueprint.route("/orders")
def orders():
    sample_orders = [
        {"id": 1001, "item": "Café", "user": "João"},
        {"id": 1002, "item": "Pão", "user": "Maria"},
    ]
    return render_template("admin/orders.html", orders=sample_orders)
  
