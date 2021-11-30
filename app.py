from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")

class produto:
    def __init__(self, id:int, nome:str, imagem:str, oldprice:float, price:float, description:str, parcela:int, valorparcela:float):
        self._nome = nome
        self._id = id
        self._imagem = imagem
        self._oldprice = oldprice
        self._price = price
        self._description = description
        self._parcela = parcela
        self._valorparcela = valorparcela
    
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def imagem(self):
        return self._imagem
    @imagem.setter
    def imagem(self, value):
        self._imagem = value

    @property
    def oldprice(self):
        return self._oldprice
    @oldprice.setter
    def oldprice(self, value):
        self._oldprice = value

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, value):
        self._description = value
    
    @property
    def parcela(self):
        return self._parcela
    @parcela.setter
    def parcela(self, value):
        self._parcela = value
    
    @property
    def valorParcela(self):
        return self._valorParcela
    @valorParcela.setter
    def valorParcela(self, value):
        self._valorParcela = value