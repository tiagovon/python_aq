#!/usr;/bin/env python3

"""exemplos de envio de email"""

import smtplib

SERVER = "localhost"
PORT =8025



FROM =  "tiago3242@gmail.com"
TO = ["destino1@server.com","destino2@server.com"]
SUBJECT = "Meu email via python"
TEXT = """\
Este e o meu email enviado pelo python <b>Ola mundo</b>
"""

mensagem =f"""\
From: {FROM}
to:{",".join(TO)}
SubJECT:{SUBJECT}

{TEXT}
"""
with smtplib.SMTP(host = SERVER , port = PORT) as server:
    server.sendmail(FROM , TO , mensagem.encode())
