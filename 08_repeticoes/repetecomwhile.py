#!/usr/bin/env python3

# While / Enquanto

#n = 0
#while True: # Loop infinito
#    print(n)  # Output: 0 1 2 3 4 5 ...
#    n += 1  # Incrementa n em 1

#n = 0
#while n < 101: # Loop até n ser menor que , condição de parada
#    print(n)  # Output: 0 1 2 3 4 5 ... 100
#    n += 1  # Incrementa n em 1

# O while verifica a condição antes de executar o bloco de código, se a condição for falsa, o loop não será executado.

#n = 0
#while n < 101:
#    if n == 40: # Condição de parada
#        break  # Interrompe o loop se n for igual a 40
#    print(n)  # Output: 0 1 2 3 4
#    n += 1  # Incrementa n em 1


n = 0
while n < 101:
    if n >= 40 and n <= 60: # Verifica se n está entre 40 e 59
        n += 1 # Incrementa n em 1 para evitar loop infinito
        continue # Pula o restante do loop se n for igual a 40
    print(n) 
    n += 1  # Incrementa n em 1

        