import time

def imprime_nome(nome, sobrenome="Sabugosa"):
    # escopo local {nome: ..., sobrenome: ...}
    print(f"Seu mome é {nome} {sobrenome}")


imprime_nome("Andréa", "Correia")
imprime_nome("Andréa")  # Sobrenome assume o valor padrão "Sabugosa"


def conecta(host, timeout=10):
    print(f"Conectando ao host {host}")
    for i in range(1, timeout + 1):
        time.sleep(1)
        print("." * i)
    print("erro ao conectar")

conecta("localhost", 5)  # Sobrescreve o valor padrão de timeout
