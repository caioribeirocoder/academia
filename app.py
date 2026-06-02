from flask import Flask, render_template

app = Flask(__name__)

# Dados fictícios por enquanto (banco de dados vem depois)
alunos = [
    {"id": 1, "nome": "João Silva", "cpf": "123.456.789-00", "telefone": "(41) 99999-0001", "email": "joao@email.com", "turma": "Manhã"},
    {"id": 2, "nome": "Maria Souza", "cpf": "987.654.321-00", "telefone": "(41) 99999-0002", "email": "maria@email.com", "turma": "Tarde"},
]

@app.route("/")
def index():
    return render_template("alunos/listar.html", alunos=alunos)

@app.route("/alunos/cadastrar")
def cadastrar():
    return render_template("alunos/cadastrar.html")

if __name__ == "__main__":
    app.run(debug=True)