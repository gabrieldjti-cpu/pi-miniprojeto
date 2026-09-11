from flask import Flask, render_template

app = Flask(__name__)

# Adicione novos dicionários aqui: o Jinja atualiza o catálogo automaticamente.
servicos = [
    {"id": 1, "nome": "Assistência funerária", "categoria": "Acolhimento", "descricao": "Acompanhamento cuidadoso na organização da despedida, com atenção às escolhas de cada família.", "destaque": True},
    {"id": 2, "nome": "Cerimônia de despedida", "categoria": "Homenagens", "descricao": "Uma homenagem pessoal, que respeita crenças, histórias e os momentos compartilhados.", "destaque": True},
    {"id": 3, "nome": "Arranjos florais", "categoria": "Homenagens", "descricao": "Flores e coroas para expressar carinho e preservar a delicadeza de uma última homenagem.", "destaque": False},
    {"id": 4, "nome": "Traslado funerário", "categoria": "Organização", "descricao": "Planejamento do transporte funerário, conforme a localidade e as necessidades da família.", "destaque": False},
    {"id": 5, "nome": "Memorial de lembranças", "categoria": "Homenagens", "descricao": "Uma seleção de fotografias e mensagens para celebrar uma vida e suas lembranças.", "destaque": True},
    {"id": 6, "nome": "Orientação à família", "categoria": "Acolhimento", "descricao": "Explicações claras sobre as etapas do atendimento e a organização da cerimônia.", "destaque": False},
]


@app.route("/")
def inicio():
    return render_template("inicio.html", servicos=[s for s in servicos if s["destaque"]])


@app.route("/servicos")
def catalogo():
    return render_template("servicos.html", servicos=servicos)


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/contato")
def contato():
    return render_template("contato.html")


@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run()
