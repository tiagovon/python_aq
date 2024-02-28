import os
import sys
import smtplib
from email.mime.text import MIMEText


argumentos = sys.argv[1:]
if not argumentos:
    print("digite o argumento nome do arquivo tipo email.txt email_tmpl.txt")
    sys.exit(1)

filename = argumentos[0]
email_file_name = argumentos[1]


path = os.curdir
file = os.path.join(path,filename)
email_file = os.path.join(path,email_file_name)



with smtplib.SMTP(host ="localhost",port =8025)as server:

    for line in open(file):
        name , email = line.split(",")
       
        
        text =      (
            open(email_file).read()
           %{
           "nome":name,
           "produto":"caneta",
           "texto":"escrever muito bem",
           "link":"http//canetaslegais.com",
           "quantidade":1,
           "preco":50.5,       }
        )

        messagem = MIMEText(text)
        Subject="compre mais"
        From_="tiago3242@gamil.com"
        To =",".join([email])
        messagem["Subject"]=Subject
        messagem["From"] = From_
        messagem["To"]=To
        server.sendmail(From_,To,messagem.as_string())
        
