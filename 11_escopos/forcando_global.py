nome = "Global"

def funcao():
    nome = "Local"
    print("Nome Local:", nome)
    nome = globals()['nome']  # Acessa a variável global 'nome'
    print("Nome Global:", nome)


funcao()



