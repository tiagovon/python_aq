import os
import sys

argumentos = sys.argv[1:]
if not argumentos:
    print("digite o argumento")
    sys.exit(1)

filename = argumentos[0]
email_file_name = argumentos[1]


path = os.curdir
file = os.path.join(path,filename)
email_file = os.path.join(path,email_file_name)


for line in open(file):
    name , email = line.split(",")
    print(f"eviando email para {email}")
    print(
        open(email_file).read()
       %{
       "nome":name,
       "produto":"caneta",
       "texto":"escrever muito bem",
       "link":"http//canetaslegais.com",
       "quantidade":1,
       "preco":50.5,       }
    )
    print("-" *50)
