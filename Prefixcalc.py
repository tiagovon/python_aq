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
import os
import sys

arguments = sys.argv[1:]

valid_operations = {
"sum":lambda a, b:a + b,
"sub":lambda a, b:a-b,
"mult":lambda a, b:a*b, 
'div':lambda a, b:a/b,
}

path = os.curdir
filepath = os.path.join(path,"prefixcalc.log")

if not arguments:
    operation = input("operação:")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("ex: sum 5 5")
    sys.exit(1)

operation, *nums = arguments

if operation not in valid_operations:
    print("Operação inválida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Numero inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)
    
n1, n2 = validated_nums

result = valid_operations[operation](n1,n2)


with open(filepath, "a") as file_:
        file_.write(f"{operation},{n1},{n2}={result}\n")

print(f"O resultado é {result}")
