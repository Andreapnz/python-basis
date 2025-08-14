
contador = 0

def incrementa_contador():
    # aqui começa o escopo local da função
    # assignment '=' '+=' '-='
    global contador  # Declara que estamos usando a variável global 'contador'
    contador += 1

incrementa_contador()
incrementa_contador()
incrementa_contador()
incrementa_contador()

print(contador)




