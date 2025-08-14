#!/usr/bin/env python3
"""
Exemplos de ennvio de e-mail usando o smtplib"""

# Bibilioteca para envio de e-mails
import smtplib 

# Importante: Para enviar e-mails, você precisa de um servidor SMTP.

SERVER = "localhost"  # ou o endereço do servidor SMTP que você está usando
PORT = 8025 # Porta de um servidor embutido no Python



# Configurações do e-mail / Dados do e-mail que será enviado
FROM = "andrea_pnz@hotmail.com"
TO = ["destino1@server.com", "destino2@server.com"]
SUBJECT = "Meu email via Python"
TEXT = """\
Este é um exemplo de envio de e-mail usando o smtplib do Python.
<b> Andréa Correia </b>"""


# SMTP / Mensagem formatada no formato SMTP
# A mensagem deve ser formatada de acordo com o protocolo SMTP.
message =f"""\
From: {FROM}
To: {",".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

# Explicação
# A mensagem é formatada como uma string com os campos From, To, Subject e o corpo do texto.
# O campo From indica o remetente, To indica os destinatários, Subject é o assunto
# e o corpo do texto é o conteúdo do e-mail.


# Envio do e-mail
# O servidor SMTP é usado para enviar o e-mail.
with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))

# Explicação
# O servidor SMTP é criado usando o contexto `with`, que garante que o servidor será fechado
# corretamente após o envio do e-mail. O método `sendmail` é usado para enviar o e-mail,
# passando o remetente, os destinatários e a mensagem codificada em UTF-8.
# A codificação é importante para garantir que caracteres especiais sejam tratados corretamente.    

