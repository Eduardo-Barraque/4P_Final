from flask import render_template
from application.model.dao.produtoDao import ProdutoDao
from application import app

@app.route("/", methods=['GET'])
def home():
    produtos = ProdutoDao().produtosBusca()
    return render_template("home.html", produtos = produtos)