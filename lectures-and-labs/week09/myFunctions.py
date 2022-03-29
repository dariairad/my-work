# Lecture 9.2

# A module of useful functions
"""
function that returns the factorial number of an int
ie
7! = 7x6x5x4x3x2x1 = 5040
"""
import logging
logging.basicConfig (level = logging.DEBUG)

def factorial (num):
    if num < 0:
        logging.warn ('factorial received number less than 0')
        return -1
    if num == 0:
        return 1
    factorial = 1
    num += 1 
    for i in range (1,num): # range runs to value - 1
        logging.debug ('before mult %s by %d', factorial, i)
        # print ('before mult', factorial, 'by', i) # to test only
        factorial *= i
        logging.debug ('after mult %d', factorial)
        # print ('after mult', factorial) # to test only
    return factorial

if  __name__ == '__main__':
    print ('In my functions', __name__)
    assert factorial (7) == 5040
