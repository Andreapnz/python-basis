#!/usr/bin/env python3

"""Cadastro de produto"""
__version__ = "0.1.0"
__autor__ = "Andréa Correia"

from  pprint import pprint

# Criando um dicionário com os dados do produto
# O dicionário é uma estrutura de dados que armazena pares de chave-valor
# As chaves são únicas e podem ser usadas para acessar os valores correspondentes
# Os valores podem ser de qualquer tipo, incluindo outros dicionários, listas, etc.
# O dicionário é definido entre chaves {} e os pares de chave-valor são separados por vírgulas
# As chaves e os valores são separados por dois pontos :

produto = {
    "nome": "Caneta",
    "cores": ["azul", "branco"],
    "preco": 3.23,
    "dimensao":{
        "altura": 12.1,
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None
}

compra = ("Andrea", produto["nome"], 3)

cliente = {
    "nome": "Andrea",
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3,
}

#pprint(compra)

total_compra =  compra["quantidade"] * compra["produto"]["preco"]

print(
    f"O cliente {compra ['cliente']['nome']}"
    f"comprou {compra['quantidade']} unidades de {compra['produto']['nome']}"
    f" e pagou o total de {total_compra} "
)


