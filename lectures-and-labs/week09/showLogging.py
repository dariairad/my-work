# Lecture 9.3 Logging

# Log is a print statement with a level
# DEBUG
# INFO
# WARNING 
# ERROR
# CRITICAL

import logging 
# logging.basicConfig (level = logging.ERROR) # you can only call basicConfig once
logging.basicConfig (filename = 'debugging.log', 
    filemode = 'a', 
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s - %(message)s - line: %(lineno)d')
name = 'joe'

logging.error ('This is an error')
logging.critical ('Hiya')
logging.warning ('dont know %s', name) # level set to warning by default
logging.info ('still going')
logging.debug ('and so is this')


