# Lecture 9.1 Errors and Exceptions

import sys
filename = sys.argv[1]

try:
    with open (filename) as f:
        print (f.read())
except FileNotFoundError:
    print (f'File {filename} does not exist.')
except: 
    print ('An exception occured.')