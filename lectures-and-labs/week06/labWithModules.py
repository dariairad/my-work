# Lecture 6.4 - Modules 
# Lab 6 with modules

import smpUtil as su 

students = []
choice = su.displayMenu ()
while (choice != 'q'):
    if choice == 'a':
        su.doAdd (students)
    elif choice == 'v':
        su.doView (students)
    elif choice != 'q':
        print ('\n\nplease select either a, v, or q: ')
    choice = su.displayMenu ()