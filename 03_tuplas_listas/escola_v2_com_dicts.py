#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.3"
__author__ = "Andréa Correia"

# Estruturas de dados:

# 1 - Criando os dicionários
salas = {
    "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"],
}

atividades = {  # <-- Corrigido aqui: de 'atividade' para 'atividades'
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Música": ["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

# Solução
# 3 - Loop externo: para cada atividade
# Solução
# Processa e imprime os alunos por atividade, agrupados por sala
for nome_atividade, participantes in atividades.items():
# nome_atividade: Ex: "Inglês"
# parcticipantes: Ex: ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
# O objetivo aqui é percorrer cada atividade e ver quem participa.

# 4 - Imprime o cabeçalho da atividade
    print(f"\nAlunos da atividade: {nome_atividade}")
    print("-" * 40)

# 5 - Loop interno: para cada sala, verifica os alunos participantes
    for nome_sala, alunos_sala in salas.items():
    # nome_sala: Ex: "sala1"
    # alunos_sala: Ex: ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]

# 6 - Verificar quem da sala está na atividade   
        alunos_participantes = [aluno for aluno in alunos_sala if aluno in participantes]
        # alunos_participantes: Ex: ["Erik", "Maia", "Joana"]
        # Aqui, estamos filtrando os alunos da sala que estão participando da atividade.

# 7 - Imprime os alunos participantes da sala
        # Se houver algum aluno da sala participando da atividade, imprime o nome da sala e os nomes dos alunos.
        # Usa capitalize() para deixar a primeira letra da sala maiúscula.
        # Usa join() para imprimir os nomes separados por vírgulas.

        if alunos_participantes:
            print(f"{nome_sala.capitalize()}: {', '.join(alunos_participantes)}")
    print("-" * 40)
