#!/usr/bin/env python3

"""Blocos de notas

$ notes.py new "minha nota"
tag:tech
text:
antaçao geral sobra carreira de tecnologia

$ notes.py read --tag=tech
...
...
"""

import os 
import sys

path = os.curdir
filepath = os.path.join(path,"notes.txt")

argumentos = sys.argv[1:]

if not argumentos:
    print("digite um argumento")
    sys.exit(1) 

cmds = ("read","new")
if argumentos[0] not in cmds:
    print(f"comando invalido {argumentos[0]}")
    sys.exit(2)
loop = True
while loop:
    if argumentos[0] == "read":
        try:
            arg_tag = argumentos[1].lower()
        except IndexError:
            arg_tag = input("qual e a tag?").strip().lower()
        
        for line in open(filepath):
           tag_txt , text_txt = line.split(",")
           if tag_txt.lower() == arg_tag:
                
                print(f"text:{text_txt}")
                
    if argumentos[0] =="new":
        tag_input = input("tag:")
        text_input = input("text:")
        with open (filepath,"a") as arquivo:
            arquivo.write(tag_input + ",")
            arquivo.write(text_input+"\n")
    aswer = input("quer continuar? s ou n:").strip().lower()
    if aswer == "n":
        loop = False




      
