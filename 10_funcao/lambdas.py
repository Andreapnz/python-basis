# Funções de Primeira Classe


# Digamos que tenhamos uma coleção de utilidades
def transforma_em_maiusculo(texto):
    return texto.upper()


def transforma_em_minusculo(texto):
    return texto.lower()


def divide_por_2(numero):
    return numero // 2


# e nossa função principal

def faz_algo(valor, funcao):
    print(f"Aplicando {funcao} em {valor}")
    return funcao(valor)

names = ["Bruno", "João", "Bernardo", "Cintia", "Marcia", "Juca"]

print(sorted(names, key=lambda name:name.count("i"))) 

print(list(filter(lambda name: name[0].lower() == "b", names)))

print(list(map(lambda name: "Hello " + name, names)))

#Calculadora

operacao = input("Operacao: [sum, mul, div, sub]:").strip()
n1 = input("n1:").strip()
n2 = input("n2:").strip()

def soma(a, b):
    return a + b

operacoes = {
    "sum":  soma,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
    "sub": lambda a, b: a - b,  
}

resultado = operacoes[operacao](int(n1), int(n2))   
print(f"O resultado é: {resultado}")

#print(faz_algo("bruno", transforma_em_maiusculo))
# BRUNO

#print(faz_algo("BRUNO", transforma_em_minusculo))
# bruno

#print(faz_algo(10, divide_por_2))
# 5