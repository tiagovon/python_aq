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

ex3









"""
#!usr/bin/env


#ex 1 
# for numero in range(1,201):
#  if numero % 2 == 0:
#      print(numero)

    
#ex 2 

import sys
import logging

log = logging.Logger("alerta")

def valores():
    try:
        valor = float(input("qual e o valor?: ").strip())
        
    except ValueError:
        log.error("valor errado,tente um numero")
        sys.exit(1)
    return valor


temperatura = valores()
umidade = valores()



if temperatura > 45:
    print("ALERTA!!! Perigo calor extremo")
elif temperatura*3 >= umidade:
    print("ALERTA!!! Perigo de calor úmido")
elif temperatura < 30 and temperatura > 10:
    print("normal")
elif temperatura < 10 and temperatura > 0:
    print("frio")
elif temperatura < 0:
    print("frio extremo")




























































































































































































































































































