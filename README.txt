Instruções de uso da plataforma Gustinni# Plataforma Gustinni

Sistema de e-commerce com integração ao Mercado Livre, Shopee, Mercado Pago, e painel para lojistas. Desenvolvido com Flask (Python), HTML, e tema escuro responsivo.

---

## Requisitos

- Python 3.10+
- Flask
- Banco SQLite (já incluso)
- Hospedagem: Render, GitHub Pages (frontend)

---

## Como rodar localmente (modo dev)

1. Acesse a pasta do projeto
2. Execute:

    python main.py

3. Acesse no navegador:  
    http://localhost:5000

---

## Estrutura de pastas

gustinni_platform/
│
├── main.py              -> Arquivo principal Flask
├── users.db             -> Banco de dados
├── README.txt           -> Este manual
│
├── backend/
│   ├── auth.py          -> Funções de login/cadastro
│   └── ml.py            -> Integração Mercado Livre
│
├── templates/
│   ├── login.html       -> Tela de login
│   ├── register.html    -> Tela de cadastro
│   └── dashboard.html   -> Painel do usuário
│
├── static/
│   └── style.css        -> Tema escuro

---

## Subir no Render

1. Crie um novo Web Service
2. Selecione o repositório do GitHub com este projeto
3. Configure:

   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`

4. Defina o ambiente como `Python 3`

---

## Dados do admin gratuito (se houver):

E-mail: admin@gustinni.com  
Senha: gustinni123

---

## Slogan (profissional):

**"Sua loja conectada ao sucesso. Com a Gustinni, você vende em todos os lugares."**

---

## Mensalidade da plataforma:

R$ 129,90 com integração completa (Mercado Livre, Shopee, fornecedores e painel)

---

Desenvolvido com amor, por você.
