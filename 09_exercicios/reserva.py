"""
Faça um programa de terminal que exibe ao usuário uma listas dos quartos
disponiveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por virgulas.
quartos.txt
# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50
O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.
O programa deve salvar esta escolha em outro arquivo contendo as reservas
reservas.txt
# cliente, quarto, dias
Bruno,3,12
Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
"""
 
"""
Faça um programa de terminal que exibe ao usuário uma listas dos quartos
disponiveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por virgulas.
quartos.txt
# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50
O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.
O programa deve salvar esta escolha em outro arquivo contendo as reservas
reservas.txt
# cliente, quarto, dias
Bruno,3,12
Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
"""
"""
Faça um programa de terminal que exibe ao usuário uma listas dos quartos
disponiveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por virgulas.
quartos.txt
# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50
O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.
O programa deve salvar esta escolha em outro arquivo contendo as reservas
reservas.txt
# cliente, quarto, dias
Bruno,3,12
Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
"""

"""
Faça um programa de terminal que exibe ao usuário uma listas dos quartos
disponiveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por virgulas.
quartos.txt
# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50
O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.
O programa deve salvar esta escolha em outro arquivo contendo as reservas
reservas.txt
# cliente, quarto, dias
Bruno,3,12
Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
""" 

import sys
import logging

RESERVAS_FILE = "reservas.txt"
QUARTOS_FILE = "quartos.txt"

# Acesso ao banco de dados
ocupados = {}  # acumulador

try:
    with open(RESERVAS_FILE) as f:
        for line in f:
            partes = [item.strip() for item in line.strip().split(",")]
            if len(partes) != 3:
                logging.warning(f"Linha inválida em {RESERVAS_FILE}: {line.strip()}")
                continue
            try:
                nome_cliente, num_quarto, dias = partes
                ocupados[int(num_quarto)] = {
                    "nome_cliente": nome_cliente,
                    "dias": int(dias),
                }
            except ValueError as e:
                logging.warning(f"Erro ao converter linha: {line.strip()} -> {e}")
except FileNotFoundError:
    logging.error("arquivo %s não existe", RESERVAS_FILE)
    sys.exit(1)

# Leitura dos quartos
quartos = {}  # acumulador

try:
    with open(QUARTOS_FILE) as f:
        for line in f:
            partes = [item.strip() for item in line.strip().split(",")]
            if len(partes) != 3:
                logging.warning(f"Linha inválida em {QUARTOS_FILE}: {line.strip()}")
                continue
            try:
                num_quarto, nome_quarto, preco = partes
                quartos[int(num_quarto)] = {
                    "nome_quarto": nome_quarto,
                    "preco": float(preco),  # TODO: Usar Decimal
                    "disponivel": False if int(num_quarto) in ocupados else True,
                }
            except ValueError as e:
                logging.warning(f"Erro ao processar linha: {line.strip()} -> {e}")
except FileNotFoundError:
    logging.error("arquivo %s não existe", QUARTOS_FILE)
    sys.exit(1)

# Programa principal
print("Reservas no Hotel Pythonico da Linux Tips")
print("-" * 52)

if len(ocupados) == len(quartos):
    print("Hotel está lotado, volte depois.")
    sys.exit(0)

nome_cliente = input("Qual é o seu nome: ").strip()
print()

# Lista de quartos
print("Lista de quartos")
print()
head = ["Número", "Nome do Quarto", "Preço", "Disponível"]
print(f"{head[0]:<6} - {head[1]:<14} - R$ {head[2]:<9} - {head[3]:<10}")
for num_quarto, dados_quarto in quartos.items():
    nome_quarto = dados_quarto["nome_quarto"]
    preco = dados_quarto["preco"]
    disponivel = "⛔" if not dados_quarto["disponivel"] else "👍"
    print(f"{num_quarto:<6} - {nome_quarto:<14} - R$ {preco:<9.2f} - {disponivel:<10}")

print("-" * 52)

# Reserva
try:
    num_quarto = int(input("Qual o quarto desejado: ").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado, escolha outro.")
        sys.exit(0)
except KeyError:
    print(f"O Quarto {num_quarto} não existe.")
    sys.exit(0)
except ValueError:
    print("Número inválido, digite apenas dígitos.")
    sys.exit(0)

try:
    dias = int(input("Quantos dias: ").strip())
except ValueError:
    print("Número inválido, digite apenas dígitos.")
    sys.exit(0)

nome_quarto = quartos[num_quarto]["nome_quarto"]
preco_diaria = quartos[num_quarto]["preco"]
total = dias * preco_diaria

print(
    f"Olá {nome_cliente}, você escolheu o quarto {nome_quarto} "
    f"e o valor total estimado será R$ {total:.2f}"
)

if input("Confirma? (digite y) ").strip().lower() in ("y", "yes", "sim", "s"):
    with open(RESERVAS_FILE, "a") as reserva_file:
        reserva_file.write(f"{nome_cliente},{num_quarto},{dias}\n")
