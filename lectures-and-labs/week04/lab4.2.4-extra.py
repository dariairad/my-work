# Lab 4.2.4 Extra

# Modified program from Lab 4.2.3
# Program tells the if their guess is too high or too low each time they guess.
# AND o generate a random number between 0 and 100 to guess

# Author: Daria Sep

# Ref: week03 - randomGeneratorExtra.py

import random

numberToGuess = random.randint (1, 100)

guess = int (input ('Please guess the number:'))
while guess != numberToGuess:
    if guess > numberToGuess:
        print ('Your number is too high.')
    else:
        print ('Your number is too low.')
    guess = int (input ('Please try again:'))

print ('Well done! Yes, the number was' , numberToGuess)