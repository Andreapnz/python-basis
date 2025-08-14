#!usr/bin/env python3

"""
Faça um programa em python que imprime os numeros pares de 1 a 200

ex:
2
4
6
8
...

"""
# Imprime os números pares de 1 a 200
for numero in range(1, 201):  
    if numero % 2 == 0:
        print(numero)


# Explicação:
# range(1, 201) gera números de 1 até 200.
# if numero % 2 == 0 verifica se o número é par (ou seja, divisível por 2).
# Se for par, imprime o número.

# Imprime apenas os números pares de 2 a 200 (pulando de 2 em 2)
for numero in range(2, 201, 2):
    print(numero)

# Explicação:
# range(2, 201, 2) gera números de 2 até 200, pulando de 2 em 2.
# Isso já garante que todos os números gerados serão pares, então não é necessário verificar com o if.
# O loop imprime diretamente os números pares.
# Essa abordagem é mais eficiente, pois evita a verificação de cada número individualmente.

for mum in range(1, 201):
    if num % 2 != 0:
        continue
    print(num)

# Explicação:
# Este código é semelhante ao primeiro, mas usa uma verificação diferente.
# A condição if num % 2 != 0 verifica se o número é ímpar
# (ou seja, não divisível por 2). Se for ímpar, o código usa continue para pular a iteração atual do loop.
# Assim, apenas os números pares são impressos, pois o print(num) só é alcançado se a condição for falsa (ou# seja,
# se o número for par).
 


