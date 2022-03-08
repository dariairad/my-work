# Lab 4.4.2

# Program that prompts the user to guess a number, 
# the program keeps prompting the user to guess the number until the user gets the right on

# Author: Daria Sep

numberToGuess = 30

guess = int (input ('Please guess the number:'))
while guess != numberToGuess:
    print ('Wrong')
    guess = int (input ('Please try again:'))

print ('Well done! Yes, the number was' , numberToGuess)