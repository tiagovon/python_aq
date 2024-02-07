

import random
import sys

argumentos = sys.argv[1:]

numero_de_montes = int(argumentos[0])

for n1 in range (0,numero_de_montes):
    lado = random.randint(1,100)
    if lado > 50:
        direçao = "emcima"
    else:
        direçao = "embaixo" 
    numero_aletorio = random.randint(1,numero_de_montes)
    print(f"o monte:{numero_aletorio} na posiçao:{direçao}")
    print("-"*50)
    numero_de_montes = numero_de_montes - 1
