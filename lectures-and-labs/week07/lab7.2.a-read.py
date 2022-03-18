# Lab 7.2.1
# Write a function that reads in a number from a file that already exists (count.txt). 
# Test the program by calling the function and outputting the number.

filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

num = readNumber()
print (num)
