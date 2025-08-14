#!usr/bin/env python3

email_tmpl = """
Olá, %(nome)s
Tem interesse em comprar %(produto)s?
Este produto é ótimo para resolver %(texto)s
Clique agora em %(link)s
Apenas %(quantidade)d disponivel!
Preço promorcional %(preco).2d
"""

clientes = ["Maria", "João", "Bruno", "Andréa"]

for cliente in clientes: # para cada cliente na lista clientes
    print(email_tmpl % {"nome": cliente, "produto": "caneta", "texto": "Escreve muito bem", 
    "link": "www.caneta.com", "quantidade": 1, "preco": 50.50})

    
