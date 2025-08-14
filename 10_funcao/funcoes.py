""" Exemplos de funções
"""

"""
f(x) = 5 * (x / 2)
"""

# Solid - Single Responsibility

def f(x): # Definição da função f
    """Calcula 5 vezes x dividido por 2."""
    result = 5 * (x / 2)
    return result  # Retorna o resultado da função f

def double(x):  # Definição da função double
    """Calcula o dobro de x."""
    return x * 2   # Retorna o dobro de x

valor = double(f(10))  # Chamada da função double com o argumento 10

print(valor)  # Imprime o resultado da função double aplicada ao resultado de f(10)
print(valor == 50)  # Verifica se o valor é igual a 50 e imprime o resultado da comparação

###
# Funções que não retornam valores são chamadas de procedimentos / procedures
# Funções que retornam valores são chamadas de funções / functions
def print_in_upper(text):
    """Imprime o texto em letras maiúsculas."""
    print(text.upper())  # Converte o texto para maiúsculas e 

print_in_upper("andrea")  # Chamada da função para imprimir "andrea" em maiúsculas

###

def heron(a, b, c):
    """Calcula a área de um triângulo usando a fórmula de Heron."""
    perimeter = (a + b + c) # Calcula o perímetro do triângulo
    s = perimeter / 2  # Calcula o semiperímetro

    # Fórmula de Heron: A = √(s * (s - a) * (s - b) * (s - c))

    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Calcula a área
    return area  # Retorna a área do 

print(heron(3, 4, 5))  # Chamada da função heron com os lados do triângulo 3, 4 e 5
print(heron(5, 12, 13))  # Chamada da função heron com os lados do triângulo 5, 12 e 13