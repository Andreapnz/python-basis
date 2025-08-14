#!/usr/bin/env python3

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Coleção materializada
# numbers = range(1, 11)  # Coleção não materializada, ocupa somente três espaços na memoria start, next, stop
#print(numbers[-1]) # Output: 10
#print(numbers[2:])  # Output: [3, 4, 5, 6, 7, 8, 9, 10]

# Iterable / Interação
#for number in numbers:
#    par = number % 2 == 0 # Verifica se é par
#    if par:
#        print(number) # Output: 2 4 6 8 10
#    else:
#        continue # Continua o loop se não for par
#    
#    print(f"mais codigo com {number}")

# For loops / Laço for
# for n in [1, 2, 3]
#     print(n * 2)  # Output: 2 4 6

# Acumular dados
# original = [1, 2, 3]
# dobrada = []
#for n in original:
#    dobrada.append(n * 2)  # Output: [2, 4, 6]
# print(dobrada) # Output: [2, 4, 6]

# Funcional
original = [1, 2, 3]

# Lista Comprehension / Gera uma lista nova a partir de uma lista existente
dobrada = [n * 2 for n in original]  # Output: [2, 4, 6]
print(dobrada)  # Output: [2, 4, 6]

# Dict Comprehension / Gera um dicionário novo a partir de uma lista existente
dados = {line for line in ['a', 'b', 'c']}  # Output: {'a': 'a', 'b': 'b', 'c': 'c'}
print(dados)  # Output: {'a', 'b', 'c'}


