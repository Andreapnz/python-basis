#!/usr/bin/env python3

"""
Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime cada uma das palavras com suas vogais duplicadas.
ex:
python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
"""

words = [] # Lista para armazenar as palavras com vogais duplicadas
# Inicia uma lista vazia para armazenar as palavras modificadas
while True: # loop infinito para receber várias palavras
    word = input("Digite uma palavra (ou enter para sair): ").strip() # digita uma palavra e remove espaços em branco no início e no final
    if not word:  # se a palavra for vazia, sai do loop, condição de parada
        break
    final_word = "" # Inicializa uma string vazia para construir a palavra com vogais duplicadas
    for letter in word: # Para cada letra da palavra
        # TODO: Remover acentuação usando função 
        if letter.lower() in  "aeiouãêíóúâêîôûäëïöü": # verifica se a letra é uma vogal (incluindo acentuadas)
            final_word += letter * 2 # duplica a vogal
        else:
            final_word += letter # adiciona a letra original se não for uma vogal

    words.append(final_word) # adiciona a palavra com vogais duplicadas à lista

print(*words, sep="\n")  # imprime cada palavra da lista em uma linha separada

# Explicação:
# - O programa solicita ao usuário que digite palavras até que uma entrada vazia seja fornecida.
# - Para cada palavra digitada, ele duplica as vogais e constrói uma nova palavra.
# - As palavras modificadas são armazenadas em uma lista e, ao final,
#   são impressas uma por linha.
# - A função `strip()` é usada para remover espaços em branco no início e no final
#   da entrada do usuário, garantindo que entradas vazias sejam tratadas corretamente.
# - A verificação de vogais inclui letras acentuadas, mas não remove acentuação.
# - A função `print(*words, sep="\n")` imprime cada palavra da lista `words` em uma nova linha.
# - A condição de parada do loop é quando o usuário pressiona Enter sem digitar nada.
# - A função `lower()` é usada para garantir que a verificação de vogais seja feita de forma case-insensitive.
# - A lista `words` armazena as palavras com vogais duplicadas.
# - O programa é interativo, permitindo que o usuário insira várias palavras até decidir parar.
# - A saída é formatada para que cada palavra modificada apareça em uma linha separada.
# - O programa é simples e fácil de entender, ideal para iniciantes em Python.
# - A lógica de duplicação de vogais é implementada dentro de um loop que percorre cada letra da palavra.
# - O programa não trata de acentuação, mas pode ser facilmente modificado para incluir essa funcionalidade.
# - 