from flask import Flask, render_template
import json
import os
from application.model.dao.produtoDao import ProdutoDao

app = Flask(__name__,static_folder=os.path.abspath("application/view/static"), 
            template_folder=os.path.abspath("application/view/templates"))




@app.route("/", methods=['GET'])
def home():
    produtos = ProdutoDao().produtosBusca()
    return render_template("home.html", produtos = produtos)