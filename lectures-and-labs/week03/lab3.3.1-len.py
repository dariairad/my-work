# Lab 3.3.1
# Program that reads in a string and outputs how long it is
# Author: Daria Sep

inputString = input ('Please enter a string: ')
# len() function returns the lenght of an object  (number of items in a list or number of characters in a string)
# ref:  https://www.w3schools.com/python/ref_func_len.asp
lenghtOfTheString = len (inputString)

print ('The lenght of {} is {} characters' .format (inputString, lenghtOfTheString))
