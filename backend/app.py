from flask import Flask, request, jsonify, render_template
from contato import Contato
import banco


import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "../frontend/templates"),
    static_folder=os.path.join(BASE_DIR, "../frontend/static")
)



banco.criar_tabela()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/contatos", methods=["GET"])
def get_contatos():
    contatos = banco.listar_contatos()
    return jsonify([
        {"id": c[0], "nome": c[1], "telefone": c[2], "email": c[3]}
        for c in contatos
    ])


@app.route("/api/contatos", methods=["POST"])
def criar_contato():
    data = request.json
    contato = Contato(data["nome"], data.get("telefone", ""), data.get("email", ""))
    banco.adicionar_contato(contato)
    return jsonify({"mensagem": "Contato criado com sucesso"}), 201


@app.route("/api/contatos/<int:id>", methods=["PUT"])
def atualizar_contato(id):
    data = request.json
    contato = Contato(data["nome"], data.get("telefone", ""), data.get("email", ""))
    banco.atualizar_contato(id, contato)
    return jsonify({"mensagem": "Contato atualizado com sucesso"})

@app.route("/api/contatos/<int:id>", methods=["DELETE"])
def deletar_contato(id):
    banco.remover_contato(id)
    return jsonify({"mensagem": "Contato removido com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)
