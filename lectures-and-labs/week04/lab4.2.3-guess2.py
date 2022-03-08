# Lab 4.2.3 

# Modified program from Lab 4.2.2
# Program tells the user if their guess is too high or too low each time they guess.
# HINT: put an if statement inside the while loop

# Author: Daria Sep

# Ref: https://stackoverflow.com/questions/36843103/while-loop-with-if-else-statement-in-python


numberToGuess = 30

guess = int (input ('Please guess the number:'))
while guess != numberToGuess:
    if guess > numberToGuess:
        print ('Your number is too high.')
    else:
        print ('Your number is too low.')
    guess = int (input ('Please try again:'))

print ('Well done! Yes, the number was' , numberToGuess)