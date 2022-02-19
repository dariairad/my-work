# Lab 3.1.3
# Program that reads in two numbers and divides the first one by the second one 
# and give the integer result and the remainder
# Author: Daria Sep

x = int (input ('Enter first number: '))
y = int (input ('Enter second number: '))
answer = x // y
remainder = x % y

print ('{} divided by {} is {} with reminder {}' .format (x, y, answer, remainder))