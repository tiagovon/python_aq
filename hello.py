#!/usr/bin/env python3

import os
import sys
import logging

log_level= os.getenv("LOG_LEVEL","WARNING").upper()
log = logging.Logger("logs.py",log_level)
ch= logging.StreamHandler()
ch.setLevel(log_level)
fnt = logging.Formatter(
" %(asctime)s %(name)s %(levelname)s"
" l:%(lineno)d f:%(filename)s: %(message)s"
)
ch.setFormatter(fnt)
log.addHandler(ch)


argumentos ={
   "lang":None,
   "count":1,
}
for args in sys.argv[1:]:
    try:
         key, value = args.split("=")
    except ValueError as e:
        log.error(
            "You need to use '=',you passed %s ,try --key=value:%s",
            args,
            str(e) 
            )
        sys.exit(1)
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



