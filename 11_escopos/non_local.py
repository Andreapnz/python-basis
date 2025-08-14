contador = 0

def funcao():
    global contador  # Declara que estamos usando a variável global 'contador'
    contador += 1 

    subcontador = 0  # Variável local para contar chamadas internas

    def funcao_interna():
        global contador  # Declara que estamos usando a variável não local 'contador'
        contador += 1  # Tenta acessar a variável global 'contador'

        nonlocal subcontador  # Declara que estamos usando a variável não local 'subcontador'
        subcontador += 1  # Incrementa o contador local

    funcao_interna()  # Chama a função interna que tenta modificar 'contador'

funcao()
funcao()

print(contador)

