#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Andréa Correia"
__license__ = "Unlicense"

import os # Importando o módulo os para acessar variáveis de ambiente
import sys # Importando o módulo sys para acessar argumentos da linha de comando

#print(f"{sys.argv=}") # Exibindo os argumentos da linha de comando

 
arguments = {"lang": None, "count": 1 }  # Dicionário para armazenar os argumentos válidos}

for arg in sys.argv[1:]: # Iterando sobre os argumentos da linha de comando, ignorando o primeiro (nome do script)
    # TODO: Trata ValueError
    key, value = arg.split("=") # Dividindo o argumento em chave e valor
    key = key.lstrip("-").strip()  # Removendo traços iniciais e espaços em branco do começo e do fim da chave
    value = value.strip()  # Removendo espaços em branco
    if key not in arguments: # Verificando se a chave é válida
        print(f"Invalid Option `{key}`")  # Se a chave não for válida, exibe mensagem de erro
        sys.exit() # Se a chave não for válida, exibe mensagem de erro e sai do programa
    arguments[key] = value  # Atribuindo o valor à chave correspondente no dicionário de argumentos

# O código abaixo verifica se a variável de ambiente LANG está configurada e, se não estiver, define um valor padrão.
current_language = arguments["lang"]
if current_language is None:  # Verifica se a linguagem foi passada como argumento
    # TODO: Usar repetição
    if "LANG" in os.environ:  # Verifica se a variável de ambiente LANG está configurada
        current_language = os.getenv("LANG")  # Define a variável de ambiente LANG como "en_US" se não estiver configurada
    else:
        current_language = input("Choose a language: ")


current_language = current_language[:5]
 
# O código abaixo define um dicionário com mensagens em diferentes idiomas.
msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, le monde!",
}

print(msg[current_language] * int(arguments["count"])) # Exibe a mensagem correspondente à linguagem configurada, multiplicada pelo número de vezes especificado
