# Lab 6.2 - Student Management Program
#  Program that allows a user to create new students and to view students.
# ( + modules and grades)

# Q2 
# Write a function that prints out a menu of commands we can perform, ie add,
# view and quit. The function should return what the user chose.
# Test the function. We don’t need to worry about error handling yet

def displayMenu ():
    print ('What would you like to do?')
    print ('\t(a) Add new student')
    print ('\t(v) View students')
    print ('\t(q) Quit')
    choice = input ('Type one letter (a/v/q):').strip()

    # strip() - Remove spaces at the beginning and at the end of the string
    # https://www.w3schools.com/python/ref_string_strip.asp

    return choice

# test

choice = displayMenu ()
print ('You chose {}' .format(choice))