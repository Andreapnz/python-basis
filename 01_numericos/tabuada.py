#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10.

Tabuada do 1
    2 x 1 = 1
    2 x 1 = 2
    3 x 1 = 3
.... 
##########################################
Tabuada do 2 
2 x 1 = 2
2 x 2 = 4
...
###########################################3
"""


__version__ = "0.1.1"
__author__ = "Andréa Correia"

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] = lista
#numeros = range(1, 11) - sequencia de números
numeros = list(range(1, 11))  # Convertendo em uma lista

# Iterable (Objetos que podem ser percorridos)
# For (para)
# Para cada mumero percorrido na lista numeros
for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("--------------")
         