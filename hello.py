#!/usr/bin/env python3

import os
import sys

argumentos ={
   "lang":None,
   "count":1,
}
for args in sys.argv[1:]:
    key, value = args.split("=")
    key = key.lstrip("-").strip()
    if key not in argumentos:
         print(f"ivalid option '{key}'")
         sys.exit()
    argumentos[key]= value


current_language = argumentos["lang"]
if current_language is None:
    if "LANG" in os.environ:
         current_language = os.getenv("LANG","en_US")
    else:
        current_language = input("choose a language")

current_language = current_language[:5]


msg = {
"en_US":"Hello World",
"pt_BR":"Ola mundo",
"it_IT":"Ciao Mondo"
}
print(msg[current_language] * int(argumentos["count"]))



