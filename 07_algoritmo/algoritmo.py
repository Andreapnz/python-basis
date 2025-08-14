# Statement / Declaração em Python (ESTADOS): 
# Palavras de ordem
# Checa alguma coisa, não retorna valor
# Verifica alguma coisa
# 
# Se -> if 
# Senão, se -> elif
# Senão -> else 
# E -> and
# Ou -> or
# Não -> not

# Assigment / Atribuição
# Atribui um valor a uma variável

# Expression / Expressão
# Retorna um valor, não altera o estado do programa
# Esperar um resposta ou valor
# é feriado?
# é natal?
# é feriado OU é natal?

# Actions / Ações
# Executa uma ação, altera o estado do programa
# Função / método / instrução


# PSEUDO CÓDIGO
import ir, pegar, pedir, tem, comer, ficar

# Premissas
# Variáveis
today = "Segunda-feira"
hora = 15
natal = False
chovendo = True
frio = True
nevando = True
semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
feriado =["quarta-feira"]
horario_padaria = {
    "semana": 19,
    "fds": 12
}

# Algoritmo
# A padaria está aberta?
if today in feriados and not natal:
    padaria_aberta = False
elif today not in semana and hora < horario_padaria["fds"]:
    padaria_aberta = True
elif today in semana and hora < horario_padaria["semana"]:
    padaria_aberta = True
else:
    padaria_aberta = False

if padaria_aberta is True:

    if chovendo and (frio or nevando):
        pegar("guarda-chuva")
        pegar("casaco")
        pegar("botas")
    elif chovendo and not frio:
        pegar("guarda-chuva")
        pegar("agua")
    elif chovendo:
        pegar("guarda-chuva")
    
    ir ("padaria")

    if tem ("pao int") and tem("baguete"):
        pedir(6, "pao int")
        pedir(6, "baguete")
    elif tem("pao int") or tem("baguete"):
        pedir(12, "qualquer um dos dois")
    else:
        pedir(6, "qualquer outro pao")

else:
    ficar ("em casa")
    comer("bolacha")
