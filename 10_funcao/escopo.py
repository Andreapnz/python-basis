# aqui começa o escopo global
nome = "Global" # Variavel global
numero = 1 # Global namespace global
flag = True # Variavel global

#print(globals()) # Exibe o namespace global

def funcao():
    #aqui começa o escopo da funcao
    nome = "Local" # Variavel local

    def funcao_interna(): # inner function / closure
        # aqui começa o escopo local da funcao interna
        nome = "Interna"
    
        #print("Escopo local da função interna:", locals()) # Exibe o namespace local
        #print("*" * 30) # Linha de separação

        print(nome)
        return nome
        # aqui termina o escopo local da funcao interna

    #print("Escopo local da função:", locals()) # Exibe o namespace local
    #print("=" * 30) # Linha de separação
    
    funcao_interna() # Chama a funcao interna
    print(nome)
    
    return nome
    # aqui termina o escopo local da funcao



# aqui termina o escopo 

#print("Escopo global:", globals()) # Exibe o namespace global

#print("_" * 30) # Linha de separação
funcao() # Chama a funcao que imprime a variavel local

print(nome) # Acessa a variavel global

# aqui termina o escopo global