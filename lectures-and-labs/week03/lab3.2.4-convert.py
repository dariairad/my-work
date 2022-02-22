# Lab 3.2.4 (Extra)

# Program that takes in a float amount of dollars and returns absoulte amount in cents. 

# Author: Daria Sep

amountInDollars = float (input ('Please enter an amount: '))
# abs() is a built in function > returns the absolute value of a number
absoluteAmount = abs (amountInDollars)
# absoulteAmount is in dollars, multiplying by 100 to convert to cents (1 Dollar = 100 Cents)
# Based on the task description and example provided, I'm working of an assumption that output should be presented as an int
# Converting to int using int ()
absoluteAmountInCent = int (absoluteAmount * 100)

print ('Absoulte value of {} dollars in cent is {} cents.' .format (amountInDollars, absoluteAmountInCent))