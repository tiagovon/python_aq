import os
import sys

argumentos = sys.argv[1:]
if not argumentos:
    print("digite o argumento")
    sys.exit(1)

filename = argumentos[0]

path = os.curdir
file = os.path.join(path,"")
