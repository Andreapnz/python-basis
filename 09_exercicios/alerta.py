#!usr/bin/env python3

"""
Alarme de temperatura
Faça um script que pergunta ao usuário qual a temperatura atual e o indice de umidade do ar sendo que caso será 
exibida uma mensagem de alerta dependendo das condições:

SE temp maior 45: "ALERTA!!! 🥵 Perigo calor extremo"
SENAO temp maior que 30 e temp vezes 3 for maior ou igual a umidade:
"ALERTA!!! 🥵♒ Perigo de calor úmido"
temp entre 10 e 30: "😀 Normal"
temp entre 0 e 10: "🥶 Frio"
temp <0: "ALERTA!!! ⛄ Frio Extremo."
ex:

python3 temperatura.py 
temperatura: 30
umidade: 90
... 
"ALERTA!!! 🥵 Perigo calor extremo"



"""

# temperatura.py

# Entrada de dados

# try:
#     temperatura = float(input("Temperatura atual (°C): "))
#     umidade = float(input("Índice de umidade (%): "))

# # Verificações de alerta
#     if temperatura > 45:
#         print("ALERTA!!! 🥵 Perigo calor extremo")
#     elif temperatura > 30 and (temperatura * 3) >= umidade:
#         print("ALERTA!!! 🥵♒ Perigo de calor úmido")
#     elif 10 <= temperatura <= 30:
#         print("😀 Normal")
#     elif 0 <= temperatura < 10:
#         print("🥶 Frio")
#     else:  # temperatura < 0
#         print("ALERTA!!! ⛄ Frio Extremo.")

# except ValueError:
#     print("❌ Entrada inválida! Por favor, digite apenas números para a temperatura e umidade.")

# Explicação:
# O script começa solicitando ao usuário a temperatura atual e o índice de umidade.
# Em seguida, ele verifica as condições de temperatura e umidade para determinar qual mensagem de alerta deverá ser exibida.
# As condições são verificadas em ordem, e a primeira condição verdadeira é a que será executada.
# Isso garante que apenas uma mensagem de alerta seja exibida, de acordo com a situação atual.
# As mensagens são exibidas de acordo com as condições especificadas no enunciado.
# O uso de float permite que o usuário insira valores decimais para temperatura e umidade, aumentando a precisão do script.

 
import sys
import logging
log = logging.Logger("alerta")


def is_completely_filled(dict_of_inputs):
    """ Returns a boolean telling if a dict is completely filled"""
    info_size = len(dict_of_inputs)
    filled_size = len([value for value in dict_of_inputs if value is not None])
    return info_size == filled_size
     
info = {"temperatura": None, "umidade": None}

while not is_completely_filled(info):

    for key in info.keys():  # ["temperatura", "umidade"]
        if info[key] is not None:
            continue  # já preenchido, pula
        try:
            info[key] = int(input(f"{key}: ").strip())
        except ValueError:
            log.error("%s inválida, digite números", key)
            break  # para o for   

temp, umidade = info.values() # unpacking 

if temp > 45:
    print("ALERTA!!! 🥵 Perigo calor extremo")
elif temp > 30 and temp * 3 >= umidade:
    print("ALERTA!!! 🥵♒ Perigo de calor úmido")
elif 10 <= temp <= 30:
    print("😀 Normal")
elif 0 <= temp < 10:
    print("🥶 Frio")
elif temp < 0:
    print("ALERTA!!! ⛄ Frio Extremo.")