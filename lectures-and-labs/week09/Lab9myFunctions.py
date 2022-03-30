# Lab 9 - Errors, Testing and Logging

# Introduction.
# In this lab we are going to make a function called Fibonacci in a module called myFunctions.
# The Fibonacci function should take in a number and return a list containing a Fibonacci sequence of that many numbers.
# A Fibonacci sequence is a series of numbers that starts off with 0 and 1 and eachsubsequence number is the sum of the previous two.
# E.g. if we called the function with the number 7, it would generate a list of a Fibonacci sequence of 7 numbers.
# [0, 1 ,1, 2, 3, 5, 8]
# If the user enters in a number less than 0 we should raise a ValueError.
# If the user enters 0 it should return an empty list.
# We will write the test cases before we write the function body.

import logging
logging.basicConfig (level = logging.DEBUG)

def fibonacci (number):
    if number == 0:
        return []
    if number < 0:
        raise ValueError ('number must be > 0')  
    a = 0
    b = 1
    fibonacciSequence = [0]
    for i in range (1,number):
        fibonacciSequence.append(b)
        a, b=b, a+b
    # logging.debug('%d: %s', number, fibonacciSequence)
      
    return fibonacciSequence

# testing code
if __name__ == '__main__':
    return7 = [0,1,1,2,3,5,8]
    return11 = [0,1,1,2,3,5,8,13,21,34,55]
    assert fibonacci(7) == return7, 'incorrect return for 7'
    assert fibonacci(11) == return11, 'incorrect return for 11'
    assert fibonacci(0) == [], 'incorrect return value for 0'
    assert fibonacci(1) == [0], 'incorrect return value for 1'
    try: 
        fibonacci (-1)
    except ValueError:
        pass
    else: 
        assert False, 'fibonnacci missing ValueError'
    print ('All good')

    
 