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
__version__ = "0.1.2"
__author__ = "Andréa Correia"
__license__ = "Unlicense"


import os # Importando o módulo os para acessar variáveis de ambiente


# Pegando os 5 primeiros caracteres da variável de ambiente LANG
# Se a variável de ambiente não estiver configurada, o padrão será "en_US"
# O método os.getenv() retorna o valor da variável de ambiente especificada
current_language = os.getenv("LANG", "en_US")[:5] 


# Criando um dicionário com as mensagens
msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_EP": "Hola, Mundo!",
    "fr_FR": "Bonjour, le monde!",
}
 
# Ordem Complexidade O(n)

print(msg[current_language]) # Imprime a mensagem correspondente à linguagem configurada
