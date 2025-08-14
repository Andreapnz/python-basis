#!/usr/bin/env python3

import os  # Importando o módulo os para acessar variáveis de ambiente
import logging # root logger (looger raiz, principal)

#BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()  # Obtendo o nível de log da variável de ambiente LOG_LEVEL, com um valor padrão de "WARNING" se não estiver definida

# Configuração do logger
# nossa instancia de logger
log = logging.Logger("logs.py", log_level) 


# level # DEBUG, INFO, WARNING, ERROR, 
ch = logging.StreamHandler() # console handler (manipulador de console)
ch.setLevel(log_level) # nível do console

# formatação # %(asctime)s - data e hora
fmt = logging.Formatter('%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s') # formatação da mensagem
ch.setFormatter(fmt) # adiciona a formatação ao manipulador de console


# destino (arquivo, console, etc)
log.addHandler(ch) # adiciona o manipulador de console ao logger


# Métodos de log
# CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET

log.debug("Mensagem pro dev, QA, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro, mas é importante")
log.error("Erro qeu afeta uma unica execução")
log.critical("Erro crítico que afeta o sistema todo")
              

print("---")

log.critical("Deu problema geral")

try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("Deu erro %s", str(e))
    