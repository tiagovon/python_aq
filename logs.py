#!/usr/bin/env python3

import logging
import os
#TODO: usar funçao
#TODO: usar lib
log_level= os.getenv("LOG_LEVEL","WARNING").upper()
log = logging.Logger("logs.py",log_level)
ch= logging.StreamHandler()
ch.setLevel(log_level)
fnt = logging.Formatter( '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s')
ch.setFormatter(fnt)
log.addHandler(ch)

"""
log.debug("Mensagem pro dev , qe , sysadmin")
log.info("mesagem para usuarios")
log.warning("aviso que nao causa erro")
log.error("erro que afeta uma unica exuxao")
log.critical("erro geral ex :banco de dados sumiu")
"""

    

    
