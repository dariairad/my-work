# Lab 7.2.2 
# Write a function that takes in a number and overwrites a file with that number (count.txt). 
# Test it and check that the file has been changed


filename = "count.txt"
def writeNumber(number):
    with open(filename, "wt") as f:
    # write takes a string so we need to convert
        f.write(str(number))

writeNumber(3)
