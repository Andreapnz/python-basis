#!/usr/bin/env python3
""" Exibe relatório de alunos por atividades.

Imprimir a lista de alunos agrupadas por sala que frequentam cada uma das atividades.
"""

__version__ = "0.1.0"
__author__ = "Andréa Correia"

# # Dados
# # 1. Criando a lista de alunos
# sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
# sala2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

# # 2. Criando a lista de atividades
# aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
# aula_musica = ["Erik", "Carlos", "Maria"]
# aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# # Criando lista atividades
# atividades = [aula_ingles, aula_musica, aula_danca]

# # Listar alunos em cada atividade por sala
# # aula_ingles_sala1 = []
# # aula_ingles_sala2 = []

# # for aluno in aula_ingles:
# #     if aluno in sala1: # Verifica se o aluno está na sala 1 / in é um operador de comparação
# #         aula_ingles_sala1.append(aluno) # Adiciona o aluno à lista da sala 1
# #     elif aluno in sala2: # Verifica se o aluno está na sala 2
# #         aula_ingles_sala2.append(aluno) # Adiciona o aluno à lista da sala 2
        
# # print("Inglês sala1", aula_ingles_sala1)
# # print("Inglês sala2", aula_ingles_sala2)

# for atividade in atividades: # Percorre a lista de atividades
#     atividade_sala1 = [] # Cria uma lista para a sala 1
#     atividade_sala2 = [] # Cria uma lista para a sala 2

#     for aluno in atividade: # Percorre a lista de alunos
#         if aluno in sala1:
#             atividade_sala1.append(aluno)
#         elif aluno in sala2:
#             atividade_sala2.append(aluno)

# print("Atividade sala1", atividade_sala1)
# print("Atividade sala2", atividade_sala2)


# Alunos por sala
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

# Atividades com os respectivos alunos
aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"] 
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# Criando dicionário de atividades
atividades = [aula_ingles, aula_musica, aula_danca]

# Listar alunos em cada atividade por sala
for atividade in atividades:

    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

print("Atividade sala1", atividade_sala1)
print("Atividade sala2",atividade_sala2)
