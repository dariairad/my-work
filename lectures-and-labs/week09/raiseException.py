# Lecture 9.1 - Errors and Exceptions

# Raising an exception.

try:
    inputVar = int(input('Enter a nummber: '))
    if (inputVar < 0):
        raise ValueError ('Negative value entered')
    print (f'{inputVar} multiplied by 2 is {inputVar * 2}')
except ValueError as e:
    print ('Please enter a positive number')
    print (e)