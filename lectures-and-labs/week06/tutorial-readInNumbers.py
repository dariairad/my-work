# Lecture 6.2 - Tutorial

def readNum (message = 'Enter a number: '):
    num = False
    while (not num):
        try:
            num = int (input (message))
        except ValueError:
            print ('That was not a number.', message)
    return num # indentation as while

num1 = readNum ()
num2 = readNum ('Enter another number: ')
answer = num1 * num2

print (f'answer is {answer}') 