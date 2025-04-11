from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Funcionou no teste!"

if __name__ == '__main__':
    print("Rodando teste Flask...")
    app.run(debug=True)
  
