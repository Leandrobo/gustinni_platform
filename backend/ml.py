from flask import Blueprint, request, redirect, session
import json

ml_blueprint = Blueprint('ml', __name__)

@ml_blueprint.route('/ml/callback')
def ml_callback():
    code = request.args.get('code')
    if not code:
        return 'Código de autorização não fornecido.', 400

    # Simula o recebimento do código e salva na sessão (exemplo)
    session['ml_code'] = code
    return redirect('/')
    
import requests
from flask import Blueprint, redirect, request, session

ml_bp = Blueprint('ml', __name__)

CLIENT_ID = '8323605292714963'
CLIENT_SECRET = 'TLQ5gEcjIoAV7VU7rrcYXjWBPSSaf88Z'
REDIRECT_URI = 'https://gustinni.onrender.com/ml/callback'

# Iniciar a conexão com Mercado Livre
@ml_bp.route('/ml/conectar')
def conectar_mercado_livre():
    auth_url = (
        f'https://auth.mercadolivre.com.br/authorization'
        f'?response_type=code'
        f'&client_id={CLIENT_ID}'
        f'&redirect_uri={REDIRECT_URI}'
    )
    return redirect(auth_url)

# Receber o token após autorização
@ml_bp.route('/ml/callback')
def ml_callback():
    code = request.args.get('code')
    if not code:
        return "Erro: Código não recebido do Mercado Livre", 400

    token_url = 'https://api.mercadolibre.com/oauth/token'
    payload = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'redirect_uri': REDIRECT_URI
    }

    response = requests.post(token_url, data=payload)
    if response.status_code == 200:
        tokens = response.json()
        # Salvar token na sessão por enquanto (mais tarde salvaremos no banco)
        session['ml_token'] = tokens
        return "Mercado Livre conectado com sucesso!"
    else:
        return f"Erro ao conectar: {response.text}", 400
      
