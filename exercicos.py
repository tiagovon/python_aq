"""
ex 1 :
faça um programa que imprime os numeros pares de 1 a 200

ex
'python3 numeros_pares.py '
2
4
6
8



ex 2 :

Faça um script que pergunta ao usuário qual a temperatura
atual e o indice de  umidade do ar sendo que caso será
exibida uma mensagem de alerta dependendo_

das condições:



temp maior 45: ALERTA!!! Perigo calor extremo
temp vezes 3 for maior ou igual a umidade: ALERTA!!!
Perigo de calor úmido

temp entre 10 e 30: Normal

temp entre 0 e 10: Frio

temp <0: ALERTA: Frio extremo_

ex 3: 
Faça um programa que pede ao usuário que digite uma ou
mais palavras e imprime cada uma das palavras
com suas vogais duplicadas.

ex:

python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo

ex 4

Faça um programa de terminal que exibe so usuário uma
listas dos quartos disponiveis para alugar e o preço de
cada quarto, esta informação está disponível en us arquivo
de texto separado por virgulas.

quartos.txt

a codigo, nome, preço

1. Suíte Master, 500

2. Quarto Familia, 200

3, Quarto Individual, 108

4, Quarto Simples, 50

O programa pergunta ao usuário o nome, qual o número do 
quarto a ser reservado e a quantidade de dias e no 
final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo
as reservas

reservas.txt

#cliente, quarto, dias

Bruno, 3,12

Se outro usuário tentar reservar o mesmo quarto o 
programa deve exibir una mensagem informando que já está
reservado.




"""
#!usr/bin/env


#ex 1 
# for numero in range(1,201):
#  if numero % 2 == 0:
#      print(numero)

    
#ex 2 

#    import sys
#    import logging

#    log = logging.Logger("alerta")

#    def valores():
#        try:
#             valor = float(input("qual e o valor?: ").strip())
        
#        except ValueError:
#             log.error("valor errado,tente um numero")
#             sys.exit(1)
#       return valor


#    temperatura = valores()
#    umidade = valores()



#    if temperatura > 45:
#         print("ALERTA!!! Perigo calor extremo")
#    elif temperatura*3 >= umidade:
#         print("ALERTA!!! Perigo de calor úmido")
#    elif temperatura < 30 and temperatura > 10:
#         print("normal")
#   elif temperatura < 10 and temperatura > 0:
#         print("frio")
#    elif temperatura < 0:
#     print("frio extremo")

#words = []
#loop = True
#while loop:
#    aswer = input('Digite uma palavra (ou enter para sair):' )
#    if aswer == "":
#        loop = False
#    voglas = "aeiouAEIOU"
#   final_word = ""
#    for letras in aswer:
    #TODO: FUNÇAO funçao
#        final_word += letras * 2 if letras in voglas else letras
#   words.append(final_word)

#print(*words , sep="\n")

#ex4

# import os
# import sys


# path = os.curdir
# filepath =os.path.join(path,"quartos.txt")
# arquivopath = os.path.join(path,"reservas.txt")
# numeros_de_quartos= []
# loop = True
# sub_loop = True
# while loop:
#    dic_dados = {}
#    dic_num = {}
#    
#    for line in  open(filepath):
#        numero , quarto , preço  = line.split(",")
#        print(f"temos o/a {quarto} de numero: {numero} "  
#         f"com o preço de {preço}")
#       dic_dados[quarto] = int(preço)
#        dic_num[numero] = {quarto:int(preço)}
    
    
#    nome_usr = input("seu nome ")
#    numero_user = input("qual e o numero do quarto que "
#    "voce quer resevar? ")
#    numeros_de_dias = input("quantos dias voce quer passar? ")
#    while sub_loop:
#         if numero_user in numeros_de_quartos:
#                 print("esse quarto ja esta resevado")
#                 input(f"tente outro numero ")
#         else:
#            sub_loop = False       
    
#    numeros_de_quartos.append(numero_user)
    
    
    
#    for keys in dic_num[numero_user]:
#        preço_user = dic_dados[keys]
    
#    valor = preço_user * int(numeros_de_dias)
    
#    print(f"o valor vai ficar {valor}")
    
#    with open(arquivopath,"a") as arquivo:
#        arquivo.write(nome_usr + ",")
#        arquivo.write(numero_user + ",")
#        arquivo.write(numeros_de_dias + "\n")

#    final_loop = input("quer conitunar? y/n: ")
#    if final_loop  == "n":
#        loop = False
    #   reservas.txt

#with open(arquivopath , "w") as arquivo:
#   pass



# ex 4  com o linutipis 

import os
import sys
import logging

path = os.curdir
filepath =os.path.join(path,"quartos.txt")
arquivopath = os.path.join(path,"reservas.txt")

dic_dados = {}
dic_reserva =  {} 



try:
         for line in  open(arquivopath):
             nome , num_quarto_re , dias  = line.split(",")
             dic_reserva[int(num_quarto_re)] = {
                 "nome":nome,
                 "dias":dias            
                      }
except FileNotFoundError:
    logging.error("arquivo na existe")
    sys.exit(1)   

try:
    for line in  open(filepath):
        numero , quarto , preço  = line.split(",")
        dic_dados[int(numero)] = {
            "nome":quarto,
            "preço":float(preço),
            "disposnivel": False if  int(numero) in dic_reserva else True         
        }
except FileNotFoundError:
    logging.error("arquivo na existe")
    sys.exit(1)

if len(dic_reserva) == len(dic_dados):
    print("hotel cheio")
    sys.exit(1)

nome = input("Nome do Cliente ").strip()  
print("-"*40)
print("Escolha um quarto")
print("-"*40)

for codigo, dados in dic_dados.items():
    disposnivel =  "ocupado" if not dados["disposnivel"] else "livre"
    print(f"{codigo}-{dados['nome']}-R${dados['preço']}"
  f"-{disposnivel}")


try:
   num_quarto = int(input("numero do quarto ").strip())
   if not dic_dados[num_quarto]["disposnivel"]:
        print(f"o quarto {num_quarto} ja esta ocupado")
        sys.exit(1)
except ValueError:
    logging.error("numero inavalido")
    sys.exit(1)
except KeyError:
    print(f"o quarto {num_quarto} nao existe ")
    sys.exit(1)

try:
   dias = int(input("dias que vai ficar ").strip())
except ValueError:
    logging.error("numero inavalido")
    sys.exit(1)

total = dic_dados[num_quarto]["preço"] * dias
print(f"vai custar {total}")



with open(arquivopath,"a") as file:
    file.write(f"{nome},{num_quarto},{dias}\n")









































































































































































































































