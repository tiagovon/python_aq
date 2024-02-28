"""exemplos de funçoes"""


#Soild - Single responsibility


def f(x):
    return 5 * (x/2)


valor = f(10)

#print(valor)



def print_in_upper(text):
    # procedure with
    print(text.upper())

#print_in_upper("tiago")




def tringulo(a,b,c):
    s =(a+b+c)/2 
    area =s*(s-a)*(s-b)*(s-c)
    return area ** 0.5

area_do_tri = tringulo(3,4,5)
#print(area_do_tri)

def ask_user (ask_color = False , ask_name = False):
    if ask_name:
        input("qual e o seu nome?")
    if ask_color:
        input("qual e a cor")

ask_user(True,True )

ask_user(True)


tiago = "tiago"

tupl = (12,423,54,762,42,653)
num , *_ = tupl
print(num)
print(_)
t , *_ = tiago
print(t)
print(_)

import time
def conecta (host,timeout =10):
    print(f"{host}")
    for i in range(1,timeout + 1):
        time.sleep(1)
        print("." * i)
    print("erro")
#onecta("localhost", 3)
def valor(a,b,c,*resto):
    reslt = a*b*c
    print(reslt)
    resto1, re2 ,re3,*restoall = resto
    print(resto1,re2,re3)
#alor(1,3,4,4)

def sei_la(b,c,a,*arg ,k="tiago",**keargs):
    print(a+c+b)
    print(keargs)
sei_la(1,3,4,5,3,53,3,k="bruno",jh=2)
