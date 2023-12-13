#!/usr/bin/env python3

import os

lang = os.getenv("LANG")

current_language = lang[:5]

msg = "hello world!"

if current_language =="pt_BR":
    msg = "Ola mundo!"
elif current_language =="it_IT":
    msg = "Ciao,Mondo!" 

print(msg)


