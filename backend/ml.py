from flask import Blueprint

ml_blueprint = Blueprint("ml", __name__)

from flask import Blueprint

ml_blueprint = Blueprint('ml', __name__)

@ml_blueprint.route('/ml')
def ml_view():
    return 'Funcionalidade de IA em desenvolvimento!'

__all__ = ['ml_blueprint']
