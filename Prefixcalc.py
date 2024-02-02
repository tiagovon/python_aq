#!/usr/bin/env python3
"""Calculadora Prefix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operação: sum
n1: 5
n2: 4
9
"""

import sys

valores = sys.argv[1:]

if valores:
    operaçao = valores[0]
    n1=int(valores[1])
    n2=int(valores[2])
else:
    operaçao = input("operaçao: ")
    n1 = int(input("n1: "))
    n2 =int(input("n2: "))


print(f"{operaçao} {n1} {n2}")

if operaçao == "sum":
    print(n1 + n2)
elif operaçao == "sub":
    print(n1 - n2)
elif operaçao == "mult":
    print(n1 * n2)
elif operaçao == "div" :
    print(n1 / n2)
else:
    print("ERRO")
