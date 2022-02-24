# Lab 3.3.3

# Program that:
# reads in a string and strips any leading or trailing spaces
# converts the string to lower case
# outputs the length of the input and output strings

# Author: Daria Sep


# strip() method returns a trimmed version of the string
# casefold() and lower() methods convert string into lower case
# Ref: https://www.w3schools.com/python/python_strings_methods.asp

# len() function returns the lenght of an object
# Ref:  https://www.w3schools.com/python/ref_func_len.asp

rawString = input ('Please enter a string: ')
normalisedString = rawString.strip().lower()

lenghtOfRawString = len (rawString)
lenghtOfNormalisedString = len (normalisedString)

print ('That string normalised is: {}' .format (normalisedString))
print ('The input string was reduced from {} to {} characters' .format (lenghtOfRawString, lenghtOfNormalisedString))
