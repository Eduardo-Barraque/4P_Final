from application.model.entity.produto import Produto
import json

class ProdutoDao:
    def __init__(self):
        self.__produtos = []
        with open("products.json") as documento:
            listajson = json.load(documento)
            documento.close()

        for i in listajson:
            id = i['id']
            nome = i['name']
            imagem = i['image']
            oldprice = i['oldPrice']
            price = i['price']
            description = i['description']
            parcelas = i['installments']
            totparcelas = parcelas['count']
            valparcelas = parcelas['value']
            carregar_produto = Produto(
                id,
                '{}'.format(nome),
                '{}'.format(imagem),
                oldprice,
                price,
                '{}'.format(description),
                totparcelas,
                valparcelas)
            self.__produtos.append(carregar_produto)
        
    def produtosBusca(self):
        return self.__produtos